from PyQt5 import QtWidgets


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(window)
    # layout = QtWidgets.QHBoxLayout(window)  # Uncomment this and try

    label = QtWidgets.QLabel("<h1> Layouts Example !", window)
    layout.addWidget(label)

    for i in range(9):
        button = QtWidgets.QPushButton(str(i), window)
        layout.addWidget(button)

    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()

# Docs: http://pyqt.sourceforge.net/Docs/PyQt5
