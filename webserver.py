from flask import Flask,render_template
from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
	id = PrimaryKeyField()
	name = CharField()
	grade = IntegerField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Student],safe=True)

app = Flask(__name__)

@app.route('/hello/<name>')
@app.route('/hello')
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route('/double/<int:num>')
def double(num):
	return '%d' %(2*num)

if __name__ == '__main__':
	app.run(debug=True)
	initialize_db()
	david = Student.create(name='David',grade=95)
	ezra = Student.create(name='Ezra',grade=50)
	db.close()
	for s in Student.select().where(Student.grade<75):
		print("aaa")