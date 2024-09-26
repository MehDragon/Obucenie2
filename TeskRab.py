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


def sum_pairs(numbers):
    sums = []

    for i in range(0, len(numbers) - 1, 2):
        pair_sum = numbers[i] + numbers[i + 1]
        sums.append(pair_sum)

    return sums

input_numbers = input("Введите числа через пробел: ")

number_list = list(map(int, input_numbers.split()))

result = sum_pairs(number_list)
print("Суммы пар чисел:", result)

