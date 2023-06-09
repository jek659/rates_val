import pycbrf.toolbox
import os
import datetime
import matplotlib.pyplot as plt

c = 0
while c != 2:
    os.system("cls")
    print("cbrf Terminal v0.0.1")
    print("1 - Запрос котировок валют сегодня")
    print("2 - Выход из терминала")
    try:
        c = int(input())
    except ValueError:
        print("Не кооректный ввод")
        _ = input("Нажмите ENTER для повторного ввода...")
        continue
    if(c == 1):
        al = str(datetime.datetime.now())[:10]
        val = input("Введите название валюты(USD) \n")
        rates = pycbrf.toolbox.ExchangeRates(al)
        result = rates[val].value
        print(result)
        _ = input("Нажмите ENTER для продолжения...")
        
                    
        
