import yaml

data = yaml.safe_load("""
married: false
spouse: null
date_of_birth: 1980-01-01
age: 42
kilograms: 80.7
""")

print(data)
