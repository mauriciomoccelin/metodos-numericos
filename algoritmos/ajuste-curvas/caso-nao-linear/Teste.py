from RegressaoExponencial import RegressaoExponencial

planoCartesiano = {
  0 : 30.6,
  20: 41.2,
  40: 70.2,
  60: 93.1,
  71: 146.2,
}

regressaoExponencial = RegressaoExponencial(planoCartesiano)
print(regressaoExponencial.gerar_equacao())
