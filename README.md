# Leitor de PDF - Assistente de Leitura com IA

## Descrição
Este é um aplicativo avançado de leitura de PDF desenvolvido com Streamlit e PyMuPDF. Ele permite que os usuários façam upload de arquivos PDF e interajam com o conteúdo através de perguntas naturais, utilizando a API da OpenAI para processar e responder as consultas de forma inteligente.

## Funcionalidades
- Upload intuitivo de arquivos PDF
- Extração precisa de texto de PDFs usando PyMuPDF (fitz)
- Interface interativa e amigável construída com Streamlit
- Processamento de linguagem natural usando a API da OpenAI
- Capacidade de fazer perguntas específicas sobre o conteúdo do PDF
- Respostas contextualizadas baseadas no conteúdo do documento
- Suporte a documentos longos e complexos

## Tecnologias Utilizadas
- **Python**: Linguagem base do projeto
- **Streamlit**: Framework para criação da interface web
- **PyMuPDF (fitz)**: Biblioteca para processamento de PDFs
- **OpenAI API**: Motor de processamento de linguagem natural
- **Python-dotenv**: Gerenciamento de variáveis de ambiente
- **Outros pacotes**: Pandas, NumPy para manipulação de dados

## Requisitos
- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- Chave de API da OpenAI
- Conexão com a internet

## Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/SaasResumePDF.git
   cd SaasResumePDF
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows
   .\venv\Scripts\activate
   # No Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API OpenAI:
     ```
     OPENAI_API_KEY=sua-chave-aqui
     ```

## Como Usar

1. Inicie o aplicativo:
   ```bash
   streamlit run app.py
   ```

2. Acesse o aplicativo no navegador (geralmente em http://localhost:8501)

3. Use o aplicativo:
   - Faça upload do seu arquivo PDF
   - Aguarde o processamento do documento
   - Digite suas perguntas na caixa de texto
   - Receba respostas baseadas no conteúdo do PDF

## Dicas de Uso
- Para melhores resultados, use PDFs com texto bem formatado
- Faça perguntas específicas e claras
- O aplicativo funciona melhor com documentos em português e inglês
- O tempo de processamento pode variar dependendo do tamanho do PDF

## Limitações
- O tamanho máximo do arquivo PDF pode ser limitado
- A qualidade das respostas depende da qualidade do texto extraído do PDF
- Alguns PDFs muito complexos ou com formatação especial podem não ser processados corretamente

## Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
