from resources.product import ProductResource, ProductList
from resources.orders import OrderResource, OrderList


def set_routes(api):
    api.add_resource(ProductResource, '/product/<int:id>')
    api.add_resource(ProductList, "/products")

    api.add_resource(OrderResource, "/order/<int:id>")
    api.add_resource(OrderList, "/orders")


