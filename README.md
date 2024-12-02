# Leitor de PDF

## Descrição
Este é um aplicativo de leitura de PDF desenvolvido com Streamlit e PyMuPDF. Ele permite que os usuários façam upload de um arquivo PDF e façam perguntas sobre seu conteúdo, utilizando uma API da OpenAI para processar as perguntas.

## Funcionalidades
- Carregamento de arquivos PDF.
- Extração de texto de PDFs usando PyMuPDF.
- Interface interativa com Streamlit para inserir perguntas e receber respostas.
- Integração com a API da OpenAI para processamento de linguagem natural.

## Requisitos
- Python 3.7 ou superior
- Streamlit
- PyMuPDF
- OpenAI API Key

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/SaasResumePDF.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd SaasResumePDF
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```
2. Insira sua OpenAI API Key na barra lateral.
3. Carregue um arquivo PDF e faça perguntas sobre seu conteúdo.

## Autor
Desenvolvido por Mauro Guimarães.
