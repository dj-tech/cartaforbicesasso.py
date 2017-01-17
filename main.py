import sys
from PyQt4 import QtGui, QtCore
from random import *


class Example(QtGui.QMainWindow):
  
  def __init__(self):
    super(Example, self).__init__()
    self.initUI()
    
  def initUI(self):
    self.x = 0
    self.y = 0
    
    self.lbl = QtGui.QLabel(self)
    self.lbl1 = QtGui.QLabel(self)
    self.lbl2 = QtGui.QLabel("0",self)
    self.lbl2.move(200, 20)
    lbl3 = QtGui.QLabel('-', self)
    lbl3.move(225, 20)
    self.lbl4 = QtGui.QLabel("0",self)
    self.lbl4.move(250, 20)
    self.lbl5 = QtGui.QLabel(self)
    self.lbl5.move(200,180)
    
    self.button = QtGui.QPushButton("Gioca", self)
    self.button.move(200, 200)
    self.button.resize(self.button.sizeHint())
    self.button.clicked.connect(self.game1Active)
    
    
    game1Action = QtGui.QAction('&1 plyr vs 2 CPU', self)
    game1Action.setShortcut('Ctrl+N')
    game1Action.setStatusTip('1 vs CPU')
    game1Action.triggered.connect(self.game1Active)
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    infoAction = QtGui.QAction('&Info', self)
    infoAction.setShortcut('Ctrl+I')
    infoAction.setStatusTip('Info application')
    infoAction.triggered.connect(self.infoout)
    
    menu = QtGui.QMenuBar(self)
    game = menu.addMenu('&File')
    game.addAction(exitAction)
    game.addAction(game1Action)
    info = menu.addMenu('&Info')
    info.addAction(infoAction)
    
    
    self.setGeometry(400, 400, 500, 300)
    self.setWindowTitle("Prova")
    self.show()
    
  def infoout(self):   
    window = QtGui.QMessageBox(self)
    window.setText('< Developement by Marco Schettini and Dj-Tech>  ')
    window.icon()
    window.exec_()
    
  def game1Active(self):
    self.button.close()
    self.lbl.setPixmap(QtGui.QPixmap("nero.jpg"))
    self.lbl.resize(self.lbl.sizeHint())
    self.lbl.move(20, 80)
    self.lbl.show()
    
    self.lbl1.setPixmap(QtGui.QPixmap("nero.jpg"))
    self.lbl1.resize(self.lbl.sizeHint())
    self.lbl1.move(300, 80)
    self.lbl1.show()
    
    combo = QtGui.QComboBox(self)
    combo.addItem('sasso')
    combo.addItem('forbice')
    combo.addItem('carta')
    combo.move(30, 250)
    combo.show()
    combo.activated[str].connect(self.onActive)
  
  
  def rand(self):
    t = randint(1,3)
    if t == 1:
      t = "sasso.jpg"
    elif t == 2:
      t = "carta.jpg"
    elif t == 3:
      t = "forbice.jpg"
    return t
  
  def risult1(self, r):
    if r == 0:
      self.lbl2.setText("0")
      self.lbl2.show()
    elif r == 1:
      self.lbl2.setText("1")
      self.lbl2.show()
    elif r == 2:
      self.lbl2.setText("2")
      self.lbl2.show()
    elif r == 3:
      self.lbl2.setText("3")
      self.lbl2.show()
      
  def risult2(self, p):
    if p == 0:
      self.lbl4.setText("0")
      self.lbl4.show()
    elif p == 1:
      self.lbl4.setText("1")
      self.lbl4.show()
    elif p == 2:
      self.lbl4.setText("2")
      self.lbl4.show()
    elif p == 3:
      self.lbl4.setText("3")
      self.lbl4.show()
      
  def contr(self, text ,s): 
    if text == 'sasso' and s == 'forbice.jpg':
      self.x = self.x + 1
      self.risult1(self.x)
    elif text == 'sasso' and s == 'carta.jpg':
      self.y = self.y + 1
      self.risult2(self.y)
    elif text == 'forbice' and s == 'carta.jpg':
      self.x = self.x + 1
      self.risult1(self.x)
    elif text == 'carta' and s == 'sasso.jpg':
      self.x = self.x + 1
      self.risult1(self.x)
    elif text == 'forbice' and s == 'sasso.jpg':
      self.y = self.y + 1
      self.risult2(self.y)
    elif text == 'carta' and s == 'forbice.jpg':
      self.y = self.y + 1
      self.risult2(self.y)
      
  
  def onActive(self, text):
    s = self.rand()
    self.lbl1.setPixmap(QtGui.QPixmap(s))
    if text == 'sasso':
      self.lbl.setPixmap(QtGui.QPixmap("sasso.jpg"))

    elif text == 'forbice':
      self.lbl.setPixmap(QtGui.QPixmap("forbice.jpg"))
      
    elif text == 'carta':
      self.lbl.setPixmap(QtGui.QPixmap("carta.jpg"))
    self.contr(text, s)
    if self.x == 3:
      mess = QtGui.QMessageBox(self)
      mess.setText("Il Giocatore uno ha vinto")
      mess.show()
      self.x = 0
      self.y = 0
      self.lbl2.setText("0")
      self.lbl4.setText("0")
    elif self.y == 3:
      mess = QtGui.QMessageBox(self)
      mess.setText("La CPU ha vinto")
      mess.show()
      self.x = 0
      self.y = 0
      self.lbl2.setText("0")
      self.lbl4.setText("0")
    
      
    
    
def main():
  
  app = QtGui.QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
  
if __name__ == '__main__':
  main()
