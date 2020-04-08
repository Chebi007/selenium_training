

def test_create_account(app, json_customers):
    customer = json_customers
    app.account.create_account(customer)
    app.session.logout_on_main_page()
    app.session.login_on_main_page(customer)
    app.session.logout_on_main_page()