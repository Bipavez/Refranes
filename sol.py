from PyQt5 import uic, QtWidgets

form, base = uic.loadUiType("holi.ui")

class SolVentana(form, base):
    def __init__(self, *args, **kwargs):
        super(base, self).__init__()
        self.setupUi(self)
if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     win = SolVentana()
     win.show()
     sys.exit(app.exec_())
