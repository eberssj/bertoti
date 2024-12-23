import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from flask import Flask, request
from telegram.ext import filters
from telegram.ext import Application


# Função para obter informações sobre as minas
def get_minas_info():
    url = "https://pt.stardewvalleywiki.com/As_Minas"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p")
            relevant_paragraphs = paragraphs[1:5]
            info = "\n\n".join([p.get_text().strip() for p in relevant_paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre as minas."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /minas
async def minas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre as minas...")
    minas_info = get_minas_info()
    info_com_link = f"{minas_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/As_Minas"
    await update.message.reply_text(info_com_link)

# Função para tratar mensagens genéricas
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text.lower()
    
    # Lista de palavras-chave que acionam a função minas
    palavras_chave_minas = ["minas", "informações minas", "quero minas"]
    # Lista de palavras-chave que acionam a função estacoes
    palavras_chave_estacoes = ["estações", "informações estações", "quero estações", "infromacoes estacoes", "estacoes"]
    # Definindo palavras-chave para cada estação
    palavras_chave_verao = [
        "verão", "verao", "informações verão", "informações verao", "verao", "informaçoes verao", "Verão", "Verao"
    ]

    palavras_chave_primavera = [
        "primavera", "informações primavera", "primaveras", "Primavera", "informaçoes primavera"
    ]

    palavras_chave_outono = [
        "outono", "informações outono", "informaçoes outono", "Outono"
    ]

    palavras_chave_inverno = [
        "inverno", "informações inverno", "Inverno", "informaçoes inverno"
    ]

    # Lista de palavras-chave que acionam a função festivais
    palavras_chave_festivais = ["festivais", "informações festivais", "quero festivais", "infromacoes festivais", "festival"]
    # Lista de palavras-chave que acionam a função aldeoes (nomes dos aldeões)
    # Lista de palavras-chave para os aldeões
    palavras_chave_aldeoes = [
        "npcs", "npc", "casavéis", "casar", "personagem", "personagens", 
        "namorar", "namoravéis", "namoraveis", "informações aldeões", 
        "informações aldeoes"
    ]

    # Palavras-chave para o Alex
    palavras_chave_alex = [
        "alex", "Alex", "informações alex", "informações Alex", 
        "infromações alex", "infromações Alex", "informações sobre Alex"
    ]

    # Palavras-chave para o Elliott
    palavras_chave_elliott = [
        "elliott", "Elliott", "informações elliott", "informações Elliott", 
        "infromações elliott", "infromações Elliott", "informações sobre Elliott"
    ]

    # Palavras-chave para o Harvey
    palavras_chave_harvey = [
        "harvey", "Harvey", "informações harvey", "informações Harvey", 
        "infromações harvey", "infromações Harvey", "informações sobre Harvey"
    ]

    # Palavras-chave para o Sam
    palavras_chave_sam = [
        "sam", "Sam", "informações sam", "informações Sam", 
        "infromações sam", "infromações Sam", "informações sobre Sam"
    ]

    # Palavras-chave para o Sebastian
    palavras_chave_sebastian = [
        "sebastian", "Sebastian", "informações sebastian", "informações Sebastian", 
        "infromações sebastian", "infromações Sebastian", "informações sobre Sebastian"
    ]

    # Palavras-chave para o Shane
    palavras_chave_shane = [
        "shane", "Shane", "informações shane", "informações Shane", 
        "infromações shane", "infromações Shane", "informações sobre Shane"
    ]

    # Palavras-chave para a Abigail
    palavras_chave_abigail = [
        "abigail", "Abigail", "informações abigail", "informações Abigail", 
        "infromações abigail", "infromações Abigail", "informações sobre Abigail"
    ]

    # Palavras-chave para a Emily
    palavras_chave_emily = [
        "emily", "Emily", "informações emily", "informações Emily", 
        "infromações emily", "infromações Emily", "informações sobre Emily"
    ]

    # Palavras-chave para a Haley
    palavras_chave_haley = [
        "haley", "Haley", "informações haley", "informações Haley", 
        "infromações haley", "infromações Haley", "informações sobre Haley"
    ]

    # Palavras-chave para a Leah
    palavras_chave_leah = [
        "leah", "Leah", "informações leah", "informações Leah", 
        "infromações leah", "infromações Leah", "informações sobre Leah"
    ]

    # Palavras-chave para a Maru
    palavras_chave_maru = [
        "maru", "Maru", "informações maru", "informações Maru", 
        "infromações maru", "infromações Maru", "informações sobre Maru"
    ]

    # Palavras-chave para a Penny
    palavras_chave_penny = [
        "penny", "Penny", "informações penny", "informações Penny", 
        "infromações penny", "infromações Penny", "informações sobre Penny"
    ]
    # Lista de palavras-chave para o comando /armazem_do_pierre
    palavras_chave_armazem_pierre = ["armazém do pierre", "armazem do pierre", "Pierre", "pierre", "loja do pierre", "informações pierre", "informaçoes pierre"]
    # Lista de palavras-chave para o comando /clinica_do_harvey
    palavras_chave_clinica_harvey = ["clínica do harvey",  "clínica harvey", "clinica harvey", "clinica do harvey", "hospital"]
    # Lista de palavras-chave que acionam o comando /start
    palavras_chave_saudacao = ["oi", "olá", "oii", "olá!","saudações", "bom dia", "boa tarde", "boa noite"]
    
   # Verifica se alguma palavra-chave está contida na mensagem
    if any(palavra in message_text for palavra in palavras_chave_minas):
        await minas(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_estacoes):
        await estacoes(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_verao):
        await verao(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_primavera):
        await primavera(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_outono):
        await outono(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_inverno):
        await inverno(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_festivais):
        await festivais(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_aldeoes):
        await aldeoes(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_alex):
        await alex(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_elliott):
        await elliott(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_harvey):
        await harvey(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_sam):
        await sam(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_sebastian):
        await sebastian(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_shane):
        await shane(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_abigail):
        await abigail(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_emily):
        await emily(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_haley):
        await haley(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_leah):
        await leah(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_maru):
        await maru(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_penny):
        await penny(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_armazem_pierre):
        await armazem_do_pierre(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_clinica_harvey):
        await clinica_do_harvey(update, context)
    elif any(palavra in message_text for palavra in palavras_chave_saudacao):
        # Chama a função start quando uma saudação é detectada
        await start(update, context)
    else:
        # Resposta padrão caso a mensagem não contenha as palavras-chave
        await update.message.reply_text("Desculpe, não entendi sua mensagem. Tente novamente.")

# Função para extrair informações sobre as Estações
def get_estacoes_info():
    url = "https://pt.stardewvalleywiki.com/Esta%C3%A7%C3%B5es"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p", limit=4)  # Pegando os primeiros 4 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre as estações."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /estacoes
async def estacoes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre as estações...")
    estacoes_info = get_estacoes_info()
    await update.message.reply_text(estacoes_info + "\n\nPara mais informações, acesse: https://pt.stardewvalleywiki.com/Esta%C3%A7%C3%B5es")

    await update.message.reply_text(
        "Qual estação você gostaria de saber com mais detalhes?\n"
        "Digite as opções:\n"
        "/verao\n"
        "/inverno\n"
        "/primavera\n"
        "/outono"
    )

# Função para extrair informações sobre o Verão
def get_verao_info():
    url = "https://pt.stardewvalleywiki.com/Ver%C3%A3o"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando os primeiros parágrafos ou conteúdo relevante
            paragraphs = content.find_all("p", limit=5)  # Pegando os primeiros 5 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre o Verão."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /verao
async def verao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Verão...")
    verao_info = get_verao_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{verao_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Ver%C3%A3o"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Primavera
def get_primavera_info():
    url = "https://pt.stardewvalleywiki.com/Primavera"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando os primeiros parágrafos ou conteúdo relevante
            paragraphs = content.find_all("p", limit=5)  # Pegando os primeiros 5 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre a Primavera."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /primavera
async def primavera(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Primavera...")
    primavera_info = get_primavera_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{primavera_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Primavera"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Outono
def get_outono_info():
    url = "https://pt.stardewvalleywiki.com/Outono"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p", limit=5)  # Pegando os primeiros 5 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre o Outono."
    else:
        return f"Erro ao acessar o site: {response.status_code}"


# Função para o comando /outono
async def outono(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Outono...")
    outono_info = get_outono_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{outono_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Outono"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Inverno
def get_inverno_info():
    url = "https://pt.stardewvalleywiki.com/Inverno"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p", limit=5)  # Pegando os primeiros 5 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre o Inverno."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /inverno
async def inverno(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Inverno...")
    inverno_info = get_inverno_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{inverno_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Inverno"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre os Festivais
def get_festivais_info():
    url = "https://pt.stardewvalleywiki.com/Festivais"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p", limit=6)  # Pegando os primeiros 6 parágrafos
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre os festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /festivais
async def festivais(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre os festivais...")
    festivais_info = get_festivais_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{festivais_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais"

    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

    await update.message.reply_text(
        "Qual dos Festivais você gostaria de saber com mais detalhes?\n"
        "Digite as opções:\n"
        "/festival_do_ovo\n"
        "/danca_das_flores\n"
        "/luau\n"
        "/danca_das_medusas\n"
        "/feira_do_vale\n"
        "/vespera_dos_espiritos\n"
        "/festival_do_gelo\n"
        "/mercado_noturno\n"
        "/festival_da_estrela"
    )

# Função para extrair informações sobre o Festival do Ovo
def get_festival_ovo_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Festival_do_Ovo"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival do Ovo
            festival_ovo_section = content.find("span", {"id": "Festival_do_Ovo"})
            if festival_ovo_section:
                # Pegando o conteúdo a partir dessa seção
                festival_ovo_info = festival_ovo_section.find_next("p")
                info = festival_ovo_info.get_text().strip() if festival_ovo_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival do Ovo."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /festival_do_ovo
async def festival_do_ovo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival do Ovo...")
    festival_ovo_info = get_festival_ovo_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{festival_ovo_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Festival_do_Ovo"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival da Dança das Flores
def get_danca_das_flores_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Dan.C3.A7a_das_Flores"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante da Dança das Flores
            danca_das_flores_section = content.find("span", {"id": "Dan%C3%A7a_das_Flores"})
            if danca_das_flores_section:
                # Pegando o conteúdo a partir dessa seção
                danca_das_flores_info = danca_das_flores_section.find_next("p")
                info = danca_das_flores_info.get_text().strip() if danca_das_flores_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival da Dança das Flores."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /danca_das_flores
async def danca_das_flores(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival da Dança das Flores...")
    danca_das_flores_info = get_danca_das_flores_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{danca_das_flores_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Dan.C3.A7a_das_Flores"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival do Luau
def get_luau_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Luau"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival do Luau
            luau_section = content.find("span", {"id": "Luau"})
            if luau_section:
                # Pegando o conteúdo a partir dessa seção
                luau_info = luau_section.find_next("p")
                info = luau_info.get_text().strip() if luau_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival do Luau."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /luau
async def luau(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival do Luau...")
    luau_info = get_luau_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{luau_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Luau"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival da Dança das Medusas-da-Lua
def get_danca_das_medusas_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Dan%C3%A7a_das_Medusas-da-Lua"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival da Dança das Medusas-da-Lua
            medusas_section = content.find("span", {"id": "Dan%C3%A7a_das_Medusas-da-Lua"})
            if medusas_section:
                # Pegando o conteúdo a partir dessa seção
                medusas_info = medusas_section.find_next("p")
                info = medusas_info.get_text().strip() if medusas_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival da Dança das Medusas-da-Lua."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"


# Função para o comando /danca_das_medusas
async def danca_das_medusas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival da Dança das Medusas-da-Lua...")
    danca_das_medusas_info = get_danca_das_medusas_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{danca_das_medusas_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Dan%C3%A7a_das_Medusas-da-Lua"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival Feira do Vale do Orvalho
def get_feira_do_vale_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Feira_do_Vale_do_Orvalho"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival Feira do Vale do Orvalho
            vale_section = content.find("span", {"id": "Feira_do_Vale_do_Orvalho"})
            if vale_section:
                # Pegando o conteúdo a partir dessa seção
                vale_info = vale_section.find_next("p")
                info = vale_info.get_text().strip() if vale_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre a Feira do Vale do Orvalho."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /feira_do_vale
async def feira_do_vale(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Feira do Vale do Orvalho...")
    feira_do_vale_info = get_feira_do_vale_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{feira_do_vale_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Feira_do_Vale_do_Orvalho"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival Véspera dos Espíritos
def get_vespera_dos_espiritos_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#V.C3.A9spera_dos_Esp.C3.ADritos"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival Véspera dos Espíritos
            espiritos_section = content.find("span", {"id": "V.C3.A9spera_dos_Esp.C3.ADritos"})
            if espiritos_section:
                # Pegando o conteúdo a partir dessa seção
                espiritos_info = espiritos_section.find_next("p")
                info = espiritos_info.get_text().strip() if espiritos_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre a Véspera dos Espíritos."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /vespera_dos_espiritos
async def vespera_dos_espiritos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Véspera dos Espíritos...")
    vespera_dos_espiritos_info = get_vespera_dos_espiritos_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{vespera_dos_espiritos_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#V.C3.A9spera_dos_Esp.C3.ADritos"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival do Gelo
def get_festival_do_gelo_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Festival_do_Gelo"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Festival do Gelo
            gelo_section = content.find("span", {"id": "Festival_do_Gelo"})
            if gelo_section:
                # Pegando o conteúdo a partir dessa seção
                gelo_info = gelo_section.find_next("p")
                info = gelo_info.get_text().strip() if gelo_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival do Gelo."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /festival_do_gelo
async def festival_do_gelo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival do Gelo...")
    festival_do_gelo_info = get_festival_do_gelo_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{festival_do_gelo_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Festival_do_Gelo"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Mercado Noturno
def get_mercado_noturno_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Mercado_Noturno"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a parte relevante do Mercado Noturno
            mercado_section = content.find("span", {"id": "Mercado_Noturno"})
            if mercado_section:
                # Pegando o conteúdo a partir dessa seção
                mercado_info = mercado_section.find_next("p")
                info = mercado_info.get_text().strip() if mercado_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Mercado Noturno."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /mercado_noturno
async def mercado_noturno(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Mercado Noturno...")
    mercado_noturno_info = get_mercado_noturno_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{mercado_noturno_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Mercado_Noturno"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Festival da Estrela Inverna
def get_festival_da_estrela_info():
    url = "https://pt.stardewvalleywiki.com/Festivais#Festival_da_Estrela_Inverna"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando a seção relevante do Festival da Estrela Inverna
            festival_section = content.find("span", {"id": "Festival_da_Estrela_Inverna"})
            if festival_section:
                # Pegando o conteúdo a partir dessa seção
                festival_info = festival_section.find_next("p")
                info = festival_info.get_text().strip() if festival_info else "Informações não encontradas."
                return info
            else:
                return "Não encontrei informações sobre o Festival da Estrela Inverna."
        else:
            return "Não consegui encontrar informações sobre festivais."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /festival_da_estrela
async def festival_da_estrela(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Festival da Estrela Inverna...")
    festival_da_estrela_info = get_festival_da_estrela_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{festival_da_estrela_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Festivais#Festival_da_Estrela_Inverna"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre os Aldeões
def get_aldeoes_info():
    url = "https://pt.stardewvalleywiki.com/Alde%C3%B5es"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            paragraphs = content.find_all("p", limit=3)  # Pegando os primeiros 3 parágrafos relevantes
            info = "\n\n".join([p.get_text().strip() for p in paragraphs])
            return info
        else:
            return "Não consegui encontrar informações sobre os aldeões."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /aldeoes
async def aldeoes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre os aldeões...")
    aldeoes_info = get_aldeoes_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{aldeoes_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Alde%C3%B5es"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

    await update.message.reply_text(
        "Qual dos Aldeões Casavéis você gostaria de saber com mais detalhes?\n"
        "Digite as opções:\n\n"

        "Homens:\n\n"

        "/alex\n"
        "/elliott\n"
        "/harvey\n"
        "/sam\n"
        "/sebastian\n"
        "/shane\n"

        "Mulheres:\n\n"

        "/abigail\n"
        "/emily\n"
        "/haley\n"
        "/leah\n"
        "/maru\n"
        "/penny"
    )

# Função para extrair informações sobre o Alex
def get_alex_info():
    url = "https://pt.stardewvalleywiki.com/Alex"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Alex
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Alex
            # Em vez de apenas pegar o primeiro parágrafo, vamos tentar encontrar descrições mais específicas
            alex_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Alex
            for para in alex_info:
                text = para.get_text().strip()
                if "Alex" in text:  # Verificando se o texto contém o nome "Alex"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Alex."
        else:
            return "Não consegui encontrar a seção correta sobre o Alex."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /alex
async def alex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Alex...")
    alex_info = get_alex_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{alex_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Alex"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Elliott
def get_elliott_info():
    url = "https://pt.stardewvalleywiki.com/Elliott"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Elliott
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Elliott
            # Vamos tentar pegar todos os parágrafos da página
            elliott_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Elliott
            for para in elliott_info:
                text = para.get_text().strip()
                if "Elliott" in text:  # Verificando se o texto contém o nome "Elliott"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Elliott."
        else:
            return "Não consegui encontrar a seção correta sobre o Elliott."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /elliott
async def elliott(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Elliott...")
    elliott_info = get_elliott_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{elliott_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Elliott"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Harvey
def get_harvey_info():
    url = "https://pt.stardewvalleywiki.com/Harvey"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Harvey
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Harvey
            # Vamos tentar pegar todos os parágrafos da página
            harvey_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Harvey
            for para in harvey_info:
                text = para.get_text().strip()
                if "Harvey" in text:  # Verificando se o texto contém o nome "Harvey"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Harvey."
        else:
            return "Não consegui encontrar a seção correta sobre o Harvey."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /harvey
async def harvey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Harvey...")
    harvey_info = get_harvey_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{harvey_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Harvey"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Sam
def get_sam_info():
    url = "https://pt.stardewvalleywiki.com/Sam"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Sam
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Sam
            # Vamos tentar pegar todos os parágrafos da página
            sam_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Sam
            for para in sam_info:
                text = para.get_text().strip()
                if "Sam" in text:  # Verificando se o texto contém o nome "Sam"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Sam."
        else:
            return "Não consegui encontrar a seção correta sobre o Sam."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /sam
async def sam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Sam...")
    sam_info = get_sam_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{sam_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Sam"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre o Sebastian
def get_sebastian_info():
    url = "https://pt.stardewvalleywiki.com/Sebastian"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Sebastian
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Sebastian
            # Vamos tentar pegar todos os parágrafos da página
            sebastian_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Sebastian
            for para in sebastian_info:
                text = para.get_text().strip()
                if "Sebastian" in text:  # Verificando se o texto contém o nome "Sebastian"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Sebastian."
        else:
            return "Não consegui encontrar a seção correta sobre o Sebastian."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /sebastian
async def sebastian(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Sebastian...")
    sebastian_info = get_sebastian_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{sebastian_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Sebastian"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)


# Função para extrair informações sobre o Shane
def get_shane_info():
    url = "https://pt.stardewvalleywiki.com/Shane"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações do Shane
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre o Shane
            # Vamos tentar pegar todos os parágrafos da página
            shane_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição do Shane
            for para in shane_info:
                text = para.get_text().strip()
                if "Shane" in text:  # Verificando se o texto contém o nome "Shane"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Shane."
        else:
            return "Não consegui encontrar a seção correta sobre o Shane."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /shane
async def shane(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Shane...")
    shane_info = get_shane_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{shane_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Shane"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Abigail
def get_abigail_info():
    url = "https://pt.stardewvalleywiki.com/Abigail"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Abigail
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Abigail
            # Vamos tentar pegar todos os parágrafos da página
            abigail_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Abigail
            for para in abigail_info:
                text = para.get_text().strip()
                if "Abigail" in text:  # Verificando se o texto contém o nome "Abigail"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Abigail."
        else:
            return "Não consegui encontrar a seção correta sobre a Abigail."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /abigail
async def abigail(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Abigail...")
    abigail_info = get_abigail_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{abigail_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Abigail"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Emily
def get_emily_info():
    url = "https://pt.stardewvalleywiki.com/Emily"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Emily
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Emily
            # Vamos tentar pegar todos os parágrafos da página
            emily_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Emily
            for para in emily_info:
                text = para.get_text().strip()
                if "Emily" in text:  # Verificando se o texto contém o nome "Emily"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Emily."
        else:
            return "Não consegui encontrar a seção correta sobre a Emily."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /emily
async def emily(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Emily...")
    emily_info = get_emily_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{emily_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Emily"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Haley
def get_haley_info():
    url = "https://pt.stardewvalleywiki.com/Haley"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Haley
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Haley
            # Vamos tentar pegar todos os parágrafos da página
            haley_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Haley
            for para in haley_info:
                text = para.get_text().strip()
                if "Haley" in text:  # Verificando se o texto contém o nome "Haley"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Haley."
        else:
            return "Não consegui encontrar a seção correta sobre a Haley."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /haley
async def haley(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Haley...")
    haley_info = get_haley_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{haley_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Haley"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Leah
def get_leah_info():
    url = "https://pt.stardewvalleywiki.com/Leah"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Leah
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Leah
            # Vamos tentar pegar todos os parágrafos da página
            leah_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Leah
            for para in leah_info:
                text = para.get_text().strip()
                if "Leah" in text:  # Verificando se o texto contém o nome "Leah"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Leah."
        else:
            return "Não consegui encontrar a seção correta sobre a Leah."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /leah
async def leah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Leah...")
    leah_info = get_leah_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{leah_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Leah"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre a Maru
def get_maru_info():
    url = "https://pt.stardewvalleywiki.com/Maru"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Maru
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Maru
            # Vamos tentar pegar todos os parágrafos da página
            maru_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Maru
            for para in maru_info:
                text = para.get_text().strip()
                if "Maru" in text:  # Verificando se o texto contém o nome "Maru"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Maru."
        else:
            return "Não consegui encontrar a seção correta sobre a Maru."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /maru
async def maru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Maru...")
    maru_info = get_maru_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{maru_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Maru"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)


# Função para extrair informações sobre a Penny
def get_penny_info():
    url = "https://pt.stardewvalleywiki.com/Penny"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção com as informações sobre a Penny
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Procurando pela primeira parte de uma descrição relevante sobre a Penny
            # Vamos tentar pegar todos os parágrafos da página
            penny_info = content.find_all("p")  # Pega todos os parágrafos

            # Vamos tentar capturar a descrição da Penny
            for para in penny_info:
                text = para.get_text().strip()
                if "Penny" in text:  # Verificando se o texto contém o nome "Penny"
                    return text

            # Se não encontrar, informar ao usuário
            return "Informações não encontradas sobre Penny."
        else:
            return "Não consegui encontrar a seção correta sobre a Penny."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para o comando /penny
async def penny(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre a Penny...")
    penny_info = get_penny_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{penny_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Penny"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)


# Função para extrair informações sobre o Centro Comunitário
def get_centro_comunitario_info():
    url = "https://pt.stardewvalleywiki.com/Centro_Comunit%C3%A1rio"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção principal do conteúdo
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Pegar todos os parágrafos e seções
            centro_info = content.find_all(["p", "h2", "h3", "ul"])  # Inclui parágrafos, subtítulos e listas
            
            # Vamos filtrar e acumular as informações de interesse
            full_info = []
            for tag in centro_info:
                if tag.name == "p":
                    full_info.append(tag.get_text().strip())
                elif tag.name in ["h2", "h3"]:  # Seção de título (subtítulos ou títulos maiores)
                    full_info.append(f"\n{tag.get_text().strip()}:\n")
                elif tag.name == "ul":  # Lista de itens
                    for li in tag.find_all("li"):
                        full_info.append(f"- {li.get_text().strip()}")

            # Juntando tudo em uma resposta
            return "\n".join(full_info) if full_info else "Informações detalhadas não encontradas sobre o Centro Comunitário."
        else:
            return "Não consegui encontrar a seção correta sobre o Centro Comunitário."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para dividir a resposta em várias partes menores
def split_message(message, max_length=4096):
    """Divida a mensagem em partes menores, caso ultrapasse o limite do Telegram."""
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

# Função para o comando /centro_comunitario
async def centro_comunitario(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações sobre o Centro Comunitário...")
    centro_comunitario_info = get_centro_comunitario_info()
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{centro_comunitario_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Centro_Comunit%C3%A1rio"
    
    # Dividir a mensagem em partes menores se necessário
    parts = split_message(info_com_link)
    
    # Enviar cada parte separada
    for part in parts:
        await update.message.reply_text(part)


# Função para extrair informações sobre o Rancho da Marnie
def get_rancho_da_marnie_info_resumido():
    url = "https://pt.stardewvalleywiki.com/Rancho_da_Marnie"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção principal do conteúdo
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Pegar informações resumidas (título, personagens, horários)
            full_info = []
            
            # Localização e personagens
            local_e_personagens = content.find_all("p")
            for p in local_e_personagens:
                text = p.get_text().strip()
                if "O Rancho da Marnie" in text:
                    full_info.append(text)
                if "Marnie" in text or "Jas" in text or "Shane" in text:
                    full_info.append(text)

            # Horário de funcionamento
            for p in content.find_all("p"):
                if "das 9:00 às 16:00" in p.get_text():
                    full_info.append("Horário de funcionamento: 9:00 às 16:00, exceto segunda e terça.")
                    break

            # Resumo de itens ou notas importantes
            full_info.append("\nResumo: A loja de Marnie vende animais e itens de pecuária. A missão \"Shorts do Prefeito\" envolve uma bermuda perdida de Lewis.")
            
            return "\n".join(full_info) if full_info else "Informações detalhadas não encontradas sobre o Rancho da Marnie."
        else:
            return "Não consegui encontrar a seção correta sobre o Rancho da Marnie."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

def split_message(message, max_length=4096):
    """Divida a mensagem em partes menores, caso ultrapasse o limite do Telegram."""
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

# Função para o comando /rancho_da_marnie
async def rancho_da_marnie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações resumidas sobre o Rancho da Marnie...")
    
    rancho_info_resumido = get_rancho_da_marnie_info_resumido()  # Obtendo as informações
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{rancho_info_resumido}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Rancho_da_Marnie"
    
    # Dividir a mensagem em partes menores se necessário
    parts = split_message(info_com_link)
    
    # Enviar cada parte separada
    for part in parts:
        await update.message.reply_text(part)

# Função para extrair informações sobre o Armazem do Pierre
def get_armazem_do_pierre_info_resumido():
    url = "https://pt.stardewvalleywiki.com/Armaz%C3%A9m_do_Pierre"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção principal do conteúdo
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Pegar informações resumidas (título, personagens, horários)
            full_info = []
            
            # Localização e personagens
            local_e_personagens = content.find_all("p")
            for p in local_e_personagens:
                text = p.get_text().strip()
                if "Armazém do Pierre" in text:
                    full_info.append(text)
                if "Pierre" in text:
                    full_info.append(text)
            
            # Horário de funcionamento
            for p in content.find_all("p"):
                if "das 9:00 às 17:00" in p.get_text():
                    full_info.append("Horário de funcionamento: 9:00 às 17:00, exceto quarta-feira.")
                    break

            # Resumo de itens ou notas importantes
            full_info.append("\nResumo: O Armazém de Pierre vende sementes e outros itens para o cultivo, além de ter um objetivo central em várias missões.")
            
            return "\n".join(full_info) if full_info else "Informações detalhadas não encontradas sobre o Armazém do Pierre."
        else:
            return "Não consegui encontrar a seção correta sobre o Armazém do Pierre."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

def split_message(message, max_length=4096):
    """Divida a mensagem em partes menores, caso ultrapasse o limite do Telegram."""
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

# Função para o comando /armazem_do_pierre
async def armazem_do_pierre(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações resumidas sobre o Armazém do Pierre...")
    
    armazem_info_resumido = get_armazem_do_pierre_info_resumido()  # Obtendo as informações
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{armazem_info_resumido}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Armaz%C3%A9m_do_Pierre"
    
    # Dividir a mensagem em partes menores se necessário
    parts = split_message(info_com_link)
    
    # Enviar cada parte separada
    for part in parts:
        await update.message.reply_text(part)

# Função para extrair informações sobre o Clínica do Harvey
def get_clinica_do_harvey_info_resumido():
    url = "https://pt.stardewvalleywiki.com/Cl%C3%ADnica_do_Harvey"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar a seção principal do conteúdo
        content = soup.find("div", {"class": "mw-parser-output"})
        
        if content:
            # Pegar informações resumidas (título, personagens, horários)
            full_info = []
            
            # Localização e personagens
            local_e_personagens = content.find_all("p")
            for p in local_e_personagens:
                text = p.get_text().strip()
                if "Clínica do Harvey" in text:
                    full_info.append(text)
                if "Harvey" in text:
                    full_info.append(text)
            
            # Horário de funcionamento
            for p in content.find_all("p"):
                if "das 9:00 às 18:00" in p.get_text():
                    full_info.append("Horário de funcionamento: 9:00 às 18:00, exceto segunda-feira.")
                    break

            # Resumo de itens ou notas importantes
            full_info.append("\nResumo: A Clínica do Harvey é onde você pode tratar a sua saúde, comprar remédios e curar doenças.")
            
            return "\n".join(full_info) if full_info else "Informações detalhadas não encontradas sobre a Clínica do Harvey."
        else:
            return "Não consegui encontrar a seção correta sobre a Clínica do Harvey."
    else:
        return f"Erro ao acessar o site: {response.status_code}"

def split_message(message, max_length=4096):
    """Divida a mensagem em partes menores, caso ultrapasse o limite do Telegram."""
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

# Função para o comando /clinica_do_harvey
async def clinica_do_harvey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Buscando informações resumidas sobre a Clínica do Harvey...")
    
    clinica_info_resumido = get_clinica_do_harvey_info_resumido()  # Obtendo as informações
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{clinica_info_resumido}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/Cl%C3%ADnica_do_Harvey"
    
    # Dividir a mensagem em partes menores se necessário
    parts = split_message(info_com_link)
    
    # Enviar cada parte separada
    for part in parts:
        await update.message.reply_text(part)




# Função de start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Mensagem simplificada sobre o bot
    intro_message = (
        "Olá! Eu sou o Helper de Stardew Valley, seu assistente para navegar pelo mundo de Stardew Valley.\n"
        "Ou você pode apenas pesquisar o que quer! Exemplpo ""informações sobre as minas"".\n"
        "Comigo, você pode acessar informações sobre diversos locais, festivais, NPCs e estações do ano.\n\n"
        
        "Escolha uma das opções abaixo para começar:\n\n"
        "Lugares:\n\n"
        "/minas - Minas\n"
        "/centro_comunitario - Centro Comunitário\n"
        "/rancho_da_marnie - Rancho da Marnie\n"
        "/armazem_do_pierre - Armazen do Pierre\n"
        "/clinica_do_harvey - Clínica do Harvey\n\n"
        "Estações do Ano:\n\n"
        "/estacoes \n\n"
        "Festivais:\n\n"
        "/festivais\n\n"
        "NPCs:\n\n"
        "/aldeoes"
    )
    
    # Enviar a mensagem de introdução com as opções simplificadas
    await update.message.reply_text(intro_message)



# Configuração do bot
async def main():
    TOKEN = "7810939484:AAFiVC1-qMJEPNCHFZxUFo-bV9GH30AhA_0"
    app = ApplicationBuilder().token(TOKEN).build()

    # Adicionando o comando /minas
    app.add_handler(CommandHandler("minas", minas))
    # Adicionando o comando /centro_comunitario
    app.add_handler(CommandHandler("centro_comunitario", centro_comunitario))
    # Adicionando o comando /estacoes
    app.add_handler(CommandHandler("estacoes", estacoes))
    # Adicionando o comando /verao
    app.add_handler(CommandHandler("verao", verao))
    # Adicionando o comando /primavera
    app.add_handler(CommandHandler("primavera", primavera))
    # Adicionando o comando /outono
    app.add_handler(CommandHandler("outono", outono))
    # Adicionando o comando /inverno
    app.add_handler(CommandHandler("inverno", inverno))
    # Adicionando o comando /festivais
    app.add_handler(CommandHandler("festivais", festivais))
    # Adicionando o comando /festival_do_ovo
    app.add_handler(CommandHandler("festival_do_ovo", festival_do_ovo))
    # Adicionando o comando /danca_das_flores
    app.add_handler(CommandHandler("danca_das_flores", danca_das_flores))
    # Adicionando o comando /luau
    app.add_handler(CommandHandler("luau", luau))
    # Adicionando o comando /danca_das_medusas
    app.add_handler(CommandHandler("danca_das_medusas", danca_das_medusas))
    # Adicionando o comando /feira_do_vale
    app.add_handler(CommandHandler("feira_do_vale", feira_do_vale))
    # Adicionando o comando /vespera_dos_espiritos
    app.add_handler(CommandHandler("vespera_dos_espiritos", vespera_dos_espiritos))
    # Adicionando o comando /festival_do_gelo
    app.add_handler(CommandHandler("festival_do_gelo", festival_do_gelo))
    # Adicionando o comando /mercado_noturno
    app.add_handler(CommandHandler("mercado_noturno", mercado_noturno))
    # Adicionando o comando /festival_da_estrela
    app.add_handler(CommandHandler("festival_da_estrela", festival_da_estrela))
    # Adicionando o comando /aldeoes
    app.add_handler(CommandHandler("aldeoes", aldeoes))
    # Adicionando o novo comando /alex
    app.add_handler(CommandHandler("alex", alex))
    # Adicionando o comando /elliott
    app.add_handler(CommandHandler("elliott", elliott))
    # Adicionando o comando /harvey
    app.add_handler(CommandHandler("harvey", harvey))
    # Adicionando o comando /sam
    app.add_handler(CommandHandler("sam", sam))
    # Adicionando o comando /shane
    app.add_handler(CommandHandler("shane", shane))
    # Adicionando o comando /sebastian
    app.add_handler(CommandHandler("sebastian", sebastian))
    # Adicionando o comando /abigail
    app.add_handler(CommandHandler("abigail", abigail))
    # Adicionando o comando /emily
    app.add_handler(CommandHandler("emily", emily))
    # Adicionando o comando /haley
    app.add_handler(CommandHandler("haley", haley))
    # Adicionando o comando /leah
    app.add_handler(CommandHandler("leah", leah))
    # Adicionando o comando /maru
    app.add_handler(CommandHandler("maru", maru))
    # Adicionando o comando /penny
    app.add_handler(CommandHandler("penny", penny))
    # Adicionando o handler para o comando /start
    app.add_handler(CommandHandler("start", start))
    # Adicionando o comando /rancho_da_marnie
    app.add_handler(CommandHandler("rancho_da_marnie", rancho_da_marnie))
    # Adicionando o comando /armazem_do_pierre
    app.add_handler(CommandHandler("armazem_do_pierre", armazem_do_pierre))
    # Adicionando o comando /clinica_do_harvey
    app.add_handler(CommandHandler("clinica_do_harvey", clinica_do_harvey))
 # Registrando os manipuladores
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    
    print("Bot rodando!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    
    # Inicializa o bot diretamente sem chamar asyncio.run()
    app = ApplicationBuilder().token("7810939484:AAFiVC1-qMJEPNCHFZxUFo-bV9GH30AhA_0").build()
    #ugares
    app.add_handler(CommandHandler("minas", minas))
    app.add_handler(CommandHandler("centro_comunitario", centro_comunitario))
    app.add_handler(CommandHandler("rancho_da_marnie", rancho_da_marnie))
    app.add_handler(CommandHandler("armazem_do_pierre", armazem_do_pierre))
    app.add_handler(CommandHandler("clinica_do_harvey", clinica_do_harvey))

    #estaçoes
    app.add_handler(CommandHandler("estacoes", estacoes))
    app.add_handler(CommandHandler("verao", verao))
    app.add_handler(CommandHandler("primavera", primavera))
    app.add_handler(CommandHandler("outono", outono))
    app.add_handler(CommandHandler("inverno", inverno))

    #festivais
    app.add_handler(CommandHandler("festivais", festivais))
    app.add_handler(CommandHandler("festival_do_ovo", festival_do_ovo))
    app.add_handler(CommandHandler("danca_das_flores", danca_das_flores))
    app.add_handler(CommandHandler("luau", luau))
    app.add_handler(CommandHandler("danca_das_medusas", danca_das_medusas))
    app.add_handler(CommandHandler("feira_do_vale", feira_do_vale))
    app.add_handler(CommandHandler("vespera_dos_espiritos", vespera_dos_espiritos))
    app.add_handler(CommandHandler("festival_do_gelo", festival_do_gelo))
    app.add_handler(CommandHandler("mercado_noturno", mercado_noturno))
    app.add_handler(CommandHandler("festival_da_estrela", festival_da_estrela))

    #npcs
    app.add_handler(CommandHandler("aldeoes", aldeoes))
    app.add_handler(CommandHandler("alex", alex))
    app.add_handler(CommandHandler("elliott", elliott))
    app.add_handler(CommandHandler("harvey", harvey))
    app.add_handler(CommandHandler("sam", sam))
    app.add_handler(CommandHandler("sebastian", sebastian))
    app.add_handler(CommandHandler("shane", shane))
    app.add_handler(CommandHandler("abigail", abigail))
    app.add_handler(CommandHandler("emily", emily))
    app.add_handler(CommandHandler("haley", haley))
    app.add_handler(CommandHandler("leah", leah))
    app.add_handler(CommandHandler("maru", maru))
    app.add_handler(CommandHandler("penny", penny))

    #start
    app.add_handler(CommandHandler("start", start))



    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    
    print("Bot rodando!")
    app.run_polling()
