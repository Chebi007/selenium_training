


def test_check_stickers(app):
    for count in app.main.count_stickers_on_products():
        assert count == 1