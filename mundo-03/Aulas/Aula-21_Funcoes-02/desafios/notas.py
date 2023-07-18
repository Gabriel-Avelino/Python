def notas(*n, sit=False):
    """
    -> Recebe as notas dos alunos, e se quer exibir a situação e retorna um relatório completo.
    O relatório traz o total de notas, a maior nota, a menor nota, a média e se solicitado, a situação.
    :param n: Recebe as notas
    :param sit: Pede se deseja adicionar a situação ao relatório.
    :return: relatorio
    """

    relatorio = {}
    relatorio['total'] = len(n)
    relatorio['maior'] = 0
    relatorio['menor'] = 0
    tot = 0
    for c, v in enumerate(n):
        tot += v
        if c == 0:
            relatorio['maior'] = v
            relatorio['menor'] = v
        elif v > relatorio['maior']:
            relatorio['maior'] = v
        elif v < relatorio['menor']:
            relatorio['menor'] = v
    relatorio['média'] = tot / relatorio['total']
    if sit:
        if relatorio['média'] < 5:
            relatorio['situação'] = 'RUIM'
        elif relatorio['média'] < 7:
            relatorio['situação'] = 'RAZOÁVEL'
        else:
            relatorio['situação'] = 'BOA'
    return relatorio


resp = notas(7, 7, 7, sit=True)
print(resp)
help(notas)
