from produto import Produto
from categoria import Categoria

class Desktop(Produto):
    def __init__(self,modelo,cor,preco,categoria=Categoria(0),potenciaDaFonte=500):
        super().__init__(modelo,cor,preco,categoria)
        self.potenciaDaFonte=potenciaDaFonte
    
    def cadastrar():
        pass

    def setFonte(self,x):
        self.potenciaDaFonte=x
        
    def getFonte(self):
        return self.potenciaDaFonte

    def getInformacoes(self):
        print("-"*20,"DESKTOP",20*"-")
        txt=super().getInformacoes()
        txt+=f"\nPotência da Fonte: {self.potenciaDaFonte}W"
        txt+=f"\n"
        return txt
        
    

    

        