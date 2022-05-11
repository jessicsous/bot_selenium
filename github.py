from cmath import e
from selenium import webdriver 
from time import sleep 


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options,
        )

    def clica_sign_in(self):
        try:
            boton_sign_in = self.chrome.find_element_by_link_text('Sign in')
            boton_sign_in.click()
        except Exception as e:
            print('Erro', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()    
    
    def faz_login(self):
        try:
            login = self.chrome.find_element_by_id('login_field')
            senha = self.chrome.find_element_by_id('password')
            boton_login = self.chrome.find_element_by_name('commit')
            
            login.send_keys('seu usuario')
            senha.send_keys('sua senha')
            sleep(2)
            boton_login.click()
        except Exception as e:
            print('Erro', e)    
    
    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > span.dropdown-caret')
            perfil.click()
        except Exception as e:
            print('Erro', e)   
    
    def clica_sair(self):
        try:
            sair_perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            sair_perfil.click()
        except Exception as e:
            print('Erro', e)    
           

if __name__=='__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    chrome.clica_sair()


    sleep(2)
    chrome.sair()
