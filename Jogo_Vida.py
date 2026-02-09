# Bibliotecas importadas.
import time # Importa a biblioteca time, que não é necessária nesse caso (extra), mas ela permite o controle do fluxo do código.
import os # Importa a biblioteca os, que também não é necessária nesse caso (extra), mas ela permite a interação com o sistema operacional.
import random # Importa a biblioteca random, necessária para formação aleatória do tabuleiro, que permite trabalhar com dados ou valores aleatórios.

# Atribuição de constantes. Por convenção, em muitas linguagens, o nome com letras maiúsculas indica que o mesmo é uma constante.
# Nesse caso, utilizei para dizer que o tamanho do tabuleiro sempre vai ser 10 X 10 e para a representação de vivo e morto.
TAMANHO = 10
CELULA_VIVA = True
CELULA_MORTA = False
SIMBOLO_CELULA_VIVA = 'V'
SIMBOLO_CELULA_MORTA = '.'

# Cria uma função para limpar a tela.
def limpar_tela():
    # Essa função do módulo permite que os comandos sejam executados diretamente no terminal. Nesse caso, há uma estrutura condicional onde são
    # executados diferentes comandos para limpar a tela, dependendo do sistema operacional (Windows, Linux/macOS).
    os.system('cls' if os.name == 'nt' else 'clear')

# Cria uma função que cria um tabuleiro somente com células mortas e recebe
# como parâmetros "tamanho", que é o tamanho ou quantidade de linhas e de colunas.
def criar_tabuleiro_vazio(tamanho):

    # Atribuição de variável. É atribuída uma lista vazia, que armazenará o tabuleiro (matriz).
    tabuleiro_completo = []
    # Laço de repetição(for) que percorre todas as linhas da matriz ou tabuleiro.
    for linha in range(tamanho):
        # Atribuição de variável. É atribuída uma lista vazia, que armazenará as linhas do tabuleiro (matriz).
        linha_exibida = []
        # Laço de repetição(for) que percorre todas os elementos da linha.
        for celula in range(tamanho):
            # Adiciona CELULA_MORTA ('.') a variável "linha_exibida", ou seja, em cada elemento.
            linha_exibida.append(CELULA_MORTA)
        # Adiciona a variável "linha_exibida" a variável "tabuleiro_completo".
        tabuleiro_completo.append(linha_exibida)

    # Retorna a variável "tabuleiro_completo" ao final da função.
    return tabuleiro_completo

# Cria uma função que exibe o estado do tabuleiro e recebe como parâmetros o "estado", que é o tabuleiro ou matriz.
def exibir_estado(estado):

    # Chama a função que limpa o terminal.
    limpar_tela()
    # Imprime o nome do jogo na tela.
    print("--- Jogo da Vida ---")
    # Laço de repetição(for) que percorre todas as linhas da matriz ou tabuleiro.
    for linha in estado:
        # Atribuição de variável. É atribuída uma lista vazia, que armazenará as linhas do tabuleiro (matriz).
        linha_para_exibir = []
        # Laço de repetição(for) que percorre todas os elementos da linha.
        for celula in linha:
            # Estrutura condicional, onde se a variável "celula" (elemento da linha) for igual a constante "CELULA_VIVA" (True),
            # é adicionada a constante "SIMBOLO_CELULA_VIVA"(V) a variável "linha_para_exibir".
            # Caso não, é adicionada a constante "SIMBOLO_CELULA_MORTA"(.) a variável "linha_para_exibir".
            if celula == CELULA_VIVA:
                linha_para_exibir.append(SIMBOLO_CELULA_VIVA)
            else:
                linha_para_exibir.append(SIMBOLO_CELULA_MORTA)
        #Imprime na tela a variável "linha_para_exibir" com um espaço.
        print(" ".join(linha_para_exibir))
    # Imprime uma barreira de "-" para mostrar onde o tabuleiro termina.
    print("-" * (TAMANHO * 2 - 1))

# Cria uma função que calcula a quantidade de vizinhos vivos em uma posição específica e recebe como parâmetros "estado, linha, coluna".
def contar_vizinhos_vivos(estado, linha, coluna):

    # Atribuição de variável. Começa um "contador" da variável vizinhos_vivos igualando a mesma a 0.
    vizinhos_vivos = 0
    # Atribuição de variável. A funcionalidade "len" calcula a quantidade de linhas (listas) em "estado" (tabuleiro ou matriz).
    num_linhas = len(estado)
    # Atribuição de variável. A funcionalidade "len" calcula a quantidade de colunas em "estado" na posição 0.
    num_colunas = len(estado[0])

    # Laço de repetição(for) que percorre os 8 vizinhos possíveis.
    for i in range(max(0, linha - 1), min(num_linhas, linha + 2)):
        for j in range(max(0, coluna - 1), min(num_colunas, coluna + 2)):
            # Estrutura condicional que evita que a própria célula seja contada.
            if i == linha and j == coluna:
                continue
            # Estrutura condicional que verifica se o vizinho está vivo.
            if estado[i][j] == CELULA_VIVA:
                # Adiciona +1 a variável "vizinhos_vivos"("contador").
                vizinhos_vivos += 1

    # Retorna a quantidade guardada na variável "vizinhos_vivos" ao final da função.
    return vizinhos_vivos

# Cria uma função que "calcula" o próximo estado do tabuleiro e recebe como parâmetros "estado_atual", ou seja, o tabuleiro atual.
def calcular_proximo_estado(estado_atual):

    # Atribuição de variável. A funcionalidade "len" calcula a quantidade de linhas (listas) em "estado_atual" (tabuleiro ou matriz).
    num_linhas = len(estado_atual)
    # Atribuição de variável. A funcionalidade "len" calcula a quantidade de colunas em "estado_atual" na posição 0.
    num_colunas = len(estado_atual[0])
    # Atribuição de variável. Começa o próximo estado com um tabuleiro morto.
    proximo_estado = criar_tabuleiro_vazio(num_linhas)

    # Laço de repetição(for) que percorre todas as linhas da matriz ou tabuleiro.
    for i in range(num_linhas):
        # Laço de repetição(for) que percorre todas as colunas da matriz ou tabuleiro.
        for j in range(num_colunas):
            # Atribuição de variável. Conta os vizinhos vivos na matriz.
            vizinhos = contar_vizinhos_vivos(estado_atual, i, j)
            # Atribuição de variável. Observa se a a célula que está sendo percorrida naquele momento é viva.
            celula_atual_viva = estado_atual[i][j] == CELULA_VIVA

            # Estrutura condicional que aplica as regras do Jogo da Vida:

            # 1. Solidão: Célula viva com menos de 2 vizinhos vivos morre.
            if celula_atual_viva and vizinhos < 2:
                proximo_estado[i][j] = CELULA_MORTA
            # 2. Sobrevivência: Célula viva com 2 ou 3 vizinhos vivos sobrevive.
            elif celula_atual_viva and (vizinhos == 2 or vizinhos == 3):
                proximo_estado[i][j] = CELULA_VIVA
            # 3. Superpopulação: Célula viva com mais de 3 vizinhos vivos morre.
            elif celula_atual_viva and vizinhos > 3:
                proximo_estado[i][j] = CELULA_MORTA
            # 4. Reprodução: Célula morta com exatamente 3 vizinhos vivos torna-se viva.
            elif not celula_atual_viva and vizinhos == 3:
                proximo_estado[i][j] = CELULA_VIVA
            # Caso contrário (célula morta sem 3 vizinhos), continua morta.

    # Retorna o próximo tabuleiro depois de modificar as células.
    return proximo_estado

# Cria uma função que permite ao usuário definir o estado (matriz) inicial manualmente e recebe como parâmetros "tamanho".
def inicializar_manual(tamanho):
    # Atribuição de variável. Controla o loop while.
    continuar = True 
    # Atribuição de variável. Começa o estado com um tabuleiro morto.
    estado = criar_tabuleiro_vazio(tamanho)
    # Imprime uma frase.
    print("\n--- Modo Manual ---")
    # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
    time.sleep(1.5)

    # Estrutura de repetição(while) que continua até o usuário começar a simulação('fim').
    while continuar:
        # Evoca uma função, que mostra o estado atual durante a inserção.
        exibir_estado(estado)
        # Bloco try que pula para o except quando a entrada estiver errada.
        try:
            # Imprime as instruções de como inserir e finalizar no modo manual.
            print(f"Digite as coordenadas (linha coluna) das células vivas (0 a {tamanho-1}).")
            print("Exemplo: '3 4' para ativar a célula na linha 3, coluna 4.")
            print("Digite 'fim' quando terminar.")
            # Atribuição de variável. É a entrada onde o usuário pode digitar a coordenada ou iniciar a simulação.
            # As funcionalidades ".strip().lower()" são utilizadas respectivamente para 
            # limpar espaços em branco nas bordas e para converter tudo para minúsculas.
            entrada = input("Coordenada (linha coluna) ou 'fim': ").strip().lower()
            # Estrutura condicional onde se "entrada" que o usuário digitou foi "fim", o loop termina e a simulação começa.
            if entrada == 'fim':
                continuar = False
            # Divide a string de "entrada" com base em espaços em branco, para verificar se ele digitou 2 strings.
            # Pega tudo isso e coloca em uma lista.
            dividir_entrada = entrada.split()
            # Estrutura condicional onde se a quantidade de elementos da lista de "dividir_entrada" for diferente de 2, a entrada é invalidada.
            if len(dividir_entrada) != 2:
                # Um erro é forçado porque a entrada não foi escrita no formato correto ('linha coluna').
                raise ValueError("Entrada inválida. Use o formato 'linha coluna'.")

            # Atribuição de variáveis. Tenta transformar as strings da coordenada em um número inteiro.
            linha = int(dividir_entrada[0])
            coluna = int(dividir_entrada[1])

            # Estrutura condicional que verifica se o tamanho das linha e da coluna digitados são válidos.
            if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                # Transforma o estado da célula quando a coordenada é digitada, pois estamos usando o True e o False.
                estado[linha][coluna] = not estado[linha][coluna]

                # Atribuição de variável para verificar o estado da célula.
                esta_viva = estado[linha][coluna]
                # Atribuição de variável que guarda uma palavra.
                string_estado = ""
                # Estrutura condicional que guarda palavras diferentes dependendo se "esta_viva" é True ou False.
                if esta_viva:
                    string_estado = "Viva"
                else:
                    string_estado = "Morta"

                # Imprime uma frase dizendo o que aconteceu com o estado da célula.
                print(f"Célula ({linha},{coluna}) agora {string_estado}.")
                # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
                time.sleep(1)
            else:
                # Imprime mensagem para coordenadas inválidas.
                print(f"Coordenadas fora do tabuleiro (0 a {tamanho-1}). Tente novamente.")
                # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
                time.sleep(1)

        except ValueError as erro:
            # Imprime mensagem de erro para entrada inválida.
            print(f"Erro: {erro}. Tente novamente.")
            # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
            time.sleep(1.5)
        except Exception as erro:
            # Imprime mensagem para erros inesperados.
            print(f"Ocorreu um erro inesperado: {erro}")
            # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
            time.sleep(1.5)

    # Retorna o estado final definido pelo usuário.
    return estado

# Cria uma função que gera um tabuleiro de forma aleatória e recebe como parâmetros tamanho (tamanho do tabuleiro) e 
# probabilidade (chance da célula se tornar viva).
def inicializar_aleatorio(tamanho, probabilidade = 0.3):

    # Imprime uma frase.
    print("\n--- Modo Aleatório ---")
    # Atribuição de variável. Cria um tabuleiro vazio.
    estado = criar_tabuleiro_vazio(tamanho)
    # Laço de repetição(for) que percorre todas as linhas da matriz ou tabuleiro.
    for i in range(tamanho):
        # Laço de repetição(for) que percorre todas as colunas da matriz ou tabuleiro.
        for j in range(tamanho):
            # Evoca a funcionalidade random() do módulo random, onde o "< probabilidade" define a probabilidade da célula estar viva.
            if random.random() < probabilidade :
                # Define que a célula percorrida é viva.
                estado[i][j] = CELULA_VIVA
    # Imprime uma frase.
    print("Tabuleiro inicial aleatório gerado.")
    # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
    time.sleep(2) 

    # Retorna o estado (tabuleiro ou matriz).
    return estado

# Cria uma função que verifica se o jogo deve terminar (células mortas ou "vida parada") e recebe como 
# parâmetros "estado_atual" e "estado_anterior", que é basicamente o tabuleiro atual e o anterior.
def verificar_fim_jogo(estado_atual, estado_anterior): 
    # Atribuição de variável. Suposição que o jogo acabou.
    todas_mortas = True
    # Laço de repetição(for) que percorre todas as linhas da matriz ou tabuleiro.
    for linha in estado_atual:
        # Laço de repetição(for) que percorre todas as colunas da matriz ou tabuleiro.
        for celula in linha:
            # Estrutura condicional onde se houver qualquer célula viva, o jogo não termina.
            if celula == CELULA_VIVA:
                # Nega a suposição.
                todas_mortas = False

    # Estrutura condicional caso o jogo tenha acabado (todas as células mortas).
    if todas_mortas:
        # Imprime uma frase.
        print("\nFim do jogo: Todas as células morreram.")
        # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
        time.sleep(2)

        # Indica que o jogo deve acabar.
        return True

    # Verifica se o estado atual é igual ao estado anterior (vida parada).
    if estado_atual == estado_anterior:
        # Imprime uma frase.
        print("\nFim do jogo: O estado tornou-se estável (vida parada).")
        # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
        time.sleep(2)

        # Indica que o jogo deve acabar
        return True

    # Indica que o jogo deve continuar.
    return False

# Cria uma função principal do "Jogo da Vida".
def main():

    # Atribuição de variável. Vai guardar futuramente o tabuleiro da rodada anterior, por isso None.
    estado_anterior = None 
    # Atribuição de variável. Vai guardar futuramente o tabuleiro daquele momento, por isso None.
    estado_atual = None    
    # Atribuição de variável. Vai acumular as gerações passadas.
    geracao = 0

    # Atribuição de variável para controlar o loop (while).
    modo_valido = True

    # Laço de repetição while que continua até "modo_valido" ser False.
    while modo_valido:
        # Entrada de dados. O usuário escolhe o modo de jogo.
        modo = input("Escolha o modo de início ('manual' ou 'aleatorio'): ").strip().lower()
        #Estrutura condicional que verifica o modo escolhido e evoca a respectiva função. O loop termina quando um modo válido for escolhido.
        if modo == 'manual':
            estado_atual = inicializar_manual(TAMANHO)
            # Interrompe o loop.
            modo_valido = False 
        elif modo == 'aleatorio':
            estado_atual = inicializar_aleatorio(TAMANHO)
            # Interrompe o loop.
            modo_valido = False 
        else:
            # Imprime uma frase.
            print("Modo inválido. Tente novamente.")
            # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
            time.sleep(1)
            

    # Atribuição de variável para controlar o loop (while).
    jogo_rodando = True

    # Laço de repetição while que continua até "jogo_rodando" ser False.
    while jogo_rodando:
        
        # Evoca uma função que exibe o estado do tabuleiro atual nesse caso.
        exibir_estado(estado_atual)
        # Imprime a geração.
        print(f"Geração: {geracao}")

        # Atribuição de variável. Verifica condições de parada "antes" de calcular o próximo estado. Supõe que não acabou.
        jogo_terminou_por_condicao = False 
        if estado_anterior is not None:
            # Chama a função que verifica as condições de fim.
            terminou = verificar_fim_jogo(estado_atual, estado_anterior)
            if terminou:
                # Se isso for verdade, continua e o jogo acaba.
                jogo_terminou_por_condicao = True 

        # Se o jogo terminou por morte ou estabilidade, para o loop principal
        if jogo_terminou_por_condicao:
            # Atribuição de variável. O jogo realmente acaba.
            jogo_rodando = False
        else:
            # Se o jogo não terminou, espera a interação do usuário ou interrupção.
            try:
                # Entrada de dados para continuar o jogo ou interromper.
                input("Pressione Enter para avançar para a próxima geração (ou Ctrl+C para sair)...")
            except KeyboardInterrupt:
                print("\nJogo interrompido pelo usuário.")
                # Pausa para o usuário ler a mensagem antes da próxima atualização da tela.
                time.sleep(1) 
                # Atribuião de variável. O jogo acaba por interrupção.
                jogo_rodando = False 

            # Estrutura condicional que atualiza os estados se o jogo ainda estiver rodando (não foi interrompido e não acabou).
            if jogo_rodando:
                # Guarda o estado atual para comparação na continuação.
                copia_estado_anterior = []
                # Laço de repetição que percorre as linhas do "tabuleiro_atual".
                for linha_original in estado_atual:
                    # Cria uma cópia da lista interna.
                    copia_linha = list(linha_original)
                    copia_estado_anterior.append(copia_linha)
                # Atribui a cópia completa à variável estado_anterior.
                estado_anterior = copia_estado_anterior

                # Atribuição de variável. Evoca uma função que calcula o próximo estado.
                estado_atual = calcular_proximo_estado(estado_atual)
                # Contador que aumenta +1 a cada geração.
                geracao += 1

    # Imprime uma frase.
    print("\n--- Jogo Encerrado ---")

# Garante que o código só será executado diretamente. 
if __name__ == "__main__":
    main()