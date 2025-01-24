import lazop
import frappe


def get_daraz_client() -> lazop.LazopClient:
    daraz_settings = frappe.get_cached_doc('Daraz Setting')
    app_id = daraz_settings.app_id
    app_secret_key = daraz_settings.app_secret_key
    api_endpoint = daraz_settings.api_endpoint
    client = lazop.LazopClient(api_endpoint, app_id, app_secret_key)
    return client