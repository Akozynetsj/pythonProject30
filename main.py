number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
start = min(number1, number2)
end = max(number1, number2)
sum_of_range = 0
for num in range(start+1, end):
    sum_of_range += num
print("Сума чисел у діапазоні між", start, "і", end, "дорівнює", sum_of_range)
