soma = 0 # Essa variável será usada para acumular (somar) os valores das alturas que o usuário digitar.
qtde_entradas = 4 # Ela representa quantas vezes o programa vai pedir uma altura ao usuário.

while qtde_entradas > 0: # Esse é o início de um **laço de repetição** (`while`), que vai continuar executando o bloco de código abaixo **enquanto** `qtde_entradas` for maior que 0.
    altura = input("Entre com a altura: ") # O valor digitado será armazenado na variável altura.
    altura = float(altura) # Converte o valor digitado (que está como **texto**) para um número do tipo **ponto flutuante** (`float`), ou seja, um número com casas decimais.
    soma += altura
    qtde_entradas -= 1 #Diminui o valor de `qtde_entradas` em 1 Isso garante que o laço `while` vai parar após 4 repetições.

print("Soma das alturas:", soma)