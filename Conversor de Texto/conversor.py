es = int(input('''Escolha o que deseja fazer com sua frase:
    (1) colocar frase em maiúsculo 
    (2) colocar frase em minúsculo
    (3) colocar a primeira letra em maiúsculo\n
    '''))
text = str(input('Digite seu texto:'))
if es == 1:
    a = text.upper()
    print(a)
elif es == 2:
    b = text.lower()
    print(b)
elif es == 3:
    c = text.capitalize()
    print(c)
