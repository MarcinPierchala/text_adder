from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog,QLineEdit, QFileDialog, QPlainTextEdit

app = QApplication([])


widget = QWidget()
widget.setWindowTitle("SUMA TXT")


textA = QPlainTextEdit(widget)
textA.insertPlainText("")
#textA.resize(400,200)
textA.setGeometry(0,0,200,50)

textB = QPlainTextEdit(widget)
textB.insertPlainText("")
#textB.resize(400,200)
textB.setGeometry(300,0,200,50)

#textC = QPlainTextEdit(widget)
#textC = Qt.ConnectionType(widget)
#textC.textChanged.connect(textA,textB)
#textC.insertPlainText()
#textC.setDisabled(True)
#textC.resize(400,200)
#textC.setGeometry(0,60,500,50)

#def suma(

textC=(str(textA)+str(textB))

suma = OPlainTextEdit(widget)
suma.setGeometry(0,60,500,50)
suma.textChanged.connect(textC)
textC.setDisabled(True)




widget.show()
app.exec_()