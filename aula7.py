#função é tudo que retorna um valor
class Calculadaora:
    def __init__(self, num1, num2):
        self.valor_a = num1 #pass para deixar vazio
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b
    def subtra(self):
        return self.valor_a - self.valor_b
    def multi(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':

    caluladora = Calculadaora(10,2)
    print(caluladora.soma())
    print(caluladora.subtra())
    print(caluladora.multi())
    print(caluladora.divisao())