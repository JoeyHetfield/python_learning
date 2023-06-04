quantosSegundos = input("Por favor, entre com o número de segundos que deseja converter: ")

quantosSegundos = int(quantosSegundos)

dias = quantosSegundos // 86400

horas = (quantosSegundos % 86400) // 3600

minutos = ((quantosSegundos % 86400) % 3600) // 60

segundos = ((quantosSegundos % 86400) % 3600) % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")