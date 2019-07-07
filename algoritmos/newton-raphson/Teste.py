from NewtonRaphson import NewtonRaphson

newtonRaphson = NewtonRaphson(
  2.5,
  5e-2,
  'x ** 2 - 5'
)

newtonRaphson.calcular()
print(newtonRaphson.resposta_formatada())