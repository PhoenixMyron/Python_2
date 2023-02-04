# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

n = int(input())
result = 0
for i in range(1, n):
    result = i * 2
    print(result)
    if result >= n - 2:
        break
