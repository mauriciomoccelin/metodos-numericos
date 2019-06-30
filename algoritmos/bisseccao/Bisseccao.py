import numpy as np

class Bisseccao:
  
  def __init__(self, intervaloInicial, intervaloFinal, toleracia, funcao):
    self.intervaloInicial = intervaloInicial
    self.intervaloFinal = intervaloFinal
    self.toleracia = toleracia
    self.funcao = funcao
    self.raiz = None
    self.erro = None
    self.iteracoes = None

  def calcular(self):
    pontoMedio = 0
    self.iteracoes = 0
    while (np.abs(self.intervaloInicial - self.intervaloFinal) > self.toleracia):
        self.iteracoes = self.iteracoes + 1
        pontoMedio = (self.intervaloInicial + self.intervaloFinal) / 2
        resultadoFuncaoParaIntervaloInicial = self.funcao(self.intervaloInicial)
        resultadoFuncaoParaIntervaloMedio = self.funcao(pontoMedio)
        
        if resultadoFuncaoParaIntervaloInicial * resultadoFuncaoParaIntervaloMedio < 0:
            self.intervaloFinal = pontoMedio
        else:
            self.intervaloInicial = pontoMedio

    self.raiz = pontoMedio
    self.erro = np.abs(self.intervaloInicial - self.intervaloFinal)
    return
  
  def resposta_formatada(self):
    return "Raiz Aproximada: {0:.4f}, Erro: {1:.4f} Numero de Iterações: {2}".format(self.raiz, self.erro, self.iteracoes)