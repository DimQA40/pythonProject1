per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму money: "))

deposit_1 = int(round(money * (per_cent['ТКБ']/100),0))
deposit_2 = int(round(money * (per_cent['СКБ']/100),0))
deposit_3 = int(round(money * (per_cent['ВТБ']/100),0))
deposit_4 = int(round(money * (per_cent['СБЕР']/100),0))
deposit = [deposit_1,deposit_2,deposit_3,deposit_4]
#Пример вывода данных
print(deposit)
#Дополнительный вариант вывода
print("Накопленные средства за год в:")
print(' ТКБ - ' + str(deposit_1),
      "\n",'СКБ - ' + str(deposit_2),
      "\n",'ВКБ - ' + str(deposit_3),
      "\n",'СБЕР - ' + str(deposit_4))
#Самостоятельное изучение. Использованием функции max
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)))
