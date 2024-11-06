import streamlit as st
from PIL import Image, ImageDraw, ImageOps

# Função para criar a imagem com bordas arredondadas (círculo perfeito)
def recorte_imagem_redonda(imagem_path):
    img = Image.open(imagem_path)
    
    # Garantindo que a imagem seja quadrada (tomando o menor lado)
    largura, altura = img.size
    tamanho = min(largura, altura)  # Pegamos o menor valor entre largura e altura para garantir o formato circular

    # Redimensionando a imagem para ser quadrada
    img = img.crop(((largura - tamanho) // 2, (altura - tamanho) // 2, (largura + tamanho) // 2, (altura + tamanho) // 2))
    
    # Criando uma máscara circular
    mask = Image.new('L', (tamanho, tamanho), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, tamanho, tamanho), fill=255)
    
    # Aplicando a máscara circular
    img.putalpha(mask)  # Colocando a máscara circular na imagem
    
    return img

# Função para exibir o currículo
def exibir_curriculo():
    st.title("Currículo Profissional")
    
    # Resumo das qualificações
    st.header("Resumo das Qualificações")
    st.write("""
    **Engenheiro Civil** com forte experiência na execução e gerenciamento de projetos estruturais. 
    Especializado na utilização de ferramentas de ponta como **Revit**, **Dynamo para Revit** e **Python**, 
    que permitem otimizar o desenvolvimento de projetos e automação de processos construtivos. 

    Profundo conhecimento em **modelagem paramétrica** e **automação de fluxos de trabalho** utilizando o **Dynamo para Revit**. 
    Além disso, sou capaz de integrar soluções digitais com **Python** para aumentar a eficiência e precisão no gerenciamento de dados e cálculos estruturais. 
    Com experiência prática na execução de obras, busco aplicar minhas habilidades para impulsionar projetos sustentáveis e inovadores no setor de engenharia civil.
    """)

# Função para exibir o objetivo
def exibir_objetivo():
    st.title("Objetivo Profissional")
    st.write("""
    Buscar novas oportunidades de **desenvolvimento e implementação de soluções tecnológicas** no setor de **engenharia civil**, 
    com foco em **automação de processos** e **inovação**. Meu objetivo é liderar projetos que integrem as tecnologias de **Revit**, **Dynamo** e **Python** 
    para otimizar a **modelagem de informações de construção (BIM)**, possibilitando a criação de **projetos sustentáveis**, 
    **eficientes** e **altamente automatizados**, proporcionando ganhos em **tempo** e **precisão**.
    """)

# Função para exibir a formação
def exibir_formacao():
    st.title("Formação Acadêmica")
    st.write("""
    - **Programação em Python** – **SENAI** (2024) :star: *Curso com ênfase em automação e integração de sistemas para a engenharia.*
    - **Dynamo para Revit** – **NeuroBIM** (Término previsto Dez/2024) :star: *Especialização em automação de fluxos de trabalho no Revit com Dynamo.*
    - **Pós-Graduação** em **Gestão de Projetos Sustentáveis de Edificações** – **Faculdade Alphaville** (2023)
    - **Graduação** em **Engenharia Civil** – **Universidade Paulista (UNIP)** (2022)
    - **Curso de AutoCAD (2D/3D)** – **UNIARA QUALIFICA** (2021)
    """)

# Função para exibir os conhecimentos
def exibir_conhecimentos():
    st.title("Conhecimentos e Habilidades")
    st.write("""
    - **Revit**: Profundo domínio em **modelagem** e **planejamento** de projetos estruturais, com ênfase em **BIM** e **coordenação de projetos**.
    - **Dynamo para Revit**: Criação de scripts para automação de tarefas, como **parametrização**, **otimização de processos** e **gerenciamento de dados** no Revit.
    - **Python**: Desenvolvimento de **scripts** para automação de cálculos estruturais, integração de **dados** e controle de **fluxos de trabalho**.
    - **AutoCAD / STRAP / Ftool**: Conhecimento avançado em **detalhamento estrutural** e **cálculos** com ferramentas especializadas.
    - **Produção em Campo**: Experiência prática em **acompanhamento de obras**, **execução de projetos** e **gestão de processos construtivos**.
    - **Idiomas**: Inglês básico (habilidade para leitura e compreensão de textos técnicos).
    """)

# Função para exibir a experiência profissional
def exibir_experiencia():
    st.title("Experiência Profissional")
    st.write("""
    **HM ENGENHARIA** (01/2020 – 10/2020)
    - **Cargo**: Estagiário
    - Levantamento de produção em campo, preenchimento de formulários e planilhas de controle.
    - Apoio com suprimentos, materiais e organização de documentos.
    
    **USICON CONSTRUÇÕES PRÉ-FABRICADAS LTDA** (10/2020 – 04/2022)
    - **Cargo**: Estagiário
    - Elaboração de projetos de **estruturas pré-fabricadas** e plotagens.
    - Acompanhamento de obras e visita à fábrica para conhecimento dos sistemas construtivos.
    - Aperfeiçoamento no uso do software **Revit**.

    **USICON CONSTRUÇÕES PRÉ-FABRICADAS LTDA** (04/2022 – Atual)
    - **Cargo**: Projetista Júnior
    - Detalhamento de peças pré-fabricadas com **AutoCAD**, **Revit** e planilhas Excel.
    - Cálculos e verificações estruturais com **STRAP**, **Ftool** e **AutoLISP**.
    - Acompanhamento de execução em campo, plotagem de projetos e resolução de dúvidas de execução.
    """)

# Função para exibir o portfólio de projetos
def exibir_portfolio():
    st.title("Portfólio de Projetos")
    st.header("Projeto 1: Projeto de Estruturas Pré-Fabricadas")
    st.write("""
    Desenvolvimento de **projetos de estruturas pré-fabricadas** para a construção de edificações sustentáveis, utilizando **AutoCAD**, **Revit**, **STRAP** e **Ftool**.
    Responsável pelo detalhamento estrutural, cálculos e supervisão de execução.
    """)

    st.header("Projeto 2: Gestão de Projetos Sustentáveis de Edificações")
    st.write("""
    Participação em projetos de **gestão sustentável** de edificações, otimizando o uso de recursos e aplicando práticas sustentáveis em toda a execução.
    Utilização de **Revit** e **Dynamo para Revit** para parametrização e automação dos fluxos de trabalho.
    """)

    st.header("Projeto 3: Acompanhamento de Obras e Execução de Projetos")
    st.write("""
    Visitas técnicas a obras para **acompanhamento da execução dos projetos estruturais**. Resolução de problemas no canteiro de obras e implementação de soluções técnicas.
    Colaboração com a equipe de campo para garantir a conformidade com os projetos aprovados.
    """)

# Função principal
def main():
    # Exibe a imagem uma vez, na parte superior da barra lateral
    img = recorte_imagem_redonda("portfolio.jpg")  # Substitua com o caminho correto da imagem
    st.sidebar.image(img, width=200)  # Exibe a imagem com recorte redondo na barra lateral no topo

    # Menu lateral para navegação
    st.sidebar.title("Menu de Navegação")
    menu = st.sidebar.radio("Escolha uma seção", 
                            ("Resumo das Qualificações", 
                             "Objetivo Profissional", 
                             "Formação Acadêmica", 
                             "Conhecimentos e Habilidades", 
                             "Experiência Profissional", 
                             "Portfólio de Projetos"))

    # Exibe a seção de acordo com a escolha do menu
    if menu == "Resumo das Qualificações":
        exibir_curriculo()
    elif menu == "Objetivo Profissional":
        exibir_objetivo()
    elif menu == "Formação Acadêmica":
        exibir_formacao()
    elif menu == "Conhecimentos e Habilidades":
        exibir_conhecimentos()
    elif menu == "Experiência Profissional":
        exibir_experiencia()
    elif menu == "Portfólio de Projetos":
        exibir_portfolio()

# Executando o aplicativo
if __name__ == "__main__":
    main()