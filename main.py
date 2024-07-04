import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QProcess
import subprocess
 
class CommandExecuter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        # 设置窗口的标题
        self.setWindowTitle('GUI')
 
        # Labelme
        self.buttonlabelme = QPushButton('Labelme', self)
 
        # 创建一个按钮和文本框
        self.button = QPushButton('Dir', self)
        self.textbox = QTextEdit(self)

        # 创建一个按钮和文本框 2
        self.button2 = QPushButton('YOLO', self)
        self.textbox2 = QTextEdit(self) 
        
        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.textbox)
 
        layout.addWidget(self.button2)
        layout.addWidget(self.textbox2)
         
        layout.addWidget(self.buttonlabelme)

        
        # 中央小部件
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
 
        # 连接按钮的点击事件
        self.button.clicked.connect(self.on_click)
 
        # 连接按钮的点击事件 2
        self.button2.clicked.connect(self.on_click_yolo)
        
        # 连接按钮的点击事件 labelme
        self.buttonlabelme.clicked.connect(self.on_click_labelme)
        
    def on_click_labelme(self):
        process = QProcess(self)
        process.start('labelme')
    
        # 需要执行的Linux命令
        #command = 'labelme'  # 示例：列出当前目录下的文件和文件夹
 
        # 执行命令并获取输出
        #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #out, err = process.communicate()

    def on_click(self):
        # 需要执行的Linux命令
        command = 'ls'  # 示例：列出当前目录下的文件和文件夹
 	
        # 执行命令并获取输出
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
 
        # 将输出显示在文本框中
        self.textbox.setText(out.decode('utf-8') + '\n' + err.decode('utf-8'))
        
    def on_click_yolo(self):
    
        # 需要执行的Linux命令
        command = 'cd yolov8 && echo "INFO. PATH : \n`pwd`" \c && echo "INFO. YOLOV8 : \n`yolo`"'  # 示例：列出当前目录下的文件和文件夹
 
        # 执行命令并获取输出
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        # 将输出显示在文本框中
        self.textbox2.setText(out.decode('utf-8') + '\n' + err.decode('utf-8'))
 
def main():
    app = QApplication(sys.argv)
    ex = CommandExecuter()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
