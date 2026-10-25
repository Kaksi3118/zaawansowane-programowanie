def is_even(number: int) -> bool:
    return number % 2 == 0


if is_even(10) is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

if is_even(9) is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
