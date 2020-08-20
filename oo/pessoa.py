class Pessoa:
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
    print(ricardo.sobrenome)
    print(ricardo.__dict__)
    print(manuel.__dict__)




