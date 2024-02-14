import re


# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки

pattern = r'<h3.*>(.+?)</h3>'
result = re.findall(pattern, text)

print(result)