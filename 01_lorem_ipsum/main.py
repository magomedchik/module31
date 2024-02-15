import re
"""
тест тест тест
"""
result = re.findall(r'\b\w{4}\b', text)

print(result)
 