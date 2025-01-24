# client = lazop.LazopClient(url, appkey ,appSecret)
# request = lazop.LazopRequest('/order/get','GET')
# request.add_api_param('order_id', '16090')
# response = client.execute(request, access_token)
# print(response.type)
import json
import lazop
import frappe
import time
from erpnext_daraz.api.shared import get_daraz_client
def save_daraz_auth_settings(data):
    doc = frappe.get_doc('Daraz Setting')
    doc.auth_token_data = data
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    

def refresh_session():
    client = get_daraz_client()
    doc = frappe.get_doc('Daraz Setting')
    data = json.loads(doc.auth_token_data)
    
    refresh_token = data['refresh_token']
    try:
        user_info = data['user_info']
    except:
        user_info = {}
    request = lazop.LazopRequest('/auth/token/refresh')
    request.add_api_param('refresh_token', refresh_token)
    response = client.execute(request)
    
    body = response.body
    body['user_info'] = user_info

    save_daraz_auth_settings(body)
    
    return response.body


def authenticate_daraz(code):
    client = get_daraz_client()
    request = lazop.LazopRequest('/auth/token/create')
    request.add_api_param('code',code )
    response = client.execute(request)
    body = response.body
    save_daraz_auth_settings(body)
    
    return response.body
    
def get_access_token():
    doc = frappe.get_doc('Daraz Setting')
    if doc.auth_token_data:
        data = json.loads(doc.auth_token_data)
    
        return data.get('access_token', None)
    return None
    
def print_hello():
    
    client = get_daraz_client()
    
    request = lazop.LazopRequest('/products/get','GET')
    
    access_token = get_access_token()
    
    request.add_api_param('filter', 'test')


    # simple type params ,Number ,String
    request.add_api_param('api_id','1')

    # response = client.execute(request)
    response = client.execute(request,access_token)

    # response type nil,ISP,ISV,SYSTEM
    # nil ：no error
    # ISP : API Service Provider Error
    # ISV : API Request Client Error
    # # SYSTEM : Lazop platform Error
    # print(response.type)

    # # response code, 0 is no error
    print("ERROR:",  response.code ==0)

    # # response error message
    # print(response.message)

    # # response unique id
    # print(response.request_id)

    # full response
    # print(json.dumps(response.body, indent=4))
        
@frappe.whitelist(allow_guest=True, methods=["GET"])
def login_daraz():
    code = frappe.request.args.get('code')
    if not code:
        frappe.throw("Missing 'code' parameter")
    data = authenticate_daraz(code)    
    
    
    redirect_url = "/app/daraz-setting"
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = redirect_url


# https://api.daraz.pk/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://erp.infintrixtech.com/api/daraz&client_id=501290