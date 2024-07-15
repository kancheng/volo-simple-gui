import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QLineEdit
from PyQt5.QtCore import QProcess
import subprocess

import time
import datetime

# dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# t = time.strftime("%Y%m%d%H%M%S", time.localtime())

# print(dt)
# print(t)


class CommandExecuter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.temlbdatapath = ''
        self.temyolov8datayamlpath = ''
        self.temtargetpath = ''
 
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

        # 创建一个按钮和文本框 3 抓路徑
        self.button3 = QPushButton('抓 Labelme data - PATH', self)
        self.textbox3 = QTextEdit(self) 

        # 创建一个按钮和文本框 4 Labelme 轉換
        self.button4 = QPushButton('Labelme 轉換 to YOLOV8', self)
        self.textbox4 = QTextEdit(self)

        # YOLOV8 用預設數據與模型 SEG
        self.button5 = QPushButton('YOLOV8 用預設數據與模型 SEG Train', self)
        self.textbox5 = QTextEdit(self) 

        # YOLOV8 YAML FILE PATH
        self.button6 = QPushButton('YOLOV8 的 YAML FILE PATH', self)
        self.textbox6 = QTextEdit(self)         

        # self.le = QLineEdit(self)
        
        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.textbox)
 
        layout.addWidget(self.button2)
        layout.addWidget(self.textbox2)

        layout.addWidget(self.button3)
        layout.addWidget(self.textbox3)

        layout.addWidget(self.button4)
        layout.addWidget(self.textbox4)

        layout.addWidget(self.button5)
        layout.addWidget(self.textbox5)

        layout.addWidget(self.button6)
        layout.addWidget(self.textbox6)

        layout.addWidget(self.buttonlabelme)

        # 中央小部件
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.resize(960,700)
        self.setCentralWidget(centralWidget)
 
        # 连接按钮的点击事件
        self.button.clicked.connect(self.on_click)
 
        # 连接按钮的点击事件 2
        self.button2.clicked.connect(self.on_click_yolo)

        # 连接按钮的点击事件 3
        self.button3.clicked.connect(self.open_folder)
        
        # 连接按钮的点击事件 labelme
        self.buttonlabelme.clicked.connect(self.on_click_labelme)

        # 连接按钮的点击事件 4
        self.button4.clicked.connect(self.on_click_labelme2yolov8)

        # 连接按钮的点击事件 5
        self.button6.clicked.connect(self.open_yoloyaml_file)

        # 连接按钮的点击事件 6
        self.button5.clicked.connect(self.use_yolov8_seg_train)
        
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

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "Open folder",
                  "./")                 # start path
        print(folder_path)
        self.temlbdatapath = folder_path
        # self.textbox3.setText(folder_path)
        self.textbox3.setText(self.temlbdatapath)

    def open_yoloyaml_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                  "Open file",
                  "./")                 # start path
        print(filename, filetype)
        self.temyolov8datayamlpath = filename
        self.textbox6.setText(self.temyolov8datayamlpath)

    def on_click_labelme2yolov8(self):
    
        # 需要执行的Linux命令
        # python labelme2yolo.py --json_dir /home/XXX/ --val_size 0.2
        command = 'python labelme2yolov8.py --json_dir ' + self.temlbdatapath  + ' --val_size 0.2 --seg'  # 示例：列出当前目录下的文件和文件夹
 
        # 执行命令并获取输出
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        # 将输出显示在文本框中
        self.textbox4.setText(out.decode('utf-8') + '\n' + err.decode('utf-8'))

    # def use_yolov8_seg_train(self):
        
    #     # 需要执行的Linux命令
    #     # yolo segment train data=xxx.yaml model=yolov8n-seg.yaml epochs=100 imgsz=640
    #     command = 'cd yolov8 && yolo segment train data='+ self.temyolov8datayamlpath +' model=yolov8n-seg.yaml epochs=100 imgsz=640'  # 示例：列出当前目录下的文件和文件夹
 
    #     # 执行命令并获取输出
    #     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     out, err = process.communicate()

    #     # 将输出显示在文本框中
    #     self.textbox5.setText(out.decode('utf-8') + '\n' + err.decode('utf-8'))

    def use_yolov8_seg_train(self):
        
        # 需要执行的Linux命令
        # yolo segment train data=xxx.yaml model=yolov8n-seg.yaml epochs=100 imgsz=640
        t = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.temtargetpath = '../yolov8runs_'+t
        command = "cd yolov8 && yolo settings runs_dir='"+ self.temtargetpath +"' && pwd &&yolo segment train data="+ self.temyolov8datayamlpath + " model=yolov8n-seg.yaml epochs=100 imgsz=640"  # 示例：列出当前目录下的文件和文件夹
 
        # 执行命令并获取输出
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        # 将输出显示在文本框中
        self.textbox5.setText(out.decode('utf-8') + '\n' + err.decode('utf-8'))
def main():
    app = QApplication(sys.argv)
    ex = CommandExecuter()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
