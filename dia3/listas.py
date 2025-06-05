# %%

# Uma maneira de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)

# %%

teo = ["Gabriel", "Telles", 20, 1, "Noivo", 1500.01]

print(teo)

# %%
type(teo)

# %%

# idade
print(teo[2])

#renda
print(teo[5])

# %%
idades = [28, 42, 43, 35, 39, 28, 38]

print("soma idades:", sum(idades)) # somando as idades

print("qtde idades", len(idades)) # quantidade de idades

print("media idades:", sum(idades)/ 7) # media idades

print("menor idade", min(idades)) # menor idade

print("maior idade:", max(idades)) #maior idade

# %%

teo = ["Gabriel",
        True,
          20, 
          "Noivo",
          ["estagiario",  "ds jr.", "ds pl", "ds sr.", "head" ],
          [1500, 4000, 4550, 6500, 10000],
          ["Ana", "Maria", "Claudia"]]

print("Tamanho da lista:", len(teo))

print(teo[6][0])

exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)