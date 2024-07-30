certamenes = [77,95,0]
entregas = [86,88,0]
seminario = 95


suma = sum(certamenes)/len(certamenes)
suma2 = sum(entregas)/len(entregas)
suma3 = seminario


if suma >=55 and suma2 >= 55 and suma3 >= 55: 
    prom_certamenes = suma * 0.5
    prom_entregas = suma2 * 0.4
    prom_seminario = suma3 * 0.1

    total = prom_certamenes + prom_entregas + prom_seminario
    print(f'promedio: {total}')