# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:59:54 2020
pyinstaller -F -w -i icom_256.ico IEEE缩写替换.py
@author: y1064
"""
import tkinter
import tkinter.filedialog

#f = open('IEEE期刊缩写.txt')
#lines = f.readlines()
#abbr = {}
#for line in lines:
#    k,v = line.split('=')
#    abbr[k.strip()]=v.strip()
#f.close()

# 缩写字典
abbr = {'Communications Surveys and Tutorials': 'Commun. Surveys Tuts.',
        '{IEEE} Communications Surveys and Tutorials': '{IEEE} Commun. Surveys Tuts.',
        'IEEE Communications Surveys   Tutorials': '{IEEE} Commun. Surveys Tuts.',
 'Internet Computing': 'Internet Comput.',
 'Journal of Display Technology': 'J. Display Technol.',
 'Journal of Lightwave Technology': 'J. Lightw. Technol.',
 'Journal of Microelectromechanical Systems': 'J. Microelectromech. Syst.',
 'Pervasive Computing': 'Pervasive Comput.',
 'Proceedings of the {IEEE}': 'Proc. {IEEE}',
 "Today's Engineer": "Today's Eng.",
 'Wireless Communications': 'Wireless Commun.',
 '{IEEE/ACM} Transactions on Networking': '{IEEE/ACM} Trans. Networking',
 '{IEEE/ASME} Journal of Microelectromechanical Systems': 'J. Microelectromech. Syst.',
 '{IEEE/ASME} Transactions on Mechatronics': '{IEEE/ASME} Trans. Mechatron.',
 '{IEEE/OSA} Journal of Lightwave Technology': 'J. Lightwave Technol.',
 '{IEEE} ASSP Magazine': '{IEEE} ASSP Mag.',
 '{IEEE} Aerospace and Electronics Systems Magazine': '{IEEE} Aerosp. Electron. Syst. Mag.',
 '{IEEE} Annals of the History of Computing': '{IEEE} Annals Hist. Comput.',
 '{IEEE} Antennas and Propagation Magazine': '{IEEE} Antennas Propagat. Mag.',
 '{IEEE} Antennas and Wireless Propagation Letters': '{IEEE} Antennas Wireless Propagat. Lett.',
 '{IEEE} Circuits and Devices Magazine': '{IEEE} Circuits Devices Mag.',
 '{IEEE} Circuits and Systems Magazine': '{IEEE} Circuits Syst. Mag.',
 '{IEEE} Communications Letters': '{IEEE} Commun. Lett.',
 '{IEEE} Communications Magazine': '{IEEE} Commun. Mag.',
 '{IEEE} Communications Society Magazine': '{IEEE} Commun. Soc. Mag.',
 '{IEEE} Computational Science and Engineering Magazine': '{IEEE} Comput. Sci. Eng. Mag.',
 '{IEEE} Computer': '{IEEE} Computer',
 '{IEEE} Computer Applications in Power': '{IEEE} Comput. Appl. Power',
 '{IEEE} Computer Architecture Letters': '{IEEE} Comput.Archit. Lett.',
 '{IEEE} Computer Graphics and Applications': '{IEEE} Comput. Graph. Appl.',
 '{IEEE} Computing in Science and Engineering': '{IEEE} Comput. Sci. Eng.',
 '{IEEE} Concurrency': '{IEEE} Concurrency',
 '{IEEE} Control Systems Magazine': '{IEEE} Control Syst. Mag.',
 '{IEEE} Design and Test of Computers': '{IEEE} Des. Test. Comput.',
 '{IEEE} Electrical Insulation Magazine': '{IEEE} Electr. Insul. Mag.',
 '{IEEE} Electron Device Letters': '{IEEE} Electron Device Lett.',
 '{IEEE} Engineering Management Review': '{IEEE} Eng. Manag. Rev.',
 '{IEEE} Engineering in Medicine and Biology Magazine': '{IEEE} Eng. Med. Biol. Mag.',
 '{IEEE} Expert': '{IEEE} Expert',
 '{IEEE} Geoscience and Remote Sensing Letters': '{IEEE} Geosci. Remote Sens. Lett.',
 '{IEEE} IT Professional': '{IEEE} IT Prof.',
 '{IEEE} Industry Applications Magazine': '{IEEE} Ind. Appl. Mag.',
 '{IEEE} Instrumentation and Measurement Magazine': '{IEEE} Instrum. Meas. Mag.',
 '{IEEE} Intelligent Systems': '{IEEE} Intell. Syst.',
 '{IEEE} Internet Computing': '{IEEE} Internet Comput.',
 '{IEEE} Journal of Oceanic Engineering': '{IEEE} J. Oceanic Eng.',
 '{IEEE} Journal of Quantum Electronics': '{IEEE} J. Quantum Electron.',
 '{IEEE} Journal of Robotics and Automation': '{IEEE} J. Robot. Automat.',
 '{IEEE} Journal of Selected Topics in Quantum Electronics': '{IEEE} J. Select. Topics Quantum Electron.',
 '{IEEE} Journal of Selected Topics in Signal Processing': '{IEEE} J. Sel. Top. Sign. Proces.',
 '{IEEE} Journal of Solid-State Circuits': '{IEEE} J. Solid-State Circuits',
 '{IEEE} Journal on Selected Areas in Communications': '{IEEE} J. Select. Areas Commun.',
 '{IEEE} Journal on Technology in Computer Aided Design': '{IEEE} J. Technol. Computer Aided Design',
 '{IEEE} Micro': '{IEEE} Micro',
 '{IEEE} Microwave Magazine': '{IEEE} Microwave',
 '{IEEE} Microwave and Guided Wave Letters': '{IEEE} Microwave Guided Wave Lett.',
 '{IEEE} Microwave and Wireless Components Letters': '{IEEE} Microwave Wireless Compon. Lett.',
 '{IEEE} Multimedia': '{IEEE} Multimedia',
 '{IEEE} Network': '{IEEE} Network',
 '{IEEE} Personal Communications': '{IEEE} Pers. Commun.',
 '{IEEE} Personal Communications Magazine': '{IEEE} Personal Commun. Mag.',
 '{IEEE} Photonics Technology Letters': '{IEEE} Photon. Technol. Lett.',
 '{IEEE} Potentials': '{IEEE} Potentials',
 '{IEEE} Power Electronics Letters': '{IEEE} Power Electron Lett.',
 '{IEEE} Power Engineering Review': '{IEEE} Power Eng. Rev.',
 '{IEEE} Power and Energy Magazine': '{IEEE} Power Energy Mag.',
 '{IEEE} Robotics and Automation Magazine': '{IEEE} Robot. Automat. Mag.',
 '{IEEE} Security and Privacy': '{IEEE} Security Privacy',
 '{IEEE} Sensors Journal': '{IEEE} Sensors J.',
 '{IEEE} Signal Processing Letters': '{IEEE} Signal Processing Lett.',
 '{IEEE} Signal Processing Magazine': '{IEEE} Signal Processing Mag.',
 '{IEEE} Software': '{IEEE} Softw.',
 '{IEEE} Spectrum': '{IEEE} Spectr.',
 '{IEEE} Technology and Society Magazine': '{IEEE} Technol. Soc. Mag.',
 '{IEEE} Transactions On Dielectrics and Electrical Insulation': '{IEEE} Trans. Dielectr. Electr. Insul.',
 '{IEEE} Transactions On Systems, Man, and Cybernetics-Part A: Systems and Humans': '{IEEE} Trans. Syst., Man, Cybern. A, Syst., Humans',
 '{IEEE} Transactions on Acoustics, Speech, and Signal Processing': '{IEEE} Trans. Acoust., Speech, Signal Processing',
 '{IEEE} Transactions on Advanced Packaging': '{IEEE} Trans. Adv. Packag.',
 '{IEEE} Transactions on Aeronautical and Navigational Electronics': '{IEEE} Trans. Aeronaut. Navig. Electron.',
 '{IEEE} Transactions on Aerospace': '{IEEE} Trans. Aerosp.',
 '{IEEE} Transactions on Aerospace and Electronic Systems': '{IEEE} Trans. Aerosp. Electron. Syst.',
 '{IEEE} Transactions on Aerospace and Navigational Electronics': '{IEEE} Trans. Aerosp. Navig. Electron.',
 '{IEEE} Transactions on Airborne Electronics': '{IEEE} Trans. Airborne Electron.',
 '{IEEE} Transactions on Antennas and Propagation': '{IEEE} Trans. Antennas Propagat.',
 '{IEEE} Transactions on Applications and Industry': '{IEEE} Trans. Applicat. Ind.',
 '{IEEE} Transactions on Applied Superconductivity': '{IEEE} Trans. Appl. Superconduct.',
 '{IEEE} Transactions on Audio': '{IEEE} Trans. Audio',
 '{IEEE} Transactions on Audio and Electroacoustics': '{IEEE} Trans. Audio Electroacoust.',
 '{IEEE} Transactions on Automatic Control': '{IEEE} Trans. Automat. Contr.',
 '{IEEE} Transactions on Automation Science and Engineering': '{IEEE} Trans. Autom. Sci. Eng.',
 '{IEEE} Transactions on Bio-Medical Electronics': '{IEEE} Trans. Bio-Med. Electron.',
 '{IEEE} Transactions on Bio-Medical Engineering': '{IEEE} Trans. Bio-Med. Eng.',
 '{IEEE} Transactions on Biomedical Engineering': '{IEEE} Trans. Biomed. Eng.',
 '{IEEE} Transactions on Broadcasting': '{IEEE} Trans. Broadcast.',
 '{IEEE} Transactions on Circuit Theory': '{IEEE} Trans. Circuit Theory',
 '{IEEE} Transactions on Circuits and Systems': '{IEEE} Trans. Circuits Syst.',
 '{IEEE} Transactions on Circuits and Systems for Video Technology': '{IEEE} Trans. Circuits Syst. Video Technol.',
 '{IEEE} Transactions on Circuits and Systems---Part {II}: Analog and Digital Signal Processing': '{IEEE} Trans. Circuits Syst. {II}',
 '{IEEE} Transactions on Circuits and Systems---Part {I}: Fundamental Theory and Applications': '{IEEE} Trans. Circuits Syst. {I}',
 '{IEEE} Transactions on Circuits and Systems-Part I: Fundamental Theory and Applications': '{IEEE} Trans. Circuits Syst. I, Fundam. Theory Appl.1',
 '{IEEE} Transactions on Circuits and Systems-Part I: Regular Papers': '{IEEE} Trans. Circuits Syst. I, Reg. Papers1',
 '{IEEE} Transactions on Circuits and Systems-Part II: ANalog and Digital Signal Processing': '{IEEE} Trans. Circuits Syst. II, Analog Digit. Signal Process.2',
 '{IEEE} Transactions on Circuits and Systems-Part II: Express Briefs': '{IEEE} Trans. Circuits Syst. II, Exp. Briefs2',
 '{IEEE} Transactions on Communication Technology': '{IEEE} Trans. Commun. Technol.',
 '{IEEE} Transactions on Communications': '{IEEE} Trans. Commun.',
 '{IEEE} Transactions on Component Parts': '{IEEE} Trans. Comp. Parts',
 '{IEEE} Transactions on Components and Packaging Technologies': '{IEEE} Trans. Comp. Packag. Technol.',
 '{IEEE} Transactions on Components and Packaging Technology': '{IEEE} Trans. Comp. Packag. Technol.',
 '{IEEE} Transactions on Components, Hybrids and Manufacturing Technology': '{IEEE} Trans. Comp., Hybrids, Manufact. Technol.',
 '{IEEE} Transactions on Components, Packaging and Manufacturing Technology---Part {A}': '{IEEE} Trans. Comp., Packag., Manufact. Technol. {A}',
 '{IEEE} Transactions on Components, Packaging and Manufacturing Technology---Part {B}: Advanced Packaging': '{IEEE} Trans. Comp., Packag., Manufact. Technol. {B}',
 '{IEEE} Transactions on Components, Packaging and Manufacturing Technology---Part {C}: Manufacturing': '{IEEE} Trans. Comp., Packag., Manufact. Technol. {C}',
 '{IEEE} Transactions on Computer-Aided Design of Integrated Circuits and Systems': '{IEEE} Trans. Computer-Aided Design Integr. Circuits Syst.',
 '{IEEE} Transactions on Computers': '{IEEE} Trans. Comput.',
 '{IEEE} Transactions on Consumer Electronics': '{IEEE} Trans. Consumer Electron.',
 '{IEEE} Transactions on Control Systems Technology': '{IEEE} Trans. Contr. Syst. Technol.',
 '{IEEE} Transactions on Cognitive Communications and Networking':'{IEEE} Trans. on Cognitive Commun. and Networking',
 '{IEEE} Transactions on Device and Materials Reliability': '{IEEE} Trans. Device Mat. Rel.',
 '{IEEE} Transactions on Dielectrics and Electrical Insulation': '{IEEE} Trans. Dielect. Elect. Insulation',
 '{IEEE} Transactions on Education': '{IEEE} Trans. Educ.',
 '{IEEE} Transactions on Electrical Insulation': '{IEEE} Trans. Elect. Insulation',
 '{IEEE} Transactions on Electromagnetic Compatibility': '{IEEE} Trans. Electromagn. Compat.',
 '{IEEE} Transactions on Electron Devices': '{IEEE} Trans. Electron Devices',
 '{IEEE} Transactions on Electronic Computers': '{IEEE} Trans. Electron. Comput.',
 '{IEEE} Transactions on Electronics Packaging Manufacturing': '{IEEE} Trans. Electron. Packag. Manufact.',
 '{IEEE} Transactions on Energy Conversion': '{IEEE} Trans. Energy Conversion',
 '{IEEE} Transactions on Engineering Management': '{IEEE} Trans. Eng. Manage.',
 '{IEEE} Transactions on Evolutionary Computation': '{IEEE} Trans. Evol. Comput.',
 '{IEEE} Transactions on Fuzzy Systems': '{IEEE} Trans. Fuzzy Syst.',
 '{IEEE} Transactions on Geoscience Electronics': '{IEEE} Trans. Geosci. Electron.',
 '{IEEE} Transactions on Geoscience and Remote Sensing': '{IEEE} Trans. Geosci. Remote Sensing',
 '{IEEE} Transactions on Human Factors in Electronics': '{IEEE} Trans. Hum. Factors Electron.',
 '{IEEE} Transactions on Image Processing': '{IEEE} Trans. Image Processing',
 '{IEEE} Transactions on Industrial Electronics': '{IEEE} Trans. Ind. Electron.',
 '{IEEE} Transactions on Industrial Electronics and Control Instrumentation': '{IEEE} Trans. Ind. Electron. Contr. Instrum.',
 '{IEEE} Transactions on Industrial Informatics': '{IEEE} Trans Ind. Informat.',
 '{IEEE} Transactions on Industry Applications': '{IEEE} Trans. Ind. Applicat.',
 '{IEEE} Transactions on Industry and General Applications': '{IEEE} Trans. Ind. Gen. Applicat.',
 '{IEEE} Transactions on Information Forensics and Security': '{IEEE} Trans.Inf. Forensics Security.',
 '{IEEE} Transactions on Information Technology in Biomedicine': '{IEEE} Trans. Inform. Technol. Biomed.',
 '{IEEE} Transactions on Information Theory': '{IEEE} Trans. Inform. Theory',
 '{IEEE} Transactions on Instrumentation and Measurement': '{IEEE} Trans. Instrum. Meas.',
 '{IEEE} Transactions on Intelligent Transportation Systems': '{IEEE} Trans. Intell. Transport. Syst.',
 '{IEEE} Transactions on Knowledge and Data Engineering': '{IEEE} Trans. Knowledge Data Eng.',
 '{IEEE} Transactions on Magnetics': '{IEEE} Trans. Magn.',
 '{IEEE} Transactions on Man-Machine Systems': '{IEEE} Trans. Man-Mach. Syst.',
 '{IEEE} Transactions on Manufacturing Technology': '{IEEE} Trans. Manufact. Technol.',
 '{IEEE} Transactions on Medical Electronics': '{IEEE} Trans. Med. Electron.',
 '{IEEE} Transactions on Medical Imaging': '{IEEE} Trans. Med. Imag.',
 '{IEEE} Transactions on Microwave Theory and Techniques': '{IEEE} Trans. Microwave Theory Tech.',
 '{IEEE} Transactions on Military Electronics': '{IEEE} Trans. Mil. Electron.',
 '{IEEE} Transactions on Mobile Computing': '{IEEE} Trans. Mobile Comput.',
 '{IEEE} Transactions on Multimedia': '{IEEE} Trans. Multimedia',
 '{IEEE} Transactions on Nanobioscience': '{IEEE} Trans. Nanobiosci.',
 '{IEEE} Transactions on Nanotechnology': '{IEEE} Trans. Nanotechnol.',
 '{IEEE} Transactions on Neural Networks': '{IEEE} Trans. Neural Networks',
 '{IEEE} Transactions on Neural Systems and Rehabilitation Engineering': '{IEEE} Trans. Neural Syst. Rehab. Eng.',
 '{IEEE} Transactions on Nuclear Science': '{IEEE} Trans. Nucl. Sci.',
 '{IEEE} Transactions on Parallel and Distributed Systems': '{IEEE} Trans. Parallel Distrib. Syst.',
 '{IEEE} Transactions on Parts, Hybrids and Packaging': '{IEEE} Trans. Parts, Hybrids, Packag.',
 '{IEEE} Transactions on Parts, Materials and Packaging': '{IEEE} Trans. Parts, Mater., Packag.',
 '{IEEE} Transactions on Pattern Analysis and Machine Intelligence': '{IEEE} Trans. Pattern Anal. Machine Intell.',
 '{IEEE} Transactions on Plasma Science': '{IEEE} Trans. Plasma Sci.',
 '{IEEE} Transactions on Power Apparatus and Systems': '{IEEE} Trans. Power App. Syst.',
 '{IEEE} Transactions on Power Delivery': '{IEEE} Trans. Power Delivery',
 '{IEEE} Transactions on Power Electronics': '{IEEE} Trans. Power Electron.',
 '{IEEE} Transactions on Power Systems': '{IEEE} Trans. Power Syst.',
 '{IEEE} Transactions on Professional Communication': '{IEEE} Trans. Prof. Commun.',
 '{IEEE} Transactions on Radio Frequency Interference': '{IEEE} Trans. Radio Freq. Interference',
 '{IEEE} Transactions on Rehabilitation Engineering': '{IEEE} Trans. Rehab. Eng.',
 '{IEEE} Transactions on Reliability': '{IEEE} Trans. Rel.',
 '{IEEE} Transactions on Robotics': '{IEEE} Trans. Robot.',
 '{IEEE} Transactions on Robotics and Automation': '{IEEE} Trans. Robot. Automat.',
 '{IEEE} Transactions on Semiconductor Manufacturing': '{IEEE} Trans. Semiconduct. Manufact.',
 '{IEEE} Transactions on Signal Processing': '{IEEE} Trans. Signal Processing',
 '{IEEE} Transactions on Software Engineering': '{IEEE} Trans. Software Eng.',
 '{IEEE} Transactions on Sonics and Ultrasonics': '{IEEE} Trans. Sonics Ultrason.',
 '{IEEE} Transactions on Speech and Audio Processing': '{IEEE} Trans. Speech Audio Processing',
 '{IEEE} Transactions on Systems Science and Cybernetics': '{IEEE} Trans. Syst. Sci. Cybernetics',
 '{IEEE} Transactions on Systems, Man, and Cybernetics': '{IEEE} Trans. Syst., Man, Cybern.',
 '{IEEE} Transactions on Systems, Man, and Cybernetics---Part {A}: Systems and Humans': '{IEEE} Trans. Syst., Man, Cybern. {A}',
 '{IEEE} Transactions on Systems, Man, and Cybernetics---Part {B}: Cybernetics': '{IEEE} Trans. Syst., Man, Cybern. {B}',
 '{IEEE} Transactions on Systems, Man, and Cybernetics---Part {C}: Applications and Reviews': '{IEEE} Trans. Syst., Man, Cybern. {C}',
 '{IEEE} Transactions on Systems, Man, and Cybernetics-Part B: Cybernetics': '{IEEE} Trans. Syst., Man, Cybern. B, Cybern.',
 '{IEEE} Transactions on Systems, Man, and Cybernetics-Part C: Applications and Reviews': '{IEEE} Trans. Syst., Man, Cybern. C, Appl. Rev.',
 '{IEEE} Transactions on Ultrasonics Engineering': '{IEEE} Trans. Ultrason. Eng.',
 '{IEEE} Transactions on Ultrasonics, Ferroelectrics, and Frequency Control': '{IEEE} Trans. Ultrason., Ferroelect., Freq. Contr.',
 '{IEEE} Transactions on Vehicular Communications': '{IEEE} Trans. Veh. Commun.',
 '{IEEE} Transactions on Vehicular Technology': '{IEEE} Trans. Veh. Technol.',
 '{IEEE} Transactions on Very Large Scale Integration ({VLSI}) Systems': '{IEEE} Trans. {VLSI} Syst.',
 '{IEEE} Transactions on Visualization and Computer Graphics': '{IEEE} Trans. Visual. Comput. Graphics',
 '{IEEE} Transactions on Wireless Communications': '{IEEE} Trans. Wireless Commun.',
 '{IEEE} Translation Journal on Magnetics in Japan': '{IEEE} Transl. J. Magn. Jpn.',
 '{IEEE} Wireless Communications Magazine': '{IEEE} Wireless Commun. Mag.',
 '{IEEE} {ASSP} Magazine': '{IEEE} {ASSP} Mag.',
 '{IEEE} {IT} Professional': '{IEEE} {IT} Prof.',
 '{IEEE}/ACM Transactions on Networking': '{IEEE}/ACM Trans. Netw.',
 '{IEEE}/ASME Transactions on Mechatronics': '{IEEE}/ASME Trans. Mechatronics', 
 }

conf_abbr={ # 会议部分
 'International Conference on Computing, Networking and Communications (ICNC)': 'Int. Conf. Comput. Netw. Commun. (ICNC)',
 'European Conference on Antennas and Propagation (EUCAP)':'Eur. Conf. Antennas Propag. (EuCAP)',
 'European Conference on Antennas and Propagation (EuCAP)':'Eur. Conf. Antennas Propag. (EuCAP)',
 'IEEE International Conference on Communications (ICC)': 'IEEE Int. Conf. Commun. (ICC)',
 'IEEE Global Communications Conference (GLOBECOM)': 'IEEE Glob. Commun. Conf. (GLOBECOM)',
 'IEEE International Conference on Communications Workshops (ICC Workshops)': 'IEEE Int. Conf. Commun. Workshops (ICCW)',
 'IEEE Wireless Communications and Networking Conference (WCNC)': 'IEEE Wireless Commun. Netw. Conf. (WCNC)',
 }
########################### 第一部分 ###########################################
def replace_abbr(inFile, outFile):
    """ 替换文件
    """
    f = open(inFile, 'r') 
    lines = f.readlines()
    newlines = []
    for line in lines:
        print(line)
        if 'journal={' in line:
            for k in abbr:
                k2 = k.replace('{IEEE}','IEEE')
                if 'journal={'+k+'}' in line: # 全段匹配
                    line = line.replace('journal={'+k+'}','journal={'+abbr[k]+'}')
                elif 'journal={'+k2+'}' in line:
                    line = line.replace('journal={'+k2+'}','journal={'+abbr[k]+'}')
        # 会议缩写替换
        for k in conf_abbr:
            line = line.replace(k,'Proc. '+conf_abbr[k])
        line = keep_capital(line)
        line = deel_month(line)
        newlines.append(line)
    f.close()
    f = open(outFile, 'w')
    f.writelines(newlines)
    f.close()

def keep_capital(line):
    """关键字保持大写"""
    keys = {'UAV', 'UAV' 'mmWave', 'MIMO', 'IoT', '5G', '6G', 'GHz', 'BS', 'MISO', 'QoS', '3D','WSN','MmWave'}
    for k in keys:
        line = line.replace(k,'{'+k+'}')
    return line

def deel_month(line):
    """月份缩写"""
    month={'January':'Jan.',
        'February':'Feb.',
        'March':'Mar.',
        'April':'Apr.',
        'May':'May',
        'June':'Jun.',
        'July':'Jul.',
        'August':'Aug.',
        'September':'Sep.',
        'October':'Oct.',
        'November':'Nov.',
        'December':'Dec.'}
    for k in month:
        line = line.replace(k,month[k])
    return line 
    

########################### 第二部分 ###########################################
########################## Tkinter事件 ########################################
inFile = ""
def addFiles_TK():
    """ 添加待处理的文件 """
    global inFile
    inFile=tkinter.filedialog.askopenfilename(filetypes=[('bib文件', '*.bib')])
    if not inFile:
        output1_TEXT.insert(tkinter.END,'\n请添加.bib文件..\n') # 原文
        return

    output1_TEXT.insert(tkinter.END,'\n添加的文件为：'+inFile+'\n') # 原文


def replace_abbr_TK():
    """替换缩写 (Tkinter按钮的事件)"""

    global inFile
    if not inFile:
        output1_TEXT.insert(tkinter.END, '\n无待处理文件！请添加...\n') # 原文
        return
    outFile = inFile.replace('.bib','_1.bib')
    if inFile and outFile:
        replace_abbr(inFile, outFile)
        output1_TEXT.insert(tkinter.END,'\n完成，输出文件为：\n  '+outFile+'\n') # 原文


########################### 第三部分 ###########################################
########################## 窗体 ########################################
root = tkinter.Tk()
root.geometry('600x400')
root.title('IEEE缩写替换')

## ======================= 布置添加文件的按钮 =========================
add_BUTTON=tkinter.Button(root,text='1. 添加文件',command=addFiles_TK)
add_BUTTON.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=0.2)
## ======================= 布置  的按钮 =========================
split_BUTTON=tkinter.Button(root,text='2. 替换缩写',command=replace_abbr_TK)  # 分割按钮
split_BUTTON.place(relx=0.55, rely=0.1, relwidth=0.2, relheight=0.2)

## ========================= 布置一个显示提示信息的文本框 =======================
output1_TEXT = tkinter.Text(root)
output1_TEXT.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.55) # relx=0.55, rely=0.5, relwidth=0.4, relheight=0.4
info='替换规则："journal={期刊全名}"-->"journal={期刊缩写}"\n'
info+='\n将在原路径下生成 "XXX_1.bib" 文件\n'
output1_TEXT.insert(tkinter.END,info)

output1_TEXT.insert(tkinter.END,'\n等待添加.bib文件...\n')

root.mainloop()