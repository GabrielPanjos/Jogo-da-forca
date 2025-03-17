import random

animais = ["leão", "elefante", "baleia"]
comidas = ["arroz", "coxinha", "strognoff"]
desenhos = ["superman", "batman", "goku"]

categorias = {
    "animal": animais,
    "comida": comidas,
    "desenho": desenhos
}

tema = random.choice(["animal", "comida", "desenho"])
palavra = random.choice(categorias[tema])

quantidade_de_letra = len(palavra)
forca = ["_" for _ in palavra]



while True:
    print("O tema é: ", tema)
    print(forca)

    adivinhar = input("Digite um caracter: ").lower()

    for i in range(len(palavra)):
        if palavra[i] == adivinhar:
            forca[i] = adivinhar

    if "".join(forca) == palavra:
        print(forca)
        print(f"Você conseguiu! a palavra era {palavra}!")
        break