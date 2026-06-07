product_catalog = { "SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50}, "SKU456": {"name": "Gadget B", "price": 34.95, "quantity": 25}, "SKU789": {"name": "Gizmo C", "price": 9.99, "quantity": 100} 
}
sku_to_find = "SKU123"
if sku_to_find in product_catalog:
    product = product_catalog[sku_to_find]
    name = product["name"]
    price = product["price"]

    print(f"The price of {name} is ${price}")