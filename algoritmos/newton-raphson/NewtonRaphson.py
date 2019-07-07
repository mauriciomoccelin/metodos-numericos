from sympy import diff, symbols

class NewtonRaphson:
  def __init__(self, estimativaInicial, tolerancia, funcao):
    self.estimativaInicial = estimativaInicial
    self.derivadaFuncao = str(diff(funcao))
    self.tolerancia = tolerancia
    self.funcao = str(funcao)
    self.raiz = None
    self.erro = None
    self.iteracoes = None
    self.resultadoFuncaoParaEstimativa = None
    self.resultadoDerivadaFuncaoParaEstimativa = None

  def calcular(self):
    x = symbols('x')
    x = self.estimativaInicial
    
    self.iteracoes = 1
    self.resultadoFuncaoParaEstimativa = float(eval(self.funcao))
    self.resultadoDerivadaFuncaoParaEstimativa = float(eval(self.derivadaFuncao))
    
    while (abs(self.resultadoFuncaoParaEstimativa) >= self.tolerancia):
      x = x - self.resultadoFuncaoParaEstimativa/self.resultadoDerivadaFuncaoParaEstimativa
      self.resultadoFuncaoParaEstimativa = float(eval(self.funcao))
      self.resultadoDerivadaFuncaoParaEstimativa = float(eval(self.derivadaFuncao))
      self.iteracoes = self.iteracoes + 1 
    
    self.raiz = x
    self.erro = abs(self.resultadoFuncaoParaEstimativa)
  
  def resposta_formatada(self):
    return "Raiz Aproximada: {0:.4f}, Erro: {1:.4f} Numero de Iterações: {2}".format(
      self.raiz,
      self.erro,
      self.iteracoes
    )