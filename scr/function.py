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

MORSE_INVE = {valor: chave for chave, valor in MORSE.items()} # De forma invertida
#############
## FUNÇÔES ##
#############

def t_para_m(frase):
    letras = list(frase.strip().upper()) 
    frase_morse = [] # Vou precisar disso depois
    for l in letras:
        frase_morse.append(MORSE[l])

    return "".join(frase_morse)

def m_para_t(frase_M):
    palavras_morse = frase_M.strip().split("/") # A barra serve para dividir sendo usado como espaço
    frase_textu = []

    for l in palavras_morse:
        letras_morse = l.split()
        letras = (MORSE_INVE[L] for L in letras_morse)
        frase_textu.append("".join(letras))

    return " ".join(frase_textu)

