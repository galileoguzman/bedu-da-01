numero = input('Dame un número: ')


try:
    numero = float(numero)
except Exception:
    print('Hey!!!! -_- ingresa un número')
    numero = float(input('Dame un número: '))



for i in range(10):
    print(f'{numero} * {i + 1} = {(i + 1)*numero}')
