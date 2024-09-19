import yaml

class Person(yaml.YAMLObject):
    yaml_tag = "!Person"
    yaml_loader = yaml.SafeLoader

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# Dumping a Person object to YAML
jdoe_yaml = yaml.dump(Person("John", "Doe"))
print(jdoe_yaml)

# Loading a YAML string back into a Person object
jdoe_object = yaml.safe_load(jdoe_yaml)
print(jdoe_object)
