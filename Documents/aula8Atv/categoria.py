class Categoria:
    def __init__(self,id,nome="Padrao"):
        self.id=id
        self.nome=nome

    def __str__(self):
        texto=f'{self.nome}, ID: {self.id}'
        return texto

