# -*- coding: utf-8 -*-

import lazop

# params 1 : gateway url
# params 2 : appkey
# params 3 : appSecret
client = lazop.LazopClient('https://api.lazada.test/rest', '${appKey}', '${appSecret}')

# create a api request
request = lazop.LazopRequest('/xiaoxuan/mockfileupload')

# simple type params ,Number ,String
request.add_api_param('file_name','pom.xml')

# file params, value should be file content
request.add_file_param('file_bytes',open('/Users/xt/Documents/work/tasp/tasp/pom.xml').read())

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
    
    
