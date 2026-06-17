import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00.00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stop Watch")
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.time_label)
        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)  # butonları da ana layout’a ekle
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setStyleSheet("""
                           
                           QPushButton, QLabel{
                               padding: 20px;
                               font-weight: bold;
                               font-family: calibri;
                           }
                           
                           QPushButton{
                               font-size: 40px;
                               color: Green;
                               background-color: Black
                               
                               
                           }
                           QLabel{
                               font-size: 120px;
                               color:red;
                               background-color: gray
                           }
                           
                           """)
         
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
        
        
         
         
         
                
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minute = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minute:02}: {seconds:02} {milliseconds:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sw = StopWatch()
    sw.show()
    sys.exit(app.exec())