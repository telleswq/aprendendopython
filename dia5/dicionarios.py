# %%

lista = [2, 132, "gabi", ["ds", "de", "da"], True]

lista [2]

# %%

#pares de chave/valor

dados_gabi = {
    "sobrenome":"telles",
    "nome":"Gabriel", "filhos":True,
    "formacao":["estatistica", "bigdata datascience"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "sas"},
        {"nome": "ds sr.", "empresa": "boticario"},
        {"nome": "ds espec.", "empresa": "via varejo"},
    ]
    }

# %%
print(dados_gabi)
print(dados_gabi["formacao"][-1])
print(dados_gabi["cargos"][-1]["empresa"])

# %%

dados_gabi["estado civil"] = "casado"

# %%

print("Chaves:", dados_gabi.keys())
print("Valores:",dados_gabi.values())
print("Items", dados_gabi.items())

# %%

for i in dados_gabi:
    print(i, "->", dados_gabi[i]) 

# %%
for chave, valor in dados_gabi.items():
    print(chave, "->", valor)
