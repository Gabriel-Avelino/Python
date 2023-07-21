from utilidadesCeV.moeda import resumir
from utilidadesCeV.dado import validar

p = validar.leianumero('Digite o preço: R$')
resumir.resumo(p, 80, 35)
