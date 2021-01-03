from PyQt5 import uic, QtWidgets
import webbrowser

#função de Login
def login():
    tela1.label_5.setText("")
    U = tela1.lineEdit.text()
    S = tela1.lineEdit_2.text()
    if U == "Hyperman" and S == "022522":
        tela1.close()
        tela2.show()
    else:
        tela1.label_5.setText("Ta Tentando Me Hackear Parcero ?")

    if U == "" and S == "":
        tela1.label_5.setText("Insira Um Nome de Usuario e Senha.")

    if U == "Hyperman" and S == "":
        tela1.label_5.setText("Insira Uma Senha.")

    if U == "" and S == "022522":
            tela1.label_5.setText("Insira Um Nome de Usuario.")
#


#função do Botão de voltar
def Voltar():
    tela2.close()
    tela1.show()

def fechar():
    tela2.close()


#Botão github
def github():
    webbrowser.open('https://github.com/Chapadox', new=1, autoraise=True)

#Botão instagram
def Instagram():
    webbrowser.open('https://www.instagram.com/dudu_436/?hl=pt-br', new=1, autoraise=True)

#chamando As telas e setando as funçoes dos botoes
app = QtWidgets.QApplication([])
tela1 = uic.loadUi("tela1.ui")
tela2 = uic.loadUi("tela2.ui")
tela1.pushButton_3.clicked.connect(login)
tela2.pushButton.clicked.connect(Voltar)
tela1.pushButton.clicked.connect(github)
tela1.pushButton_2.clicked.connect(Instagram)
tela2.pushButton_2.clicked.connect(fechar)
tela1.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
#

tela1.show()
app.exec()