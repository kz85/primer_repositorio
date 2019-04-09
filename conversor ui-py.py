import os
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QDialog, QFileSystemModel, QMessageBox
from PyQt5.QtGui import QIcon
from gui import InterfazGrafica  # Importo mi diseño gráfico desde la carpeta gui

app = QApplication(sys.argv)
gui = InterfazGrafica.Ui_Dialog()  # Crea un nuevo objeto de interfaz gráfica
ventana = QDialog()  # Crea un nuevo objeto del tipo ventana
gui.setupUi(ventana)  # Carga la configuracion de los elementos gráficos en la ventana

icono_de_ventana = QIcon("engrane32px.png")

ventana.setWindowTitle("Conversor .ui a .py")
ventana.setWindowIcon(icono_de_ventana)

path_a_mostrar = QDir.homePath()  # Acá elijo la ruta sobre la que voy a trabajar


def carpeta_cargada():
    numColumns = model.columnCount(model.index(path_a_mostrar))
    numRows = model.rowCount(model.index(path_a_mostrar))
    print("Filas: " + str(numRows) + "\n" + "Columnas: " + str(numColumns))

    print("\n")

    print("Listando archivos en: " + path_a_mostrar)

    for row in range(numRows):
        index = model.index(row, 0, model.index(path_a_mostrar))
        text = model.data(index, 0)  # El 0 corresponde a DisplayRole: The key data to be rendered in the form of text.
        print(text)


def cambio_de_seleccion():
    index = gui.treeView.currentIndex() # IMPORTANTE devuelve el index del dato sobre el que hago click ya sea nombre tamaño o fecha
    path = model.filePath(index)    # Si importar lo de la aclaracion anterior me devuelve el path al archivo correspondiente a la fila done se hizo click
    nombre = model.fileName(index)
    text = model.data(index, 0)  # text y nombre me dan exactamente lo mismo. Con extension de archivo incluida


def convertir():
    index = gui.treeView.currentIndex()  # Obtengo el index del item actual seleccionado en la vista en arbol
    source_path = model.filePath(index)  # Obtengo la ruta del item seleccionado, incluye nombre de archivo con extension

    nombre_de_archivo_origen = model.fileName(index)  # Obtengo el nombre del item seleccionado incluida la extension

    extension = nombre_de_archivo_origen[len(nombre_de_archivo_origen)-2:]  # Leo desde los 2 ultimos caracteres hasta el final del nombre, osea la extension

    if extension == "ui":
        nombre_de_archivo_destino = nombre_de_archivo_origen.replace(".ui", ".py")  #  genero el nombre del archivo de salida cambiando la extension a .py

        destination_path = source_path.replace(nombre_de_archivo_origen, nombre_de_archivo_destino)

        os.system('python -m PyQt5.uic.pyuic -x "' + source_path + '" -o "' + destination_path + '"')
    else:
        mensaje = QMessageBox()  # Creo un nuevo objeto mensaje emergente
        mensaje.setWindowTitle("Error")
        mensaje.setText("Solo se pueden convertir archivos con extension .ui")
        mensaje.exec_()

# Model/View Programming

"""# The Model is the application object, the View is its screen presentation, and the Controller defines the way the user interface reacts to user input."""

"""""""#QAbstractitemModel class defines an interface that is used by views and delegates to access data."""

"""""""#QFileSystemModel provides information about files and directories in the local filing system."""
model = QFileSystemModel()  #los models son interfaces para poder mostrar los datos con cierta organizacion
# model.directoryLoaded.connect(lambda: carpeta_cargada())  #cuando se emita la señal de directorio cargado llama a la funcion carpeta_cargada()
model.setRootPath(path_a_mostrar)  #Sets the directory that is being watched by the model
name_filters = ["a*", "b*", "c*", "d*", "e*", "f*", "g*", "h*", "i*", "j*", "k*", "l*", "m*", "n*", "ñ*", "o*", "p*", "q*", "r*", "s*", "t*", "u*", "v*", "w*", "x*", "y*", "z*"]
model.setNameFilters(name_filters)  # Setea los filtros para nombres de archivos y carpetas a una lista de strings que son los filtros
model.setNameFilterDisables(False)  # Poner False hace que no aparesca lo que no coincide con los filtros
model.setFilter(QDir.Files | QDir.NoDotAndDotDot | QDir.Dirs)



"""#QtreeView implementa la representacion en arbol de los elementos de un modelo"""

gui.treeView.setModel(model)  # aplica el modelo establecido a la vista en arbol
gui.treeView.setRootIndex(model.index(path_a_mostrar))  # setea que directorio se va a mostrar
gui.treeView.setColumnWidth(0, 180)  # ensancha la columna nombre

# gui.treeView.clicked.connect(lambda: cambio_de_seleccion())

gui.pushButton.clicked.connect(lambda: convertir())

ventana.show()

sys.exit(app.exec_())
