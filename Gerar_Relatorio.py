import os
import pandas as pd
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #Deixando o vocabulario do codigo em pt-br

#region Organizado datas
agora = datetime.now()
ano = agora.strftime('%Y')
mes = agora.strftime('%B')


#endregion

#region parametros da tarefa
DiretorioRaiz = rf'C:\Estudo Python\Planilhas Mae'
Diretorio = rf"{DiretorioRaiz}\TALAO\PEDIDOS\{ano}\{mes}"
dfRelatorio = pd.DataFrame()
#endregion

#region criando o relatorio
for Pedido in os.listdir(Diretorio):
  #region Pegando o Informações do cabeçalho do talao
  print(rf"{Diretorio}\{Pedido}")
  dfIformações = pd.read_excel(rf"{Diretorio}\{Pedido}")
  dfIformações = dfIformações.head(3)
  CodigoCliente = dfIformações['Unnamed: 1'][1]
  #print(f'{Pedido} : {dfIformações["Unnamed: 3"][0]}')
  dataPedido = datetime.strftime(dfIformações['Unnamed: 3'][0],'%d/%m') 
  NomeFantasia = dfIformações['Unnamed: 3'][1] #Pegando o nome fantasia no talao
  #endregion
  #region Pegando os itens do talao
  dfPedido = pd.read_excel(rf"{Diretorio}\{Pedido}", skiprows=7)
  dfPedido = dfPedido.dropna() #Removendo os espaços em branco do talao
  dfPedido['Cliente'] = NomeFantasia
  dfPedido['Data'] = dataPedido
  dfPedido['Codigo'] = CodigoCliente
  dfRelatorio = pd.concat([dfRelatorio,dfPedido],axis=0,ignore_index=True) #Juntando as informações de todos os taloes
  #endregion
  dfRelatorioFinal = dfRelatorio.groupby(['Codigo','Cliente','Produto','Preço']).agg({'QTD':'sum','Total':'sum','Data':'max'}).reset_index() #--> agrupando as informações do relatorio
#endregion
  #region Soma total do final do mes
  dfSomaMensal = dfRelatorio.groupby(['Codigo','Cliente']).agg({'Total':'sum'}).reset_index()
  dfSomaMensal.to_excel(f"{DiretorioRaiz}\Relatorios Mensais\Soma Final do mes\{mes}\Soma total {mes}.xlsx",index=False)#Escrevendo o data frame da soma mensal em planilha
  #endregion

  #region Soma de produtos
  dfProdutosMax =  dfRelatorio.groupby(['Produto']).agg({'QTD':'sum'}).reset_index() #--> agrupando as informações do relatorio
  dfProdutosMax.to_excel(f"{DiretorioRaiz}\Relatorios Mensais\Produtos\{mes}\Produtos {mes}.xlsx",index=False)#Escrevendo o data frame da soma mensal em planilha
  #endregion


#region Colocando um espaço para dividir os grupos e colocando a data max em cada grupo

  #region Parametros para o for
NomeCliente = dfRelatorioFinal['Cliente'][0]
#DataMaior = dfRelatorioFinal['Data'][0]
DataMaior = datetime.strptime(f"{dfRelatorioFinal['Data'][0]}/{datetime.now().year}", "%d/%m/%Y")# --> transformando em tipo data para poder usar no if
dfLinhaEmBranco = pd.DataFrame(columns = dfRelatorioFinal.columns.values)
dataPedido = 0
  #endregion


for index, row in dfRelatorioFinal.iterrows():
  #Verificando se são clientes diferentes
  if row['Cliente'] != NomeCliente:
    dfLinhaEmBranco.loc[len(dfLinhaEmBranco.index)] = ['']*len(dfRelatorioFinal.columns.values)
    dfLinhaEmBranco.loc[len(dfLinhaEmBranco.index)] = row
    NomeCliente = row['Cliente'] 
    DataMaior = row['Data']
    DataMaior = datetime.strptime(f"{row['Data']}/{datetime.now().year}", "%d/%m/%Y") # --> transformando em tipo data para poder usar no if

  else:
    dfLinhaEmBranco.loc[len(dfLinhaEmBranco.index)] = row
    DataAtualDF = datetime.strptime(f"{row['Data']}/{datetime.now().year}", "%d/%m/%Y")# --> transformando em tipo data para poder usar no if
    
    if DataMaior < DataAtualDF:
      DataMaior = DataAtualDF
    
    dfLinhaEmBranco['Data'][dfLinhaEmBranco.last_valid_index()] = f"{'{:02d}'.format(DataMaior.day)}/{'{:02d}'.format(DataMaior.month)}" #Pega o ultimo index do df e preenche a linha o a maior data do grupo


dfLinhaEmBranco.to_excel(f"{DiretorioRaiz}\Relatorios Mensais\Contador\{mes}\Relatorio de {mes}_{ano}.xlsx",index=False)#Escrevendo o data frame em planilha
#endregion      
