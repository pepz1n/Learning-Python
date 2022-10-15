# estados = ['SC', 'SP', 'RS']
# estados = ['Santa catarina', 'São paulo', 'Rio grande do sul']
estados = {
  'NY': 'New York',
  'SC': 'Santa Catarina',
  'RS': 'Rio Grande Do Sul'
}

estados.pop('NY')
estados['NOVO'] = 'Partido'

print(estados)
print(estados.get('dsa', 'Não encontrado'))
