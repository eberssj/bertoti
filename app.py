import asyncio
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from bs4 import BeautifulSoup
import requests
from fuzzywuzzy import fuzz
import unicodedata

TOKEN = "6698271536:AAEWL7Z7wcRg7qFuVoakmb0AKtqngkQkyjY"

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


# Função principal
async def main():
    # Criar aplicação
    application = Application.builder().token(TOKEN).build()

    # Adicionar o handler do comando /buscar
    application.add_handler(CommandHandler("buscar", buscar))

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
