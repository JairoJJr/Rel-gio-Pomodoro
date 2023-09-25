from views import itens , Tela


class  C_controller:
    def __init__(self,root):
        self.tela = Tela(root)
        self.itens = itens(root)
