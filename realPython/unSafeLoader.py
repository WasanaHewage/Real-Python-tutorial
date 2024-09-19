import yaml

data = yaml.unsafe_load("""
custom_class: !!python/object:__main__.CustomClass {}
function_call: !!python/name:__main__.my_function ''
shell_command: !!python/object/apply:subprocess.Popen ["ls", []]
""")

print(data)
