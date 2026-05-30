# auditoria-inteligente-ml
Detecção automatizada de fraudes e anomalias operacionais em contratos utilizando algoritmos de Machine Learning (Isolation Forest) aplicados à Controladoria.
# 🔍 Auditoria Inteligente e Detecção de Anomalias em Contratos

Este projeto desenvolve uma solução automatizada de Inteligência Artificial voltada para áreas de **Controladoria, Auditoria e Compliance Financeiro**. O objetivo é identificar automaticamente fraudes, erros de faturamento ou desvios graves de SLA (Acordo de Nível de Serviço) em contratos de prestadores de serviços de grande escala.

## 💼 O Desafio de Negócio
Em auditorias tradicionais, a checagem de relatórios de faturamento e conformidade operacional é feita por amostragem ou de forma manual através de planilhas. Em operações massivas, isso gera furos de governança, permitindo falhas como superfaturamento ou aceitação de serviços fora do padrão acordado. 

Esta solução propõe uma abordagem de **Auditoria Contínua (End-to-End)**, onde 100% dos contratos são analisados por algoritmos estatísticos que filtram instantaneamente apenas os casos de altíssimo risco para investigação humana.

## 🛠️ Tecnologias e Algoritmos Utilizados
*   **Linguagem:** Python 3.x
*   **Manipulação de Dados:** Pandas e NumPy
*   **Machine Learning (Não Supervisionado):** `Isolation Forest` (Scikit-Learn)
*   **Visualização Espacial:** Matplotlib e mpl_toolkits (Gráfico de Dispersão 3D)

### Por que o Isolation Forest?
Diferente de abordagens supervisionadas que exigem um histórico massivo de fraudes já rotuladas, o *Isolation Forest* baseia-se no princípio de que anomalias são **raras e estatisticamente diferentes** dos dados normais. O algoritmo isola os pontos fora da curva criando partições no espaço de atributos. Registros fraudulentos ou errôneos exigem menos divisões para serem isolados, sendo detectados logo no início da árvore de decisão.

## 📊 Resultados do Modelo
O modelo foi calibrado com uma taxa de contaminação de 3% (`contamination=0.03`) e isolou com precisão cirúrgica três comportamentos críticos inseridos na base:
1.  **Suspeita de Superfaturamento:** Contrato com baixíssimo volume de horas trabalhadas e faturamento atipicamente elevado.
2.  **Risco de Quebra Operacional:** Contrato apresentando volume extremo de erros de SLA acumulados em um único mês.
3.  **Desvio de Escala:** Registro com valores financeiros e operacionais completamente fora da distribuição estatística padrão da empresa.

---
*Desenvolvido por Celio Cipriano Braz - Cientista de Dados & Especialista em Controladoria (CRA-SP 157031).*
