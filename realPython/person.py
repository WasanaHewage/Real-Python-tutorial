import yaml
from modelss import Person

# Flow style
person_yaml_flow = """
!!python/object/apply:models.Person [John, Doe]
"""

# Block style
person_yaml_block = """
!!python/object/apply:models.Person
  - John
  - Doe
"""

person_flow = yaml.unsafe_load(person_yaml_flow)
person_block = yaml.unsafe_load(person_yaml_block)
print(person_flow.first_name, person_flow.last_name)
print(person_block.first_name, person_block.last_name)



# Using args and kwds
person_yaml_args_kwds = """
!!python/object/apply:models.Person
args: [John]
kwds: {last_name: Doe}
"""

person_args_kwds = yaml.unsafe_load(person_yaml_args_kwds)
print(person_args_kwds.first_name, person_args_kwds.last_name)
