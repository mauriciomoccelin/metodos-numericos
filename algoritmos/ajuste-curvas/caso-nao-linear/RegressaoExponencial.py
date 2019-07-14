import numpy as np

class RegressaoExponencial:

  def __init__(self, planoCartesiano):
    self.planoCartesiano = planoCartesiano
    self.somatorioAbscissas = None
    self.somatorioOrdenadas = None
    self.somatorioQuadradoAbscissas = None
    self.somatorioLogaritmoNatualOrdenada = None
    self.somatorioAbscissaPorLogaritmoNatualOrdenada = None
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
    self.somatorioLogaritmoNatualOrdenada = sum(
      map(
        lambda ordenada: np.log(ordenada),
        self.planoCartesiano.values()
      )
    )
    self.somatorioAbscissaPorLogaritmoNatualOrdenada = sum(
      map(
        lambda abscissa, ordenada: abscissa * np.log(ordenada),
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
      [
        self.somatorioAbscissaPorLogaritmoNatualOrdenada, 
        self.somatorioLogaritmoNatualOrdenada
      ]
    )
    self.solucao = np.linalg.solve(
      self.matrizSistemaAbscissas,
      self.matrizSistemaOrdenadas
    )
    self.coeficienteAngular = self.solucao[0]
    self.intercepcaoReta = np.exp(self.solucao[1])
    return '{1:+.4f}e^{0:+.4f}x'.format(self.coeficienteAngular, self.intercepcaoReta)
