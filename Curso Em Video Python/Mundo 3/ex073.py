"""
Crie uma tupla preenchida com os 20 primeiros numeros colocados da tabela do campeonato brasileiro de futebol, na
ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os time em ordem alfabética
D) Em que posição na tabela, esta o time chapecoense
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico',
         'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba',
         ' Avai', 'Ponte Preta', 'Atletico-GO')
print('-' * 50)
print(f'Lista de times do Brasileirão: {times}')
print('-' * 50)
print(f'Os 5 primeiros são {times[0:5]}')
print('-' * 50)
print(f'Os 4 ultimos são {times[-4:]}')
print('-' * 50)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-' * 50)
print(f'A posição do chapecoense é de {times.index("Chapecoense") + 1}º lugar')
