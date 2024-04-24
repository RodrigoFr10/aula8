from desktop import Desktop
from notebook import Notebook
from categoria import Categoria


#prod1=Produto("Home","Preto",2500,Categoria(0,"Desktop"))
desk1=Desktop("Home","Preto",2500,Categoria(0,"Desktop"),700)
note1=Notebook("Office","Prata",2000,Categoria(0,"Notebook"),120)


print(desk1.getInformacoes())
print(note1.getInformacoes())
desk1.setFonte(800)
note1.setBateria(480)
print(desk1.getFonte())
print(note1.getBateria())
print(desk1.getInformacoes())
print(note1.getInformacoes())
