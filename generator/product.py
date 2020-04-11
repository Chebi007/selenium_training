from model.product import Product
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
f = "data/products.json"

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


testdata = [Product(name=random_string('name', 15),
                    code=random_digits("1", 10),
                    quantity=random_digits("2", 4),
                    date_valid_from='2020-04-04',
                    date_valid_to='2021-04-04',
                    manufacturer='ACME Corp.',
                    keywords=random_string('keyword', 15),
                    short_description=random_string('short_description', 20),
                    description=random_string('long description', 250),
                    head_title=random_string('head title', 15),
                    meta_description=random_string('meta description', 30),
                    price=random_digits('2', 4)
                    )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))