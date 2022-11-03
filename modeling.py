# import sqlite3
# import pandas as pd
# from sqlalchemy import create_engine
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from category_encoders import OrdinalEncoder
# # from sklearn.pipeline import make_pipeline
# # from sklearn.metrics import classification_report, ConfusionMatrixDisplay, precision_score, recall_score, f1_score, roc_curve
# # from lightgbm import LGBMClassifier
# # import pickle

# #msqlite db 연결, pandas를 통해 table 읽어오기
# engine = create_engine('sqlite:///waterpoint.db', convert_unicode=True)
# conn = engine.connect()
# df = pd.read_sql_table('waterpoint_model', conn, )

# #데이터를 train과 validation, test데이터로 나눠줌
# train, test = train_test_split(df, train_size=0.80, test_size=0.20, stratify=df['status'], random_state=2)
# train, val = train_test_split(train, train_size=0.80, test_size=0.20, stratify=train['status'], random_state=2)

# #데이터를 X,y로 분리
# target = 'status'
# features = df.drop(columns=[target]).columns

# X_train = train[features]
# y_train = train[target]
# X_val = val[features]
# y_val = val[target]
# X_test = test[features]
# y_test = test[target]

# #LightGBM 모델
# pipe_lgb = make_pipeline(
#     OrdinalEncoder(),
#     LGBMClassifier(objective ='multiclass',
#                    num_class=3,learning_rate= 0.1,
#                    num_leaves= 100, max_depth= 50, min_data_in_leaf=5,
#                    feature_fraction= 0.5, bagging_fraction= 0.8, bagging_freq= 7,
#                    boosting_type= 'gbdt', random_state=29,
#                    class_weight = 'balanced'))

# #모델 학습
# pipe_lgb.fit(X_train, y_train)

# #테스트데이터 예측
# y_pred_final = pipe_lgb.predict(X_test)


# with open('model.pkl','wb') as pickle_file:
#     pickle.dump(pipe_lgb, pickle_file)
    
#lightgbm 설치 오류로 lightgbm 사용 못함, 모델 변경
#lightgbm 설치 오류로 lightgbm 사용 못함, 모델 변경
#lightgbm 설치 오류로 lightgbm 사용 못함, 모델 변경
#lightgbm 설치 오류로 lightgbm 사용 못함, 모델 변경