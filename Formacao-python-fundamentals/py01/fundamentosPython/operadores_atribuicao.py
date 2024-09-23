# Operadores de Atribuição em Python

# Atribuição Simples (=)
x = 10  # Atribui o valor 10 à variável x

# Atribuição com Adição (+=)
x += 5  # Equivalente a: x = x + 5 (x agora é 15)

# Atribuição com Subtração (-=)
x -= 3  # Equivalente a: x = x - 3 (x agora é 12)

# Atribuição com Multiplicação (*=)
x *= 2  # Equivalente a: x = x * 2 (x agora é 24)

# Atribuição com Divisão (/=)
x /= 4  # Equivalente a: x = x / 4 (x agora é 6.0)

# Atribuição com Divisão Inteira (//=)
x //= 2  # Equivalente a: x = x // 2 (x agora é 3.0)

# Atribuição com Módulo (%=)
x %= 2  # Equivalente a: x = x % 2 (x agora é 1.0)

# Atribuição com Exponenciação (**=)
x **= 3  # Equivalente a: x = x ** 3 (x agora é 1.0)



# Atribuição com Operador Bitwise AND (&=)
x = 5
x &= 3  # Equivalente a: x = x & 3 (x agora é 1)

# Atribuição com Operador Bitwise OR (|=)
x |= 2  # Equivalente a: x = x | 2 (x agora é 3)

# Atribuição com Operador Bitwise XOR (^=)
x ^= 1  # Equivalente a: x = x ^ 1 (x agora é 2)

# Atribuição com Deslocamento à Esquerda (<<=)
x <<= 1  # Equivalente a: x = x << 1 (x agora é 4)

# Atribuição com Deslocamento à Direita (>>=)
x >>= 2  # Equivalente a: x = x >> 2 (x agora é 1)

saldo =  1000
saque = 250
limite = 200
conta_especial = True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_saldo_suficiente = (saldo >= saque and saque <= limite)

conta_especial_saldo_insuficiente = (conta_especial and saldo >= saque)

exp_3 = conta_saldo_suficiente or conta_especial_saldo_insuficiente
print(exp_3)


