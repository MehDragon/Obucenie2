nums = input("Введите числа через пробел: ")

numbers = []
for num_str in nums.split():
    numbers.append(int(num_str))

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Список чётных чисел:", even_numbers)


word = input('Введите слово: ')

cleaned_word = word.replace(" ", "").lower()

if cleaned_word == cleaned_word[::-1]:
    print("Слово является палиндромом.")
else:
    print("Слово не является палиндромом.")