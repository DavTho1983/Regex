import re

split_term = '@'

email = 'user@gmail.com'
email2 = 'david@gmail.com'.split('@')

print(re.split(split_term, email))
print(email2)
