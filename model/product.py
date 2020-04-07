

class Product:

    def __init__(self, id=None, name=None, code=None, manufacturer=None, price=None, regular_price=None,
                 campaign_price=None):
        self.id = id
        self.name = name
        self.code = code
        self.manufacturer = manufacturer
        self.price = price
        self.regular_price = regular_price
        self.campaign_price = campaign_price

    def __repr__(self):
        return "\"%s %s %s %s\"" % (self.name, self.manufacturer, self.regular_price, self.campaign_price)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and \
               self.code == other.code