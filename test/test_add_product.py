

def test_add_new_product(app, json_products):
    product = json_products
    old_list = app.product.get_list()
    app.product.add_new(product)
    new_list = app.product.get_list()
    old_list.append(product.name)
    assert sorted(old_list) == sorted(new_list)