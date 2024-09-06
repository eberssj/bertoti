from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Rodar em modo headless
    navegador = webdriver.Chrome(options=options)
    return navegador

def buscar_informacoes(termo_busca):
    navegador = iniciar_navegador()
    url = "https://stardewvalleywiki.com/"
    navegador.get(url)
    
    try:
        # Encontrar a barra de pesquisa na wiki e inserir o termo de busca
        search_box = navegador.find_element(By.NAME, "search")
        search_box.send_keys(termo_busca)
        search_box.send_keys(Keys.RETURN)
        
        # Pegar o conteúdo da primeira seção relevante
        conteudo_principal = navegador.find_element(By.ID, "bodyContent")
        informacoes = conteudo_principal.text
    except NoSuchElementException:
        informacoes = "Não consegui encontrar informações sobre esse termo."
    
    navegador.quit()
    return informacoes

def buscar(update: Update, context: CallbackContext) -> None:
    termo_busca = ' '.join(context.args)
    if termo_busca:
        informacoes = buscar_informacoes(termo_busca)
        update.message.reply_text(informacoes)
    else:
        update.message.reply_text('Por favor, forneça um termo para buscar na wiki.')

def main() -> None:
    updater = Updater("6698271536:AAEWL7Z7wcRg7qFuVoakmb0AKtqngkQkyjY")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("buscar", buscar))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
