import yaml

data = yaml.safe_load("""
number: 3.14
string: !!str 3.14
""")

print(data)
