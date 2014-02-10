#!/usr/bin/python
# -*- encoding: utf-8 -*-

from Pessoa import Pessoa

import urllib2, urllib, json

from urllib2 import URLError, HTTPError

p = Pessoa()

url = 'http://api.brlight.net/api/base_ses/reg'

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

def SendData():
    FormInput()
    dados = json.dumps(p, default=lambda o: o.__dict__)  #Convertendo dicionario objeto para jsons
    dadosEnviar = {'json_reg': str(dados)}
    data = urllib.urlencode(dadosEnviar)
    try:
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
    except urllib2.HTTPError as e:
        print "Ocorreu um erro na requisição http.\n Status: %s" % str(e.code)
        print e.read()
        Inicio()
    Inicio()

def GetAllData():
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    a = {}
    a = json.loads(the_page) #convertendo de json para dicionario python
    print "%-20s-+-%-7s" % ("-" * 20, "-" * 7) #imprime linha pra formatacao
    print "%-20s | %-7s" % ("Nome","Idade")
    print "%-20s-+-%-7s" % ("-" * 20, "-" * 7) #imprime linha pra formatacao
    b = a['results']
    c = b #[0]#['json_reg']
    for i in c:
        #for item in i['json_reg'].items():
        print "%-20s | %-7s" % (i['json_reg']['nm_nome'], i['json_reg']['idade'])
    #for nm_nome, idade in c.items():
    #    print "%-20s | %-7s" % (nm_nome, idade)
    print "%-20s-+-%-7s" % ("-" * 20, "-" * 7) #imprime linha pra formatacao
    Inicio()
    
def ChooseApp(num):
    if num == 1:
        GetAllData()
    elif num == 2:
        SendData()
    else:
        print 'Escolha uma opção!!!'
        Inicio()

def Inicio():
    escolha = input("[1]- Buscar Dados.\n[2]- Enviar Dados.\nEscolha uma opção: ")
    ChooseApp(escolha)

if __name__ == "__main__":
    try:
        Inicio()
    except KeyboardInterrupt:
		print "\nA execução foi interrompitada ^C"
