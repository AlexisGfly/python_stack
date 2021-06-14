class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in range (len(nums)):
            self.result += nums[i]
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for i in range (len(nums)):
            self.result -= nums[i]
        return self




# Pruebas para método add
md = MathDojo()
x = md.add(5,5,10).result
print('Prueba add N. 1, x=',x)
md = MathDojo()
x = md.add(1,2,3,4,5,6,7,8,9).result
print('Prueba add N. 2, x=',x)
md = MathDojo()
x = md.add(20).result
print('Prueba add N. 3, x=',x)

print('\n')

# Pruebas para método subtract
md = MathDojo()
x = md.subtract(20,10,5).result
print('Prueba add N. 1, x=',x)
md = MathDojo()
x = md.subtract(45,5,10,20).result
print('Prueba add N. 2, x=',x)
md = MathDojo()
x = md.subtract(20).result
print('Prueba add N. 3, x=',x)

print('\n')

# Para Método encadenado:
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print('Resultado encadenado, x=',x)	# debe imprimir 5
