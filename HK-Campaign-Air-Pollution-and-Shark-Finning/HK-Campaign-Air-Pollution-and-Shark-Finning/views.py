#Import all functions from api.py. Funny how there's only one isn't it
from api import *
from __init__ import app
import threading
from flask import Flask, render_template, redirect, make_response
app = Flask(__name__)
#Redirect if no route specified
async def air_api_task():
  while True:
    await get_data()
    time.sleep(360)
def define_response():
  with open('air_aqi.txt','r') as txtfile:
    return (txtfile.read())
def api_task_loop():
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(air_api_task())
  loop.close()
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
@app.route('/petition')
def render_petition_page():
  return(render_template('petition.html'))
@app.route('/games')
def render_games():
  return(render_template('games.html'))
@app.route('/aqi_stats')
def render_aqi_stats():
  return(render_template('aqi_stats.html'))
@app.route('/air_aqi.txt')
def return_data():
  print("Getting data.")
  response = make_response(str(define_response()), 200)
  response.mimetype = "text/plain"
  return(response)
@app.errorhandler(404)
def page_not_found(e):
  return(render_template('404.html'))
thread = threading.Thread(target = api_task_loop)
thread.start()
app.run(host = '0.0.0.0', port = 8080, threaded = True)