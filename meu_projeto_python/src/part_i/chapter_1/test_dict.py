
# Exemplo com Mapping (Dicionário)
dicionario = {'a': 1, 'b': 2, 'c': 3}

# A partir do Python 3.7, dicionários preservam a ordem de inserção
print("\nDicionário (ordem de inserção preservada):")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Tentando percorrer o dicionário de trás para frente (não é reversível)
print("\nTentando percorrer o dicionário de trás para frente:")
try:
    for chave in reversed(dicionario):  # Erro, dicionário não é reversível
        print(chave)
except TypeError as e:
    print(f"Erro: {e}")

