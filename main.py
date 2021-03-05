import flask
from flask import Flask, render_template, redirect
app = Flask('HK Campaign| Air Pollution and Shark Finning Official Website')
#Redirect if no route specified
@app.route('/')
def redirect_to_home():
  print("Pong!")
  return redirect('https://HK-Campaign-Air-Pollution-and-Shark-Finning.98129182.repl.co/home',302)
@app.route('/home')
def render_home():
  print("Rendering....")
  return(render_template('home.html'))
@app.route('/shark_finning')
def render_shark_finning():
  return(render_template('shark_finning.html'))
@app.route('/air_pollution')
def render_air_pollution():
  return(render_template('air_pollution.html'))
app.run(host='0.0.0.0',port=8080)
