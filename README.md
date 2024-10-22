Sistema de Gerenciamento de Pedidos e Relatórios
Descrição
Sistema integrado para gerenciamento de pedidos e geração de relatórios de vendas mensais. O sistema permite a criação e controle de talões de pedidos, bem como a geração automatizada de relatórios analíticos ao final de cada período.
Funcionalidades Principais

Gestão de Pedidos

Criação de talões de pedidos
Histórico completo de transações

Relatórios

Geração automática de relatórios mensais
Análise de vendas por período
Estatísticas de desempenho

Requisitos do Sistema

Sistema Operacional: Windows/Linux/Mac
Banco de Dados: Excel

Instalação

Clone o repositório

Uso

# Criação de Pedidos
Acessar o Arquivo TALAO\Exemplo Talao.xlsx

No Campo "Codigo", Colocar o codigo que esta no arquivo TALAO\Banco de Dados.xlsx na aba "Dados Clientes"--id
Campo "Data" colocar a data que o pedido foi criado.

Na coluna A apartir da linha 9, colocar o codigo dos produtos que esta no arquivo ALAO\Banco de Dados.xlsx na aba "Dados Produtos"--id
Na coluna B apartir da linha 9, colocar a quantidade de venda do produto.

# Gerar relatorios

executar Pastas_Mensais.py para criar as pastas mesnsais.
executar Gerar_Relatorio.py para gerar os relatorios.

Contribuição

Fork o projeto
Crie sua branch de feature
Commit suas alterações
Push para a branch
Abra um Pull Request


Lançamento inicial
Sistema base de pedidos
Relatórios mensais básicos

Versão 1.1.0

Adicionado criação de pastas mensais.
Criado as pastas para separação dos relatorios (Contador, Produtos, Soma Final do Mes)
