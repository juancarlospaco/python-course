from PyQt5 import QtWidgets


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()
