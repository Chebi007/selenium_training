

def test_countries_order(app):
    list_of_countries = app.admin.get_list_of_countries()
    list_of_countries_sorted = sorted(list_of_countries)
    assert list_of_countries == list_of_countries_sorted

def test_zones_order_from_countries(app):
    dict = app.admin.get_zones_from_countries()
    for key in dict:
        assert dict[key] == sorted(dict[key])

def test_zones_order_from_geo_zones(app):
    dict = app.admin.get_zones_from_geozones()
    for key in dict:
        assert dict[key] == sorted(dict[key])
