# Operadores de associação: 'in' e 'not in'
# Esses operadores são usados para verificar se um valor está presente em uma sequência, como strings, listas, tuplas, etc.

# Exemplo 1: Operador 'in'
# Verifica se um valor está presente na sequência.
lista_numeros = [1, 2, 3, 4, 5]
# Verificamos se o número 3 está presente na lista
resultado_in = 3 in lista_numeros
# O resultado será True, pois 3 está na lista
# Exemplo de uso em uma condicional
if resultado_in:
    # Não usamos print pois não é relevante, mas esta linha indica que 3 foi encontrado
    pass

# Exemplo 2: Operador 'not in'
# Verifica se um valor NÃO está presente na sequência.
frase = "Olá, bem-vindo ao curso de Python!"
# Verificamos se a palavra "Java" não está presente na frase
resultado_not_in = "Java" not in frase
# O resultado será True, pois a palavra "Java" não está na frase
if resultado_not_in:
    # A palavra "Java" não foi encontrada
    pass

frutas = ['limao', 'uva']
curso = 'curso de python'

print('laranja' not in frutas)
print('limao' in frutas)
print('Python' in curso)
