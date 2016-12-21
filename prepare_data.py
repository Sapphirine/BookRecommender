import csv
from numpy.random import randint
import gzip
import json

#Function for parsing json file.
def parse(path):
	g = gzip.open(path, 'r')
	# g = open(path, 'r')
	for l in g:
		yield json.dumps(eval(l))

#Input and output files
rating_input_file = open('ratings_Books.csv','r')
title_input_file = "meta_Books.json.gz"
rating_output_file = open('ratings.csv','w')
title_output_file = open('books.csv','w')
mydict = dict()
user_count = 1
title_count = 1
#Create ratings.csv file and build dictionary 
for l in rating_input_file:
	line = l.split(',')
	user_id_key = line[0]
	book_id_key = line[1]
	if (user_id_key in mydict):
		user_id = mydict[user_id_key]
	else:
		user_id = user_count
		mydict[user_id_key] = user_count
		user_count+=1
	if (book_id_key in mydict):
		book_id = mydict[book_id_key]
	else:
		book_id = title_count
		mydict[book_id_key] = title_count
		title_count+=1
	rating = line[2]
	rating_output_file.write(str(user_id)+','+str(book_id)+','+str(rating)+','+str(randint(10))+'\n')
#Use dictionary created above to create books.csv
for l in parse(title_input_file):
	tempdict = json.loads(l)
	if 'title'  in tempdict and 'asin' in tempdict:
		book_id_key = tempdict['asin']
		if book_id_key in mydict and  isinstance( mydict[book_id_key], int ):
			title_output_file.write(str(mydict[book_id_key])+","+str(tempdict['title'])+'\n')

rating_output_file.close()
title_output_file.close()

