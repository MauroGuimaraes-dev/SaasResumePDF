import streamlit as st
import fitz  # PyMuPDF para leitura eficiente de PDFs
import openai

def extract_text(pdf_document):
    text = ""
    for page in pdf_document:
        text += page.get_text()
    return text

def summarize_text(text, max_length=1000):
    """Resuma o texto para não exceder o número máximo de tokens."""
    # Esta é uma implementação simples que corta o texto
    # Você pode substituir por uma técnica de resumo mais sofisticada
    return text[:max_length]

def process_question(question, text):
    # Função simulada para processar a pergunta
    # Aqui você pode integrar a lógica real para processar a pergunta usando o texto extraído
    if question.strip() == "":
        return "Por favor, insira uma pergunta válida."
    # Simular uma resposta
    return "Esta é uma resposta simulada para a pergunta: " + question

def process_question_with_rag(question, text):
    if question.strip() == "":
        return "Por favor, insira uma pergunta válida."

    # Configurar a chave da API
    openai.api_key = st.session_state['api_key']

    # Resumir o texto do livro antes de enviar para a API
    summarized_text = summarize_text(text)
    prompt = f"Texto do livro: {summarized_text}\n\nPergunta: {question}\nResposta:"

    try:
        # Usar a interface correta para o modelo GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Erro ao obter resposta da API: {e}"

def display_interface():
    st.set_page_config(page_title="Leitor de PDF", layout="centered")
    st.sidebar.title("Configurações")
    
    # Inicializar o estado da sessão para a chave da API, se não estiver já inicializado
    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = None

    api_key = st.sidebar.text_input("Insira sua OpenAI API Key:", type="password")
    register_button = st.sidebar.button("Registrar API Key")

    # Atualizar a chave da API ao clicar no botão
    if register_button:
        st.session_state['api_key'] = api_key
        st.success("API Key registrada com sucesso!")

    # Remover a exibição da chave da API para mantê-la oculta
    # if st.session_state['api_key']:
    #     st.sidebar.write(f"API Key atual: {st.session_state['api_key']}")

    st.sidebar.write("### Instruções:")
    st.sidebar.write("1. Selecione o arquivo PDF.")
    st.sidebar.write("2. Faça perguntas sobre o conteúdo.")

    st.markdown("<h1 style='text-align: center; color: #00BFFF; background-color: darkblue;'>Leitor de PDF</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Desenvolvido por Mauro Guimarães</h3>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Selecione um arquivo PDF", type="pdf")
    if uploaded_file is not None:
        st.write("Arquivo carregado com sucesso!")  # Mensagem de depuração
        try:
            pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = extract_text(pdf_document)
            pdf_document.close()
            st.write("Texto extraído com sucesso!")  # Mensagem de depuração
        except Exception as e:
            st.error(f"Erro ao processar o arquivo PDF: {e}")

        question = st.text_input("Faça uma pergunta sobre o arquivo carregado:")

        # Estilizar botões com CSS
        st.markdown("""
            <style>
            .stButton > button {
                background-color: darkblue;
                color: #00BFFF;
                margin-right: 10px;
            }
            </style>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            ask_button = st.button("Perguntar")
        with col2:
            new_file_button = st.button("Carregar novo Arquivo")

        if ask_button:
            resposta = process_question_with_rag(question, text)
            st.write(resposta)

        if new_file_button:
            # Alternativa para st.experimental_rerun
            st.stop()

# Instanciando e exibindo a interface
if __name__ == "__main__":
    display_interface()
