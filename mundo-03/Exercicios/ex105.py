def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Recebe uma ou mais notas dos alunos (aceita várias).
    :param sit: Define se a situação será exibida ou não.
    :return: dicioná
    """
    relatorio = {}
    relatorio['total'] = len(n)
    relatorio['maior'] = max(n)
    relatorio['menor'] = min(n)
    relatorio['media'] = sum(n) / relatorio['total']
    if sit:
        if relatorio['media'] < 5:
            relatorio['situação'] = 'RUIM'
        elif relatorio['media'] < 7:
            relatorio['situação'] = 'RAZOÁVEL'
        else:
            relatorio['situação'] = 'BOA'
    return relatorio


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
