""" PDF文件分割合并工具
    需安装PyPDF2: pip install PyPDF2
    PyInstaller封装命令：
        pyinstaller --icon="baidufanyi.ico" -F PDFTools.py -w
"""
import os
import re
import tkinter
import tkinter.filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

########################### 第一部分 ###########################################
########################## 使用PyPDF2进行分割、合并的函数 #######################
def splitPDF(inFile, outPath):
    """ 拆分PDF文件为单页
    """
#    if not os.path.exists(outPath):
#        os.makedirs(outPath)
    f = open(inFile, 'rb') # 二进制方式打开文档
    reader = PdfFileReader(f)
    numPages = reader.getNumPages()  #计算此PDF文件中的页数
    for i in range(numPages):
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(i))
        outFile = os.path.join(outPath, str(i+1)+'.pdf') # 组合文件输出路径
        with open(outFile, 'wb') as outf:
            writer.write(outf)
    f.close()

def mergePDF(inFileList,outFile):
    """ 合并inFileList中的文件为一个PDF文件 """
    pdfMerger = PdfFileMerger() # pdf文件合并对象
    for infile in inFileList: #逐个添加pdf
        pdfMerger.append(open(infile,'rb'))
    
    with open(outFile,'wb') as f: #将内存中合并的pdf文件写入
        pdfMerger.write(f)

def extractPDF(inFile, outFile, pages):
    """ 提取特定页，组成一个新的PDF文件
        pages: 列表型 如：[1] 将提取第1页
                         [1,2,3] 将提取 1-3页 
                         [3,5,7] 将提取3,5,7页
    """
    pages = sorted(pages) # 顺序永远是由小到大
    f = open(inFile, 'rb') # 二进制方式打开文档
    reader = PdfFileReader(f)
    writer = PdfFileWriter()
    numPages = reader.getNumPages()  #计算此PDF文件中的页数
    for i in range(numPages):
        if i+1 in pages:
            writer.addPage(reader.getPage(i))

    with open(outFile, 'wb') as outf:
        writer.write(outf)
    f.close()

########################### 第二部分 ###########################################
########################## Tkinter事件 ########################################
FileList = [] # 全局变量，存放要处理的文件

def addFiles_TK():
    """ 添加待处理的文件 """
    global FileList
    tempFileList=tkinter.filedialog.askopenfilenames(filetypes=[('pdf文件', '*.pdf')])
    if not tempFileList:
        output1_TEXT.insert(tkinter.END,'请继续添加文件，或开始处理..\n') # 原文
        return
    FileList+=tempFileList
    
    output1_TEXT.delete(0.0,tkinter.END) # 清空文本框中的内容
    show_info = "待处理文件为(将按此顺序合并文档)：\n"
    for f in FileList:
        show_info+='  '+f+'\n'
    output1_TEXT.insert(0.0,show_info) # 原文
    info_LABEL.config(text='请继续添加文件，或开始处理..')

def clearFiles_TK():
    """清空文件列表，清空提示信息"""
    global FileList
    FileList = []
    output1_TEXT.delete(0.0,tkinter.END) # 清空文本框中的内容
    
    
def split_TK():
    """分割 (Tkinter按钮的事件)"""
    # 根据条件输出提示信息 
    global FileList
    if len(FileList)==0:
        output1_TEXT.insert(tkinter.END, '无待处理文件！请添加\n') # 原文
        return
    elif len(FileList)>1:
        output1_TEXT.insert(tkinter.END, '添加文档多于一个，将只处理第一个文档！\n')
        
    inFile = FileList[0]
    outPath = tkinter.filedialog.askdirectory(title='选择输出目录') # 文件夹选择对话框
    if inFile and outPath:
        splitPDF(inFile, outPath)
        info_LABEL.config(text='文件分割完成！')
        output1_TEXT.insert(tkinter.END,'完成，输出目录为：\n  '+outPath+'\n') # 原文

def merge_TK():
    """合并 (Tkinter按钮的事件)"""
    global FileList
    if len(FileList)==0:
        output1_TEXT.insert(tkinter.END, '无待处理文件！请添加\n') # 原文
        return
    else:
        output1_TEXT.insert(tkinter.END, '将按此顺序合并文档\n')
        
    options={'defaultextension':'.pdf',
             'filetypes':[('任意类型', '.*'),('pdf文件', '.pdf')],
             'initialfile':'temp.pdf',
             'title':'合并为',
             'parent':root}  
    outFile = tkinter.filedialog.asksaveasfile(mode='w',**options)  # 保存
    if outFile:
        mergePDF(FileList,outFile.name)
        info_LABEL.config(text='文件合并完成！')
        output1_TEXT.insert(tkinter.END,'完成，输出为：\n  '+outFile.name+'\n') # 原文


def extract_TK():
    """提取指定页 (Tkinter按钮的事件)
       弹出子窗体，输入要提取的页的页码
    """
    # 根据条件输出提示信息 
    global FileList
    if len(FileList)==0:
        output1_TEXT.insert(tkinter.END, '无待处理文件！请添加\n') # 原文
        return
    elif len(FileList)>1:
        output1_TEXT.insert(tkinter.END, '添加文档多于一个，将只处理第一个文档！\n')
    inFile = FileList[0]

    def input_Pages():
        """ 输入想要提取的页码，并开始提取"""
        pages_str=in_TEXT.get(0.0,tkinter.END)
        pages = re.findall(r'\d+-\d+',pages_str) # 输入格式为 3-7的情况，
        if pages: 
            pages = [int(i) for i in pages[0].split('-')]
            pages = [i for i in range(pages[0],pages[1]+1)] # 补全列表为 [3,4,5,6,7]
        else:# 输入格式为 1 或 1,5,7 的情况
            pages = re.findall(r'\d+',pages_str)
            pages = [int(i) for i in pages]
        if not pages:
            subinfo_LABEL.config(text='尚未输入或格式有误，请重新输入！')
            return
        
        winSub.destroy() # 销毁子窗体
        options={'defaultextension':'.pdf',
                 'filetypes':[('任意类型', '.*'),('pdf文件', '.pdf')],
                 'initialfile':'out.pdf',
                 'title':'保存为',
                 'parent':root}  
        outFile = tkinter.filedialog.asksaveasfile(mode='w',**options)  # outFile是一个对象
        if outFile:
            extractPDF(inFile, outFile.name, pages)
            info_LABEL.config(text='文件提取完成！')
            output1_TEXT.insert(tkinter.END,'完成，输出为：\n  '+outFile.name+'\n') # 原文
    
    ## 弹出新窗体，继续接收想要提取的页
    winSub = tkinter.Toplevel(root)  
    winSub.geometry('440x240')
    winSub.title('PDF提取')
    subinfo_LABEL = tkinter.Label(winSub,
                                  text='提取一页或多页保存为一个单独的文件：\n1.提取单个页面： 如 输入 1，则提取第1页\n2.提取多页连续： 如 输入 3-7，则提取3,4,5,6,7页\n3.提取多页不连续： 如 输入 3,5,7，则提取3,5,7页\n',
                                  justify=tkinter.LEFT) # # 字符串进行左对齐
    subinfo_LABEL.place(relx=0.05,rely=0.05, relwidth=0.9, relheight=0.8)

    in_TEXT = tkinter.Text(winSub)
    in_TEXT.place(relx=0.15, rely=0.8, relwidth=0.4, relheight=0.15)
    confirm_BUTTON=tkinter.Button(winSub,text='输入页码并确认',command=input_Pages)
    confirm_BUTTON.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.15)


########################### 第三部分 ###########################################
########################## 窗体 ########################################
root = tkinter.Tk()
root.geometry('800x400')
root.title('PDF合并分割工具')
#  一个显示信息的Label
info_LABEL = tkinter.Label(root,text='等待添加文件',justify=tkinter.LEFT,fg='red')
info_LABEL.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.1)

## ======================= 布置添加文件、清空文件的按钮 =========================
add_BUTTON=tkinter.Button(root,text='添加文件\n(一次可添加多个,\n可多次添加)',command=addFiles_TK)
add_BUTTON.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
clear_BUTTON=tkinter.Button(root,text='清空文件',command=clearFiles_TK)
clear_BUTTON.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.1)

## ======================= 布置 分割、提取、合并 的按钮 =========================
split_BUTTON=tkinter.Button(root,text='分割成单页',command=split_TK)  # 分割按钮
split_BUTTON.place(relx=0.65, rely=0.1, relwidth=0.2, relheight=0.1)
extract_BUTTON=tkinter.Button(root,text='提取指定页',command=extract_TK)  # 提取按钮
extract_BUTTON.place(relx=0.65, rely=0.225, relwidth=0.2, relheight=0.1)
merge_BUTTON=tkinter.Button(root,text='合并多个PDF',command=merge_TK)  # 合并按钮
merge_BUTTON.place(relx=0.65, rely=0.35, relwidth=0.2, relheight=0.1)
## ========================= 布置一个显示提示信息的文本框 =======================
output1_TEXT = tkinter.Text(root)
output1_TEXT.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4) # relx=0.55, rely=0.5, relwidth=0.4, relheight=0.4

root.mainloop()