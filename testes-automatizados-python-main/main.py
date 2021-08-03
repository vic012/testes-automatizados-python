from dominio import Usuario, Lance, Leilao

#Cria os usuários
pedro = Usuario('Pedro')
iara = Usuario('Iara')

#Cria os lances por usuário
lance_pedro = Lance(pedro, 100.80)
lance_iara = Lance(iara, 1546.23)

#Cria o Leilão de uma peça
leilao = Leilao('Celular')

#Adciona ao leilão os lances dos usuários
leilao.lances.append(lance_pedro)
leilao.lances.append(lance_iara)

#Percorre os lances
for lance in leilao.lances:
	print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')