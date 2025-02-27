Aqui está um **conversor de TXT para PDF** em Python com uma **janela gráfica**, **botões**, **menu**, **caixas de texto** para selecionar pastas e uma **barra de progresso**. Vamos usar **Tkinter** para a interface e **FPDF** para a conversão.  

---

## **📌 Instalação dos módulos necessários**
Antes de rodar o script, instale os módulos:
```bash
pip install fpdf tk
```

- **fpdf** → Para criar e salvar o PDF.  
- **tk** (Tkinter) → Para criar a interface gráfica.  

---

## **🖥️ Código Completo**
Este script cria uma janela com:
✅ **Caixas de texto** para selecionar a pasta de entrada e saída.  
✅ **Botão "Converter"** para iniciar a conversão.  
✅ **Botão "Sair"** para fechar o programa.  
✅ **Barra de progresso (%)** mostrando o andamento.  
✅ **Menu "Ficheiro"** com opções para abrir e sair.  

## **📌 Explicação do Código**
1. **Interface gráfica com Tkinter**:
   - Criamos uma janela com **caixas de texto** para selecionar a pasta de entrada (TXT) e saída (PDF).
   - Incluímos **botões** para selecionar pastas, converter e sair.
   - Adicionamos um **menu "Ficheiro"** com opções para abrir uma pasta e sair.

2. **Conversão TXT para PDF**:
   - O botão "Converter" busca todos os arquivos `.txt` da pasta de entrada.
   - Converte cada arquivo em um **PDF com o mesmo nome** na pasta de saída.
   - Utilizamos **FPDF** para gerar o PDF com texto formatado.

3. **Barra de progresso**:
   - Exibe a porcentagem da conversão conforme os arquivos são processados.

4. **Mensagens de erro e sucesso**:
   - Exibe avisos caso as pastas não sejam selecionadas ou se não houver arquivos `.txt`.

---

## **🎯 Como usar o programa**
1. Execute o script.
2. Clique em **"Selecionar"** e escolha a **pasta de entrada** com arquivos TXT.
3. Clique em **"Selecionar"** e escolha a **pasta de saída** onde os PDFs serão salvos.
4. Pressione **"Converter"** e aguarde a barra de progresso finalizar.
5. Quando terminar, uma mensagem **"Conversão concluída!"** será exibida.
