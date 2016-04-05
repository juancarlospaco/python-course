from PyQt5 import QtWidgets


def main():
    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    layout_numbers = QtWidgets.QVBoxLayout(window)

    result = QtWidgets.QTextEdit()
    layout_numbers.addWidget(result)

    # Numbers from 0 to 9, Numeros de 0 a 9
    for number in range(10):
        button = QtWidgets.QPushButton(str(number))
        button.clicked.connect(lambda _, number=number:
                               result.insertPlainText(str(number)))
        layout_numbers.addWidget(button)

    # Math Operators, Operadores Matematicos
    operators = QtWidgets.QWidget()
    layout_operators = QtWidgets.QHBoxLayout(operators)
    for operator in ("*", "/", "+", "-", "//"):
        button = QtWidgets.QPushButton(str(operator))
        button.clicked.connect(lambda _, operator=operator:
                               result.insertPlainText(str(operator)))
        layout_operators.addWidget(button)
    layout_numbers.addWidget(operators)

    # Solve the user input, Resolver lo ingresado por el usuario
    solve = QtWidgets.QPushButton("EVAL", window)
    solve.clicked.connect(lambda _, maths=result:
                          result.setPlainText(str(eval(maths.toPlainText()))))
    layout_numbers.addWidget(solve)

    window.show()
    exit(application.exec_())


if __name__ == '__main__':
    main()
