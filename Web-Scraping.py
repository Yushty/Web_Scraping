import requests
import string
from bs4 import BeautifulSoup

def analyseContenu(url):
    url_open = requests.get(url)
    
    soup = BeautifulSoup(url_open.content,'html.parser')
    return soup('table',{'class' : 'infobox'})

def extractionTitre(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content,'html.parser')
    
    return " Le titre de l'article est : "+ soup('title')[0].text

def extraireParagraphe(url):
    dic = {}
    heads = ['h1','h2','h3','h4','h5','h6']
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content,'html.parser')

    heading = soup.find_all(heads)
    
    for i in heading:
        pa = i.find_next_sibling('p')
        if pa is not None:
            print(i.get_text()," : ",pa.get_text())
            print("*"*50)
            dic[i.get_text()] = pa.get_text()
    return dic     

def collecterLien(url):
    dic ={}
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content,'html.parser')
    links = soup.find_all('a') 
    for link in links:
        if link.get('href') != None: 
            if '/wiki/' in link.get('href'):
                if "https://" in link.get('href'):
                    print( link.get_text() ,end=" : ")
                    print(link.get('href'))
                    dic[link.get_text()] = link.get('href')
                else:
                    print( link.get_text() ,end=" : ")
                    print("https://en.wikipedia.org/"+link.get('href'))
                    l = "https://en.wikipedia.org/"+link.get('href')
                    dic[link.get_text()] = l
                    
                print("-"*50)       
    return dic

def getUrl():
    Enter_input = input("Search: ")
    u_i = string.capwords(Enter_input)
    lists = u_i.split()
    word = "_".join(lists)
    return "https://en.wikipedia.org/wiki/" + word

url = getUrl()

def menu(url):
    choix=1
    while(choix!=8):
        print("-*"*15,"-Menu-","*-"*15)
        print("1-/ Analyser le contenu html d'une page Wikipedia")
        print("2-/ Extraire le titre de l'article")
        print("3-/ Extraire le texte des paragraphe ")
        print("4-/ Collecter l'ensemble des liens")
        print("5-/ Quitter")
        
        print("Faites votre choix : ",end=" ")
        choix = int(input(""))
        
        
        if(choix==1):
            res = analyseContenu(url)
            print(res)
        elif(choix==2):
            res = extractionTitre(url)
            print(res)
        elif(choix==3):
            res = extraireParagraphe(url)
            #print(res)
        elif(choix==4):            
            res = collecterLien(url)
            #print(res)
        elif(choix==5):
            print("Au revoir")
            break
        else:
            print("Votre choix n'est pas reconnu'")
menu(url)