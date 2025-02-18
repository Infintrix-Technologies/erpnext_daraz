
import json
import lazop
import frappe
import time
from erpnext_daraz.api.shared import get_daraz_client
from erpnext_daraz.api.auth import get_access_token
from datetime import datetime, timedelta
import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# def get_all_products(filter='all', limit=50):
#     client = get_daraz_client()
#     access_token = get_access_token()
#     offset = 0
#     all_products = []
    
#     while True:
#         print("Page: ", offset // limit + 1)
#         request = lazop.LazopRequest('/products/get', 'GET')
#         request.add_api_param('filter', filter)
#         request.add_api_param('limit', str(limit))
#         request.add_api_param('offset', str(offset))
#         response = client.execute(request, access_token)
#         if response.code != '0':
#             print("Error:", response.message)
#             break
#         products = response.body.get('data', {}).get('products', [])
#         print("Products:", len(products))
#         all_products.extend(products)
#         if len(products) < limit:
#             break
#         offset += limit
#     print("Total Products are: ", len(all_products))
    
#     with open(os.path.join(BASE_DIR, "sample",'get_all_products.json'), 'w') as f:
#         json.dump(all_products, f)
#     return all_products

def get_all_products(filter='all', limit=50):
    file_path = os.path.join(BASE_DIR, "sample", 'get_all_products.json')
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            all_products = json.load(f)
        print("Loaded products from file.")
        return all_products

    client = get_daraz_client()
    access_token = get_access_token()
    offset = 0
    all_products = []
    
    while True:
        print("Page: ", offset // limit + 1)
        request = lazop.LazopRequest('/products/get', 'GET')
        request.add_api_param('filter', filter)
        request.add_api_param('limit', str(limit))
        request.add_api_param('offset', str(offset))
        response = client.execute(request, access_token)
        if response.code != '0':
            print("Error:", response.message)
            break
        products = response.body.get('data', {}).get('products', [])
        # print("Products:", len(products))
        all_products.extend(products)
        if len(products) < limit:
            break
        offset += limit
        
    # Save the products to the file
    with open(file_path, 'w') as f:
        json.dump(all_products, f)
    
    return all_products

def get_all_orders(status='all', limit=50, mp3_order=None, update_before=None, sort_direction=None, offset=0, update_after=None, sort_by=None, created_before=None, created_after=None):
    client = get_daraz_client()
    access_token = get_access_token()
    all_orders = []
    days =99999
    
    file_path = os.path.join(BASE_DIR, "sample", 'get_all_orders.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            all_orders = json.load(f)
        print("Loaded orders from file.")
        return all_orders


    # Calculate the date 7 days ago
    if created_after is None and update_after is None:
        seven_days_ago = datetime.now() - timedelta(days=days)
        created_after = seven_days_ago.strftime('%Y-%m-%dT%H:%M:%S%z')

    while True:
        print("Page: ", offset // limit + 1)
        request = lazop.LazopRequest('/orders/get', 'GET')
        request.add_api_param('status', status)
        request.add_api_param('limit', str(limit))
        request.add_api_param('offset', str(offset))

        if mp3_order is not None:
            request.add_api_param('mp3_order', str(mp3_order))
        if update_before is not None:
            request.add_api_param('update_before', update_before)
        if sort_direction is not None:
            request.add_api_param('sort_direction', sort_direction)
        if sort_by is not None:
            request.add_api_param('sort_by', sort_by)
        if created_before is not None:
            request.add_api_param('created_before', created_before)
        if created_after is not None:
            request.add_api_param('created_after', created_after)
        if update_after is not None:
            request.add_api_param('update_after', update_after)

        response = client.execute(request, access_token)
        if response.code != '0':
            print("Error:", response.message)
            break

        orders = response.body.get('data', {}).get('orders', [])
        print("Orders:", len(orders))
        all_orders.extend(orders)
        if len(orders) < limit:
            break
        offset += limit

    print("Total Orders are: ", len(all_orders))
    with open(os.path.join(file_path), 'w') as f:
        json.dump(all_orders, f)
    return all_orders


def get_order_items(order_id='206917434692960'):
    file_path = os.path.join(BASE_DIR, "sample", 'get_order_items.json')
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            items = json.load(f)
        print("Loaded order items from file.")
        return items

    client = get_daraz_client()
    access_token = get_access_token()
    request = lazop.LazopRequest('/order/items/get', 'GET')
    request.add_api_param('order_id', order_id)
    response = client.execute(request, access_token)
    if response.code != '0':
        print("Error:", response.message)
        return None
    
    items = response.body.get('data')
    
    # Save the items to the file
    with open(file_path, 'w') as f:
        json.dump(items, f)
    
    return items