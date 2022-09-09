'''Um usuário da rede social é unicamente identificado
  pelo seu número de telefone.'''

'''Grupo de usuários na rede social.
  Um grupo possui um nome e um conjunto de membros.
  Além disso, ele possui exatamente um dono, que é um membro.
  Um grupo não pode estar vazio.
  '''

 '''Adiciona usuário como membro do grupo'''

'''Remove um usuário do grupo, se possível.
    Em alguns casos NÃO é possível remover o usuário do grupo:
    * Se o usuário é o único membro do grupo
    * Se o usuário é dono do grupo
    * Se o usuário não pertence ao grupo
    :return: `True` se o usuário foi removido ou `False` caso contrário
    '''

'''Destitui o dono atual e elege um novo dono.
    O dono deve ser membro do grupo.
    Retorna `True` se o usuário informado é o novo dono
    ou `False` caso contrário.
    '''

'''Indica se um usuário faz parte do grupo'''

'''Retorna uma cópia da lista de membros'''

 '''Retorna quantidade de membros'''