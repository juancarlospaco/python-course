from PyQt5 import QtWidgets


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    calendar = QtWidgets.QCalendarWidget(window)
    calendar.resize(640, 480)
    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()
