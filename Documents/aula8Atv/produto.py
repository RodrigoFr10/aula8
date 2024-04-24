from categoria import Categoria
from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self,modelo,cor,preco,categoria=Categoria(0)):
        self.modelo=modelo
        self.cor=cor
        self.preco=preco
        self.categoria=categoria
    
    def getInformacoes(self):
        texto=f'Modelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.preco}\nCategoria: {self.categoria}'
        return texto
    
    @abstractmethod
    def cadastrar():
        pass

