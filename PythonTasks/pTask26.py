text = input()
total_kop = len(text) * 40
rub = total_kop // 100
kop = total_kop % 100
print(f"{rub} р. {kop} коп.")