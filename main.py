import pafy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from des import *
import sys
import time
import os
import urllib.request
from urllib.error import URLError
import time

class downloader(QtCore.QThread):
	mysignal2 = QtCore.pyqtSignal(str)
	mysignal3 = QtCore.pyqtSignal(str)
	mysignal4 = QtCore.pyqtSignal(str)
	progressChanged4 = QtCore.pyqtSignal(int)
	msg = QtCore.pyqtSignal(str)
	dem = QtCore.pyqtSignal(str)
	gig = QtCore.pyqtSignal(str)
	heh = QtCore.pyqtSignal(str)
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.url = None
	def run(self):
		try:	
			video = pafy.new(self.url)
			self.mysignal2.emit(video.title)
			self.mysignal3.emit(video.bigthumb)
			self.mysignal4.emit("Статус: Загрузка началась")
			time.sleep(1)
			self.mysignal4.emit("Статус: Загрузка в прогрессе")
			best = video.getbest()
			best.download(callback=self.callback, quiet=True)
			self.gig.emit("Статус: Загрузка закончилась")
			time.sleep(5)
			self.heh.emit("Статус: Ожидание действий пользователя")
		except ValueError:
			self.msg.emit("Ссылка на видео указана не верно!")
		except OSError:
			self.msg.emit("Вы не подключены к сети интернет!")	
	def callback(self, total, recvd, ratio, rate, eta):
		val = int(ratio * 100)
		self.progressChanged4.emit(val)
	def init_args(self, url):
		self.url = url
class gui(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_fon()
		self.ui.setupUi(self)
		self.download_folder = None
		self.ui.pushButton.clicked.connect(self.get_folder)
		self.ui.pushButton_2.clicked.connect(self.start)
		self.ui.pushButton_3.clicked.connect(self.light)
		self.ui.pushButton_4.clicked.connect(self.night)
		self.mythread = downloader()
		self.mythread.msg.connect(self.func)
		self.mythread.mysignal2.connect(self.title1)
		self.mythread.mysignal3.connect(self.pb)
		self.mythread.progressChanged4.connect(self.start)
		self.mythread.dem.connect(self.boom)
		self.mythread.mysignal4.connect(self.status)
		self.mythread.gig.connect(self.funcion)
		self.mythread.heh.connect(self.ishak)
		path = 'loading.gif'
		gif = QtGui.QMovie(path)  # !!!
		self.ui.label_2.setMovie(gif)
		gif.start()
	
	def start(self, value):
		if len(self.ui.lineEdit.text()) > 5:
			if self.download_folder != None:
				link = self.ui.lineEdit.text()
				self.mythread.init_args(link)
				self.mythread.start()
				self.ui.progressBar.setValue(value)
				if value == 1:
					self.locker(True)
				elif value == 100:
					self.locker(False)	
			else:
				msg = QMessageBox()
				msg.setWindowTitle("Ошибка!")
				msg.setText("Папка не выбрана!")
				msg.setIcon(QMessageBox.Warning)
				x = msg.exec_()	
		else:
			msg = QMessageBox()
			msg.setWindowTitle("Ошибка!")
			msg.setText("Ссылка на видео не указана!")
			msg.setIcon(QMessageBox.Warning)
			x = msg.exec_()	
	
	def pb(self, str):
		url = str
		data = urllib.request.urlopen(url).read()
		image = QtGui.QPixmap()
		image.loadFromData(data)
		self.ui.label_2.setPixmap(image)
	
	def title1(self, text):
		self.ui.title1.setText("Название видео: " + str(text))
	
	def status(self, lel):
		self.ui.title1_2.setText(lel)
	
	def light(self):
		self.ui.pushButton.setStyleSheet("QPushButton{\nborder: 2px solid #c9c9c9;\nbackground-color: #a3a3a3;\ncolor: black;\n}\n\nQPushButton:hover{\nborder: 2px solid #c9c9c9;\nbackground-color: #bdbdbd;\ncolor: black;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #a3a3a3;\ncolor: black;\n}")
		self.ui.lineEdit.setStyleSheet("border: 2px solid #a8a8a8;\nbackground-color: #bdbdbd;\ncolor: black;")
		self.ui.progressBar.setStyleSheet("QProgressBar {\n    border: 2px solid grey;\n    border-radius: 5px;\n	background-color: #c7c7c7;\n}\n\nQProgressBar::chunk {\n    background-color: #e8e8e8;\n    width: 20px;\n}")
		self.ui.title1.setStyleSheet("color:000;")
		self.ui.title1_2.setStyleSheet("color: #000")
		self.setStyleSheet("""QMainWindow{
			background: #b8b8b8;
		}
		
		""")
		self.ui.pushButton_3.setStyleSheet("QPushButton{\nborder: 2px solid #c9c9c9;\nbackground-color: #a3a3a3;\ncolor: black;\n}\n\nQPushButton:hover{\nborder: 2px solid #c9c9c9;\nbackground-color: #bdbdbd;\ncolor: black;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #a3a3a3;\ncolor: black;\n}")
		self.ui.pushButton_4.setStyleSheet("QPushButton{\nborder: 2px solid #c9c9c9;\nbackground-color: #a3a3a3;\ncolor: black;\n}\n\nQPushButton:hover{\nborder: 2px solid #c9c9c9;\nbackground-color: #bdbdbd;\ncolor: black;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #a3a3a3;\ncolor: black;\n}")
		self.ui.pushButton_2.setStyleSheet("QPushButton{\nborder: 2px solid #c9c9c9;\nbackground-color: #a3a3a3;\ncolor: black;\n}\n\nQPushButton:hover{\nborder: 2px solid #c9c9c9;\nbackground-color: #bdbdbd;\ncolor: black;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #a3a3a3;\ncolor: black;\n}")
	
	def night(self):
		self.ui.pushButton_2.setStyleSheet("QPushButton{\nborder: 2px solid #666;\nbackground-color: #404040;\ncolor: white;\n}\n\nQPushButton:hover{\nborder: 2px solid #666;\nbackground-color: #3b3b3b;\ncolor: white;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #444444;\ncolor: white;\n}")
		self.ui.pushButton.setStyleSheet("QPushButton{\nborder: 2px solid #666;\nbackground-color: #404040;\ncolor: white;\n}\n\nQPushButton:hover{\nborder: 2px solid #666;\nbackground-color: #3b3b3b;\ncolor: white;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #444444;\ncolor: white;\n}")
		self.ui.pushButton_3.setStyleSheet("QPushButton{\nborder: 2px solid #666;\nbackground-color: #404040;\ncolor: white;\n}\n\nQPushButton:hover{\nborder: 2px solid #666;\nbackground-color: #3b3b3b;\ncolor: white;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #444444;\ncolor: white;\n}")
		self.ui.pushButton_4.setStyleSheet("QPushButton{\nborder: 2px solid #666;\nbackground-color: #404040;\ncolor: white;\n}\n\nQPushButton:hover{\nborder: 2px solid #666;\nbackground-color: #3b3b3b;\ncolor: white;\n}\n\nQPushButton:pressed{\nborder: 2px solid white;\nbackground-color: #444444;\ncolor: white;\n}")
		self.ui.progressBar.setStyleSheet("QProgressBar {\n    border: 2px solid grey;\n    border-radius: 5px;\n	background-color: #404040;\n}\n\nQProgressBar::chunk {\n    background-color: #292929;\n    width: 20px;\n}")
		self.ui.title1.setStyleSheet("color: #fff")
		self.ui.title1_2.setStyleSheet("color: #fff")
		self.ui.lineEdit.setStyleSheet("border: 2px solid #666;\n		background-color: #3b3b3b;\n		color: white;")
		self.setStyleSheet("background: #1a1a1a")
	
	def get_folder(self):
		self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выбрать папку для сохранения')
		try:
			os.chdir(self.download_folder)
		except:
			pass
	
	def func(self, data):
		msg = QMessageBox()
		msg.setWindowTitle("Ошибка!")
		msg.setText(str(data))
		msg.setIcon(QMessageBox.Warning)
		x = msg.exec_()
	
	def boom(self, bom):
		msg = QMessageBox()
		msg.setWindowTitle("Ошибка!")
		msg.setText(str(bom))
		msg.setIcon(QMessageBox.Warning)
		x = msg.exec_()	
	
	def locker(self, lock_value):
		base = [self.ui.pushButton, self.ui.pushButton_2]
		for item in base:
			item.setDisabled(lock_value)	
	
	def funcion(self, flotik):
		self.ui.title1_2.setText(flotik)
	
	def ishak(self, hah):
		self.ui.title1_2.setText(hah)	

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = gui()
	MainWindow.show()
	sys.exit(app.exec_())