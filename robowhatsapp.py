import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
import urllib
import pandas as pd

contatos_df = pd.read_excel('contatosMay.xlsx')
print(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements(By.CLASS_NAME,'_ai05')) < 1:
    time.sleep(1) 
    print(navegador.find_elements(By.CLASS_NAME,'_ai05'))
                                   

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i,"Nome"]
    numero = contatos_df.loc[i,"Telefone"]
    mensagem_formatada = urllib.parse.quote(f"Boa tarde{pessoa}! {mensagem}")
    print(mensagem_formatada)

    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_formatada}"
    navegador.get(link)

    loop = 0
    while loop < 20 and len(navegador.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')) < 1:
        time.sleep(1)
        loop +=1 

    elemento = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    elemento.send_keys(Keys.ENTER)
    time.sleep(15)

    
