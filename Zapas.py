char = str(input('Введите символ: '))

for i in range (1,6):
   print(char*i)

char = str(input('Введите символ: '))

print (char)
print (char+char)
print (char+char+char)
print (char+char+char+char)
print (char+char+char+char+char)

month_number = input('Введите номер месяца: ')

d = {"1":"Январь", "2":"Февраль", "3":"Март", "4":"Апрель", "5":"Май", "6":"Июнь", "7":"Июль", "8":"Август", "9":"Сентябрь", "10":"Октрябрь", "11":"Ноябрь", "12":"Декабрь"}

print (d.get(month_number,"Такого месяца не существует"))