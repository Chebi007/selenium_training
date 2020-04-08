from model.customer import Customer
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/customers.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

def random_digits(prefix, maxlen):
    symbols = string.digits
    return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Customer(tax_id=random_string('9', 9), company=random_string('company', 15),
                     firstname=random_string('firstname', 15),
                     lastname=random_string('lastname', 15),
                     address1=random_string('addresss1', 15),
                     address2=random_string('addresss2', 15),
                     postcode='12345',
                     city=random_string('city', 15),
                     country='United States',
                     zone_code='Arizona',
                     email=random_string('e', 15) + ''.join('@gmail.com'),
                     phone=random_digits('1', 11),
                     password='password',
                     confirmed_password='password'
                     )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))