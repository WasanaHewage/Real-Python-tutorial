import yaml

# Serialize a Python object using the default YAML dumper (implemented in Python)
print(yaml.dump(3.14, Dumper=yaml.Dumper))

# Serialize the same Python object using the YAML dumper implemented in C
print(yaml.dump(3.14, Dumper=yaml.CDumper))
