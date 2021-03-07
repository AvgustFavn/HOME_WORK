n = int(input("Введи до скольки генерируем: "))
gen_of_nums = (num for num in range(1, n + 1, 2))

for gen in gen_of_nums:
    print(next(gen_of_nums))

# Выполнил со звездочкой: *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.