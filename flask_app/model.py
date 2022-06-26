import os
import csv
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
import joblib, pickle

dataset = pd.read_csv('Airpollution_dataset.csv')

target = 'total_bad'

# 학습, 훈련 데이터 분리
train, test = train_test_split(dataset, train_size = 0.8, stratify= dataset[target], random_state=2)

#훈련, 검증 데이터 분리
train, val = train_test_split(train, train_size = 0.8, stratify= train[target], random_state=2)

#타겟 분리
features = train.drop(columns=[target]).columns

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]

# X_test = X_test[['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']]
# X_val = X_val[['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']]
# X_train = X_train[['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']]



#랜덤포레스트 객체 생성 및 학습
pipe = make_pipeline(
    SimpleImputer(),
    RandomForestClassifier())
    # max_depth = 6,
    # n_estimators = 200,
    # class_weight = 'balanced',
    # n_jobs = -1,
    # random_state = 2,
    # oob_score = True))

pipe.fit(X_train, y_train)

y_val_pred = pipe.predict(X_val)

#모델 저장
"""from sklearn.externals import joblib 
# 객체를 pickled binary file 형태로 저장한다 
file_name = 'object_01.pkl' 
joblib.dump(obj, file_name) """
# joblib.dump(pipe, 'model.joblib')

#모델 읽을 때
"""from sklearn.externals import joblib 
# pickled binary file 형태로 저장된 객체를 로딩한다 
file_name = 'object_01.pkl' 
model(pipe) = joblib.load('model.joblib')
"""

pickle.dump(pipe, open('airpollution.pkl', 'wb'))

model = pickle.load(open('airpollution.pkl', 'rb'))
