import pandas as pd
import random
import string
from faker import Faker
from datetime import datetime, timedelta

# Variáveis
num_registros = 5351
data_inicio_contrato = datetime(2024, 1, 1)
data_fim_global = datetime(2025, 3, 6)
churn_probability = 0.3
motivos_churn = ["Engajamento", "Produto", "Atendimento"]
vendedores = ["Vendedor A", "Vendedor B", "Vendedor C", "Vendedor D"]
caminho = "C:/Users/Thiago/Desktop/cohort_database.csv"

planos = {
    "essencial": 50,
    "avancado": 100,
    "profissional": 200
}

# Lista de UFs
ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
       "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
       "SP", "SE", "TO"]

regiao_map = {
    "Norte": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-Oeste": ["DF", "GO", "MT", "MS"],
    "Sudeste": ["ES", "MG", "RJ", "SP"],
    "Sul": ["PR", "RS", "SC"]
}

def get_regiao(uf):
    for regiao, estados in regiao_map.items():
        if uf in estados:
            return regiao
    return None

def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

def next_month(date):
    """Retorna o primeiro dia do próximo mês."""
    if date.month == 12:
        return datetime(date.year + 1, 1, 1)
    else:
        return datetime(date.year, date.month + 1, 1)

# Faker para gerar nomes (em pt_BR)
fake = Faker('pt_BR')
dados = []

for i in range(1, num_registros + 1):
    # Gera um id_cliente com 6 caracteres alfanuméricos
    id_cliente = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    nome_cliente = fake.name()

    # Gera data de contratação
    data_contratacao = random_date(data_inicio_contrato, data_fim_global - timedelta(days=1))
    data_contratacao_str = data_contratacao.strftime("%Y-%m-%d")
    mes_inicio = data_contratacao.strftime("%Y-%m-01")
    
    # Verifica se é possível ter churn (próximo mês <= data_fim_global)
    proximo_mes = next_month(data_contratacao)
    pode_ter_churn = proximo_mes <= data_fim_global

    # Define status do cliente
    if pode_ter_churn and random.random() < churn_probability:
        status_cliente = "churn"
        churn_date = random_date(proximo_mes, data_fim_global)
        data_fim_str = churn_date.strftime("%Y-%m-%d")
        mes_fim = churn_date.strftime("%Y-%m-01")
        motivo = random.choice(motivos_churn)
    else:
        status_cliente = "ativo"
        data_fim_str = ""
        mes_fim = ""
        motivo = ""
    
    # Escolhas aleatórias
    estado = random.choice(ufs)
    regiao = get_regiao(estado)
    nome_vendedor = random.choice(vendedores)
    plano = random.choice(list(planos.keys()))
    valor_mrr = planos[plano]

    # Criação do registro
    registro = {
        "id_cliente": id_cliente,
        "nome_cliente": nome_cliente,
        "data_contratacao": data_contratacao_str,
        "data_fim": data_fim_str,
        "mes_inicio": mes_inicio,
        "mes_fim": mes_fim,
        "estado": estado,
        "regiao": regiao,
        "nome_vendedor": nome_vendedor,
        "motivo_churn": motivo,
        "status_cliente": status_cliente,
        "valor_mrr": valor_mrr,
        "plano": plano
    }
    
    dados.append(registro)

df = pd.DataFrame(dados)

# Salva a base em um arquivo CSV
df.to_csv(caminho, index=False)
print('Base de dados salva com sucesso!')
