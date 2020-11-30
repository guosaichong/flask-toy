from flask import Flask,request,render_template,redirect,session
from setting import DebugConfig,TestingConfig
from flask_login import current_user
from toy_app.views import toy

app=Flask(__name__)
app.config.from_object(DebugConfig)


app.register_blueprint(toy)

if __name__ == "__main__":
    app.run()