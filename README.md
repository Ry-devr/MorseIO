# Tradutor/Leitor de Código Morse

## Objetivos do Programa
- Traduzir qualquer palavra em código morse
- Traduzir qualquer código morse em palavras
- Tocar o sonzinho do código morse

## Funcionalidades
- **Opção 1 — Texto → Morse:** digita uma frase e vê o código morse. O som do morse toca automaticamente.
- **Opção 2 — Morse → Texto:** digita o código morse (usando `.` para ponto, `-` para traço, `/` para espaço entre palavras) e vê a tradução.
- **Opção 3 — Histórico:** mostra o histórico de traduções salvas.
- **Opção 0 — Sair:** fecha o programa.

## Como Usar
```bash
python3 src/main.py
```

### Exemplo
```
Opção 1:
  Digite: ola
  Resultado: --- .-.. .-
  (toca o som do código morse)

Opção 2:
  Digite: --- .-.. .-
  Resultado: ola
```

## Estrutura do Projeto
```
src/
├── main.py                  # Menu principal e loop do programa
├── function.py              # Dicionário morse, funções de som, classe TradutorMorse
└── gerenciador_arquivo.py   # Classe para salvar/ler histórico em CSV

historico.csv                # Histórico das traduções
```

## Código

### `src/main.py`
Entrada do programa. Mostra o menu, lê a opção do usuário e chama as funções de tradução e som.

- **Importações:** `TradutorMorse`, `limpar_terminal`, `reproduzir_morse` de `function.py`; `GerenciadorArquivo` de `gerenciador_arquivo.py`
- **Loop principal:** `while True` que exibe o menu e processa as opções 1, 2, 3 e 0.
- **Entrada:** usa `input()` com tratamento de `ValueError` (entrada inválida) e `EOFError` (fim de entrada).

### `src/function.py`
Contém o dicionário morse, funções de som e a classe de tradução.

- **`MORSE`:** dicionário que mapeia letras, números e pontuação para código morse.
- **`limpar_terminal()`:** limpa o terminal (funciona no Windows e Linux/Mac).
- **`beep(duracao)`:** toca um som de 700Hz pela duração especificada.
  - Windows: usa `winsound.Beep()`
  - Linux/Mac: usa `subprocess.Popen(["play", ...])` com `stdin=subprocess.DEVNULL` para não consumir a entrada do teclado
- **`reproduzir_morse(codigo)`:** toca o código morse completo.
  - `.` (ponto): beep de 0.1s
  - `-` (traço): beep de 0.3s
  - Pausa entre símbolos: 0.1s
  - Pausa entre letras: 0.3s
  - `/` (espaço entre palavras): pausa de 0.7s
- **`TradutorMorse`:**
  - `texto_para_morse(frase)`: converte texto para código morse
  - `morse_para_texto(frase_M)`: converte código morse para texto

### `src/gerenciador_arquivo.py`
Gerencia o arquivo CSV de histórico.

- **`GerenciadorArquivo`:**
  - `salvarDados(lista)`: salva uma lista no CSV
  - `recuperaDados()`: lê o CSV e retorna os dados com tipos convertidos (int, float, string)

## Dependências
- Python 3
- SoX (somente Linux/Mac) — necessário para o som:
  ```bash
  sudo apt install sox        # Debian/Ubuntu
  brew install sox            # Mac
  ```

## Notas
- O som funciona no Windows usando `winsound.Beep()` (nativo).
- No Linux/Mac é necessário ter o `play` do SoX instalado.
