import re
"""
бла бла бла 
"""
result = re.findall(r'\b\w{4}\b', text)

print(result)