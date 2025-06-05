# Tupla sao listas que nao podem ser alteradas

# %%

dados_gabi = [20, 1, "Solteiro", "dev goLang"]
dados_gabi

# %%

dados_gabi.append("3241.43")
dados_gabi[0] = 28
dados_gabi

# %%
tupla_gabi = (20, 1, "Solteiro", "dev goLang")

print(type(tupla_gabi))
print(tupla_gabi)

# %%
tupla_gabi[0] = 28

# %%
