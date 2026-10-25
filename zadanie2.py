# 2a
names = ["Krystian", "Maksymilian", "Kacper", "Michał", "Krzysztof"]
for name in names:
    print(name)
# 2b
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2)

number_mno = [number * 2 for number in numbers]
print(number_mno)

# for 2c and 2d
ten_numbers = range(1, 11)

# 2c
for number in ten_numbers:
    if number % 2 == 0:
        print(number)
# 2d
i = 0
for number in ten_numbers:
    i += 1
    if i % 2 == 0:
        print(number)
