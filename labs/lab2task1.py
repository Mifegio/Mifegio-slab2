money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
c_mont = 0
while money_capital + salary > spend:
    money_capital = (salary - spend) + money_capital
    c_mont += 1
    spend = (spend * increase) + spend
print("Количество месяцев, которое можно протянуть без долгов:", c_mont)
