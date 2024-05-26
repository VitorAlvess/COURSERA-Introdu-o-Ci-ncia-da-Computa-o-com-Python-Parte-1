def calcula_assinatura(texto):
    # Função para calcular os traços linguísticos de um texto
    # Tamanho médio de palavra
    palavras = texto.split()
    tamanho_total_palavras = sum(len(palavra) for palavra in palavras)
    tamanho_medio_palavra = tamanho_total_palavras / len(palavras)
    
    # Relação Type-Token
    palavras_diferentes = set(palavras)
    relacao_type_token = len(palavras_diferentes) / len(palavras)
    
    # Razão Hapax Legomana
    palavras_unicas = [palavra for palavra in palavras if palavras.count(palavra) == 1]
    razao_hapax_legomana = len(palavras_unicas) / len(palavras)
    
    # Tamanho médio de sentença
    sentencas = texto.split('.')
    tamanho_total_sentencas = sum(len(sentenca) for sentenca in sentencas)
    tamanho_medio_sentenca = tamanho_total_sentencas / len(sentencas)
    
    # Complexidade de sentença
    frases = texto.split('.')
    numero_total_frases = sum(len(frase.split(',')) for frase in frases)
    complexidade_sentenca = numero_total_frases / len(sentencas)
    
    # Tamanho médio de frase
    frases = texto.split('.')
    tamanho_total_frases = sum(len(frase) for frase in frases)
    tamanho_medio_frase = tamanho_total_frases / len(frases)
    
    return [tamanho_medio_palavra, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def compara_assinatura(assinatura_coahpiah, assinatura_texto):
    # Função para calcular o grau de similaridade entre duas assinaturas
    soma_diferencas = 0
    for i in range(6):
        diferenca = abs(assinatura_coahpiah[i] - assinatura_texto[i])
        soma_diferencas += diferenca
    return soma_diferencas / 6

def avalia_textos(textos, assinatura_coahpiah):
    # Função para identificar o texto mais provavelmente escrito por um aluno infectado
    similaridade_minima = float('inf')
    texto_infectado = ""
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_coahpiah, assinatura_texto)
        if similaridade < similaridade_minima:
            similaridade_minima = similaridade
            texto_infectado = texto
    return texto_infectado

def main():
    # Receber a assinatura do portador de COH-PIAH
    assinatura_coahpiah = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]  # Exemplo de assinatura
    
    # Receber os textos desconhecidos
    textos = []
    texto = input("Digite um texto ou digite fim para encerrar a entrada de textos:\n")
    while texto.lower() != "fim":
        textos.append(texto)
        texto = input()
    
    # Identificar o texto mais provavelmente escrito por um aluno infectado
    texto_infectado = avalia_textos(textos, assinatura_coahpiah)
    
    # Exibir o texto mais provavelmente infectado
    print("O texto mais provavelmente escrito por um aluno infectado é:\n", texto_infectado)

if __name__ == "__main__":
    main()
