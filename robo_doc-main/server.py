from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from chat import chat
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template("auth.html",name ="sampie" )

@app.route('/chatbot')
def chatbot():
   return send_from_directory("bot_frontend/public","index.html")

@socketio.on('user_input',namespace='/test')
def handle_my_custom_event(json):
   emit('bot_response',{'response' : chat(json['data'])}, namespace='/test')
   print(json)

if __name__ == '__main__':
   # app.run(debug = True)
   socketio.run(app,debug=True)