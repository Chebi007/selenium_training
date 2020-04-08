

class Customer:

    def __init__(self, id=None, tax_id=None, company=None, firstname=None, lastname=None, address1=None, address2=None,
                 postcode=None, city=None, country=None, zone_code=None, email=None, phone=None, newsletter=None,
                 password=None, confirmed_password=None):
        self.id = id
        self.tax_id = tax_id
        self.company = company
        self.firstname = firstname
        self.lastname = lastname
        self.address1 =address1
        self.address2 = address2
        self.postcode = postcode
        self.city = city
        self.country = country
        self.zone_code = zone_code
        self.email = email
        self.phone = phone
        self.newsletter = newsletter
        self.password = password
        self.confirmed_password = confirmed_password

    def __repr__(self):
        return "\"%s %s\"" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname