import yaml

data = yaml.full_load("""
list: [1, 2]
tuple: !!python/tuple [1, 2]
""")

print(data)
