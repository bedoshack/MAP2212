import random
import statistics
from scipy.stats import norm

def geraPonto():
    ponto = [random.uniform(-1,1), random.uniform(-1,1)]
    return ponto

def verificaPonto(ponto):
    raio = ponto[0]**2 + ponto[1]**2
    if raio > 1: return 0
    else: return 1

def PontosDentro(quantidade_de_pontos):
    total_de_pontos_dentro = 0

    for i in range(quantidade_de_pontos):
        ponto = geraPonto()
        total_de_pontos_dentro += verificaPonto(ponto)
    
    return total_de_pontos_dentro
    

def verificarPrecisao(amostra_de_pontos_dentro, tamanho_da_amostra, quantidade_de_pontos):
    
    
    
    media_pi = statistics.mean(amostra_de_pontos_dentro)
    n = tamanho_da_amostra
    p = media_pi/quantidade_de_pontos
    desvio_padrao = (n*p*(1-p))**0.5
    
    limite_inferior = n*p*(1-1/2000)
    limite_superior = n*p*(1+1/2000)
    
    
    
    confianca = norm.cdf( limite_inferior , media_pi, desvio_padrao) - norm.cdf( limite_superior , media_pi, desvio_padrao)
    
    #-----------------
    #-----------------
    print(confianca)
    
    if confianca >= 0.9:
        print("passou") 
    else:
        print("falhou")

    #maior_desvio = max(max(estimativas_de_pi) - media_pi, media_pi - min(estimativas_de_pi) )
    
    #precisao_dos_testes = maior_desvio/media_pi
    #return precisao_dos_testes

    
def testes():
    tamanho_da_amostra = int(input("Digite o tamanho da amostra: "))
    quantidade_de_pontos = int(input("Digite a quantidade de pontos por amostra: "))

    amostra_de_pontos_dentro = []
    
    for i in range(tamanho_da_amostra):
        amostra_de_pontos_dentro.append(PontosDentro(quantidade_de_pontos))
    
    verificarPrecisao(amostra_de_pontos_dentro, tamanho_da_amostra,quantidade_de_pontos)
          
    pi_estimado = 4* statistics.mean(amostra_de_pontos_dentro)/quantidade_de_pontos
    print(f"O valor de pi estimado é: {pi_estimado}")
    
testes()


# video: queremos precisao maior ou igual a 0,05%
'''
considerar salvar lista da soma dos pontos de cada teste ao invés da estima de pi - economiza tempo
limite_inferior = int( 1+ np(1-1/2000) )limite_superior = min ( int( np(1-1/2000) ) , n )
confianca = binom.cdf( limite_inferior ) - binom.cdf( limite_superior)
if confianca >= 0.9: print("passou")return 1
else: print("falhou")return 0

Repetir o testeCom *10 pontos
'''
