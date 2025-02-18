import frappe
from erpnext_daraz.api.products import get_all_products, get_all_orders

def sync_daraz_orders():
    daraz_orders = get_all_orders()[:10]
    
    if not frappe.db.exists("Customer Group", 'Daraz Customer'):
            customer_group_doc = frappe.get_doc({
            "doctype": "Customer Group",
            "customer_group_name": 'Daraz Customer'
            })
            customer_group_doc.insert()
    
    for order in daraz_orders:
        print(order.get('order_number'))
        
        daraz_customer_name = order.get('address_billing').get('first_name') + " " + order.get('address_billing').get('last_name')
        daraz_billing_phone = order.get('address_billing').get('phone')
        daraz_customer_country = order.get('address_billing').get('country')
        
        if not frappe.db.exists("Customer", daraz_customer_name):
            customer_doc = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": daraz_customer_name,
            "customer_type": 'Individual',
            "customer_group": 'Daraz Customer',
            "territory":daraz_customer_country,
            "mobile_number" : daraz_billing_phone,
            "city" : order.get('address_billing').get('city'),
            "country" :daraz_customer_country ,
            "address_line1" : order.get('address_billing').get('address1'),
            "address_line2" : order.get('address_billing').get('address2'),
            })
            customer_doc.insert()
            
            
        new_sales_order = frappe.new_doc("Sales Order")
        new_sales_order.customer = daraz_customer_name
        new_sales_order.po_no = order.get('order_number')
        new_sales_order.transaction_date = order.get('created_at')
        
        new_sales_order.flags.ignore_mandatory = True
        new_sales_order.flags.created_by_sync = True
        new_sales_order.insert()

    
    

def sync_daraz_items():
    daraz_products = get_all_products()
    for product in daraz_products:
        item_code = str(product.get("item_id"))
        item_name = (product["attributes"].get("name_en") or product["attributes"].get("name"))[:140]
        description = product["attributes"].get("description_en") or product["attributes"].get("description")
        price = product["skus"][0].get("price")
        standard_rate = product["skus"][0].get("special_price", price)
        stock_uom = "Nos"
        item_group = "Daraz Items"  # Custom Item Group
        # Ensure the item group exists
        if not frappe.db.exists("Item Group", item_group):
            item_group_doc = frappe.get_doc({
            "doctype": "Item Group",
            "item_group_name": item_group,
            "parent_item_group": "All Item Groups",
            "is_group": 0
            })
            item_group_doc.insert()
        
        # Ensure the brand exists
        brand = product["attributes"].get("brand", "No Brand")
        if not frappe.db.exists("Brand", brand):
            brand_doc = frappe.get_doc({
            "doctype": "Brand",
            "brand": brand
            })
            brand_doc.insert()
        
        images = product.get("images", [])
        image = images[0] if images else None
        disabled = 0 if product.get("status", "").lower() == "active" else 1
        
        # Check if the item already exists
        item = frappe.db.get_value("Item", {"item_code": item_code})
        
        if item:
            # Update existing item
            frappe.db.set_value("Item", item_code, {
                "item_name": item_name,
                "description": description,
                "standard_rate": standard_rate,
                "item_group": item_group,
                "stock_uom": stock_uom,
                "brand": brand,
                "image": image,
                "disabled": disabled,
            })
        else:
            # Create new item
            new_item = frappe.get_doc({
                "doctype": "Item",
                "item_code": item_code,
                "item_name": item_name,
                "description": description,
                "standard_rate": standard_rate,
                "item_group": item_group,
                "stock_uom": stock_uom,
                "brand": brand,
                "image": image,
                "disabled": disabled,
            })
            new_item.insert()
        
        frappe.db.commit()