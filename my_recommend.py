import sys

import itertools
from math import sqrt
from operator import add
from os.path import join, isfile, dirname

from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel
from BookRecommend import parseRating,parseBook,loadRatings

def recommend(rating_file):
    conf = SparkConf().setAppName("BookRecommend").set("spark.executor.memory", "4g")
    sc = SparkContext(conf=conf)
    Books = dict(sc.textFile(join("books.csv")).map(parseBook).collect())
    myRatings = loadRatings(rating_file)
    load_model = MatrixFactorizationModel.load(sc,'my_best_model')

    myRatedBookIds = set([x[1] for x in myRatings])
    candidates = sc.parallelize([m for m in Books if m not in myRatedBookIds])
    predictions = load_model.predictAll(candidates.map(lambda x: (0, x))).collect()
    recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)[:5]

    # print ("Books recommended for you:")
    result = ''
    for i in range(len(recommendations)):
        p = Books[recommendations[i][1]]
        print (("%2d: %s" % (i + 1, p)).encode('ascii', 'ignore'))
        result = result+p+'\n'
    print(result)
    return result
