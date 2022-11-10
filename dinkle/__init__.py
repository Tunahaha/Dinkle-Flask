from flask import Flask
from dinkle.route import index,hp1,monitor1,image,fix,form,information,statics
from dinkle.route import data,cost,detail_image,sta


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/index','index',index)
    app.add_url_rule('/hp1','hp1',hp1)
    app.add_url_rule('/monitor1','monitor1',monitor1)
    app.add_url_rule('/image','image',image)
    app.add_url_rule('/fix','fix',fix)
    app.add_url_rule('/form','form',form)
    app.add_url_rule('/information','information',information)
    app.add_url_rule('/statics','statics',statics)
    return app