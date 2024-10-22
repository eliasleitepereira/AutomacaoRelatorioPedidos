# Sistema de Gerenciamento de Pedidos e Relatórios

## Descrição
Sistema integrado para gerenciamento de pedidos e geração de relatórios de vendas mensais. O sistema permite a criação e controle de talões de pedidos, bem como a geração automatizada de relatórios analíticos ao final de cada período.

## Funcionalidades Principais

### Gestão de Pedidos
- Criação de talões de pedidos via Excel
- Histórico completo de transações

### Relatórios
- Geração automática de relatórios mensais
- Análise de vendas por período
- Estatísticas de desempenho
- Organização em pastas específicas (Contador, Produtos, Soma Final do Mês)

## Requisitos do Sistema
- Sistema Operacional: Windows/Linux/Mac
- Microsoft Excel
- Python (para execução dos scripts de relatório)

## Estrutura de Arquivos
```
TALAO/
├── Exemplo Talao.xlsx
├── Banco de Dados.xlsx
│   ├── Aba: Dados Clientes
│   └── Aba: Dados Produtos
├── Pastas_Mensais.py
└── Gerar_Relatorio.py
```

## Instalação
1. Clone o repositório para sua máquina local
2. Certifique-se de ter o Excel e Python instalados
3. Mantenha a estrutura de pastas conforme indicado acima

## Uso

### Criação de Pedidos
1. Abra o arquivo `TALAO\Exemplo Talao.xlsx`
2. Preencha os campos:
   - **Código**: Insira o código do cliente (disponível em `TALAO\Banco de Dados.xlsx` > aba "Dados Clientes")
   - **Data**: Insira a data de criação do pedido
   - **Produtos**: A partir da linha 9:
     - Coluna A: Código do produto (disponível em `TALAO\Banco de Dados.xlsx` > aba "Dados Produtos")
     - Coluna B: Quantidade do produto

### Geração de Relatórios
1. Execute `Pastas_Mensais.py` para criar a estrutura de pastas mensais
2. Execute `Gerar_Relatorio.py` para gerar os relatórios nas respectivas pastas:
   - Contador
   - Produtos
   - Soma Final do Mês

## Contribuição
1. Fork o projeto
2. Crie sua branch de feature
3. Commit suas alterações
4. Push para a branch
5. Abra um Pull Request

## Changelog

### Versão 1.0.0
- Lançamento inicial
- Sistema base de pedidos
- Relatórios mensais básicos

### Versão 1.1.0
- Adicionada criação automática de pastas mensais
- Implementada organização de relatórios em categorias:
  - Contador
  - Produtos
  - Soma Final do Mês
