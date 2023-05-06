# BINÁRIO PARA DECIMAL

# input do numero binario pelo usuário é armazenado em uma variável e depois transformado em uma lista, em string
bi =  input("Digite o número em binário: ")
bi = list(bi)
binario = []

#verificação 

try:
	for c in bi:
		if c == "0" or c == "1":
			# se for uma número válido (em binário), ele será convertido em inteiro e adicionado a lista "binario"
			binario.append(int(c))
		else:
			raise Exception

except:
	print("Número inválido")

else:
			
	#ordem da lista é invertida, por motivos práticos
	binario.reverse()
	
	decimal = 0
	i = 0

	#realiza a operação de conversão
	for c in binario:
		decimal += ( c * (2**i))
		i += 1

	#exibe o numero em decimal
	print("O número em decimal: ", end="")
	print(decimal)
	