graus_p = [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]
graus_C = [0, -1, -2]

direito = int(input("Grau periferico do olho direito:"))

esquerdo = int(input("Grau periferico do olho esquerdo: "))

if (direito in graus_p) and (esquerdo in graus_p):
    print('Para sua receita temos as lentes Prime.')
else:
    print('As lentes Prime não tem suporte para seu grau.')

vdireito = int(input("Grau cilindrico do olho direito"))

vesquerdo = int(input("Grau cilindrico do olho esquerdo"))

if (vdireito in graus_C) and (vesquerdo in graus_C):
    print('Para sua receita temos as lentes Prime.')
else:
    print('As lentes Prime não tem suporte para seu grau.')


graus_V = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
graus_C = [0, -1, -2, -3, -4, -5]

sim = str(input('Voce deseja conhecer as lentes Vision?'))

if sim == sim:
    direito = int(input("Grau periferico do olho direito:"))

    esquerdo = int(input("Grau periferico do olho esquerdo: "))

    if (direito in graus_V) and (esquerdo in graus_V):
        print('Para sua receita temos as lentes Prime.')
    else:
        print('As lentes Prime não tem suporte para seu grau.')

    vdireito = int(input("Grau cilindrico do olho direito"))

    vesquerdo = int(input("Grau cilindrico do olho esquerdo"))

    if (vdireito in graus_C) and (vesquerdo in graus_C):
        print('Para sua receita temos as lentes Vision.')
    else:
        print('As lentes Vision não tem suporte para seu grau.')


