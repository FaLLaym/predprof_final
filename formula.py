import numpy as np
#from scipy.optimize import minimize_scalar

T = 20

#одна единица дает мощности
def reactor_power(fuel):
    return 0.01 * fuel

#каждый процент мощности реактора
def electricity_power(reactor_power):
    return 0.11 * reactor_power

#определение скорости корабля
def ship_speed(ship_mass):
    max_speed = 2
    speed = max_speed * (200/ship_mass)
    return speed

#расчет коэфа прироста SH
def growth_koef(T, oxygen):
    return np.sin((-np.pi/2)+((np.pi*(T+0.5*oxygen))/40))

#численность новой популяции
def new_generation(growth_koef, go):
    pass

#расчет количества электроэнергии для автоклава
def energy_required(T):
    pass

#расчет общей массы корабля
def ship_mass(population):
    #изменить return 192 + population*1000
    pass

#функция расчета общего количества в автоклаве
def sh_population(T, oxygen):
    if T < 0 or T > 30:
        return 0
    population = 8
    oxygen_per_sh = oxygen/population
    for i in range(population):
        if oxygen_per_sh > 60:
            return 0
        growth = growth_koef(T, oxygen_per_sh)
        population += growth*population
        if population < 8:
            return 0
    return population








