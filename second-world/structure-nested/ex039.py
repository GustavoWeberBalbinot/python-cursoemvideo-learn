""""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date

birth_year = int(input('Enter with your year of birht: '))
actual_year = date.today().year
year_person = actual_year - birth_year

if year_person >= 16 and year_person < 18:
    print('You can still enlist')
elif year_person == 18:
    print('You need still enlist')
elif year_person > 18:
    print('You are late for enlistment')