import yaml
import io

# Load YAML from a StringIO stream (text)
yaml_text_stream = io.StringIO("name: Иван")
data_from_text_stream = yaml.safe_load(yaml_text_stream)
print(data_from_text_stream)  # Output: {'name': 'Иван'}

# Load YAML from a BytesIO stream (binary)
yaml_binary_stream = io.BytesIO(b"name: \xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd")
data_from_binary_stream = yaml.safe_load(yaml_binary_stream)
print(data_from_binary_stream)  # Output: {'name': 'Иван'}

# Load YAML from a string
yaml_string = "name: Иван"
data_from_string = yaml.safe_load(yaml_string)
print(data_from_string)  # Output: {'name': 'Иван'}


with open("sample.yaml", mode="w", encoding="utf-8") as file:
    file.write("name: Иван")

# Load YAML from the file
with open("sample.yaml", mode="r", encoding="utf-8") as file:
    data_from_file = yaml.safe_load(file)
print(data_from_file)  # Output: {'name': 'Иван'}



# Load YAML from a StringIO stream (text)
yaml_text_stream = io.StringIO("name: Иван")
data_from_text_stream = yaml.safe_load(yaml_text_stream)
print(data_from_text_stream)  # Output: {'name': 'Иван'}

# Load YAML from a BytesIO stream (binary)
yaml_binary_stream = io.BytesIO(b"name: \xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd")
data_from_binary_stream = yaml.safe_load(yaml_binary_stream)
print(data_from_binary_stream)  # Output: {'name': 'Иван'}
