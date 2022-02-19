__versión__ = "1.0"

from sqlite3 import connect
import pandas as pd

from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtCore import Qt, QFileInfo, QTextCodec, QByteArray, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QTreeWidget, QTreeWidgetItem, QDialog, QPushButton, QFileDialog,
                             QMessageBox, QToolBar)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog


class visualizarImprimirExportar(QDialog):
    def __init__(self, parent=None):
        super(visualizarImprimirExportar, self).__init__()

        self.setWindowTitle("Просмотр, печать и экспорт данных в PDF")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(612, 408)

        self.initUI()

    def initUI(self):
        self.documento = QTextDocument()

        buttonBuscar = QPushButton("Найти пользователей", self)
        buttonBuscar.setFixedSize(426, 26)
        buttonBuscar.move(20, 20)

        buttonLimpiar = QPushButton("Очистить", self)
        buttonLimpiar.setFixedSize(140, 26)
        buttonLimpiar.move(452, 20)

        self.treeWidgetUsuarios = QTreeWidget(self)

        self.treeWidgetUsuarios.setFont(QFont(self.treeWidgetUsuarios.font().family(), 10, False))
        self.treeWidgetUsuarios.setRootIsDecorated(False)
        self.treeWidgetUsuarios.setHeaderLabels(("Id", "Имя", "Фамилия", "Пол", "Дата рождения", "Страна",
                                                 "Телефон"))

        self.model = self.treeWidgetUsuarios.model()

        for indice, ancho in enumerate((110, 150, 150, 160), start=0):
            self.model.setHeaderData(indice, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
            self.treeWidgetUsuarios.setColumnWidth(indice, ancho)

        self.treeWidgetUsuarios.setAlternatingRowColors(True)

        self.treeWidgetUsuarios.setFixedSize(572, 300)
        self.treeWidgetUsuarios.move(20, 56)

        buttonVistaPrevia = QPushButton("предварительный просмотр", self)
        buttonVistaPrevia.setFixedSize(180, 26)
        buttonVistaPrevia.move(116, 364)

        buttonImprimir = QPushButton("печать", self)
        buttonImprimir.setFixedSize(140, 26)
        buttonImprimir.move(304, 364)

        buttonExportarPDF = QPushButton("Экспорт в EXEL", self)
        buttonExportarPDF.setFixedSize(140, 26)
        buttonExportarPDF.move(452, 364)

        buttonBuscar.clicked.connect(self.Buscar)
        buttonLimpiar.clicked.connect(self.limpiarTabla)

        buttonVistaPrevia.clicked.connect(self.vistaPrevia)
        buttonImprimir.clicked.connect(self.Imprimir)
        buttonExportarPDF.clicked.connect(self.exportarPDF)

    def Buscar(self):
        conexionDB = connect("DB_SIACLE/DB_SIACLE.db")
        cursor = conexionDB.cursor()

        cursor.execute("SELECT NOMBRE, APELLIDO, SEXO, FECHA_NACIMIENTO, PAIS, TELEFONO_CELULAR FROM CLIENTES ")
        datosDB = cursor.fetchall()

        conexionDB.close()

        if datosDB:
            self.documento.clear()
            self.treeWidgetUsuarios.clear()

            datos = ""
            item_widget = []
            for dato in datosDB:
                datos += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % dato
                item_widget.append(QTreeWidgetItem((str(dato[0]), dato[1], dato[2], dato[3], dato[4], dato[5])))

            reporteHtml = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
h3 {
    font-family: Helvetica-Bold;
    text-align: center;
   }

table {
       font-family: arial, sans-serif;
       border-collapse: collapse;
       width: 100%;
      }

td {
    text-align: left;
    padding-top: 4px;
    padding-right: 6px;
    padding-bottom: 2px;
    padding-left: 6px;
   }

th {
    text-align: left;
    padding: 4px;
    background-color: black;
    color: white;
   }

tr:nth-child(even) {
                    background-color: #dddddd;
                   }
</style>
</head>
<body>

<h3>Клиенты<br/></h3>

<table align="left" width="100%" cellspacing="0">
  <tr>
    <th>Имя</th>
    <th>Фамилия</th>
    <th>Пол</th>
    <th>Дата рождения</th>
    <th>Страна</th>
    <th>Телефон</th>
  </tr>
  [DATOS]
</table>

</body>
</html>
""".replace("[DATOS]", datos)

            datos = QByteArray()
            datos.append(str(reporteHtml))
            codec = QTextCodec.codecForHtml(datos)
            unistr = codec.toUnicode(datos)

            if Qt.mightBeRichText(unistr):
                self.documento.setHtml(unistr)
            else:
                self.documento.setPlainText(unistr)

            self.treeWidgetUsuarios.addTopLevelItems(item_widget)
        else:
            QMessageBox.information(self, "Найти пользователей", "Результатов не найдено.      ",
                                    QMessageBox.Ok)

    def limpiarTabla(self):
        self.documento.clear()
        self.treeWidgetUsuarios.clear()

    def vistaPrevia(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)

            vista = QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("предварительный просмотр")
            vista.setWindowFlags(Qt.Window)
            vista.resize(800, 600)

            exportarPDF = vista.findChildren(QToolBar)
            exportarPDF[0].addAction(QIcon("exportarPDF.png"), "Экспорт в PDF", self.exportarPDF)

            vista.paintRequested.connect(self.vistaPreviaImpresion)
            vista.exec_()
        else:
            QMessageBox.critical(self, "предварительный просмотр", "Нет данных для отображения.   ",
                                 QMessageBox.Ok)

    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def Imprimir(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)

            dlg = QPrintDialog(impresion, self)
            dlg.setWindowTitle("Распечатать документ")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.documento.print_(impresion)

            del dlg
        else:
            QMessageBox.critical(self, "печать", "Нет данных для печати.   ",
                                 QMessageBox.Ok)

    def exportarPDF(self):
        if not self.documento.isEmpty():
            nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Экспорт в EXEL", "Список пользователей ",
                                                           "EXEL файлы  (*.xlsx);;All Files (*)",
                                                           options=QFileDialog.Options())
            conexionDB = connect("DB_SIACLE/DB_SIACLE.db")
            data = pd.read_sql(
                'SELECT * FROM CLIENTES',
                conexionDB)
            conexionDB.close()

            if nombreArchivo:
                # impresion = QPrinter(QPrinter.HighResolution)
                # impresion.setOutputFormat(QPrinter.PdfFormat)
                # impresion.setOutputFileName(nombreArchivo)
                # self.documento.print_(impresion)
                # print(nombreArchivo)
                data.to_excel(f'{nombreArchivo}.xlsx')

                QMessageBox.information(self, "Экспорт в EXEL", "Данные успешно экспортированы.   ",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Экспорт в EXEL", "Нет данных для экспорта.   ",
                                 QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    aplicacion = QApplication(sys.argv)

    qt_traductor = QTranslator()
    qt_traductor.load("qtbase_" + QLocale.system().name(),
                      QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    aplicacion.installTranslator(qt_traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Times new roman")

    aplicacion.setFont(fuente)

    ventana = visualizarImprimirExportar()
    ventana.show()

    sys.exit(aplicacion.exec_())
