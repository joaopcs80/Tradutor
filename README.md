# 🖼️✨ **App de Tradução de Imagens**  

## 🌟 **Descrição do Projeto**  

O **App de Tradução de Imagens** é uma ferramenta incrível que combina tecnologias avançadas para transformar textos de imagens em conteúdo traduzido para o português, com rapidez e simplicidade.  

🎯 **Principais recursos**:  
- **📂 Carregar imagens** diretamente do computador.  
- **📋 Colar imagens** copiadas para a área de transferência.  
- **🌐 Traduzir o texto** extraído diretamente para o português.  

---

## 💻 **Requisitos do Sistema**  

📌 **Python 3.8+**  
📌 Bibliotecas Python necessárias:  
  - `pytesseract`  
  - `Pillow`  
  - `tkinter` (nativa do Python)  
  - `deep_translator`  

---

## 🔧 **Configuração do Tesseract OCR**  

### 1️⃣ **Instale o Tesseract OCR**  
- Baixe o instalador a partir do site oficial:  
  [🔗 https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)  
- Durante a instalação, anote o caminho do Tesseract no seu sistema (exemplo: `C:\Program Files\Tesseract-OCR` no Windows).  

### 2️⃣ **Adicione o Caminho ao PATH do Sistema**  
🔹 **Windows**:  
- Vá em **"Painel de Controle" > "Sistema" > "Configurações Avançadas do Sistema" > "Variáveis de Ambiente"**.  
- Encontre ou crie uma variável `PATH` e adicione o caminho do Tesseract (exemplo: `C:\Program Files\Tesseract-OCR`).  

🔹 **Linux/macOS**:  
- Adicione ao arquivo `.bashrc`, `.zshrc` ou equivalente:  
  ```bash
  export PATH="$PATH:/caminho/para/tesseract"
  ```  

### 3️⃣ **Verifique a Instalação**  
✅ Abra um terminal e execute:  
```bash
tesseract --version
```  
Se o comando retornar a versão instalada, o Tesseract está configurado corretamente.  

---

## 🛠️ **Como Usar o Aplicativo**  

1️⃣ **Inicie o aplicativo**  
- Execute o arquivo Python para abrir a interface gráfica.  

2️⃣ **Escolha como carregar a imagem**  
- Clique em **"Carregar Imagem"** 📂 para selecionar uma imagem do computador.  
- Ou copie uma imagem para a área de transferência e pressione **Ctrl + V** 📋 para colá-la no aplicativo.  

3️⃣ **Traduza o texto**  
- Clique em **"Traduzir Imagem"** 🌐 para processar e traduzir o texto extraído.  

4️⃣ **Limpe a tela**  
- Pressione **Ctrl + Z** 🔄 para limpar a imagem carregada e a tradução exibida.  

---

## 🎨 **Paleta de Cores do App**  

| **Elemento**       | **Cor**                | **Código HEX** |  
|---------------------|------------------------|----------------|  
| Fundo principal     | Azul escuro           | `#2C3E50`      |  
| Botão "Carregar"    | Azul claro            | `#3498DB`      |  
| Botão "Traduzir"    | Verde esmeralda       | `#2ECC71`      |  
| Fundo da tradução   | Cinza claro           | `#ECF0F1`      |  

---

## ⚡ **Atalhos do Teclado**  

💡 **Ctrl + V**: Cola uma imagem da área de transferência.  
💡 **Ctrl + Z**: Limpa a tela e os resultados exibidos.  

---

## 🌈 **Funcionalidades Adicionais**  

💬 **Interface Estilizada**: Combinação de cores para tornar a experiência visual mais agradável.  
🌍 **Suporte Multilinguagem**: Detecta automaticamente o idioma original do texto.  
🛡️ **Privacidade Garantida**: A extração do texto é feita localmente no computador.  

---

## 🛑 **Problemas Comuns e Soluções**  

1️⃣ **Erro ao traduzir texto**:  
🌐 Certifique-se de que a internet está conectada.  

2️⃣ **Erro ao extrair texto**:  
⚙️ Verifique se o Tesseract OCR está instalado e configurado no `PATH`.  

3️⃣ **Nenhuma imagem encontrada ao colar**:  
📋 Confirme que há uma imagem válida copiada na área de transferência.  

---

## 📜 **Licença**  

🆓 Este projeto é de código aberto! Sinta-se à vontade para modificá-lo conforme suas necessidades. 😊  

🎉 **Divirta-se traduzindo!** 🌟
