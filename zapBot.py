from selenium import webdriver 
import time 

class WhatsappBot: 
    def __init__(self):
        self.mensagem = "testando"
        self.grupos = ["Design"] 
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options) 

    def EnviarMensagens(self):
        # <span dir="auto" title="Design" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Design</span> 
        # <div tabindex="-1" class="p3_M1"> 
        # <span data-testid="send" data-icon="send" class=""> 
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon= 'send']")
            time.sleep(3)
            botao_enviar.click() 
            time.sleep(5) 


bot = WhatsappBot()
bot.EnviarMensagens()

        

                


    