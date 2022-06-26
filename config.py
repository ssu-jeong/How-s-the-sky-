# config.py

# 파이보에 orm을 적용하기 위한 설정파일
import os 

# 이는 현재 수행중인 코드를 담고 있는 파일이 위치한 경로를 보여준다.
BASE_DIR = os.path.dirname(__file__)


"""SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소
air.db라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장하려는 것.
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') # 배포한 상태에선 os가 해로쿠주소"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'air.db'))

# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

"""이렇게 config파일을 만들었으면 __init__.py에 orm 적용하러 가야함.
지금 설정한 내용은 air.db라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장하려는 것이다."""


#SECRET_KEY = "dev"