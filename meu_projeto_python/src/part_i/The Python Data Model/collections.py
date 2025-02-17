class Mycollections:
    
    def __init__(self, itens):
        self.itens = list(itens)
     
    #self.itens.__getitem__(indice)

    def __getitem__(self, indice):
        return self.itens[indice]
    
    def __len__(self):
        return len(self.itens)


    def __setitem__(self, indice, valor):
        self.itens[indice] = valor

c = Mycollections([1,2])

print(c[1]) #O python vai procurar pelo método __getitem__ c.__getitem__(indice) e executar o return
print(len(c)) #O Python vai procurar pelo método c.__len__()
subs = c[1] = 3
print(subs)

