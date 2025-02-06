# [001]查詢本期用戶帳單API

import pytest
import logging
import json
#from test_data.get_data_from_excel import process_excel_data   #多一個excel
from test_data.get_data_from_excel import process_data
from api_objects.GetBillingInfoAPIs import getBillingInfoAPIs
from utils.object_utils import ObjectUtils

# EXCEL 路徑
file_path = r'test_data/GetBillingInfoAPIs.xlsx'
sheet_name = '工作表1'
data_dicts = process_data(file_path, sheet_name)

@pytest.mark.parametrize('data_dict', data_dicts)
def test_GetBillingInfoAPIs_success(data_dict, get_session):

    request_params = data_dict['params']
    excel_result = data_dict['result']

    try:
        querySvcItem_apis = getBillingInfoAPIs(get_session)
 
        request_params = json.loads(request_params)
        response = querySvcItem_apis.get_data_info(request_params)

        if response.status_code != 200:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
            assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"
            return
        
        response_data = json.loads(response.text)
        excel_data = json.loads(excel_result)

        ObjectUtils.equal_str("Json 內容比對失敗", excel_data, response_data) 


    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        raise

    finally:
        logging.info("END")
