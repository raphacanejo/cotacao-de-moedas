# Bibliotecas
import requests
import json
from tkinter import Tk, Button
from tkinter import ttk


# Função/Código principal
def cotacao_moedas():
    # Variáveis da API
    cotacoes = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()

# >>> CÓDIGO PRINCIPAL <<<
# Variáveis
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_btc = cotacoes['BTCBRL']['bid']

    # Programa
    print(f'Cotação do Dólar: R${cotacao_dolar}')
    print(f'Cotação do Euro: R${cotacao_euro}')
    print(f'Cotação do Bitcoin: R${cotacao_btc}')

    texto_resposta['text'] = (f'''
    Cotação do Dólar: R${cotacao_dolar} \n
    Cotação do Euro: R${cotacao_euro} \n
    Cotação do Bitcoin: R${cotacao_btc}''')


# Interface do programa
janela = Tk()

janela.title('Cotações de Moedas em Reais')

texto_principal = ttk.Label(
    janela,
    text='Clique no botão abaixo para mostrar a \ncotação atual do Dólar, Euro e Bitcoin.',
    font=('Arial', 12)
)
texto_principal.grid(column=0, row=0, padx=50, pady=10)

botao = Button(
    janela,
    text='MOSTRAR COTAÇÕES',
    command=cotacao_moedas,
    font=('Arial', 12)
)
botao.grid(column=0, row=1, padx=10)

texto_resposta = ttk.Label(
    janela,
    text='',
    font=('Arial', 12)
)
texto_resposta.grid(column=0, row=2, padx=10)

janela.mainloop()
