# DECIMAL PARA BINÁRIO

try:
	# entrada do número em decimal
	decimal = int(input("Digite o número em decimal: "))
except:
	#verificação 
	print("ERRO: Valor digitado não é válido...")
else:
	binarios = []
	if decimal == 0:
		# se o número em decimal for "0", retorna apenas o 0 como binario
		binarios.append(0)
	else:
		#enquanto o decimal muda seu valor para a metade do seu valor anterior (divisão inteira), o i guarda o resto da divisão por 2 e então esse valor é adicionado na lista "binarios".
		while decimal != 0:
			i = decimal%2
			decimal = decimal//2
			binarios.append(i)
	# a ordem dos valores da lista é invertida e então o resultado é imprimido.
	binarios.reverse()
	print("Convertido para binário: ", end="")
	for c in range(len(binarios)):
		print(binarios[c], end="")