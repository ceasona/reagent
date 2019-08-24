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


headers={
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
     "Accept": "*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
     "Cache-Control": "no-cache",
     "Connection": "akeep-alive"
 }
def spiderData(reagent, Nowrow):
    import urllib.request
    import random

    url = 'https://www.chemicalbook.com/Search.aspx?keyword=' + reagent


    # iplist = ['219.223.251.173:3128', '203.174.112.13:3128', '122.72.18.34:80']
    # # 创建一个代理opener
    # proxy_support = urllib.request.ProxyHandler({'http': iplist[random.randint(0, len(iplist))]})
    # opener = urllib.request.build_opener(proxy_support)
    #
    # # 添加浏览器的伪装头部
    # opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0')]
    #
    #
    # response = opener.open(url)
    #
    # a = response.read().decode('utf-8')
    # print(a)

    data = requests.get(url,headers=headers)
    time.sleep(3)
    a = data.text
    # with open("we.html", "w") as f:
    #     f.write(a)
    soup = BeautifulSoup(a, 'lxml')
    print(soup.select('td[align="right"] + td'))
    if soup.select('td[align="right"] + td'):
        allContent = soup.select('td[align="right"] + td')
        arry = []
        window.label.setText("正在获取第" + str(Nowrow+1) + "行数据")
        for i in range(6):
            m = allContent[i].get_text()
            arry.append(m)
        print(arry,flush=True)
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
