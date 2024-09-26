nums = input("Введите числа через пробел: ")

numbers = list(map(int, nums.split()))
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Список чётных чисел:", even_numbers)