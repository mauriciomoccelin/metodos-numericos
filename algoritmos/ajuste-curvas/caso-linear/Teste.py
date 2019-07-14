from RegressaoLinear import RegressaoLinear

planoCartesiano = {
  0.5: 4.4,
  2.8: 1.8,
  4.2: 1.0,
  6.7: 0.4,
  8.3: 0.2
}

regressaoLinear = RegressaoLinear(planoCartesiano)
print(regressaoLinear.gerar_equacao())
