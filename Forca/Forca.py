import random
import unidecode


def inicializa_letras():
    return  ["_" for letra in palavra_secreta]


def imprime_letras():
    for letra in letras:
        print(letra, end=' ')
    print()

def preenche_palavra(chute):
    contador = 0
    for letra in palavra_secreta:
        if letra == chute:
            letras[contador] = f"\033[4m{letra}\033[m".upper()
        contador += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |       |     ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("\033[33m       ___________      \033[m")
    print("\033[33m      '._==_==_=_.'     \033[m")
    print("\033[33m      .-\\:      /-.    \033[m")
    print("\033[33m     | (|:.     |) |    \033[m")
    print("\033[33m      '-|:.     |-'     \033[m")
    print("\033[33m        \\::.    /      \033[m")
    print("\033[33m         '::. .'        \033[m")
    print("\033[33m           ) (          \033[m")
    print("\033[33m         _.' '._        \033[m")
    print("\033[33m        '-------'       \033[m")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def carrega_palavra_secreta(arquivo):
    arquivo = open(f"{arquivo}", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        linha = unidecode.unidecode(linha)
        palavras.append(linha)

    arquivo.close()
    print(palavras)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def escolhe_tema():
    tema = ["frutas", "animais"]
    n = 1
    for i in tema:
        print(f"{n} - {i}")
        n += 1
    et = int(input(f"Digite o tema que quiser:"))
    arquivo = tema[et - 1]+".txt"
    return arquivo

# --------------------- INICIO JOGO ---------------------------------
arquivo = escolhe_tema()
palavra_secreta = carrega_palavra_secreta(arquivo)
letras = inicializa_letras()
contador = 0
erros = 0

print()
desenha_forca(erros)
imprime_letras()
print()

while erros < 6:
    contador = 0
    chute = input('\nDigite uma letra: ').upper()
    print(f'seu chute foi {chute}')
    if chute in letras:
        print("voce ja jogou esta letra")

    if chute in palavra_secreta:
        print(f"\033[1;32mvoce acertou!\033[m")
        preenche_palavra(chute)
    else:
        erros += 1
        desenha_forca(erros)
        print(f"\033[1;31mvoce errou {erros} vez(es)\033[m\n")


    if not "_" in letras:
        desenha_forca(erros)
        print(f"\033[1;32mVoce Venceu!!!!\033[m")
        imprime_letras()
        imprime_mensagem_vencedor()
        break

    imprime_letras()

if erros == 6:
    print("\033[1;31mVoce perdeu :(\033[m")
    imprime_mensagem_perdedor(palavra_secreta)