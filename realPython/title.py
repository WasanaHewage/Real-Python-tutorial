import yaml

# Dump multiple YAML documents
print(yaml.dump_all([
    {"title": "Document #1"},
    {"title": "Document #2"},
    {"title": "Document #3"},
]))
