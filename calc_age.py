from datetime import datetime 
year = int(input('Какого ты года рождения?'))
current_year = datetime.now().year
age = current_year - year
print('Тебе', age, 'лет!') 