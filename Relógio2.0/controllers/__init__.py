from views import itens , Tela


class  C_controller:
    def __init__(self,root):
        self.tela = Tela(root)
        self.data = itens(root).get_data()
        self.hora = itens(root).get_hora()
