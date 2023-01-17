#Practica primos


def primo(numero):
    contador = 0

    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador += 1
    if contador != 0:
        return False
    else:
        return True


def principal():
    print('*' * 30)
    print('DETECTOR DE NUMERO PRIMO')
    num = int(input('Ingrese un numero: '))
    resutado = primo(num)

    if resutado:
        print(f'El numero {num} es primo')
    else:
        print(f'El numero {num} es compuesto')


if __name__ == '__main__':
    principal()
