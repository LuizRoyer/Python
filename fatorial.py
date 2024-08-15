#recursividade

def fatorial(number):
	if number == 0 or number ==1:
		return 1
	return number * fatorial(number -1)


if __name__ =='__main__':
	
	number = int(input('digite um numero: '))
	try:
		result = fatorial(number)
	except RecursionError:
		print('numero invalido')
	else:
		print(f'o Fatorial de {number} = {result}') 
