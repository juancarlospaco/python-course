from PyQt5 import QtWidgets


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    label = QtWidgets.QLabel("<h1> Hello World !", window)
    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()

# Docs: http://pyqt.sourceforge.net/Docs/PyQt5
