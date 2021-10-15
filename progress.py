from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
import time
import sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('progress.ui', self)
        #### button
        self.btn_go.clicked.connect(lambda: self.progress())

    def progress(self):
        count = 0
        for i in range(100):
            count += 1
            time.sleep(0.01)
            self.progressBar.setValue(count)



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())