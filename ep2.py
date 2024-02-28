# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np

#0.7420135182433   valor verdadeiro da integral

def Funcao_f(x):
    a, b = 0.55297, 0.48854
    f = math.exp(-a*x) * math.cos(b*x)
    
    return f

def Funcao_p(x):
    m = 0.492
    p = -m * x + 1
    return p

def Integral_de_p(x):
    m = 0.492
    i_P = -m *(x**2) + x
    
    return i_P

def main():
    tamanho = 100000   #Tamanho da amostra gerada
    
    amostra_uniforme = np.random.uniform(0, 1, tamanho)
    pontos_uniforme = np.random.uniform(0, 1, (tamanho, 2))
    
    """
    a,b = 0,1
    amostra_beta = np.random.beta(a, b, tamanho)   
    pontos_beta = np.random.beta(a, b, (tamanho, 2))   
    
    Beta:
    E(X) = a/(a+b)
    
    k,teta= 0,1
    amostra_gamma = np.random.gamma(k, teta, tamanho)
    Gama
    E(X) = k*teta
   
    amostra_weibull = np.random.weibull(a, tamanho)
    """
    teste = MonteCarlo_Cru(amostra_uniforme, tamanho)
    print(teste)
    
    teste= MonteCarlo_HitMiss(pontos_uniforme, tamanho)
    print(teste)

    teste= MonteCarlo_ImportanceSampling(amostra_uniforme, tamanho)
    print(teste)
    
    teste= MonteCarlo_ControlVariates(amostra_uniforme, tamanho)
    print(teste)

#-------------------------------------------#
#-------MÉTODOS DE MONTE CARLO -------------#
#-------------------------------------------#

def MonteCarlo_Cru(amostra_aleatoria, tamanho):
    
    area_estimada_cru = 0
    
    for i in amostra_aleatoria:
        area_estimada_cru += Funcao_f(i)

    area_estimada_cru *= (1-0)
    area_estimada_cru /= tamanho
    
    return area_estimada_cru

def MonteCarlo_HitMiss(pontos_aleatorios,tamanho):
    
    funcao_h = 0
    
    for i in pontos_aleatorios:
        if i[1]<= Funcao_f(i[0]):
            funcao_h += 1
    area_estimada = funcao_h / tamanho
    
    return area_estimada

def MonteCarlo_ImportanceSampling(amostra_aleatoria, tamanho):
    
    area_da_funcao_p = Integral_de_p(1) - Integral_de_p(0) #0.50797443885501
    gama_s = 0
    
    for i in amostra_aleatoria:
        gama_s += Funcao_f(i) / Funcao_p(i)
        
    gama_s /= tamanho
    
    
    area_estimada = gama_s * area_da_funcao_p
    
    return area_estimada

def MonteCarlo_ControlVariates(amostra_aleatoria, tamanho):
    gama_chapeu = 0
    
    for i in amostra_aleatoria:
        gama_chapeu += Funcao_f(i) - Funcao_p(i) + Integral_de_p(i)
        
    gama_chapeu /= tamanho
    
    return gama_chapeu

#-----------------------------------------#
#-----------------------------------------#

def ErroRelativo():
    erro_relativo = 0
    
    return erro_relativo