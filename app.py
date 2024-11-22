<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Função para extrair informações sobre as minas
def get_minas_info():
    url = "https://pt.stardewvalleywiki.com/As_Minas"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo informações principais (ajuste de acordo com a estrutura da página)
        content = soup.find("div", {"class": "mw-parser-output"})
        if content:
            # Pegando todos os parágrafos, mas vamos filtrar os irrelevantes
            paragraphs = content.find_all("p")
            
            # Vamos começar pegando os parágrafos a partir do segundo (ignorando o primeiro "Anão")
            relevant_paragraphs = paragraphs[1:5]  # Pegando os próximos 4 parágrafos relevantes
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
    
    # Adicionando o link ao final da mensagem
    info_com_link = f"{minas_info}\n\nPara mais informações acesse: https://pt.stardewvalleywiki.com/As_Minas"
    
    # Enviando a mensagem com o link
    await update.message.reply_text(info_com_link)

# Função para extrair informações sobre as Estaçoes
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
    
    print("Bot rodando!")
    await app.run_polling()

if __name__ == "__main__":
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

    print("Bot rodando!")
    app.run_polling()
=======
import asyncio
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bs4 import BeautifulSoup
import requests
from fuzzywuzzy import fuzz
import unicodedata

TOKEN = "7810939484:AAFiVC1-qMJEPNCHFZxUFo-bV9GH30AhA_0"

def remover_acentos(texto):
    """
    Remove acentos de um texto para facilitar comparações.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def identificar_intencao(frase):
    """
    Identifica a intenção do usuário com base nas palavras-chave.
    """
    palavras_chave = {
        "presentes": ["presente", "favoritos", "gosto", "desgosto", "odio", "ama", "gosta"],
        "horários": ["horario", "agenda", "rotina", "primavera", "verao", "inverno", "outono"],
        "eventos": ["evento", "festival", "festa"],
        "locais": ["local", "cidade", "praia", "montanha"],
    }

    # Normalizar a frase de entrada
    frase_normalizada = remover_acentos(frase.lower())

    # Detectar intenção
    for categoria, palavras in palavras_chave.items():
        for palavra in palavras:
            if palavra in frase_normalizada:
                return categoria
    return "geral"  # Caso nenhuma intenção específica seja identificada

# Buscar informações na wiki
def buscar_informacoes(termo_busca):
    print(f"Buscando informações para: {termo_busca}")
    url = f"https://pt.stardewvalleywiki.com/{termo_busca.replace(' ', '_')}"
    
    try:
        # Fazer a requisição para a URL da pesquisa
        response = requests.get(url)
        response.raise_for_status()

        # Analisar o HTML da resposta
        soup = BeautifulSoup(response.text, 'html.parser')
        conteudo_principal = soup.find(id="bodyContent")

        if not conteudo_principal:
            return "Erro: Não foi possível encontrar o conteúdo principal da página."

        # Extrair título
        titulo = escapar_markdown(soup.find("h1").get_text(strip=True))

        # Identificar intenção
        intencao = identificar_intencao(termo_busca)

        if intencao == "presentes":
            tabela = buscar_tabela_por_titulo(conteudo_principal, ["Presentear", "Favoritos", "Ama", "Gosta"])
        elif intencao == "horários":
            tabela = buscar_tabela_por_titulo(conteudo_principal, ["Horário", "Agenda", "Rotina", "Primavera"])
        else:
            # Buscar a tabela infoboxtable para intenções gerais
            tabela = conteudo_principal.find("table", {"id": "infoboxtable"})
            if tabela:
                texto_tabela = formatar_tabela(tabela)
                return f"*{escapar_markdown(titulo)}*\n\n{texto_tabela}\n\n[Leia mais na Wiki]({url})"
            else:
                paragrafos = conteudo_principal.find_all("p", limit=3)
                texto_paragrafos = "\n\n".join([escapar_markdown(p.get_text(strip=True)) for p in paragrafos if p.get_text(strip=True)])
                return f"*{escapar_markdown(titulo)}*\n\n{texto_paragrafos}\n\n[Leia mais na Wiki]({url})"

        # Se uma tabela foi encontrada
        if tabela:
            texto_tabela = formatar_tabela(tabela)
            print(f"Texto da tabela formatado:\n{texto_tabela}")  # Debug
            return f"*{escapar_markdown(titulo)}*\n\n{texto_tabela}\n\n[Leia mais na Wiki]({url})"
        else:
            return f"*{escapar_markdown(titulo)}*\n\nNão consegui encontrar informações relevantes para '{termo_busca}'.\n\n[Leia mais na Wiki]({escapar_markdown(url)})"
    except Exception as e:
        print(f"Erro ao buscar informações: {e}")
        return f"Erro ao buscar informações no site. Detalhes: {escapar_markdown(str(e))}"
    
def buscar_tabela_por_titulo(conteudo, titulos_desejados):
    """
    Busca uma tabela pelo título ou conteúdo próximo a ela.
    """
    tabelas = conteudo.find_all("table", {"class": "wikitable"})
    for tabela in tabelas:
        # Verifica se há uma legenda ou cabeçalho próximo que corresponde ao título desejado
        legenda = tabela.find_previous_sibling(["h2", "h3", "h4", "a", "p"])
        if legenda and any(titulo.lower() in legenda.get_text(strip=True).lower() for titulo in titulos_desejados):
            return tabela
    return None

def formatar_tabela(tabela):
    """
    Formata uma tabela em MarkdownV2 para o Telegram.
    """
    linhas = tabela.find_all("tr")
    texto_tabela = []
    for linha in linhas:
        colunas = linha.find_all(["th", "td"])
        if len(colunas) == 2:
            chave = escapar_markdown(colunas[0].get_text(strip=True))
            valor = escapar_markdown(" ".join(colunas[1].stripped_strings))  # Garante espaços adequados entre palavras e links
            
            # Melhorar formatação para listas ou parentescos
            valor = re.sub(r"([A-Za-z])\(", r"\1 (", valor)  # Adiciona espaço antes do parêntese
            valor = re.sub(r"\)", r") ", valor)  # Garante fechamento correto do parêntese e adiciona espaço
            
            texto_tabela.append(f"*{chave}:* {valor}")
        elif len(colunas) == 1:
            texto_tabela.append(f"*{escapar_markdown(colunas[0].get_text(strip=True))}*")
    return "\n".join(texto_tabela)

def escapar_markdown(texto):
    """
    Escapa caracteres reservados no modo MarkdownV2 do Telegram.
    """
    caracteres_reservados = r'[_*[\]()~`>#+\-=|{}.!]'
    return re.sub(caracteres_reservados, r'\\\g<0>', texto)

# Processar frases para identificar palavras-chave
def processar_frase(frase):
    # Lista de palavras-chave principais para Stardew Valley
    palavras_chave = {
    "personagens": [
        "sebastian", "abigail", "penny", "leah", "maru", "elliott", "sam", "haley", "alex", 
        "harvey", "shane", "emily", "krobus", "linus", "demetrius", "robin", "willy", "pam",
        "caroline", "pierre", "gus", "george", "evelyn", "clint", "jas", "vincent", "dwarf",
        "sandy", "lewis", "marnie"
    ],
    "presentes": [
        "presente", "favoritos", "amor", "gosto", "desgosto", "ódio", "comida", "bebida", 
        "gema", "peixe", "fruta", "vegetal", "flor", "artesanato", "recurso", "mineração",
        "quartzo", "amatista", "rubi", "esmeralda", "diamante", "obsidiana", "mel", "cerveja",
        "vinho", "café", "chá", "pão", "bolo", "torta", "trufa", "cogumelo", "lagosta", 
        "caranguejo", "ostra", "marisco", "morango", "pêssego", "melão", "melancia", "amora",
        "mirtilo", "cereja", "leite", "queijo", "maionese", "iogurte", "manteiga", "ovo",
        "ovo grande", "ovo dourado"
    ],
    "cultivos": [
        "primavera", "verão", "outono", "inverno", "morango", "tomate", "milho", "abóbora", 
        "melancia", "mirtilo", "girassol", "café", "cerejeira", "macieira", "pereira", 
        "laranjeira", "romãzeira", "damasqueiro", "trigo", "arroz", "chá", "lúpulo", "ameixa", 
        "melão", "fertilizante", "solo", "irrigação", "regador", "espantalho"
    ],
    "pesca": [
        "vara de pescar", "anzol", "isca", "peixe", "carpa", "tilápia", "bagre", "linguado", 
        "salmão", "lago", "rio", "oceano", "praia", "caverna", "lenda", "peixes-lendários", 
        "isca mágica", "isca do coveiro", "rede de pesca", "bolha", "pesca perfeita", 
        "baú do tesouro"
    ],
    "mineração": [
        "mina", "caverna", "crânio", "vulcão", "ferro", "cobre", "ouro", "irídio", "carvão", 
        "quartzo", "cristal", "esmeralda", "geodo", "geodo omni", "geodo congelado", 
        "geodo magmático", "espada", "picareta", "adaga", "maça", "monstros", "gosma", 
        "fantasma", "morcego", "sombra", "esqueleto"
    ],
    "fazenda": [
        "galpão", "estufa", "celeiro", "galinheiro", "silo", "moinho", "poço", "estábulo", 
        "vaca", "cabra", "ovelha", "porco", "cavalo", "galinha", "pato", "coelho", 
        "galinha azul", "galinha dourada", "ovo", "leite", "lã", "trufa", "enxada", 
        "machado", "regador", "foice", "cerca", "portão", "estufa", "árvores", "grama", 
        "gotejamento", "poço", "trilho de mina"
    ],
    "locais": [
        "cidade", "pelicanos", "praia", "floresta", "mina", "montanha", "deserto", "vulcão", 
        "praça", "feira", "museu", "biblioteca", "loja", "mercado", "cavernas", "templo", 
        "lago", "rio", "oceano"
    ],
    "eventos": [
        "feira", "festival", "inverno", "verão", "primavera", "outono", "dança das flores", 
        "mercado noturno", "festival do gelo", "festival do ovo", "espírito", "halloween", 
        "festival da colheita", "dia das geleias", "casamento", "aniversário", "presente", 
        "coração"
    ],
    "mecânicas": [
        "coração", "amizade", "presente", "evento", "missão", "pedido especial", "loja", 
        "venda", "dinheiro", "ouro", "moeda", "habilidades", "profissões", "combate", 
        "mineração", "pesca", "agricultura", "coleta", "culinária", "receita", "artesanato", 
        "criação", "baú", "mochila", "organizador"
    ],
    "outros": [
        "mods", "wiki", "save", "farm", "multiplayer", "jogo", "console", "clima", "chuva", 
        "neve", "sol", "comunidade", "centro comunitário", "pacotes", "mercado Joja", 
        "abandono", "casamento", "divórcio", "filhos", "adoção", "cachorro", "gato", "cavalo"
    ]
    }

        # Normalizar a frase de entrada (minúsculas para facilitar comparação)
    frase_normalizada = frase.lower()

    termos_encontrados = {}

    # Detectar palavras-chave na frase usando fuzzy matching
    for categoria, palavras in palavras_chave.items():
        for palavra in palavras:
            # Usar fuzzy matching para encontrar correspondências aproximadas
            similaridade = fuzz.partial_ratio(frase_normalizada, palavra)
            if similaridade > 70:
                termos_encontrados[palavra] = similaridade

    # Ordenar os termos encontrados pela maior similaridade
    termos_ordenados = sorted(termos_encontrados.items(), key=lambda x: x[1], reverse=True)

    # Retorna apenas o termo mais relevante ou mensagem padrão
    return termos_ordenados[0][0] if termos_ordenados else "não entendi sua consulta"

# Função do comando /buscar
async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    frase = ' '.join(context.args)
    if frase:
        await update.message.reply_text("Processando sua consulta, por favor aguarde...")

        # Identificar termos na frase
        termos_busca = processar_frase(frase)
        if termos_busca:
            informacoes = buscar_informacoes(termos_busca)
            
            # Verificar se há conteúdo antes de responder
            if informacoes.strip():
                # Dividir a mensagem em partes menores
                max_length = 4096  # Limite do Telegram
                partes = [informacoes[i:i + max_length] for i in range(0, len(informacoes), max_length)]
                
                for parte in partes:
                    await update.message.reply_text(parte, parse_mode="MarkdownV2")
            else:
                await update.message.reply_text("Não consegui encontrar informações relevantes.")
        else:
            await update.message.reply_text("Desculpe, não consegui entender sua consulta.")
    else:
        await update.message.reply_text("Por favor, forneça uma frase para buscar na wiki.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Função chamada quando o comando /start é dado no Telegram"""
    # Exibe uma mensagem interativa de boas-vindas
    mensagem_boas_vindas = (
        "Olá! Eu sou o bot do Stardew Valley! 👋\n\n"
        "Para usar o bot, basta digitar um comando relacionado ao que você deseja saber. Aqui estão algumas opções:\n\n"
        "✅ Para buscar presentes e gostos dos NPCs, digite algo como: `/buscar Presentes de Sebastian`\n"
        "✅ Para consultar horários e rotina dos NPCs, digite: `/buscar Horário de Abigail`\n"
        "✅ Para saber mais sobre eventos no jogo, tente: `/buscar Eventos de Primavera`\n\n"
        "Esses são apenas exemplos! Experimente diferentes comandos como `/buscar` para ver o que você pode descobrir sobre Stardew Valley! 😄\n"
    )
    
    # Envia a mensagem de boas-vindas
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mensagem_boas_vindas)

# Função principal
async def main():
    # Criar aplicação
    application = Application.builder().token(TOKEN).build()

    # Adicionar o handler do comando /buscar
    application.add_handler(CommandHandler("buscar", buscar))
    application.add_handler(CommandHandler("start", start))

    # Iniciar o bot
    await application.initialize()
    await application.start()
    print("Bot iniciado!")
    try:
        await application.updater.start_polling()
        await asyncio.Event().wait()  # Aguarda o encerramento manual
    finally:
        await application.stop()
        await application.shutdown()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
>>>>>>> 387415f4823ad7c20b91fbae24344f6b813ac1d2
