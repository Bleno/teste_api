#!/usr/bin/python
# -*- encoding: utf-8 -*-

from Pessoa import Pessoa

import urllib2, urllib, json

from urllib2 import URLError, HTTPError
from ConfigUrl import urlpath

p = Pessoa()

url = urlpath()

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = { 'User-Agent' : user_agent }

#data = urllib.urlencode(values)


def FormInput():
    try:
        p.nm_nome = str(raw_input("digite o nome da pessoa: "))

        p.idade = int(input("digite a idade da pessoa: "))
    except:
        print "Erro ao capturar dados"
        Inicio()

def SendData(method = 'POST'):
    FormInput()
    dados = json.dumps(p, default=lambda o: o.__dict__)  #Convertendo dicionario objeto para jsons
    dadosEnviar = {'json_reg': str(dados)}
    data = urllib.urlencode(dadosEnviar)
    try:
        if method == "PUT":
            global url
            url +="/%s" % str(p.id_reg)
        req = urllib2.Request(url, data, headers)
        req.get_method = lambda: method
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page
    except urllib2.HTTPError as e:
        print "Ocorreu um erro na requisição http.\n Status: %s" % str(e.code)
        print e.read()
        Inicio()
    Inicio()

def GetAllData(root = True):
    lista_codigos = []
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    a = {}
    a = json.loads(the_page) #convertendo de json para dicionario python
    print "%-7s-+-%-20s-+-%-7s" % ("-" * 7, "-" * 20, "-" * 7) #imprime linha pra formatacao
    print "%-7s | %-20s | %-7s" % (u"Código", "Nome", "Idade")
    print "%-7s-+-%-20s-+-%-7s" % ("-" * 7, "-" * 20, "-" * 7) #imprime linha pra formatacao
    b = a['results']
    c = b #[0]#['json_reg']
    for i in c:
        #for item in i['json_reg'].items():
        print "%-7d | %-20s | %-7s" % (i['json_reg']['id_reg'],i['json_reg']['nm_nome'], i['json_reg']['idade'])
        if root != True:
            lista_codigos.append(i['json_reg']['id_reg'])
    #for nm_nome, idade in c.items():
    #    print "%-20s | %-7s" % (nm_nome, idade)
    print "%-7s-+-%-20s-+-%-7s" % ("-" * 7, "-" * 20, "-" * 7) #imprime linha pra formatacao
    if root:
        Inicio()
    else:
        return lista_codigos

def AlteraDados():
    lista = GetAllData(False)

    #try:
    codigo = int(raw_input("digite o código do dado a ser alterado: "))

    contem_valor = False

    for i in lista:
        
        if i == codigo:
            contem_valor = True

    if contem_valor == True:
        p.id_reg = codigo
        SendData("PUT")
    else:
        print "O código não existe no banco"
        Inicio()

   # except:
     #  print "Erro ao capturar dados"
       
def ExcluirRegistro():
    try:
        list_id =  GetAllData(False)
        codigo = int(raw_input("digite o código do registro a ser excluído: "))
        global url
        url +="/%s" % str(codigo)
        req = urllib2.Request(url)
        req.get_method = lambda: "DELETE"
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page
        Inicio()
    except urllib2.HTTPError as e:
        print "Ocorreu um erro na requisição http.\n Status: %s" % str(e.code)
        print e.read()
    
    
    
def ChooseApp(num):
    if num == 1:
        GetAllData()
    elif num == 2:
        SendData()
    elif num == 3:
        AlteraDados()
    elif num == 4:
        ExcluirRegistro()
    else:
        print 'Escolha uma opção!!!'
        Inicio()

def Inicio():
    escolha = input("[1]- Buscar Dados.\n[2]- Cadastrar Pessoa.\n[3]- Editar Dados.\n[4]- Excluir Registro.\nEscolha uma opção: ")
    ChooseApp(escolha)

if __name__ == "__main__":
    try:
        Inicio()
    except KeyboardInterrupt:
		print "\nA execução foi interrompitada ^C"


		
