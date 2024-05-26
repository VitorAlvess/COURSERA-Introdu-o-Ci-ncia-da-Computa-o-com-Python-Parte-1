segundos_totais = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos_totais // (24 * 3600)
segundos_restantes = segundos_totais % (24 * 3600)
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos_restantes %= 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
