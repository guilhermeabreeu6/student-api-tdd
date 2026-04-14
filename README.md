🎓 API de Gerenciamento de Alunos (Abordagem TDD)
📌 Descrição
Este projeto é uma evolução de um sistema de gestão escolar, apresentando agora uma API REST para operações de CRUD de Alunos. O desenvolvimento seguiu rigorosamente a estratégia TDD (Test-Driven Development), garantindo que todas as regras de negócio fossem validadas por testes automatizados antes da implementação.

🛠️ Tecnologias
Python 3

Flask (Framework Web)

Flask-SQLAlchemy (ORM)

SQLite (Banco de Dados Relacional)

Unittest (Framework de Testes)

⚖️ Regras de Negócio (Implementadas)
Para garantir a integridade dos dados e as políticas institucionais, foram aplicadas as seguintes regras:

Maioridade: Os alunos devem ter pelo menos 18 anos de idade.

Restrição de Capital: O cadastro é restrito a alunos nascidos em capitais de estado.

Telefone Nacional: Apenas números de telefone brasileiros são aceitos (formato nacional padrão).

Identificadores Únicos: É permitido apenas um aluno por CPF, E-mail ou número de Telefone.

🚀 Processo de Desenvolvimento (TDD)
O histórico do projeto está dividido em duas etapas principais para demonstrar o ciclo de vida do TDD:

🔴 Passo 1: Fase Vermelha / Red Phase (Commit 1)
Nesta etapa inicial, os testes unitários foram criados em test_student.py, definindo o comportamento esperado para cada regra de negócio. Neste ponto, a lógica da aplicação ainda não existia, portanto, a execução dos testes resultava em falhas.

Objetivo: Definir requisitos técnicos e falhas esperadas.

🟢 Passo 2: Fase Verde / Green Phase (Commit 2)
O arquivo service.py foi desenvolvido para satisfazer todos os casos de teste. Foram implementadas as lógicas de cálculo de idade, validação de naturalidade contra uma lista de capitais e persistência no banco de dados via SQLAlchemy.

Objetivo: Implementar o código mínimo necessário para fazer os testes passarem.

Como Executar
Instalar dependências:


pip install -r requirements.txt
Executar os testes:


python -m unittest test_student.py
Iniciar a API:

python app.py

📂 Estrutura do Projeto
app.py: Ponto de entrada, rotas da API e configuração do Flask/SQLAlchemy.

models.py: Esquema do banco de dados e definição da entidade Aluno (Student).

service.py: Regras de negócio, validações e camada de serviço.

test_student.py: Testes unitários utilizados durante o processo de TDD.
