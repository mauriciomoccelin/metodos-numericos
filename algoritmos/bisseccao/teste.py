from Bisseccao import Bisseccao

bisseccao = Bisseccao(
  0, 
  3, 
  1e-3, 
  lambda x: x**3 - 9 * x + 5
)

bisseccao.calcular()
print(bisseccao.resposta_formatada())