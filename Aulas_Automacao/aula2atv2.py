from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


navegador = Firefox() #define o navegador
url = "https://web.whatsapp.com" #define a URL utilizada
navegador.get(url) #abre navegador e a url

#Espera um tempo para garantir que a página seja totalmente carregada
input("Aperte ENTER após login")
sleep(5)

lista_msg = navegador.find_element(By.ID, "pane-side") # Encontra a lista de conversas do lado esquerdo
grupo = navegador.find_element(By.XPATH, "//span[contains(text(), '[3] IJJ - BUGOU? QA TÁ ON!')]") #Encontra o grupo específico usando XPATH
grupo.click() #Clica no grupo

#Econtra a conversa e o campo para digitar mensagem
campo_msg = navegador.find_element(By.ID,"main") 
mensagem = navegador.find_element(By.XPATH,"//div[@contenteditable='true' and @title='Digite uma mensagem']")
mensagem.click()

texto_msg = "Automação do WhatsApp - SQUAD 1"

# Digita a mensagem letra por letra | Fiz dessa forma, porque o Firefox estava considerando só a primeira letra
for letra in texto_msg:
    mensagem.send_keys(letra)
    sleep(0.2)  # Adiciona um pequeno atraso entre as letras

# Envia a mensagem pressionando Enter
mensagem.send_keys(Keys.ENTER)

sleep(10)
