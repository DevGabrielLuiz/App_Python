# importar o app, Builder (GUI)->interface do usuario.

from kivy.app import App
from kivy.lang import Builder
# criar aplicativo 

GUI = Builder.load_file('tela.kv') 

class MeuAplicativo(App):    # isso já é suficiente para criar o aplicativo
    def build(self):
        return GUI  # peguei a interface gráfica do usuario e passei para o app 
    def on_start(self): # todas as funções que devem ser atualizadas sempre que o app for aberto
        self.root.ids['coin1'].text   # /self.root.ids/estão fazendo referencia ao arquivo da GUI
        self.root.ids['coin2'].text   
        self.root.ids['coin3'].text  
        self.root.ids['coin4'].text   
        return super().on_start()

    def pegar_cotacao(self, moeda):
        link = f''

# criar a função build

MeuAplicativo().run()