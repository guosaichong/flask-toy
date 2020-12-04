from flask import Flask,request,render_template
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)

socket_list=[]

@app.route("/ws")
def ws():
    sock=request.environ.get("wsgi.websocket") # type:WebSocket
    socket_list.append(sock)
    print(socket_list)
    while True:
        msg=sock.receive()

        for i in socket_list:
            if i == sock:
                continue
           
            i.send(msg)
    return "200"

@app.route("/")
def index():
    return render_template("ws_client.html")

if __name__ == "__main__":
    http_serv = WSGIServer(("0.0.0.0", 9527), app,
                           handler_class=WebSocketHandler)
    http_serv.serve_forever()
