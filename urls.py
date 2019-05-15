
BASE_URL = "https://apiv2.shiprocket.in"


class Authentication(object):
    access_token = "/v1/external/auth/login"

class Order(object):
    create_custom_order = "/v1/external/orders/create/adhoc"
    create_channel_order = "/v1/external/orders/create"
    update_order_address = "/v1/external/orders/address/update"
    cancel_order = "/v1/external/orders/cancel"
    bulk_import = "/v1/external/orders/import"
    all_orders = "/v1/external/orders"
    order_details = "/v1/external/orders/show/{}"
    sync_status = "/v1/external/orders/status"
    fetch_orders_channel = "/v1/external/orders/fetch"

class Shipment(object):
    all_shipment_details = "/v1/external/shipments"
    specific_shipment_details = "/v1/external/shipments/{}"


class Courier(object):
    """docstring for Couriers"""
    check_serviceability = "/v1/external/courier/serviceability/"
    check_international_serviceability = "/v1/external/courier/international/serviceability"
    create_awb = "/v1/external/courier/assign/awb"
