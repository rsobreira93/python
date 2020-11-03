class error(Exception):
    pass

class InputError(error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota: '))
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas números.')

    except InputError as ex:
        print(ex)