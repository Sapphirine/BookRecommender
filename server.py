import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
from my_recommend import recommend
from rate_books import rates

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/start')
def start():
  return render_template("start.html")

@app.route('/rate', methods=['POST'])
def rate():
  # return test_func(name)
  context=dict()
  ratings = request.form['ratings']
  rcmd = recommend(rates(ratings)).split("\n")
  # return render_template("start.html")
  return render_template("rate.html",data=rcmd)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    HOST, PORT = host, port
    print ("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=True, threaded=threaded)


  run()
