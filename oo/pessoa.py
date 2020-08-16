class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimento(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Manuel')
    print(Pessoa.cumprimento(p))
    print(id(p))
    print(p.cumprimento())
    print(p.nome)
    p.nome = 'Ricardo'
    print(p.nome)
    print(p.idade)



