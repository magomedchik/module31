import re
"""
ssacas 
,kf ,kf ,kf
sasaca
"""
result = re.findall(r'\b\w{4}\b', text)

print(result)
 