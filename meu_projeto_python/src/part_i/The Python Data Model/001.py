1. Coleções
Para criar objetos que se comportam como coleções (listas, dicionários, etc.), implementamos métodos como __getitem__, __setitem__, __len__, etc.

python
Copy
class MinhaColecao:
    def __init__(self, itens):
        self.itens = list(itens)

    def __getitem__(self, indice):
        return self.itens[indice]

    def __setitem__(self, indice, valor):
        self.itens[indice] = valor

    def __len__(self):
        return len(self.itens)

# Uso
colecao = MinhaColecao([10, 20, 30])
print(colecao[1])  # Saída: 20 (usa __getitem__)
colecao[1] = 99  # Usa __setitem__
print(colecao[1])  # Saída: 99
print(len(colecao))  # Saída: 3 (usa __len__)
2. Acesso a atributos
Podemos controlar o acesso a atributos usando métodos como __getattr__, __setattr__ e __delattr__.

python
Copy
class MeuObjeto:
    def __init__(self):
        self.atributo = 42

    def __getattr__(self, nome):
        return f"Atributo '{nome}' não existe!"

    def __setattr__(self, nome, valor):
        print(f"Definindo {nome} = {valor}")
        super().__setattr__(nome, valor)

# Uso
obj = MeuObjeto()
print(obj.atributo)  # Saída: 42
print(obj.inexistente)  # Saída: Atributo 'inexistente' não existe!
obj.novo_atributo = 100  # Saída: Definindo novo_atributo = 100
3. Iteração (incluindo iteração assíncrona com async for)
Para criar objetos iteráveis, implementamos __iter__ ou __aiter__ (para iteração assíncrona).

python
Copy
class MeuIteravel:
    def __init__(self, dados):
        self.dados = dados

    def __iter__(self):
        return iter(self.dados)

# Uso
for item in MeuIteravel([1, 2, 3]):
    print(item)  # Saída: 1, 2, 3
4. Sobrecarga de operadores
Podemos definir como operadores como +, -, *, etc., funcionam para nossos objetos.

python
Copy
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

# Uso
p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = p1 + p2
print(p3)  # Saída: Ponto(4, 6)
5. Invocação de funções e métodos
Podemos fazer um objeto ser "chamável" como uma função implementando __call__.

python
Copy
class Multiplicador:
    def __init__(self, fator):
        self.fator = fator

    def __call__(self, x):
        return x * self.fator

# Uso
dobro = Multiplicador(2)
print(dobro(5))  # Saída: 10
6. Representação e formatação de strings
Usamos __str__ e __repr__ para definir como o objeto é exibido como string.

python
Copy
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Pessoa: {self.nome}"

    def __repr__(self):
        return f"Pessoa(nome={self.nome!r})"

# Uso
p = Pessoa("Alice")
print(str(p))  # Saída: Pessoa: Alice
print(repr(p))  # Saída: Pessoa(nome='Alice')
7. Programação assíncrona usando await
Para criar objetos que podem ser usados com await, implementamos __await__.

python
Copy
import asyncio

class MeuAwaitable:
    def __await__(self):
        yield from asyncio.sleep(1)
        return "Feito!"

# Uso
async def main():
    resultado = await MeuAwaitable()
    print(resultado)  # Saída: Feito!

asyncio.run(main())
8. Criação e destruição de objetos
Usamos __init__ para inicialização e __del__ para limpeza (embora __del__ seja raramente usado).

python
Copy
class Recurso:
    def __init__(self, nome):
        self.nome = nome
        print(f"Recurso {self.nome} criado.")

    def __del__(self):
        print(f"Recurso {self.nome} destruído.")

# Uso
r = Recurso("Arquivo")
del r  # Saída: Recurso Arquivo destruído.
9. Contextos gerenciados usando as instruções with ou async with
Implementamos __enter__ e __exit__ para criar gerenciadores de contexto.

python
Copy
class GerenciadorDeArquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, "r")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()

# Uso
with GerenciadorDeArquivo("arquivo.txt") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)