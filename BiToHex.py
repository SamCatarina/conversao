

bi = input("Digite o número em binário: ")
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

	#divide em grupos de 4 números e adc na lista binarios
	binario.reverse()
	binarios = []
	i = 0
	while i < len(binario):
		tempBi = []
		for c in range(i, i+4):
			if c >= len(binario):
				binario.append(0)
			tempBi.append(binario[c])
			i += 1
		tempBi.reverse()
		binarios.append(tempBi)


	binarios.reverse()

	hexadecimal = []

	hexLett = ["a", "b", "c", "d", "e", "f"]

	
	#converte de binario para decimal e depois para hexadecimal
	for c in binarios:
		hex = 0
		i = 0
		c.reverse()
		for a in c:
			hex += ( a * (2**i))
			i += 1
		if hex >= 10:
			hexL = hexLett[hex - 10]
			hexadecimal.append(hexL)
		else:
			hexadecimal.append(hex)


	#imprime o número em hexadecimal
	print("O número em hexadecimal: ", end="")
	for c in hexadecimal:
		print(c, end="")
			
	