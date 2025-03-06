# Database Cohort
Este repositório contém um script em Python para gerar uma base de dados simulada (em excel), com o objetivo de realizar análises de cohort (retenção de clientes) em soluções SaaS. 
A ideia é facilitar a criação de datasets com registros realistas, permitindo a análise de métricas de retenção e churn de clientes.

## Utilização dos Scripts

#### 1) Bibliotecas necessárias
Instale previamente as bibliotecas python abaixo:
```
pip install pandas
pip install random
pip install pandas Faker
pip install datetime
```
#### 2) Alterar as variáveis
- ```num_registros```: define a quantidade de registros da base a ser gerada
- ```data_inicio_contrato```: define o ínicio dos contratos dos clientes
- ```data_fim_global```: definem o período final dos contratos dos clientes (se estiver vazio, então ele está ativo)
- ```motivo_churn```: coloque quantos motivos preferir alternando-os com vírgula
- ```vendedores```: coloque quantos vendedores preferir alternando-os com vírgula
- ```churn_probability```: define o percentual de churn de toda a base
- ```plano```: dicionário com os nomes e valores dos planos, altere como preferir
- ```caminho```: defina o caminho onde a base .csv será salva

#### 3) Executar o script
```python
python cohort_database.py
```

#### 4) Analisar
Agora basta utilizar essa base na ferramenta de dados que preferir
<br>
