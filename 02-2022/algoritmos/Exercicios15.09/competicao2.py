# Estabelencendo a velocidade maxima permitida da via como 80Km/h e a velocidade minima
# como 50% da velocidade maxima. FUA que leia e mostre a velocidade que um veiculo trafega
# na via, e se o mesmo levou uma multa "LEVE", "GRAVE", "GRAVISSIMA" ou
# "NAO LEVOU MULTA".

#    Multa leve: +10 sob a velocidade maxima,e < que a velocidade minima, imprima "LEVOU MULTA LEVE"
#    Multa grave: entre +11 e +20 sob a velocidade maxima,imprima "LEVOU MULTA GRAVE"
#    Multa gravissima: +20 sob a velocidade maxima,imprima "LEVOU MULTA GRAVISSIMA".
#    Nao levou multa: >= a velocidade minima e <= a velocidade maxima.

velocidade = float(input("A que velocidade estava o veiculo ?"))

if multaLeve >= 90 or multaLeve <= 39:
    print("Levou multa leve !")
elif multaGrave >= 91 or multaGrave 