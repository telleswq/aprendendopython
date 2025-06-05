# %%
nome = "Gabriel Telles"

for letra in nome:
    print(letra)
# %%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)

# %%

for numero in range(4, 101):
    if numero % 4 == 0:
        print(numero)
