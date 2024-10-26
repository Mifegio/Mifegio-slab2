salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
circle1 = 0
c_month = months
while c_month > 0:
    circle1 = (salary - spend)
    if circle1 < 0:
        money_capital = (spend - salary) + money_capital
    c_month -= 1
    spend = (spend * increase) + spend

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
