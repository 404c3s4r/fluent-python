import math 
'''
    v=(2,3) 
    Se move 2 unidades para a direita, eixo X
    e 3 unidades para cima (eixo y).

Soma de vetores: juntando as direções; 
    

    magnitude do vetor: o tamanho da seta pelo teorema de pitagoras; 

'''
class Vector: 

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, v2):
        x  = self.x + v2.x
        y = self.y + v2.y 
        return Vector(x, y)
    
    #O resultado da hipotenusa é sempre um valor absoluto.
    def __abs__(self):
        return math.hypot(self.x, self.y)

    #Multiplicação do vetor: Não altera a direção, apenas aumenta ou diminui tamanho;
    #Existe uma limitação aqui: não conseguimos multiplicar um número com vetor; __rmul__
    def __mul__(self, scala):
        return Vector(self.x * scala, self.y *scala)
    
    
    
    
    
    #!r retorna o valor oficial         
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    #Se  Vector(0,0) a magnitude é 0, FALSE; 
    
#O autor menciona o uso do len(obj) que pode ser utilizado para verificar o tamanho
    
    def __bool__(self):
        return bool(self.x or self.y)

        

#Adição: 
#v1 = Vector(2, 4)  
#v2 = Vector(3, 4)  

#v3 = v1 + v2  

#abs retorna o valor absoluto; 
#print(abs(v2))

#Multiplicação: 
#v1 = Vector(2, 4) * 3 
#print(f"O valor do vetor é {v1.x} {v1.y}")

#v = Vector(3, 4.5)
#print(repr(v))
 
#Bool
v = Vector(2, 0)
print(bool(v))