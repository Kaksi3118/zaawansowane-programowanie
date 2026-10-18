#zad1
names = ['Krystian', 'Maksymilian', 'Kacper', 'Michał', 'Krzysztof']
for name in names:
    print(name)
#zad2
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2)

number_mno = [number * 2 for number in numbers]
print(number_mno)

ten_numbers = range(1, 11)

#zad3
for number in ten_numbers:
    if number%2 == 0:
        print(number)
#zad4

i=0
for number in ten_numbers:
        i+=1
        if i%2 == 0:
            print(number) 