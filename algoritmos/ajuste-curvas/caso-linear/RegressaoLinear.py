import numpy as np

class RegressaoLinear:

  def __init__(self, planoCartesiano):
    self.planoCartesiano = planoCartesiano
    self.somatorioAbscissas = None
    self.somatorioOrdenadas = None
    self.somatorioQuadradoAbscissas = None
    self.somatorioMultiplicacaoAbscissaPorOrdenada = None
    self.totalParOrdenados = None
    self.intercepcaoReta = None
    self.coeficienteAngular = None
    self.matrizSistemaOrdenadas = None
    self.matrizSistemaAbscissas = None
    self.solucao = None
  
  def calcular_sistema(self):
    self.totalParOrdenados = len(self.planoCartesiano)
    self.somatorioAbscissas = sum(self.planoCartesiano.keys())
    self.somatorioOrdenadas = sum(self.planoCartesiano.values())
    self.somatorioQuadradoAbscissas = sum(
      map(
        lambda abscissa: abscissa**2, 
        self.planoCartesiano.keys()
      )
    )
    self.somatorioMultiplicacaoAbscissaPorOrdenada = sum(
      map(
        lambda abscissa, ordenada: abscissa * ordenada,
        self.planoCartesiano.keys(),
        self.planoCartesiano.values()
      )
    )

  def gerar_equacao(self):
    self.calcular_sistema()
    self.matrizSistemaAbscissas = np.array([
      [self.somatorioQuadradoAbscissas, self.somatorioAbscissas],
      [self.somatorioAbscissas, self.totalParOrdenados]
    ])
    self.matrizSistemaOrdenadas = np.array(
      [self.somatorioMultiplicacaoAbscissaPorOrdenada, self.somatorioOrdenadas]
    )
    self.solucao = np.linalg.solve(
      self.matrizSistemaAbscissas,
      self.matrizSistemaOrdenadas
    )
    self.coeficienteAngular = self.solucao[0]
    self.intercepcaoReta = self.solucao[1]
    return '{0:+.4f}x {1:+.4f}'.format(self.coeficienteAngular, self.intercepcaoReta)
