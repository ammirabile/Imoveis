#import libraries

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#Url to be Scraped

url = 'https://direcional.com.br/sao-paulo/encontre-seu-imovel/'

# Connect to Url
response = requests.get(url)

#print(response) if 200 it worked

soup = BeautifulSoup(response.text,"html.parser")

#create key for each record
key = 1
#create variables as list
cidade=[]
nome=[]
renda=[]
status_code=[]
status=[]
link=[]
#loop through each TAG DIV has 'slide-empreendimento-interna' as a CSS class
for find_tag in soup.findAll('div','slide-empreendimento-interna'):
    
    cidade.append(find_tag['data-cidade'])
    nome.append(find_tag['data-nome'])
    renda.append(find_tag['data-renda'])
    status_code.append(find_tag['data-status'])
    #data below was extracted for their website, double check if code and descriptions are matching
    if status_code[key-1]=="0":
        status.append("Breve Lancamento")
    elif status_code[key-1]=='2':
        status.append("Obras Iniciadas")
    elif status_code[key-1]=='3':
        status.append("Obras Avancadas")    
    elif status_code[key-1]=='1':
        status.append("Lancamento")
    elif status_code[key-1]=='4':
        status.append("Pronto para morar")
    else:
        status.append("N/A")

    find_link =  find_tag.find('a')
    link.append(find_link['href'])
    print("*********************************Novo Registro*********************************")
    print(cidade[key-1],nome[key-1],renda[key-1],status_code[key-1],status[key-1],link[key-1], sep='\n')    #pause for a second, avoid Spam filers
    time.sleep(1)
    key +=1