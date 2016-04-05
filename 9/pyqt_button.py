from PyQt5 import QtWidgets


def say_something():
    print("TEST")
    QtWidgets.QMessageBox.information(None, "Title here", "Message here !")


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    button = QtWidgets.QPushButton("CLICK !", window)
    button.clicked.connect(say_something)
    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()
