import itertools

# Função para calcular a distância entre duas cidades
def calcular_distancia(cidade1, cidade2):
    # Distâncias aproximadas fornecidas anteriormente (em quilômetros)
    distancias = {
        ('Belo Horizonte', 'Manaus'): 2760,
        ('Belo Horizonte', 'Fortaleza'): 2000,
        ('Belo Horizonte', 'Salvador'): 1150,
        ('Belo Horizonte', 'Porto Alegre'): 1300,
        ('Manaus', 'Fortaleza'): 2200,
        ('Manaus', 'Salvador'): 3000,
        ('Manaus', 'Porto Alegre'): 4000,
        ('Fortaleza', 'Salvador'): 1350,
        ('Fortaleza', 'Porto Alegre'): 3000,
        ('Salvador', 'Porto Alegre'): 2400
    }

    # Verifica se a distância é conhecida
    if (cidade1, cidade2) in distancias:
        return distancias[(cidade1, cidade2)]
    elif (cidade2, cidade1) in distancias:
        return distancias[(cidade2, cidade1)]
    else:
        # Caso não haja distância conhecida, retorna um valor alto
        return float('inf')

def calcular_distancia_total(rota, distancias):
    distancia_total = 0
    for i in range(len(rota) - 1):
        cidade_atual = rota[i]
        prox_cidade = rota[i + 1]
        
        if (cidade_atual, prox_cidade) in distancias:
            distancia_total += distancias[(cidade_atual, prox_cidade)]
        elif (prox_cidade, cidade_atual) in distancias:
            distancia_total += distancias[(prox_cidade, cidade_atual)]
        else:
            distancia_total += calcular_distancia(cidade_atual, prox_cidade)
    
    return distancia_total

# Função que implementa o algoritmo do Caixeiro Viajante
def caixeiro_viajante(cidades):
    # Cria todas as permutações possíveis das cidades
    todas_rotas = list(itertools.permutations(cidades))

    # Dicionário para armazenar as distâncias entre as cidades
    distancias = {}

    # Calcula as distâncias entre todas as cidades
    for rota in todas_rotas:
        distancias[rota] = calcular_distancia_total(rota, distancias)

    # Encontra a rota com a menor distância total
    menor_distancia = float('inf')
    melhor_rota = None

    for rota in todas_rotas:
        distancia = distancias[rota]
        print(rota , distancia)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_rota = rota

    return melhor_rota, menor_distancia

# Exemplo de utilização
cidades = ['Belo Horizonte', 'Manaus', 'Fortaleza', 'Salvador', 'Porto Alegre']
melhor_rota, menor_distancia = caixeiro_viajante(cidades)

print("Melhor rota encontrada:", melhor_rota)
print("Menor distância total:", menor_distancia)
