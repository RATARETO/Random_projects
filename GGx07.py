# case 1 ---------------------------------------------------------------------------------------------------------------
# number = float(input("Введите температуру в цельсиях: "))
#
# print(f"Темпиратура в цельсиях -> Фарингейты: {number} : {number * 9/5 + 32: 0.2f}")
# print(f"Темпиратура в цельсиях ->   Кельвины: {number} : {number + 273.15: 0.2f}")

# case 2 ---------------------------------------------------------------------------------------------------------------
# number = float(input("Введите число: "))
#
# print("1. ", end="")
# if number % 2 == 0:
#     print("число чётное")
# else:
#     print("число не чётное")
#
# print("2. ", end="")
# if number > 0:
#     print("число положительное")
# elif number == 0:
#     print("число равно 0")
# else:
#     print("число отрицательное")
#
# print("3. ", end="")
# if 10 <= number <= 50:
#     print("число в диапазоне [10, 50]")
# else:
#     print("число не в диапазоне [10, 50]")
#
# альтернатива
# print("1. ", end="")
# print(["число чётное", "число не чётное"][number % 2 != 0])

# case 3 ---------------------------------------------------------------------------------------------------------------
# from random import randint, shuffle, sample
#
# alf_1 = "QWERTYUIOPASDFGHJKLZXCVBNM"
#
# alf_2 = "0123456789"
#
# alf_3 = "!@#$%^&*"
#
# password = [alf_1[randint(0, 25)] for _ in range(3)] + [alf_2[randint(0, 9)] for _ in range(3)] + [alf_3[randint(0, 7)] for _ in range(2)]
#
# shuffle(password)
#
# print(*password, sep="")

# case 4 ---------------------------------------------------------------------------------------------------------------
from collections import Counter
from typing import Set


#
# text = input("Введите текст: ")
#
# // test //
# text = "d" * 10 + "a" * 8 + "c" * 4 + "f"
#
# text = text.lower()
#
# print(f"Самые частые символы: {[x[0][0] for x in Counter(text).most_common(3)]}")

# case 5 ---------------------------------------------------------------------------------------------------------------


def get_prime_numbers(number: int) -> list[int]:
    list_numbers = [i for i in range(number + 1)]  # 0, 1, 2, ... n

    list_numbers[1] = 0  # 0, 0, 2, ... n

    i = 2
    while i <= number:
        if list_numbers[i] != 0:
            j = 2 * i
            while j <= number:
                list_numbers[j] = 0
                j += i
        i += 1

    list_numbers = set(list_numbers)
    list_numbers.remove(0)

    return list(list_numbers)


print(get_prime_numbers(11))

