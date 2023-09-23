from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#ABRIR NAVEGADOR
navegador = Firefox()

url = "https://www.jogajuntoinstituto.org/"

#ACESSAR SITE
navegador.get(url)

def verify_title(title):
    assert "Instituto Joga Junto" in navegador.title
    return

def find_element_by_name(nome):
    return navegador.find_element(By.NAME, nome)

verify_title("Instiituto Joga Junto")
form_nome = find_element_by_name("nome").send_keys("Myllena")
form_email = find_element_by_name("email").send_keys("mylenarodrigues.rocha@gmail.com")
form_body = find_element_by_name("body").send_keys("Automação com Selenium Web Driver")
form_select = find_element_by_name("assunto")

#seleciona o assunto
select = Select(form_select)

select.select_by_visible_text("Contratar profissionais")

form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

print(form_btn)

form_btn.submit()

# resultados.click()