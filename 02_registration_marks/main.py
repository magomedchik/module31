import re



text_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666 Б992ТЕ766 тест мастер ветки'

result_personal_cars = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text_numbers)
result_taxi = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', text_numbers)
print('Список номеров частных автомобилей: ', result_personal_cars)
print('Список номеров такси: ', result_taxi)