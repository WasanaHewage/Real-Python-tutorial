import yaml
import codecs

class User:
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

    def __setstate__(self, state):
        self.name = codecs.decode(state["name"], "rot13")

user_yaml = """
!!python/object:models.User
name: Wbua Qbr
"""

user = yaml.unsafe_load(user_yaml)
print(user.name)  # Output: John Doe
