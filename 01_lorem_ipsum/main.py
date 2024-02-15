import re
"""
 
,kf ,kf ,kf
sdasd sda sda
"""
result = re.findall(r'\b\w{4}\b', text)

print(result)
