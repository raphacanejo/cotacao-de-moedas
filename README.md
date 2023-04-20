# Programa de cotação de moedas
Esse é um programa básico de Python para estudo de API e criação de interfaces gráficas com Tkinter.

Ao executar o programa ele irá abrir a janela a seguir:

![image](https://user-images.githubusercontent.com/98648504/233418560-87b24b99-6055-42d4-a0ec-3b2aad031b18.png)

Clicando no botão "MOSTRAR COTAÇÕES" o programa irá exibir a cotação atual do Dólar, Euro e Bitcoin em Reais como na imagem a seguir:

![image](https://user-images.githubusercontent.com/98648504/233419114-53b4accb-bdb9-4763-bcc6-155895be13b9.png)

# Criar executável do programa
Com o ambiente virtual criado, para criar um executável do programa só seguir os passos a seguir:

1. É necessário instalar a ferramenta que vai criar o executáve. Abra o terminal e digite:
~~~~
pip install pyinstaller
~~~~
2. Agora vamos criar o arquivo executável. No terminal digite:
~~~~
pyinstaller --onefile -w nome_do_arquivo.py
~~~~
