

def test_compare_name_price(app):
    product_on_main_page = app.product.get_product_by_index_on_main_page(0, "campaigns")
    product_on_edit_page = app.product.get_product_by_index_on_edit_page(0, "campaigns")
    assert product_on_main_page == product_on_edit_page

def test_regular_price_css(app):
    dict = app.product.get_css_properties_for_regular_price_on_main_page()
    dict2 = app.product.get_css_properties_for_regular_price_on_edit_page()
    assert dict["color"][0] == dict["color"][1] == dict["color"][2]
    assert dict["text_decoration_line"] == dict2["text_decoration_line"] == "line-through"
    assert dict2["color"][0] == dict2["color"][1] == dict2["color"][2]

def test_campaign_price_css_firefox(app):
    dict = app.product.get_css_properties_for_campaign_price_on_main_page()
    dict2 = app.product.get_css_properties_for_campaign_price_on_edit_page()
    assert dict["color"][1] == dict["color"][2] == dict2["color"][1] == dict2["color"][2] == '0'
    assert dict["font_weight"] == '900'
    assert dict2["font_weight"] == '700'

def test_campaign_price_css_ie(app):
    dict = app.product.get_css_properties_for_campaign_price_on_main_page()
    dict2 = app.product.get_css_properties_for_campaign_price_on_edit_page()
    assert dict["color"][1] == dict["color"][2] == dict2["color"][1] == dict2["color"][2] == '0'
    assert dict["font_weight"] == '900'
    assert dict2["font_weight"] == '900'

def test_campaign_price_css_chrome(app):
    dict = app.product.get_css_properties_for_campaign_price_on_main_page()
    dict2 = app.product.get_css_properties_for_campaign_price_on_edit_page()
    assert dict["color"][1] == dict["color"][2] == dict2["color"][1] == dict2["color"][2] == '0'
    assert dict["font_weight"] == '700'
    assert dict2["font_weight"] == '700'

def test_compare_font_sizes_on_main_page(app):
    dict = app.product.get_css_properties_for_regular_price_on_main_page()
    dict2 = app.product.get_css_properties_for_campaign_price_on_main_page()
    font_size_regular_price = dict["font_size"]
    font_size_campaign_price = dict2["font_size"]
    assert font_size_regular_price < font_size_campaign_price

def test_compare_font_sizes_on_edit_page(app):
    dict = app.product.get_css_properties_for_regular_price_on_edit_page()
    dict2 = app.product.get_css_properties_for_campaign_price_on_edit_page()
    font_size_regular_price = dict["font_size"]
    font_size_campaign_price = dict2["font_size"]
    assert font_size_regular_price < font_size_campaign_price