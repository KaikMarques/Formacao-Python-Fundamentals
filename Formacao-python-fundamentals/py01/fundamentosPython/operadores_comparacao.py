# Operadores de comparação em Python


saldo = 200
saque = 200

# Igualdade (==)
print(saldo == saque)

# Diferença (!=)
print(saldo != saque)

# Maior que (>)
print(saque > saldo)

# Menor que (<)
print(saldo < saque)

# Maior ou igual (>=)
print(saldo >= saque)

# Menor ou igual (<=)
print(saque <= saldo)



# Operador de negação com valores não booleanos

# Negação de um número
x = 0
print(not x)  # True, pois 0 é considerado False

x = 10
print(not x)  # False, pois qualquer número diferente de 0 é considerado True

# Negação de uma lista vazia
lista = []
print(not lista)  # True, lista vazia é considerada False

# Negação de uma string não vazia
texto = "Python"
print(not texto)  # False, pois uma string com valor é considerada True

