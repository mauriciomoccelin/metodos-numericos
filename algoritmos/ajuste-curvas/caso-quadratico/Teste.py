from RegressaoQuadratica import RegressaoQuadratica

planoCartesiano = {
  0: 34,
  1: 45,
  2: 63,
  3: 88,
  4: 120,
  5: 159,
  6: 205
}

regressaoQuadratica = RegressaoQuadratica(planoCartesiano)
print(regressaoQuadratica.gerar_equacao())
