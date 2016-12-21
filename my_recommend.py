import sys
import itertools
from math import sqrt
from operator import add
from os.path import join, isfile, dirname

from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel
from BookRecommend import parseRating,parseBook

def loadRatings(ratingsFile):
    """
    Load ratings from file.
    """
    if not isfile(ratingsFile):
        print ("File %s does not exist." % ratingsFile)
        sys.exit(1)
    f = open(ratingsFile, 'r')
    ratings = filter(lambda r: r[2] > 0, [parseRating(line)[1] for line in f])
    f.close()
    if not ratings:
        print ("No ratings provided.")
        sys.exit(1)
    else:
        return ratings


if __name__ == "__main__":
	conf = SparkConf().setAppName("BookRecommend").set("spark.executor.memory", "4g")
	sc = SparkContext(conf=conf)
	Books = dict(sc.textFile(join("books.csv")).map(parseBook).collect())
	myRatings = loadRatings('personalRatings.txt')
	load_model = MatrixFactorizationModel.load(sc,'best.model')

	myRatedBookIds = set([x[1] for x in myRatings])
	candidates = sc.parallelize([m for m in Books if m not in myRatedBookIds])
	predictions = load_model.predictAll(candidates.map(lambda x: (0, x))).collect()
	recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)[:5]

	print ("Books recommended for you:")
	for i in range(len(recommendations)):
	    print (("%2d: %s" % (i + 1, Books[recommendations[i][1]])).encode('ascii', 'ignore'))
