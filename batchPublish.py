import subprocess
import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()


widget.setGeometry(300, 100, 500, 700)
widget.setWindowTitle('Batch Publish')
layout = QtGui.QHBoxLayout()
save_button = QtGui.QPushButton("Publish selected")
layout.addWidget(save_button)
widget.setLayout(layout)

publish_all = QtGui.QPushButton("Publish All")
layout.addWidget(publish_all)
widget.setLayout(layout)

system = [getSystem];

len = len(system)
cb = []
a = 0

for i in system:
    cb.append(QtGui.QCheckBox(i, widget))
    a = a + 1;


a = 0
for i in system:
    cb[a].move(10, 20*a)
    a = a + 1

array = {}

def hello():
    for i in range(0,len):
        if cb[i].isChecked():
            pass
def publish():
    for i in range(0,len):
        if cb[i].isChecked():
            filepath="C:/Release.bat"
            input = system[i]
            print(system[i])
            p = subprocess.call([filepath,input])

save_button.clicked.connect(publish)

def publishall():
    reply = QtGui.QMessageBox.question(widget, 'Message',"Are you sure to Publish all?", QtGui.QMessageBox.Yes |QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
        print("Publishing all")
        for i in range(0,len):
            filepath="C:/Release.bat"
            input = system[i]
            print(system[i])
            p = subprocess.call([filepath,input])
    else:
        print("Nothing is published")

publish_all.clicked.connect(publishall)

for i in range(0,len):
    widget.connect(cb[i], QtCore.SIGNAL('stateChanged(int)'), hello)

widget.show()
sys.exit(app.exec_())


