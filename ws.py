from flask import Flask, request, render_template,redirect
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket
import json

app = Flask(__name__)

socket_dict={}


@app.route("/ws/<username>")
def ws(username):
    sock = request.environ.get("wsgi.websocket")  # type:WebSocket
    if not sock:
        return "请使用WS协议连接"
    socket_dict[username]=sock
    print(socket_dict)
    while True:
        try:
            msg = sock.receive()
            print(type(msg),msg)
            
        except:
            break
        print(socket_dict.values())
        for so in socket_dict.values():
            if so == sock:
                continue
            try:
                so.send(msg)
            except:
                continue
        # print(msg)

    return "200"


@app.route("/",methods=["GET"])
def index():
    
    return render_template("ws_client.html")


if __name__ == "__main__":
    http_serv = WSGIServer(("0.0.0.0", 9527), app,
                           handler_class=WebSocketHandler)
    http_serv.serve_forever()
