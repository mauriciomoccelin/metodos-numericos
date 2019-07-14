import numpy as np

class RegressaoQuadratica:

  def __init__(self, planoCartesiano):
    self.planoCartesiano = planoCartesiano
    self.somatorioAbscissas = None
    self.somatorioOrdenadas = None
    self.somatorioQuadradoAbscissas = None
    self.somatorioCuboAbscissas = None
    self.somatorioQuartaPotenciaAbscissas = None
    self.somatorioMultiplicacaoAbscissaPorOrdenada = None
    self.somatorioMultiplicacaoQuadradoAbscissaPorOrdenada = None
    self.totalParOrdenados = None
    self.intercepcaoReta = None
    self.coeficienteAngular = None
    self.coeficienteAngularQuadratico = None
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
    self.somatorioCuboAbscissas = sum(
      map(
        lambda abscissa: abscissa**3, 
        self.planoCartesiano.keys()
      )
    )
    self.somatorioQuartaPotenciaAbscissas = sum(
      map(
        lambda abscissa: abscissa**4, 
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
    self.somatorioMultiplicacaoQuadradoAbscissaPorOrdenada = sum(
      map(
        lambda abscissa, ordenada: abscissa**2 * ordenada,
        self.planoCartesiano.keys(),
        self.planoCartesiano.values()
      )
    )

  def gerar_equacao(self):
    self.calcular_sistema()
    self.matrizSistemaAbscissas = np.array([
      [self.somatorioQuartaPotenciaAbscissas, self.somatorioCuboAbscissas, self.somatorioQuadradoAbscissas],
      [self.somatorioCuboAbscissas, self.somatorioQuadradoAbscissas, self.somatorioAbscissas],
      [self.somatorioQuadradoAbscissas, self.somatorioAbscissas, self.totalParOrdenados]
    ])
    self.matrizSistemaOrdenadas = np.array(
      [
        self.somatorioMultiplicacaoQuadradoAbscissaPorOrdenada, 
        self.somatorioMultiplicacaoAbscissaPorOrdenada, 
        self.somatorioOrdenadas
      ]
    )
    self.solucao = np.linalg.solve(
      self.matrizSistemaAbscissas,
      self.matrizSistemaOrdenadas
    )
    self.coeficienteAngularQuadratico = self.solucao[0]
    self.coeficienteAngular = self.solucao[1]
    self.intercepcaoReta = self.solucao[2]
    return '{0:+.4f}x^2 {1:+.4f}x {2:+.4f}'.format(
      self.coeficienteAngularQuadratico, 
      self.coeficienteAngular, 
      self.intercepcaoReta
    )
