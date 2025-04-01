budget_january = input("¿Cual es tu presupuesto de enero?")
budget_february = input("¿Cual es tu presupuesto de Febrero?")
budget_march = input("¿Cual es tu presupuesto de Marzo?")

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

budget_total = budget_january + budget_february + budget_march
print("el total de los primeros 3 meses del año es", budget_total)

promedio_budget = budget_total / 3
print("el promedio de presupuesto es: ", promedio_budget)
