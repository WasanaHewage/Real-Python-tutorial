import yaml

data = yaml.safe_load("""
Shipping Address: &shipping |
    1111 College Ave
    Palo Alto
    CA 94306
    USA
Invoice Address: *shipping
""")

print(data)
