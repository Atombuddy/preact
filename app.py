from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/chat")
# def chat():
#     username = request.args.get("username")
#     room = request.args.get("room")
#     if username and room:
#         return render_template("chat.html", username=username, room=room)
#     else:
#         return redirect(url_for("home"))


# this will be handling the data of socket, emited in chat.html
@socketio.on("join_room")
def handle_join_room_event(data):
    # advantage of using app.logger.info is
    # that it will also print the datetime when it was logged
    app.logger.info("{} has joined the room {}".format(data["username"], data["room"]))
    # this will make a particular client to join with particular room id
    join_room(data["room"])
    # sending an announcement of someone joining the room
    socketio.emit("join_room_announcement", data)


@socketio.on("send_message")
def handle_send_message_event(data):
    print(data)
    data["name"] = "Sam"
    app.logger.info("{} has joined the room {}".format(data["name"], data["message"]))

    #  send/emit out the message to other people with same room id
    socketio.emit("receive_message", data)


@socketio.on("leave_room")
def handle_leave_room_event(data):
    print(data)
    app.logger.info("{} has left the room {}".format(data["username"], data["room"]))
    leave_room(data["room"])
    #  send/emit out the message to other people with same room id
    socketio.emit("leave_room_announcement", data, room=data["room"])


# Note:
# SocketIO already has a concept of storing all the socket connection/rooms
