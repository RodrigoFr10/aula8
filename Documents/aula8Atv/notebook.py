from produto import Produto
from categoria import Categoria

class Notebook(Produto):
    def __init__(self,modelo,cor,preco,categoria=Categoria(0),tempoDeBateria=480):
        super().__init__(modelo,cor,preco,categoria)
        self.tempoDeBateria=tempoDeBateria
    
    def cadastrar():
        pass

    def setBateria(self,x):
        self.tempoDeBateria=x

    def getBateria(self):
        return self.tempoDeBateria
    
    def getInformacoes(self):
        print("-"*20,"NOTEBOOK",20*"-")
        txt=super().getInformacoes()
        txt+=f"\nTempo de Bateria: {self.tempoDeBateria} minutos({self.tempoDeBateria/60} horas)"
        txt+=f"\n"
        return txt