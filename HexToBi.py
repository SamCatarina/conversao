#DE HAXADECIMAL PARA BINÁRIO

hexNum = []
binarios = []


#cria uma lista de letras do "a" até o "f"
hexLett = "abcdef"
hexLett = list(hexLett)

#cria uma lista de números de 0 até 9 
for c in range (0, 10):
	hexNum.append(str(c))

hex =  input("Digite o número em hexadecimal: ")
hex = list(hex)
decimal = []

try:
	#percorre os numeros digitados, se estiverem na lista de hexadecimais-numericos(hexNum) ou na lista de hexadecimais-letras (hexLett) o número será adicionado a lista "decimal" (no caso das letras, ele será convertido primeiro para decimal e depois adc à lista)
	for c in hex:
		if c in hexNum:
			decimal.append(c)
		elif c in hexLett: 
			decC = hexLett.index(c)
			decimal.append(decC + 10)
		else:
			raise Exception 

except:
	print("Número inválido")

else:
	if decimal == 0:
			# se o número em decimal for "0", retorna apenas o 0000 como binario
			binarios.append([0,0,0,0])
	else:
		#converte cada numero presente na lista "decimal" para binário
		for c in decimal:
			dec = int(c)
			tempBi = []
			while dec != 0:
				i = dec%2
				dec = dec//2
				tempBi.append(i)
			tempBi.reverse()
				
			while len(tempBi) < 4:
				tempBi.insert(0, 0)

			binarios.append(tempBi)

	#exibe
	print("O número em binário: ", end="")
	
	for c in binarios:
		for i in c:
			print(i, end="")
		print(" ", end="")
