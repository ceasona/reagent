from PyQt5.Qt import *
from resource.control import Ui_Form
import requests
import xlrd
import xlwt
from bs4 import BeautifulSoup
import sys
import io
import re
import os
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

class ControlPane(QWidget,Ui_Form):

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.outName2 = "outFile.xls"

    def openCsv(self):
        url = QFileDialog.getOpenFileUrls()[0]
        if url:
            filenames = [item.toLocalFile().split('/')[-1] for item in url][0]
            global InfilPath
            InfilPath = url[0].toLocalFile()
            global OutfilPath
            outName1 = re.findall(r'.+\/', InfilPath)[0]
            OutfilPath =outName1 +"outputFile.xls"
            if os.path.exists(OutfilPath):
                self.outName2 = "outputFile"+str(round(time.time()))[-5:]+".xls"
                OutfilPath = outName1 + self.outName2
            if InfilPath.__contains__('.xls'):
                global writeSheet
                global writebook
                writebook = xlwt.Workbook()
                writeSheet = writebook.add_sheet('Reagent')
                downThread = Download_thread(self)
                downThread.start()
                self.label.setText("正在下载，请耐心等待......")
                self.pushButton.setEnabled(False)
                downThread.signal.connect(finish)
            else:
                self.label.setText("请导入格式正确的文件.")
        else:
            pass



class Download_thread(QThread):
    signal = pyqtSignal()
    def run(self):
        start(InfilPath,OutfilPath)
        self.signal.emit()
def finish():
    window.label.setText("导出成功--"+ window.outName2)
    window.pushButton.setEnabled(True)
def start(InfilPath,OutfilPath):
    readbook = xlrd.open_workbook(InfilPath)
    readSheet = readbook.sheet_by_index(0)
    nrows = readSheet.nrows

    for i in range(nrows):
        reagent = readSheet.cell(i, 0).value
        spiderData(reagent, i)
    writebook.save(OutfilPath)

session = requests.session()
def spiderData(reagent, Nowrow):
    url = 'https://www.energy-chemical.com/search.html?key=' + reagent
    headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
     "Accept": "*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
     "Cache-Control": "no-cache",
     "Connection": "akeep-alive"
    }

    data = session.get(url=url,headers=headers)
    a = data.text
    soup = BeautifulSoup(a, 'lxml')
    allContent = soup.select('tbody > tr >td')
    if allContent:
        name_Chinese = re.findall("(.+)\(订货以英文名称为准\)", allContent[2].get_text())[0]
        name_English = re.findall("(.+)\(订货以英文名称为准\)", allContent[4].get_text())[0]
        arry = [name_Chinese, name_English, allContent[6].get_text(), allContent[10].get_text(),
                allContent[12].get_text()]
        window.label.setText("正在获取第" + str(Nowrow+1) + "行数据")
        writeDate(arry, Nowrow)
    else:
        if reagent:
            window.label.setText("第"+str(Nowrow+1)+"行查不到")
        else:
            window.label.setText("第" + str(Nowrow+1) + "行值为空")


def writeDate(arry, Nowrow):

    for clo, content in zip(range(2, 9), arry):
        writeSheet.write(Nowrow, clo, content)

if  __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = ControlPane()
    window.setWindowTitle("Reagent Data")
    window.show()
    sys.exit(app.exec())
