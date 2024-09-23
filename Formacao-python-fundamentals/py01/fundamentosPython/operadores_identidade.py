# Operadores de Identidade em Python
# Eles são usados para comparar se dois objetos ocupam o mesmo espaço na memória.

# 'is' verifica se duas variáveis referenciam o mesmo objeto.
# 'is not' verifica se duas variáveis não referenciam o mesmo objeto.

# Exemplo 1: Usando 'is'
a = [1, 2, 3]
b = a  # 'b' está referenciando o mesmo objeto que 'a'
c = [1, 2, 3]  # 'c' é um novo objeto com o mesmo conteúdo, mas outro endereço de memória

# Comparando se 'a' e 'b' são o mesmo objeto
print(a is b)  # True, pois 'a' e 'b' referenciam o mesmo objeto

# Comparando se 'a' e 'c' são o mesmo objeto
print(a is c)  # False, pois 'a' e 'c' são objetos diferentes na memória, mesmo com o mesmo conteúdo

# Exemplo 2: Usando 'is not'
d = [4, 5, 6]
e = [4, 5, 6]

# Comparando se 'd' e 'e' não são o mesmo objeto
print(d is not e)  # True, pois 'd' e 'e' são objetos diferentes

# Mesmo que o conteúdo de 'd' e 'e' seja o mesmo, eles ocupam espaços diferentes na memória.
