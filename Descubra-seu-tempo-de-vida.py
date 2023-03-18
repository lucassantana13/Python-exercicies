from datetime import datetime, timedelta


aniv = input('Insira a data do seu aniversário: (ex: dd/mm/aaaa)')
f = '%d/%m/%Y'

aniv = datetime.strptime(aniv, f)

hoje = datetime.now()

idade = hoje - aniv

idade = idade.days

print(f'Você tem {idade//365} anos')
print(f'Você tem {idade//30} meses')
print(f'Você tem {idade//7} semanas')
print(f'Você tem {idade} dias')


