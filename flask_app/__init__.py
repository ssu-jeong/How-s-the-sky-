import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

"""db객체를 create_app함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수 없어서 
db, migrate와 같은 객체를 creat_app 함수 밖에서 생성하고
실제 객체 초기화는 create_app함수에서 init_app함수를 통해 진행"""
db = SQLAlchemy() 
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # config.py파일에 작성한 항목을 app.config 환경 변수로 부르기 위해 추가한 코드


    #ORM 
    db.init_app(app)
    # migrate.init_app(app, db) 
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    #블루프린트
    from .views import index_view, predict_view
    app.register_blueprint(index_view.bp)
    app.register_blueprint(predict_view.bp)

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    return app


if __name__ == '__main__' : 
    app = create_app()
    app.run(debug=True)