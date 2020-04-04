

def test_check_left_menu(app):
    app.admin.check_left_menu()
    app.session.logout()
