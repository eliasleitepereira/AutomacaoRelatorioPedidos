import os
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #Deixando o vocabulario do codigo em pt-br

#region Organizado datas
agora = datetime.now()
ano = agora.strftime('%Y')
mes = agora.strftime('%B')

DiretorioRaiz = rf'C:\Estudo Python\Planilhas Mae'

#region Criando pastas para Contador
if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Contador\{ano}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Contador\{ano}")


if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Contador\{ano}\{mes}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Contador\{ano}\{mes}")

#ednregion

#region Criando pastas para Produtos
if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Produtos\{ano}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Produtos\{ano}")
    print("Nao tem essa pasta ano")


if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Produtos\{ano}\{mes}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Produtos\{ano}\{mes}")
    print("Nao tem essa pasta mes")

#ednregion

#region Criando pastas para Soma Final do mes
if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Soma Final do mes\{ano}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Soma Final do mes\{ano}")
    print("Nao tem essa pasta ano")


if not os.path.isdir(rf"{DiretorioRaiz}\Relatorios Mensais\Soma Final do mes\{ano}\{mes}"):
    os.mkdir(rf"{DiretorioRaiz}\Relatorios Mensais\Soma Final do mes\{ano}\{mes}")
    print("Nao tem essa pasta mes")

#ednregion

#region Criando pastas para Pedidos
if not os.path.isdir(rf"{DiretorioRaiz}\TALAO\PEDIDOS\{ano}"):
    os.mkdir(rf"{DiretorioRaiz}\TALAO\PEDIDOS\{ano}")
    print("Nao tem essa pasta ano")


if not os.path.isdir(rf"{DiretorioRaiz}\TALAO\PEDIDOS\{ano}\{mes}"):
    os.mkdir(rf"{DiretorioRaiz}\TALAO\PEDIDOS\{ano}\{mes}")
    print("Nao tem essa pasta mes")

#ednregion