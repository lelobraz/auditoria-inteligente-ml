import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Configuração para reprodutibilidade
np.random.seed(42)
n_contratos = 200

# 2. Criação de Dados Históricos Normais (Simulação baseada em cenários de Auditoria)
horas_normais = np.random.normal(loc=160, scale=20, size=n_contratos)  # Média de 160h/mês
valor_normal = np.random.normal(loc=15000, scale=3000, size=n_contratos)  # Média de R$ 15.000
erros_sla = np.random.poisson(lam=1.2, size=n_contratos)  # Média baixa de erros operacionais

df = pd.DataFrame({
    'ID_Contrato': [f'CTR-{i:04d}' for i in range(1, n_contratos + 1)],
    'Horas_Trabalhadas': np.round(horas_normais, 1),
    'Valor_Faturado': np.round(valor_normal, 2),
    'Erros_SLA_Registrados': erros_sla  # <-- Corrigido aqui (sem o 's')
})

# 3. Injeção de Anomalias Proposicionais (Simulando Fraudes, Erros de Digitação e Desvios de Compliance)
# Caso A: Faturamento altíssimo com poucas horas trabalhadas (Supreço/Fraude)
df.loc[15, 'Valor_Faturado'] = 85000.00
df.loc[15, 'Horas_Trabalhadas'] = 45.0

# Caso B: Contrato com volume extremo de quebras de SLA (Risco de Operação)
df.loc[42, 'Erros_SLA_Registrados'] = 18

# Caso C: Valores excessivos fora do padrão estatístico do contrato
df.loc[112, 'Valor_Faturado'] = 79000.00
df.loc[112, 'Horas_Trabalhadas'] = 210.0

print("✅ Base de dados consolidada com sucesso!")

# 4. Preparação dos Dados para a Inteligência Artificial
recursos_auditoria = df[['Horas_Trabalhadas', 'Valor_Faturado', 'Erros_SLA_Registrados']]

# 5. Aplicação do Modelo de Machine Learning (Isolation Forest)
modelo_auditor = IsolationForest(contamination=0.03, random_state=42)
modelo_auditor.fit(recursos_auditoria.values)  # Usando .values para evitar avisos de nomes de colunas

# 6. Predição: O modelo classifica 1 para registros normais e -1 para anomalias
df['Resultado_Auditoria'] = modelo_auditor.predict(recursos_auditoria.values)
df['Status'] = df['Resultado_Auditoria'].map({1: 'Em Conformidade', -1: '⚠️ Alerta de Auditoria'})

# 7. Filtragem e Exibição dos Contratos Suspeitos
contratos_suspeitos = df[df['Resultado_Auditoria'] == -1]

print(f"\n🔍 RESULTADO DA AUDITORIA AUTOMATIZADA: Encontrados {len(contratos_suspeitos)} contratos suspeitos.")
print("-" * 90)
print(contratos_suspeitos[['ID_Contrato', 'Horas_Trabalhadas', 'Valor_Faturado', 'Erros_SLA_Registrados', 'Status']].to_string(index=False))
print("-" * 90)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Configurando a figura 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 2. Separando os dados para plotagem
normais = df[df['Resultado_Auditoria'] == 1]
anomalias = df[df['Resultado_Auditoria'] == -1]

# 3. Plotando os contratos normais (em azul e com transparência)
ax.scatter(normais['Horas_Trabalhadas'], 
           normais['Valor_Faturado'], 
           normais['Erros_SLA_Registrados'], 
           c='royalblue', marker='o', s=40, alpha=0.6, label='Em Conformidade')

# 4. Plotando as anomalias/fraudes (em vermelho, maiores e bem destacadas)
ax.scatter(anomalias['Horas_Trabalhadas'], 
           anomalias['Valor_Faturado'], 
           anomalias['Erros_SLA_Registrados'], 
           c='crimson', marker='x', s=120, linewidths=3, label='⚠️ Alerta de Auditoria')

# 5. Configurando os títulos e eixos (Mathtext/Estilo limpo)
ax.set_title('Detecção de Anomalias em Contratos com Isolation Forest', fontsize=14, pad=20, fontweight='bold')
ax.set_xlabel('Horas Trabalhadas (Mês)', fontsize=10, labelpad=10)
ax.set_ylabel('Valor Faturado (R$)', fontsize=10, labelpad=10)
ax.set_zlabel('Erros de SLA', fontsize=10, labelpad=10)

# 6. Adicionando legenda e exibindo o gráfico
ax.legend(loc='upper left', fontsize=11)
plt.tight_layout()
plt.show()
