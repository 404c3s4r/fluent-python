import collections 
from random import choice 

#tuplas nomeadas;   
    #são imutáveis; 
    #dados sao estruturados: podendo acessar rank e suit ao invés de indíce; 


suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)
Card = collections.namedtuple('Card', ['rank', 'suit'])


'''strings são sequências de caracteres, 
    a função list sempre vai converter a sequência em elementos individuais'''

'''.split() pega uma unica string(sequencia de caracteres) 
e divide em uma lista de substring'''

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


#_cards o sublinhado indica que a variável não deve ser acessada fora da classe 

    def __init__(self): 
        self._cards = [Card(rank, suit) 
            for suit in self.suits
                for rank in self.ranks]
            
   
    def __len__(self):
        return len(self._cards)

    #indexação 
    # suporta o fateamento :3
    def __getitem__(self, index):
        return self._cards[index]
    

dock = FrenchDeck()
#print(choice(dock))# __getitem__: suporta o random.choice; 
#print(dock[12::13]) #__getitem__:suporta o fateamento; 

#print(dock[2]) #__getitem__ como é interável, suporta o for e função reversed; 

'''
for c in dock: 
    print(c)
'''
'''for c in reversed(dock):
    print(c)
'''
#__getitem__ suporta operadores: in 
'''if Card(rank='10', suit='hearts') in dock: 
    print('verdadeiro')
'''

def spades_high(card):

    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# 2 3 4 5 6 7 8 9 10 J Q K A 
# INDICES: 0 1 2 3 4 5 6 7 8 9 10 11 12 

'''for card in sorted(dock, key=spades_high):
    print(f"aqui po {card}")'''
