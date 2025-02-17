
# Exemplo com Set
conjunto = {1, 2, 3, 4}

# Sets não possuem ordem garantida
print("\nConjunto (sem ordem definida):")
for item in conjunto:
    print(item)

# Tentando percorrer o conjunto de trás para frente (não é reversível)
print("\nTentando percorrer o conjunto de trás para frente:")
try:
    for item in reversed(conjunto):  # Erro, conjunto não é reversível
        print(item)
except TypeError as e:
    print(f"Erro: {e}")
