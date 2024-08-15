isPar=lambda x: x%2==0
print(isPar(10))

numbers =[1,2,4,5,6,77,44,33,53,2323,54,55]
isvalid=list(map(isPar,numbers))

print(isvalid)


fruits = ['apple', 'banana', 'cherry','lemon', 'orange']
find = list(filter(lambda x: 'an' in x, fruits))
print(find)

findImpar = list(filter(lambda x: x%2!=0, numbers))
print(findImpar)


quadrado = [1,3,4,5,6,10]
quadrados = list(map(lambda x: x**2, quadrado))
print(quadrados)

# ou compreensao de lista
quadrados = [num**2 for num in quadrado]
print(quadrados)

#criar lista de numero pares
pares = [par for par in numbers if isPar(par)]
print(pares)

distributiva = [n1* n2 for n1 in [4,5,6] for n2 in [1,2,3]]
print(distributiva)

# ternarios
a = 60 
b = 50
print(f'se A menor que B retorna {b} se nao retorna {a} resultado =  {(a , b ) [ a < b ] }')

