from os import system, name
import platform, time, threading, subprocess

##########################
#### BIBLIOTECA MORSE ####
##########################

MORSE = {
    # Letras
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    # Números
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    # Pontuação
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',
    ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-','@': '.--.-.', ' ': '/'
}  # Nao é uma lista mais sim um dicionario

#############
## FUNÇÔES ##
#############

# limpar o terminal
def limpar_terminal():
    try: 
        input("Presione ENTER para continuar/limpar...")
        system("cls" if name == "nt" else "clear")
    except:
        pass

#####################
## NAO FUNCIONANDO ##
#####################


def beep(duracao):
    if platform.system() == "Windows": # verifica se o sistema é windows ou linux/mac
        import winsound
        winsound.Beep(700, int(duracao * 1000))

    else:
        subprocess.Popen(
            ["play", "-n", "synth", str(duracao), "sine", "700"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(duracao)

def reproduzir_morse(codigo):
    for simbolo in codigo.split():
        if simbolo == "/":
            time.sleep(0.7)
        else:
            for sinal in simbolo:
                if sinal == ".":
                    beep(0.1)
                elif sinal == "-":
                    beep(0.3)
                time.sleep(0.1)
            time.sleep(0.3)

def reproduzir_morse_async(codigo):
    t = threading.Thread(target=reproduzir_morse, args=(codigo,))
    t.start()

#########################
## class para traduzir ##
#########################

class TradutorMorse:
    def __init__(self):
        self.morse = MORSE
        self.morse_inve = {valor: chave for chave, valor in MORSE.items()} # De forma invertida

    def texto_para_morse(self, frase):
        letras = list(frase.strip().upper()) 
        frase_morse = []
        for l in letras:
            frase_morse.append(self.morse[l])
        
        return " ".join(frase_morse)

    def morse_para_texto(self, frase_M):
        palavras_morse = frase_M.strip().split("/") # A barra serve para dividir sendo usado como espaço
        frase_textu = []

        for l in palavras_morse:
            letras_morse = l.split()
            letras = (self.morse_inve[L] for L in letras_morse)
            frase_textu.append("".join(letras))

        return " ".join(frase_textu) 


