# importar o app, Builder (GUI)->interface do usuario.

from kivy.app import App
from kivy.lang import Builder
import requests
# criar aplicativo 

GUI = Builder.load_file('tela.kv') 

class MeuAplicativo(App):    # isso já é suficiente para criar o aplicativo
    def build(self):
        return GUI  # peguei a interface gráfica do usuario e passei para o app 
    def on_start(self): # todas as funções que devem ser atualizadas sempre que o app for aberto
        # /self.root.ids/estão fazendo referencia ao arquivo da GUI
        self.root.ids['coin1'].text  = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids['coin2'].text  = f"Euro R${self.pegar_cotacao('EUR')}" 
        self.root.ids['coin3'].text  = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids['coin4'].text  = f"Peso Argentino R${self.pegar_cotacao('ARS')}"
        
# criar a função build

    def pegar_cotacao(self, coin):
        link = f'https://economia.awesomeapi.com.br/last/{coin}-BRL'
        requesicao = requests.get(link)   # pegando a informação da internet
        dic_requisicao = requesicao.json()
        cotacao = dic_requisicao[f'{coin}BRL']['bid']
        return cotacao

MeuAplicativo().run()