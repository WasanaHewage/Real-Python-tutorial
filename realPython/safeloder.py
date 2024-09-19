import yaml

email_message = """\
message:
  date: 2022-01-16 12:46:17Z
  from: john.doe@domain.com
  to:
    - bobby@domain.com
    - molly@domain.com
  cc:
    - jane.doe@domain.com
  subject: Friendly reminder
  content: |
    Dear XYZ,

    Lorem ipsum dolor sit amet...
  attachments:
    image1.gif: !!binary
        R0lGODdhCAAIAPAAAAIGAfr4+SwAA
        AAACAAIAAACDIyPeWCsClxDMsZ3CgA7
"""

parsed_email = yaml.safe_load(email_message)

print(parsed_email)
