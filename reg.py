import re


title = "Regular Expressions in 10 different languages"
result = re.match(r'.*\d+.*', title)

match = re.search(r'(\d+)', title)
# This will return None match is not found
if (match):
    print('There are {} languages represented.'.format(match.group(1))