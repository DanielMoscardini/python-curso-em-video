"""
Faça um software que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta, ou passou do prazo
"""
import datetime
anoAtual = datetime.datetime.now()
anoNasc = int(input('Ano de Nascimento: '))
idade = (anoAtual.year) - anoNasc
#print(f'Voce tem {idade} anos')
if (idade < 18):
    print(f'Voce vai se alistar daqui a: {(idade - 18) * -1} ano, pois esta com {idade} anos')
elif (idade == 18):
    print(f'Voce deve se alistar esse ano, pois esta com {idade} anos')
else :
    print(f'Voce esta {idade - 18} atrasado com o alistamento, pois esta com {idade} anos')
