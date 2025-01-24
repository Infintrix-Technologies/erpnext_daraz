# -*- coding: utf-8 -*-

from erpnext_daraz.daraz_sdk.lazop.base import LazopClient, LazopRequest, LazopResponse

# params 1 : gateway url
# params 2 : appkey
# params 3 : appSecret
client = LazopClient('https://api.daraz.pk/rest', '501290', 'ZRcsmsiTHzMVwoUXnAXQnQYgWqj9JRnC')

# create a api request set GET mehotd
# default http method is POST
request = LazopRequest('/mock/api/get','GET')

# simple type params ,Number ,String
request.add_api_param('api_id','1')

response = client.execute(request)
#response = client.execute(request,access_token)

# response type nil,ISP,ISV,SYSTEM
# nil ：no error
# ISP : API Service Provider Error
# ISV : API Request Client Error
# SYSTEM : Lazop platform Error
print(response.type)

# response code, 0 is no error
print(response.code)

# response error message
print(response.message)

# response unique id
print(response.request_id)

# full response
print(response.body)
    
