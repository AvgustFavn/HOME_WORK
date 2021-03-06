from utils import currency_rates

currency_rates("usd")
currency_rates("euro")
currency_rates("FYJFYFLUYKGLUGK")

# Я не вижу смысла использовать здесь Decimal. Если бы я что-то расчитывал, а не простов вырезал из строки, то да. Можно чтобы не зависило от
# регистра, сначало currency опустить регистр(lower)и потом если currency == "usd" то все ок, в общем, можно, но я уже сделал немного по-другому
