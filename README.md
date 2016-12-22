# BookRecommender
##Authors: 
jf3030, yp2419<br>
##Team ID:
201612-37<br>
##Instruction:
Make the recommendation using the ratings given by costumers. Datasets and trained models are too big, so they are not listed here. Using Flask to build a webserver to show the result of recommendtation.<br>
##Architecture and explanations:
```
Book_Recommender/
├── BookRecommend.py
├── my_recommend.py
├── personalRatings.txt
├── prepare_data.py
├── rate_books.py
├── server.py
└── templates/
    ├── index.html
    ├── start.html
    └── rate.html
```
1. `BooksRecommend.py`: Import datasets, train model then save it.<br>
2. `my_recommend.py`: Load trained model and personal ratings to get recommendtation.<br>
3. `personalRatings.txt`: A text file to save personal ratings.<br>
4. `prepare_data.py`: Pre-process datasets to adjust model.<br>
5. `rate_books.py`: Generate `personalRatings.txt` according to users's ratings.<br>
6. `server.py`: Webserver to show the result of recommendation.<br>
7. `templates/`: The folder to store html files, which are used to build the web page.<br>
##Requirements:
1. pyspark<br>
2. python2 or python3<br>
3. flask<br>
4. numpy<br>
##Usage:
1. Set path of spark home. E.g.`export SPARK_HOME=/path/to/spark/home`
1. run webserver by `python server.py`