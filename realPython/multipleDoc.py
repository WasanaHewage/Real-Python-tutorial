import yaml

stream = """\
---
3.14
---
name: John Doe
age: 53
---
- apple
- banana
- orange
"""

for document in yaml.safe_load_all(stream):
    print(document)
