import pandas as pd
import numpy as np

def predict_bike_count(model, season_value, workingday_value, weather_value, month_value):
    """모델과 인자를 전달받으면 바이크 수요량을 반환한다"""
    df_input = pd.DataFrame({"season":[season_value], 
                             "workingday":[workingday_value], 
                             "weather":[weather_value], 
                             "month":[month_value]})
    
    df_struct = pd.read_excel('ml_model/data_structure.xlsx')
    df = pd.concat([df_input, df_struct], ignore_index=True)
    df_ohe = pd.get_dummies(df, columns=df.columns)

    data = df_ohe.iloc[0,:]
    data = pd.DataFrame(data).T
    pred_value = model.predict(data)
    pred_value = round(np.expm1(pred_value)[0], 1)

    return pred_value
