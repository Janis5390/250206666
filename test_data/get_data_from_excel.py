import pandas as pd
import logging

def process_data(file_name,sheet_name):
    df = pd.read_excel(file_name,sheet_name=sheet_name,dtype=str)
    
    #處理缺失值
    df.fillna("n/a", inplace=True)
    
    #轉換成字典並組成列表
    data_dicts = df.to_dict(orient='records')
    
    logging.info(data_dicts)
    return data_dicts