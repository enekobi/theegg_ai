def get_gcd(num, denom):
    div = num
    while div in range(num + 1):
        if num % div == 0 and denom % div == 0:
            return div
        div -= 1


def minimum_fraction(num):
    if 0 < num < 1:
        denom = 10000
        # Redondear para evitar el error por punto flotante.
        multiplied = int(round(num * denom))
        # MCD se puede calcular usando Math.gcd() pero para el ejercicio lo calcularemos a mano.
        divisor = get_gcd(multiplied, denom)
        min_num = multiplied/divisor
        min_denom = denom/divisor
        print("Fraccion minima de %.4f: %d/%d" % (num, min_num, min_denom))
    else:
        raise Exception()


while True:
    try:
        number = float(
            input("Mete un número entre [0.0001, 0.9999]: (1 para salir)\n"))
        if int(number) == 1:
            break
        else:
            minimum_fraction(number)
    except:
        print("Mal input")
        continue
