from tkinter import *
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)

pegar_cotacoes()

janela = Tk()
janela.geometry("300x400")
janela.title("Cotação atual de moedas")

texto = Label(janela, text="Clique para ver as cotações de moedas")
texto.grid(column=0, row=0, padx= 50, pady= 20)

botao = Button(text="Buscar cotações", bg="black", fg="red", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=50, pady=20)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=50, pady=20)
janela.mainloop()
