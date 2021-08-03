from dominio import Usuario, Lance, Leilao, Avaliador

#Cria os usuários
pedro = Usuario('Pedro')
iara = Usuario('Iara')

#Cria os lances por usuário
lance_pedro = Lance(pedro, 100)
lance_iara = Lance(iara, 150)

#Cria o Leilão de uma peça
leilao = Leilao('Celular')

#Adciona ao leilão os lances dos usuários
leilao.lances.append(lance_pedro)
leilao.lances.append(lance_iara)

#Percorre os lances
for lance in leilao.lances:
	print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior {avaliador.maior_lance}')