# 🕵️‍♂️ Web Scraping com Selenium e Python

Este projeto demonstra como realizar **web scraping automatizado** utilizando o **Selenium**, extraindo dados de forma estruturada e exportando-os para planilhas.  
A coleta foi feita no site **Books to Scrape**, um ambiente seguro criado para fins de aprendizado e prática de scraping.

---

## 🚀 Objetivo

Automatizar a navegação em um site dinâmico, coletando informações de livros (título e preço) e salvando os resultados em um arquivo Excel.  
O projeto mostra, de forma simples e didática, como usar Selenium com Python para **explorar múltiplas páginas**, aplicar **esperas dinâmicas** e **tratar exceções** durante o processo.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.12+**  
- **Selenium WebDriver**  
- **Pandas**  
- **OpenPyXL**  
- **Google Chrome / ChromeDriver**

---

## 🧩 Estrutura do projeto
┣ 📜 treino_books.py
┣ 📜 livros_scrapping.xlsx
┣ 📜 requirements.txt
┗ 📜 README.md

---

## 📘 Etapas da análise

1. Inicializa o **WebDriver** e acessa o site `https://books.toscrape.com/`.  
2. Percorre automaticamente todas as páginas do catálogo.  
3. Extrai o **título** e o **preço** de cada livro.  
4. Armazena os dados em um **DataFrame** com Pandas.  
5. Exporta o resultado para um arquivo Excel (`livros_scrapping.xlsx`).

---

## 📊 Exemplo de saída

| Título | Preço |
|:-------|:------:|
| A Light in the Attic | £51.77 |
| Tipping the Velvet | £53.74 |
| Soumission | £50.10 |

---

## 💡 Possíveis melhorias

- Capturar **avaliação (rating)** e **disponibilidade em estoque**.  
- Adicionar logs e tratamento de erros mais detalhados.  
- Permitir scraping de múltiplas categorias de livros.  
- Automatizar a execução com **agendamento**.

---

## 👤 Autor

**Lucas Borges**  
Estudante de Sistemas de Informação • Foco em Automação e Análise de Dados  
[LinkedIn](https://www.linkedin.com/in/lucas-borges21)  
[GitHub](https://github.com/LucasBorges21)

---

<p align="center"><em>Projeto criado para fins de aprendizado e demonstração de portfólio em Web Scraping com Selenium.</em></p>
