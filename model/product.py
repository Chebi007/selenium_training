

class Product:

    def __init__(self, id=None, name=None, code=None, quantity=None, date_valid_from=None, date_valid_to=None,
                 manufacturer=None, supplier=None, keywords=None,  short_description=None, description=None,
                 head_title=None, meta_description=None,
                 price=None, regular_price=None, campaign_price=None):
        self.id = id
        self.name = name
        self.code = code
        self.quantity = quantity
        self.date_valid_from = date_valid_from
        self.date_valid_to = date_valid_to
        self.manufacturer = manufacturer
        self.supplier = supplier
        self.keywords = keywords
        self.short_description = short_description
        self.description = description
        self.head_title = head_title
        self.meta_description = meta_description
        self.price = price
        self.regular_price = regular_price
        self.campaign_price = campaign_price

    def __repr__(self):
        return "\"%s %s %s %s\"" % (self.name, self.manufacturer, self.regular_price, self.campaign_price)

    def __eq__(self, other):
        return self.name == other.name and self.code == other.code