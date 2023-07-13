import sys
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.showFileDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.runButton = QPushButton("Run")
        self.runButton.clicked.connect(self.runANTLR)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.runButton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('ANTLR4 GUI')
        self.show()

    def showFileDialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open file", "", "ANTLR Grammar Files (*.g4)")
        if file:
            with open(file, "r") as f:
                content = f.read()
                self.textEdit.setPlainText(content)

    def runANTLR(self):
        code = self.textEdit.toPlainText()

        # Aquí se puede generar el archivo .g4 dinámicamente
        with open("Expr.g4", "w") as f:
            f.write(code)

        # Aquí se puede generar y compilar el lexer y el parser utilizando ANTLR4
        lexer = YAPLLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        parser = YAPLParser(stream)

        # Obtener el árbol sintáctico
        tree = parser.program()

        # Mostrar el árbol sintáctico
        tree_str = tree.toStringTree(recog=parser)
        self.textEdit.clear()
        self.textEdit.setPlainText(tree_str)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())