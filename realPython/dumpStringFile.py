import yaml

# Dump YAML data to a string
data = {"name": "John"}
yaml_string = yaml.dump(data)
print(yaml_string)

# Dump YAML data to a file in text mode with UTF-8 encoding
with open("file.yaml", mode="wt", encoding="utf-8") as file:
    yaml.dump(data, file)

# Dump YAML data to a file in binary mode with UTF-8 encoding
with open("file1.yaml", mode="wb") as file:
    yaml.dump(data, file, encoding="utf-8")
