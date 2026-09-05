A = [3, 5, 7 ,8]
B = A[:]

B.append(99)

print(f'lista A: {A}')
print(f'lista A: {B}') # agora ela fez uma copia em vez em se conectar
