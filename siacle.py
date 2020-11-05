import sqlite3

from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
                         QRegExpValidator)
from PyQt5.QtCore import (Qt, QFile, QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,
                          QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu,
                             QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
                             QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
                             QDateEdit, QComboBox)
import visualizarImprimirExportar
import os


class Ayuda(QDialog):
    def __init__(self, parent=None):
        super(Ayuda, self).__init__()

        self.setWindowTitle("Помощь")
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setPixmap(QPixmap("Imagenes/siacle.jpg").scaled(450, 450, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        label.move(0, 0)

        botonCerrar = QPushButton("Закрыть", self)
        botonCerrar.setFixedSize(430, 32)
        botonCerrar.move(10, 457)

        botonCerrar.clicked.connect(self.close)


class Acerca(QDialog):
    def __init__(self, parent=None):
        super(Acerca, self).__init__()

        self.setWindowTitle("Печать")
        # self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
        #                     Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        # self.initUI()
        os.system('python visualizarImprimirExportar.py')


class nuevoCliente(QDialog):
    def __init__(self, parent=None):
        super(nuevoCliente, self).__init__()

        self.setWindowIcon(QIcon("Imagenes/new.jpg"))
        self.setWindowTitle("Новый клиент")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(320, 478)

        self.initUI()

    def initUI(self):

        self.groupBoxDatosGenerales = QGroupBox("Новый клиент", self)
        self.groupBoxDatosGenerales.setFixedSize(300, 223)
        self.groupBoxDatosGenerales.move(10, 13)

        labelNombre = QLabel("<font color='#FF3300'>*</font> Имя",
                             self.groupBoxDatosGenerales)
        labelNombre.move(15, 28)

        self.lineEditNombre = QLineEdit(self.groupBoxDatosGenerales)
        self.lineEditNombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+"),
                                                          self.lineEditNombre))
        self.lineEditNombre.setMaxLength(30)
        self.lineEditNombre.setFixedWidth(270)
        self.lineEditNombre.setFocus()
        self.lineEditNombre.move(15, 46)

        labelApellido = QLabel("<font color='#FF3300'>*</font> Фамилия",
                               self.groupBoxDatosGenerales)
        labelApellido.move(15, 74)

        self.lineEditApellido = QLineEdit(self.groupBoxDatosGenerales)
        self.lineEditApellido.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+"),
                                                            self.lineEditApellido))
        self.lineEditApellido.setMaxLength(30)
        self.lineEditApellido.setFixedWidth(270)
        self.lineEditApellido.move(15, 92)

        labelSexo = QLabel("<font color='#FF3300'>*</font> Пол", self.groupBoxDatosGenerales)
        labelSexo.move(15, 120)

        self.comboBoxSexo = QComboBox(self.groupBoxDatosGenerales)
        self.comboBoxSexo.addItems(["М", "Ж"])
        self.comboBoxSexo.setCurrentIndex(-1)
        self.comboBoxSexo.setFixedWidth(270)
        self.comboBoxSexo.move(15, 138)

        labelFechaNacimiento = QLabel("<font color='#FF3300'>*</font> Дата рождения",
                                      self.groupBoxDatosGenerales)
        labelFechaNacimiento.move(15, 166)

        self.dateEditFechaNacimiento = QDateEdit(self.groupBoxDatosGenerales)
        self.dateEditFechaNacimiento.setDate(QDate.currentDate())
        self.dateEditFechaNacimiento.setMaximumDate(QDate.currentDate())
        self.dateEditFechaNacimiento.setDisplayFormat("dd/MM/yyyy")
        self.dateEditFechaNacimiento.setCalendarPopup(True)
        self.dateEditFechaNacimiento.setCursor(Qt.PointingHandCursor)
        self.dateEditFechaNacimiento.setFixedWidth(270)
        self.dateEditFechaNacimiento.move(15, 184)

        self.groupBoxUbicacion = QGroupBox("Проживание", self)
        self.groupBoxUbicacion.setFixedSize(300, 86)
        self.groupBoxUbicacion.move(10, 250)

        labelPais = QLabel("<font color='#FF3300'>*</font> Страна", self.groupBoxUbicacion)
        labelPais.move(15, 28)

        self.lineEditPais = QLineEdit(self.groupBoxUbicacion)
        self.lineEditPais.setMaxLength(30)
        self.lineEditPais.setFixedWidth(270)
        self.lineEditPais.move(15, 48)

        self.groupBoxContacto = QGroupBox("Контакты", self)
        self.groupBoxContacto.setFixedSize(300, 86)
        self.groupBoxContacto.move(10, 350)

        labelTelCel = QLabel("<font color='#FF3300'>*</font> Номер телефона",
                             self.groupBoxContacto)
        labelTelCel.move(15, 28)

        self.lineEditTelCel = QLineEdit(self.groupBoxContacto)
        self.lineEditTelCel.setInputMask("9999999999999999; ")
        self.lineEditTelCel.setFixedWidth(270)
        self.lineEditTelCel.move(15, 48)

        # ==========================================================

        labelInformacion = QLabel("<font color='#FF3300'>*</font> Обязательные поля.", self)
        labelInformacion.move(10, 445)

        buttonAceptar = QPushButton("Сохранить", self)
        buttonAceptar.setCursor(Qt.PointingHandCursor)
        buttonAceptar.move(154, 445)

        buttonCerrar = QPushButton("Закрыть", self)
        buttonCerrar.setCursor(Qt.PointingHandCursor)
        buttonCerrar.move(236, 445)

        buttonAceptar.clicked.connect(self.Aceptar)
        buttonCerrar.clicked.connect(self.close)

    def Aceptar(self):
        nombre = " ".join(self.lineEditNombre.text().split()).title()
        apellido = " ".join(self.lineEditApellido.text().split()).title()
        sexo = self.comboBoxSexo.currentText()
        fecNacimiento = self.dateEditFechaNacimiento.text()
        pais = " ".join(self.lineEditPais.text().split()).title()
        telCel = self.lineEditTelCel.text()

        if not nombre:
            self.lineEditNombre.setFocus()
        elif not apellido:
            self.lineEditApellido.setFocus()
        elif not sexo:
            self.comboBoxSexo.setFocus()
        elif not pais:
            self.lineEditPais.setFocus()
        elif not telCel:
            self.lineEditTelCel.setFocus()
        else:
            if QFile.exists("DB_SIACLE/DB_SIACLE.db"):
                conexion = sqlite3.connect("DB_SIACLE/DB_SIACLE.db")
                cursor = conexion.cursor()

                try:
                    datos = [nombre, apellido, sexo, fecNacimiento, pais, telCel]
                    cursor.execute("INSERT INTO CLIENTES (NOMBRE, APELLIDO, SEXO, "
                                   "FECHA_NACIMIENTO, PAIS, TELEFONO_CELULAR) "
                                   "VALUES (?,?,?,?,?,?)", datos)

                    conexion.commit()
                    conexion.close()

                    self.lineEditNombre.clear()
                    self.lineEditApellido.clear()
                    self.comboBoxSexo.setCurrentIndex(-1)
                    self.dateEditFechaNacimiento.setDate(QDate.currentDate())
                    self.lineEditPais.clear()
                    self.lineEditTelCel.clear()

                    QMessageBox.information(self, "Новый клиент", "Клиент зарегестрирован.   ",
                                            QMessageBox.Ok)
                except:
                    conexion.close()
                    QMessageBox.critical(self, "Новый клиент", "Неизвестная ошибка.   ",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Новый клиент", "База данных не найдена."
                                                           "   ", QMessageBox.Ok)

            self.lineEditNombre.setFocus()


class actualizarCliente(QDialog):
    def __init__(self, indice, datos, parent=None):
        super(actualizarCliente, self).__init__()

        self.parent = parent
        self.indice = indice
        self.datos = datos

        self.setWindowIcon(QIcon("Imagenes/ch.png"))
        self.setWindowTitle("Обновление клиента")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(320, 478)

        self.initUI()

    def initUI(self):

        self.groupBoxDatosGenerales = QGroupBox("Общие данные ", self)
        self.groupBoxDatosGenerales.setFixedSize(300, 223)
        self.groupBoxDatosGenerales.move(10, 13)

        labelNombre = QLabel("<font color='#FF3300'>*</font> Имя",
                             self.groupBoxDatosGenerales)
        labelNombre.move(15, 28)

        self.lineEditNombre = QLineEdit(self.groupBoxDatosGenerales)
        self.lineEditNombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+"),
                                                          self.lineEditNombre))
        self.lineEditNombre.setMaxLength(30)
        self.lineEditNombre.setFixedWidth(270)
        self.lineEditNombre.setFocus()
        self.lineEditNombre.move(15, 46)

        labelApellido = QLabel("<font color='#FF3300'>*</font> Фамилия",
                               self.groupBoxDatosGenerales)
        labelApellido.move(15, 74)

        self.lineEditApellido = QLineEdit(self.groupBoxDatosGenerales)
        self.lineEditApellido.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+"),
                                                            self.lineEditApellido))
        self.lineEditApellido.setMaxLength(30)
        self.lineEditApellido.setFixedWidth(270)
        self.lineEditApellido.move(15, 92)

        labelSexo = QLabel("<font color='#FF3300'>*</font> Пол", self.groupBoxDatosGenerales)
        labelSexo.move(15, 120)

        self.comboBoxSexo = QComboBox(self.groupBoxDatosGenerales)
        self.comboBoxSexo.addItems(["М", "Ж"])
        self.comboBoxSexo.setCurrentIndex(-1)
        self.comboBoxSexo.setFixedWidth(270)
        self.comboBoxSexo.move(15, 138)

        labelFechaNacimiento = QLabel("<font color='#FF3300'>*</font> Дата рождения",
                                      self.groupBoxDatosGenerales)
        labelFechaNacimiento.move(15, 166)

        self.dateEditFechaNacimiento = QDateEdit(self.groupBoxDatosGenerales)
        self.dateEditFechaNacimiento.setDate(QDate.currentDate())
        self.dateEditFechaNacimiento.setMaximumDate(QDate.currentDate())
        self.dateEditFechaNacimiento.setDisplayFormat("dd/MM/yyyy")
        self.dateEditFechaNacimiento.setCalendarPopup(True)
        self.dateEditFechaNacimiento.setCursor(Qt.PointingHandCursor)
        self.dateEditFechaNacimiento.setFixedWidth(270)
        self.dateEditFechaNacimiento.move(15, 184)

        self.groupBoxUbicacion = QGroupBox("Проживание", self)
        self.groupBoxUbicacion.setFixedSize(300, 86)
        self.groupBoxUbicacion.move(10, 250)

        labelPais = QLabel("<font color='#FF3300'>*</font> Страна", self.groupBoxUbicacion)
        labelPais.move(15, 28)

        self.lineEditPais = QLineEdit(self.groupBoxUbicacion)
        self.lineEditPais.setMaxLength(30)
        self.lineEditPais.setFixedWidth(270)
        self.lineEditPais.move(15, 48)

        self.groupBoxContacto = QGroupBox("Контакты", self)
        self.groupBoxContacto.setFixedSize(300, 86)
        self.groupBoxContacto.move(10, 350)

        labelTelCel = QLabel("<font color='#FF3300'>*</font> Номер телефона",
                             self.groupBoxContacto)
        labelTelCel.move(15, 28)

        self.lineEditTelCel = QLineEdit(self.groupBoxContacto)
        self.lineEditTelCel.setInputMask("9999999999999999; ")
        self.lineEditTelCel.setFixedWidth(270)
        self.lineEditTelCel.move(15, 48)

        labelInformacion = QLabel("<font color='#FF3300'>*</font> Обязательные поля.", self)
        labelInformacion.move(10, 445)

        buttonActualizar = QPushButton("Обновить", self)
        buttonActualizar.setCursor(Qt.PointingHandCursor)
        buttonActualizar.move(154, 445)

        buttonCerrar = QPushButton("Закрыть", self)
        buttonCerrar.setCursor(Qt.PointingHandCursor)
        buttonCerrar.move(236, 445)

        buttonActualizar.clicked.connect(self.Actualizar)
        buttonCerrar.clicked.connect(self.close)

        self.cargarDatos(self.datos)

    def cargarDatos(self, datos):

        self.lineEditNombre.setText(datos[1])
        self.lineEditApellido.setText(datos[2])

        itemsComboBox = [self.comboBoxSexo.itemText(i) for i in range(self.comboBoxSexo.count())]
        if datos[3] in itemsComboBox:
            posicionItem = itemsComboBox.index(datos[3])
            self.comboBoxSexo.setCurrentIndex(posicionItem)
        else:
            self.comboBoxSexo.setCurrentIndex(-1)

        self.dateEditFechaNacimiento.setDate(QDate.fromString(datos[4], "dd/MM/yyyy"))
        self.lineEditPais.setText(datos[5])
        self.lineEditTelCel.setText(datos[6])

        return

    def Actualizar(self):
        nombre = " ".join(self.lineEditNombre.text().split()).title()
        apellido = " ".join(self.lineEditApellido.text().split()).title()
        sexo = self.comboBoxSexo.currentText()
        fecNacimiento = self.dateEditFechaNacimiento.text()
        pais = " ".join(self.lineEditPais.text().split()).title()
        telCel = self.lineEditTelCel.text()

        if not nombre:
            self.lineEditNombre.setFocus()
        elif not apellido:
            self.lineEditApellido.setFocus()
        elif not sexo:
            self.comboBoxSexo.setFocus()
        elif not pais:
            self.lineEditPais.setFocus()
        elif not telCel:
            self.lineEditTelCel.setFocus()
        else:
            if QFile.exists("DB_SIACLE/DB_SIACLE.db"):
                conexion = sqlite3.connect("DB_SIACLE/DB_SIACLE.db")
                cursor = conexion.cursor()

                try:
                    datos = [nombre, apellido, sexo, fecNacimiento, pais, telCel,
                             self.datos[0]]

                    cursor.execute("UPDATE CLIENTES SET NOMBRE = ?, APELLIDO = ?, SEXO = ?, "
                                   "FECHA_NACIMIENTO = ?, PAIS = ?, TELEFONO_CELULAR = ? "
                                   "WHERE ID = ?", datos)

                    conexion.commit()
                    conexion.close()

                    nuevos_datos = (str(self.datos[0]), nombre, apellido, sexo, fecNacimiento,
                                    pais, telCel)
                    self.parent.tabla.removeRow(self.indice)

                    numFilas = self.parent.tabla.rowCount()
                    self.parent.tabla.insertRow(numFilas)

                    for indice, dato in enumerate(nuevos_datos):
                        dato = QTableWidgetItem(dato)
                        if indice == 0:
                            dato.setTextAlignment(Qt.AlignCenter)

                        self.parent.tabla.setItem(numFilas, indice, dato)

                    self.lineEditNombre.clear()
                    self.lineEditApellido.clear()
                    self.comboBoxSexo.setCurrentIndex(-1)
                    self.dateEditFechaNacimiento.setDate(QDate.currentDate())
                    self.lineEditPais.clear()
                    self.lineEditTelCel.clear()

                    QMessageBox.information(self, "Обновление клиента ", "Клиент обновлен."
                                                                         "   ", QMessageBox.Ok)

                    self.close()
                except:
                    conexion.close()
                    QMessageBox.critical(self, "Обновление клиента", "Неизвестная ошибка.   ",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Обновление клиента", "База не найдена "
                                                                 "datos.   ", QMessageBox.Ok)


class Configuracion(QDialog):
    def __init__(self, parent=None):
        super(Configuracion, self).__init__(parent)

        self.setWindowFlags(Qt.Popup)
        self.setFixedSize(450, 500)

        paleta = self.palette()
        paleta.setColor(QPalette.Background, QColor("white"))
        self.setPalette(paleta)

        self.initUI()

    def initUI(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setFixedSize(450, 500)
        frame.move(0, 0)

        label = QLabel(frame)
        label.setPixmap(QPixmap("Imagenes/siacle.jpg").scaled(447, 447, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        label.move(1, 1)

        botonConfigurar = QPushButton("Информация", frame)
        botonConfigurar.setFixedSize(430, 32)
        botonConfigurar.move(10, 457)

        botonConfigurar.clicked.connect(self.Configuracion)

    def Configuracion(self):
        QMessageBox.information(self, "Информация", " 2 Лабораторная работа по ОНИТ\n "
                                                    "Выполнил: Сухоруков Я.И.\n "
                                                    "2020 г. Москва", QMessageBox.Ok)


class Boton(QToolButton):
    def __init__(self, parent=None):
        super(Boton, self).__init__(parent)

        self.setMask(QRegion(QRect(2, 2, 220, 36), QRegion.Rectangle))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(26, 26))
        self.setIcon(QIcon("Imagenes/Qt.png"))
        self.setFixedSize(224, 40)


class Widgets(QWidget):
    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)

        self.initUI()

    def initUI(self):

        fuenteSiacle = self.font()
        fuenteSiacle.setBold(True)
        fuenteSiacle.setPointSize(12)

        paletaBotones = self.palette()
        paletaBotones.setColor(QPalette.Background, QColor("#2EFEC8"))

        frameBotones = QFrame()
        frameBotones.setFrameStyle(QFrame.NoFrame)
        frameBotones.setAutoFillBackground(True)
        frameBotones.setPalette(paletaBotones)
        frameBotones.setFixedWidth(220)

        paletaPanel = self.palette()
        paletaPanel.setBrush(QPalette.Background, QBrush(QColor(255, 90, 0), Qt.SolidPattern))
        paletaPanel.setColor(QPalette.Foreground, Qt.white)

        labelSiacle = QLabel("ПАНЕЛЬ УПРАВЛЕНИЯ", frameBotones)
        labelSiacle.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        labelSiacle.setFont(fuenteSiacle)
        labelSiacle.setAutoFillBackground(True)
        labelSiacle.setPalette(paletaPanel)
        labelSiacle.setFixedSize(220, 46)
        labelSiacle.move(0, 0)

        # ============================================================

        tamanioIcono = QSize(30, 30)

        botonNuevo = Boton(frameBotones)
        botonNuevo.setText(" Новый")
        botonNuevo.setToolTip("Новый клиент")
        botonNuevo.setCursor(Qt.PointingHandCursor)
        botonNuevo.move(-2, 45)

        botonActualizar = Boton(frameBotones)
        botonActualizar.setText(" Обновление")
        botonActualizar.setToolTip("Обновление клиента ")
        botonActualizar.setCursor(Qt.PointingHandCursor)
        botonActualizar.move(-2, 82)

        botonEliminar = Boton(frameBotones)
        botonEliminar.setText(" Удалить")
        botonEliminar.setToolTip("Удалить клиента")
        botonEliminar.setCursor(Qt.PointingHandCursor)
        botonEliminar.move(-2, 119)

        botonLimpiar = Boton(frameBotones)
        botonLimpiar.setText(" Закрыть")
        botonLimpiar.setToolTip("Закрыть бд")
        botonLimpiar.setCursor(Qt.PointingHandCursor)
        botonLimpiar.move(-2, 156)

        # ============================================================

        paletaSuscribete = self.palette()
        paletaSuscribete.setBrush(QPalette.Background, QBrush(QColor(135, 206, 250),
                                                              Qt.SolidPattern))

        fuenteSuscribete = self.font()
        fuenteSuscribete.setBold(True)
        fuenteSuscribete.setFamily("Arial")
        fuenteSuscribete.setPointSize(11)

        labelSuscribete = QLabel("<a href='https://t.me/yarosla_0v'>АВТОР</a>", frameBotones)

        labelSuscribete.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        labelSuscribete.setOpenExternalLinks(True)
        labelSuscribete.setFont(fuenteSuscribete)
        labelSuscribete.setAutoFillBackground(True)
        labelSuscribete.setPalette(paletaSuscribete)
        labelSuscribete.setFixedSize(220, 46)
        labelSuscribete.move(0, 210)

        paletaFrame = self.palette()
        paletaFrame.setColor(QPalette.Background, QColor("blue"))

        frameBienvenido = QFrame()
        frameBienvenido.setFrameStyle(QFrame.NoFrame)
        frameBienvenido.setAutoFillBackground(True)
        frameBienvenido.setPalette(paletaFrame)
        frameBienvenido.setFixedHeight(46)

        # ============================================================

        paletaTitulo = self.palette()
        paletaTitulo.setColor(QPalette.Foreground, Qt.yellow)

        labelBienvenido = QLabel("Клиенты")
        labelBienvenido.setAlignment(Qt.AlignCenter)
        labelBienvenido.setFont(fuenteSiacle)
        labelBienvenido.setPalette(paletaTitulo)

        botonConfiguracion = QPushButton()
        botonConfiguracion.setIcon(QIcon("Imagenes/configuracion.png"))
        botonConfiguracion.setIconSize(QSize(24, 24))
        botonConfiguracion.setToolTip("Конфигурация")
        botonConfiguracion.setCursor(Qt.PointingHandCursor)
        botonConfiguracion.setFixedWidth(36)

        disenioFrame = QHBoxLayout()
        disenioFrame.addWidget(labelBienvenido, Qt.AlignCenter)
        disenioFrame.addStretch()
        disenioFrame.addWidget(botonConfiguracion)
        disenioFrame.setContentsMargins(0, 0, 5, 0)
        frameBienvenido.setLayout(disenioFrame)

        # ============================================================

        self.buscarLineEdit = QLineEdit()
        self.buscarLineEdit.setObjectName("Enter")
        self.buscarLineEdit.setPlaceholderText("Имя клента")
        self.buscarLineEdit.setMinimumSize(200, 26)

        botonBuscar = QPushButton("Поиск")
        botonBuscar.setObjectName("Поиск")
        botonBuscar.setCursor(Qt.PointingHandCursor)
        botonBuscar.setMinimumSize(60, 26)

        separadorTodos = QFrame()
        separadorTodos.setFrameShape(QFrame.VLine)
        separadorTodos.setFrameShadow(QFrame.Raised)
        separadorTodos.setFixedSize(1, 26)

        botonTodos = QPushButton("Все записи")
        botonTodos.setObjectName("Все записи")
        botonTodos.setCursor(Qt.PointingHandCursor)
        botonTodos.setMinimumSize(60, 26)

        nombreColumnas = ("Id", "Имя", "Фамилия", "Пол", "Дата рождения", "Страна",
                          "Телефон")

        menuMostrarOcultar = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menuMostrarOcultar)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menuMostrarOcultar.addAction(accion)

        botonMostrarOcultar = QPushButton("Скрыть столбцы")
        botonMostrarOcultar.setCursor(Qt.PointingHandCursor)
        botonMostrarOcultar.setMenu(menuMostrarOcultar)
        botonMostrarOcultar.setMinimumSize(180, 26)

        disenioBuscar = QHBoxLayout()
        disenioBuscar.setSpacing(10)
        disenioBuscar.addWidget(self.buscarLineEdit)
        disenioBuscar.addWidget(botonBuscar)
        disenioBuscar.addWidget(separadorTodos)
        disenioBuscar.addWidget(botonTodos)
        disenioBuscar.addWidget(botonMostrarOcultar)

        self.tabla = QTableWidget()

        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tabla.setDragDropOverwriteMode(False)

        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        self.tabla.setTextElideMode(Qt.ElideRight)  # Qt.ElideNone

        self.tabla.setWordWrap(False)

        self.tabla.setSortingEnabled(False)

        self.tabla.setColumnCount(7)

        self.tabla.setRowCount(0)

        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                          Qt.AlignCenter)

        self.tabla.horizontalHeader().setHighlightSections(False)

        self.tabla.horizontalHeader().setStretchLastSection(True)

        self.tabla.verticalHeader().setVisible(False)

        self.tabla.setAlternatingRowColors(True)

        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # self.tabla.verticalHeader().setHighlightSections(True)

        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        for indice, ancho in enumerate((80, 240, 240, 140, 150, 130), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        # ============================================================

        disenioBuscarTabla = QVBoxLayout()
        disenioBuscarTabla.addLayout(disenioBuscar)
        disenioBuscarTabla.addWidget(self.tabla)
        disenioBuscarTabla.setSpacing(8)
        disenioBuscarTabla.setContentsMargins(10, 10, 10, 0)

        disenioDerecho = QVBoxLayout()
        disenioDerecho.addWidget(frameBienvenido)
        disenioDerecho.addLayout(disenioBuscarTabla)
        disenioDerecho.setContentsMargins(0, 0, 0, 0)

        disenioFinal = QGridLayout()
        disenioFinal.addWidget(frameBotones, 0, 0)
        disenioFinal.addLayout(disenioDerecho, 0, 1)
        disenioFinal.setSpacing(0)
        disenioFinal.setContentsMargins(0, 0, 0, 0)

        self.setLayout(disenioFinal)

        self.copiarInformacion = QApplication.clipboard()

        botonNuevo.clicked.connect(self.Nuevo)
        botonActualizar.clicked.connect(self.Actualizar)
        botonEliminar.clicked.connect(self.Eliminar)
        botonLimpiar.clicked.connect(self.limpiarTabla)

        self.buscarLineEdit.returnPressed.connect(self.Buscar)
        botonBuscar.clicked.connect(self.Buscar)
        botonTodos.clicked.connect(self.Buscar)

        botonConfiguracion.clicked.connect(lambda: Configuracion(self).exec_())

        self.tabla.itemDoubleClicked.connect(self.Suscribete)

        menuMostrarOcultar.triggered.connect(self.mostrarOcultar)

    def Nuevo(self):
        nuevoCliente(self).exec_()

    def Actualizar(self):
        fila = self.tabla.selectedItems()

        if fila:
            indice = fila[0].row()
            datos = [self.tabla.item(indice, i).text() for i in range(7)]

            actualizarCliente(indice, datos, self).exec_()
        else:
            QMessageBox.critical(self, "Обновление клиента", "Выберите клиента.   ",
                                 QMessageBox.Ok)

    def Eliminar(self):
        fila = self.tabla.selectedItems()

        if fila:
            eliminar = QMessageBox(self)

            eliminar.setWindowTitle("Удалить клиента")
            eliminar.setIcon(QMessageBox.Question)
            eliminar.setText("Вы уверены, что хотите удалить клиента?   ")
            botonSi = eliminar.addButton("Да", QMessageBox.YesRole)
            botonCancelar = eliminar.addButton("Отмена", QMessageBox.NoRole)

            eliminar.exec_()

            if eliminar.clickedButton() == botonSi:
                indiceFila = fila[0].row()
                idCliente = self.tabla.item(indiceFila, 0).text()

                if QFile.exists("DB_SIACLE/DB_SIACLE.db"):
                    conexion = sqlite3.connect("DB_SIACLE/DB_SIACLE.db")
                    cursor = conexion.cursor()

                    try:
                        cursor.execute("DELETE FROM CLIENTES WHERE ID = ?", (idCliente,))
                        conexion.commit()

                        conexion.close()

                        self.tabla.removeRow(indiceFila)
                        self.tabla.clearSelection()

                        QMessageBox.information(self, "Удалить клиента.", "Клиент удален."
                                                                          "   ", QMessageBox.Ok)
                    except:
                        conexion.close()
                        QMessageBox.critical(self, "Удалить клиента.", "Неизвестная ошибка.   ",
                                             QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Поиск клиентов", "База не найдена. "
                                                                 "datos.   ", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Удалить клиента ", "Выберите клиента.   ",
                                 QMessageBox.Ok)

    def Suscribete(self, celda):
        QMessageBox.warning(self, "", " "
                                      "\n "
                                      "   ".format(celda.text()), QMessageBox.Ok)

    def Buscar(self):
        widget = self.sender().objectName()

        if widget in ("Enter", "Поиск"):
            cliente = " ".join(self.buscarLineEdit.text().split()).lower()

            if cliente:
                sql = "SELECT * FROM CLIENTES WHERE NOMBRE LIKE ?", ("%" + cliente + "%",)
            else:
                self.buscarLineEdit.setFocus()
                return
        else:
            self.buscarLineEdit.clear()
            sql = "SELECT * FROM CLIENTES"

        if QFile.exists("DB_SIACLE/DB_SIACLE.db"):
            conexion = sqlite3.connect("DB_SIACLE/DB_SIACLE.db")
            cursor = conexion.cursor()

            try:
                if widget in ("Enter", "Поиск"):
                    cursor.execute(sql[0], sql[1])
                else:
                    cursor.execute(sql)

                datosDevueltos = cursor.fetchall()
                conexion.close()

                self.tabla.clearContents()
                self.tabla.setRowCount(0)

                if datosDevueltos:
                    fila = 0
                    for datos in datosDevueltos:
                        self.tabla.setRowCount(fila + 1)

                        idDato = QTableWidgetItem(str(datos[0]))
                        idDato.setTextAlignment(Qt.AlignCenter)

                        self.tabla.setItem(fila, 0, idDato)
                        self.tabla.setItem(fila, 1, QTableWidgetItem(datos[1]))
                        self.tabla.setItem(fila, 2, QTableWidgetItem(datos[2]))
                        self.tabla.setItem(fila, 3, QTableWidgetItem(datos[3]))
                        self.tabla.setItem(fila, 4, QTableWidgetItem(datos[4]))
                        self.tabla.setItem(fila, 5, QTableWidgetItem(datos[5]))
                        self.tabla.setItem(fila, 6, QTableWidgetItem(datos[6]))

                        fila += 1
                else:
                    QMessageBox.information(self, "Поиск клиента ", "Не найдено "
                                                                    "информации.   ", QMessageBox.Ok)
            except:
                conexion.close()
                QMessageBox.critical(self, "Поиск клиента", "Неизвестная ошибка.   ",
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Buscar clientes", "База данных не найдена.   ",
                                 QMessageBox.Ok)

        self.buscarLineEdit.setFocus()

    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)

    def limpiarTabla(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(0)

    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Скопировать все ", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Копировать поле")
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)

                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

        if accion.text() == "Скопировать все":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        self.copiarInformacion.clear(mode=QClipboard.Clipboard)
        self.copiarInformacion.setText(str(filaSeleccionada), QClipboard.Clipboard)


class Siacle(QMainWindow):
    def __init__(self, parent=None):
        super(Siacle, self).__init__(parent)

        self.setWindowIcon(QIcon("Imagenes/Qt.png"))
        self.setWindowTitle("КЛИЕНТЫ")
        self.setMinimumSize(820, 302)

        self.initUI()

    def initUI(self):

        salir = QAction(self.style().standardIcon(QStyle.SP_MessageBoxCritical), " Выйти",
                        self)
        salir.setShortcut("ESC")
        salir.triggered.connect(self.close)

        ayuda = QAction(self.style().standardIcon(QStyle.SP_MessageBoxQuestion),
                        " Помощь", self)
        ayuda.setShortcut("Ctrl+A")
        ayuda.triggered.connect(lambda: Ayuda(self).exec_())

        acercaDe = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation),
                           " Печать", self)
        acercaDe.setShortcut("Ctrl+D")
        acercaDe.triggered.connect(lambda: os.system('python visualizarImprimirExportar.py'))

        menu = self.menuBar()

        siacleMenu = menu.addMenu("&фаил")
        siacleMenu.addAction(salir)

        ayudaMenu = menu.addMenu("&информация")
        ayudaMenu.addAction(ayuda)
        ayudaMenu.addSeparator()
        ayudaMenu.addAction(acercaDe)

        self.widgets = Widgets(self)
        self.setCentralWidget(self.widgets)

        labelVersion = QLabel(self)
        labelVersion.setText("Version 1.0")

        hora = QTime.currentTime().toString("hh:mm:ss A ")

        self.labelHora = QLabel(self)
        self.labelHora.setText("Время: {}".format(hora))

        statusBar = self.statusBar()
        statusBar.addPermanentWidget(self.labelHora, 1)
        statusBar.addPermanentWidget(labelVersion, 0)

        # Actualizar la hora cada segundo (1000 milisegundos)
        self.hora = QTimer(self)
        self.hora.setInterval(1000)
        self.hora.timeout.connect(self.Hora)
        self.hora.start()

    def Hora(self):
        hora = QTime.currentTime().toString("hh:mm:ss A ")
        self.labelHora.setText("Время: {}".format(hora))

    def closeEvent(self, event):
        cerrar = QMessageBox(self)

        cerrar.setWindowTitle("Выйти")
        cerrar.setIcon(QMessageBox.Question)
        cerrar.setText("Вы уверены, что хотите выйти? ")
        botonSalir = cerrar.addButton("Да", QMessageBox.YesRole)
        botonCancelar = cerrar.addButton("Нет", QMessageBox.NoRole)

        cerrar.exec_()

        if cerrar.clickedButton() == botonSalir:
            event.accept()
        else:
            event.ignore()


# ===============================================================           

if __name__ == "__main__":
    import sys

    aplicacion = QApplication(sys.argv)

    traductor = QTranslator(aplicacion)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    aplicacion.installTranslator(traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = Siacle()
    ventana.showMaximized()

    sys.exit(aplicacion.exec_())
