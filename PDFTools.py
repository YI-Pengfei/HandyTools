""" PDF文件分割合并工具

    PyInstaller封装命令：
        pyinstaller --icon="baidufanyi.ico" -F PDFTools.py -w
"""
import os
import tkinter
import tkinter.filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

########################### 第一部分 ###########################################
########################## 使用PyPDF2进行分割、合并的函数 #######################
def splitPDF(inFile, outPath):
    """ 拆分PDF文件为单页 """
    if not os.path.exists(outPath):
        os.makedirs(outPath)
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
    

########################### 第二部分 ###########################################
########################## Tkinter事件 #######################
def split_TK():
    """分割 (作为Tkinter按钮的事件)"""
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
        lb.config(text='文件分割完成！')
        output1_TEXT.insert(tkinter.END,'完成，输出目录为：\n\t'+outPath+'\n') # 原文

def merge_TK():
    """合并 (作为Tkinter按钮的事件)"""
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
    if FileList and outFile:
        mergePDF(FileList,outFile.name)
        lb.config(text='文件合并完成！')
        output1_TEXT.insert(tkinter.END,'完成，输出为：\n\t'+outFile.name+'\n') # 原文

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
        show_info+='\t'+f+'\n'
    output1_TEXT.insert(0.0,show_info) # 原文

def clearFiles_TK():
    global FileList
    FileList = []
    output1_TEXT.delete(0.0,tkinter.END) # 清空文本框中的内容


FileList = []

root = tkinter.Tk()
root.geometry('400x300')
root.title('PDF合并分割工具')

lb = tkinter.Label(root,text='')
lb.pack()

add_BUTTON=tkinter.Button(root,text='添加文件\n(一次可添加多个,可多次添加)',command=addFiles_TK)
add_BUTTON.pack()
clear_BUTTON=tkinter.Button(root,text='清空待处理文件',command=addFiles_TK)
add_BUTTON.pack()

split_BUTTON=tkinter.Button(root,text='开始分割',command=split_TK)
split_BUTTON.pack()
merge_BUTTON=tkinter.Button(root,text='开始合并',command=merge_TK)
merge_BUTTON.pack()
## ========================= 布置一个显示提示信息的文本框 =======================
output1_TEXT = tkinter.Text(root)
output1_TEXT.pack() # relx=0.55, rely=0.5, relwidth=0.4, relheight=0.4

root.mainloop()