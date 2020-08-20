class Pessoa:
    olhos = 2 #atributo defoul ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimento(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    manuel = Pessoa(nome='Manuel')
    ricardo = Pessoa(manuel, nome='Ricardo')
    print(Pessoa.cumprimento(ricardo))
    print(id(ricardo))
    print(ricardo.cumprimento())
    print(ricardo.nome)
    print(ricardo.idade)
    for filho in ricardo.filhos:
        print(filho.nome)
    ricardo.sobrenome = 'Marques'
    del ricardo.filhos
    manuel.olhos = 1
    del manuel.olhos
    print(ricardo.sobrenome)
    print(ricardo.__dict__)
    print(manuel.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(ricardo.olhos)
    print(manuel.olhos)
    print(id(Pessoa.olhos), id(ricardo.olhos), id(manuel.olhos))





