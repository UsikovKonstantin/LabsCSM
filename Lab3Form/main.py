from PyQt6 import QtCore, QtGui, QtWidgets

from SolverSMO import SolverSMO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_smo_type = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_smo_type.setGeometry(QtCore.QRect(20, 50, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_smo_type.setFont(font)
        self.label_smo_type.setObjectName("label_smo_type")
        self.label_lambda = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_lambda.setGeometry(QtCore.QRect(20, 90, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_lambda.setFont(font)
        self.label_lambda.setObjectName("label_lambda")
        self.label_t_obsl = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_t_obsl.setGeometry(QtCore.QRect(430, 90, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_t_obsl.setFont(font)
        self.label_t_obsl.setObjectName("label_t_obsl")
        self.label_n = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_n.setGeometry(QtCore.QRect(20, 130, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_n.setFont(font)
        self.label_n.setObjectName("label_n")
        self.label_m = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_m.setGeometry(QtCore.QRect(420, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_m.setFont(font)
        self.label_m.setObjectName("label_m")
        self.label_n.setVisible(False)
        self.label_m.setVisible(False)
        self.pushButton_solve = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_solve.setGeometry(QtCore.QRect(20, 175, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_solve.setFont(font)
        self.pushButton_solve.setObjectName("pushButton_solve")
        self.pushButton_solve.clicked.connect(self.solve_button_clicked)
        self.comboBox_smo_type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_smo_type.setGeometry(QtCore.QRect(120, 45, 631, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_smo_type.setFont(font)
        self.comboBox_smo_type.setCurrentText("")
        self.comboBox_smo_type.setObjectName("comboBox_smo_type")
        self.comboBox_smo_type.addItem("Одноканальная с отказами в обслуживании")
        self.comboBox_smo_type.addItem("Одноканальная с ограниченной очередью")
        self.comboBox_smo_type.addItem("Одноканальная с неограниченной очередью")
        self.comboBox_smo_type.addItem("Многоканальная с отказами в обслуживании")
        self.comboBox_smo_type.addItem("Многоканальная с ограниченной очередью")
        self.comboBox_smo_type.addItem("Многоканальная с неограниченной очередью")
        self.comboBox_smo_type.currentIndexChanged.connect(self.combo_box_changed)
        self.lineEdit_lambda = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_lambda.setGeometry(QtCore.QRect(240, 85, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_lambda.setFont(font)
        self.lineEdit_lambda.setText("")
        self.lineEdit_lambda.setObjectName("lineEdit_lambda")
        self.lineEdit_t_obsl = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_t_obsl.setGeometry(QtCore.QRect(640, 85, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_t_obsl.setFont(font)
        self.lineEdit_t_obsl.setObjectName("lineEdit_t_obsl")
        self.lineEdit_n = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_n.setGeometry(QtCore.QRect(240, 125, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_n.setFont(font)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.lineEdit_m = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_m.setGeometry(QtCore.QRect(640, 125, 113, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_m.setFont(font)
        self.lineEdit_m.setObjectName("lineEdit_m")
        self.lineEdit_n.setVisible(False)
        self.lineEdit_m.setVisible(False)
        self.label_input_data = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_input_data.setGeometry(QtCore.QRect(320, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_input_data.setFont(font)
        self.label_input_data.setObjectName("label_input_data")
        self.label_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(340, 230, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.textEdit_result = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setGeometry(QtCore.QRect(20, 260, 731, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_result.setFont(font)
        self.textEdit_result.setObjectName("textEdit_result")
        self.textEdit_result.setTextColor(QtGui.QColor(0, 0, 0))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа №3"))
        self.label_smo_type.setText(_translate("MainWindow", "Тип СМО:"))
        self.label_lambda.setText(_translate("MainWindow", "Интенсивность потока:"))
        self.label_t_obsl.setText(_translate("MainWindow", "Время обслуживания:"))
        self.label_n.setText(_translate("MainWindow", "Количество каналов:"))
        self.label_m.setText(_translate("MainWindow", "Число мест в очереди:"))
        self.pushButton_solve.setText(_translate("MainWindow", "Найти характеристики"))
        self.label_input_data.setText(_translate("MainWindow", "Входные данные"))
        self.label_result.setText(_translate("MainWindow", "Результат"))

    def solve_button_clicked(self):
        smo_type = self.comboBox_smo_type.currentIndex() + 1
        lambda_str = self.lineEdit_lambda.text()
        t_obsl_str = self.lineEdit_t_obsl.text()
        n_str = self.lineEdit_n.text()
        m_str = self.lineEdit_m.text()

        lambda_float = 0
        try:
            lambda_float = float(lambda_str)
        except ValueError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Интенсивность потока невозможно привести к вещественному числу")
            return
        if lambda_float <= 0:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Интенсивность потока должна быть больше нуля")
            return

        t_obsl_float = 0
        try:
            t_obsl_float = float(t_obsl_str)
        except ValueError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Время обслуживания невозможно привести к вещественному числу")
            return
        if t_obsl_float <= 0:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Время обслуживания должно быть больше нуля")
            return

        n_int = None
        if smo_type > 3:
            try:
                n_int = int(n_str)
            except ValueError:
                QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Количество каналов невозможно привести к целому числу")
                return
            if n_int <= 0:
                QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Количество каналов должно быть больше нуля")
                return

        m_int = None
        if smo_type == 2 or smo_type == 5:
            try:
                m_int = int(m_str)
            except ValueError:
                QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка","Число мест в очереди невозможно привести к целому числу")
                return
            if m_int <= 0:
                QtWidgets.QMessageBox.critical(self.centralwidget, "Ошибка", "Число мест в очереди должно быть больше нуля")
                return

        solver = SolverSMO(smo_type, lambda_float, t_obsl_float, m_int, n_int)
        self.textEdit_result.setPlainText(str(solver))

    def combo_box_changed(self):
        smo_type = self.comboBox_smo_type.currentIndex() + 1
        self.label_n.setVisible(False)
        self.lineEdit_n.setVisible(False)
        self.label_m.setVisible(False)
        self.lineEdit_m.setVisible(False)

        if smo_type > 3:
            self.label_n.setVisible(True)
            self.lineEdit_n.setVisible(True)

        if smo_type == 2 or smo_type == 5:
            self.label_m.setVisible(True)
            self.lineEdit_m.setVisible(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
