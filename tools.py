from pynput.keyboard import Listener
import pyperclip
import pyautogui
import random
import json
from http import client
from hashlib import md5
from urllib.parse import quote
import translate
import jsonAction
import screenRecognition
import os
import subprocess
import nameNamingDevice
import mysqlDB
import easygui as g
import os
import subprocess
import re
import time
from PIL import Image,ImageGrab
import glob

baseUrl = "C:\\Users\\ligc\\Desktop\\脚本\\个人脚本\\个人脚本大整理\\兴趣\\小工具集合\\"
fistD = ""
second = ""
# http://www.pythontutor.com  代码分析神器，这个集成一下
#下划线
def spatial_variable_underline(strd,type=0):
    try:
        strd = str(strd).strip().replace(" ","_")[0].lower()+str(strd).strip().replace(" ","_")[1:]
        if type == 1: # 下划大写
            strd = strd.upper()
        return strd
    except Exception as e:
        print(e)
        return strd

"""
把空格转为首字母大写
"""
def turn_the_space_into_capital_letters(strd):
    try:
        strResult = ""
        for obj in str(strd).split(" "):
            if obj.find(" ") == -1:
                if len(obj)>1:
                    strResult = strResult + obj[0].title()+obj[1:]
                else:
                    strResult = strResult + obj.title()
        strd = strResult
        return strd
    except Exception as e:
        print(e)
        return strd


def  getMain():
    pyautogui.hotkey('ctrl', 'c')
    sentence = pyperclip.paste()
    sentence = sentence.replace('\n', ' ')
    print(sentence)
    #这个是调用翻译接口
    dataResult = translate.getOriginalResult(sentence)
    result = pyautogui.confirm(text=dataResult,title='变量翻译',buttons=['ok','下划线',"首字母","下划大写","全小写"])
    # print(result)
    if str(result).find("下划线")>-1:
        dataResult = spatial_variable_underline(dataResult)
    if str(result).find("首字母")>-1:
        dataResult = turn_the_space_into_capital_letters(dataResult)
    if str(result).find("下划大写")>-1:
        dataResult = spatial_variable_underline(dataResult,1)
    pyperclip.copy(dataResult)
    #pyautogui.alert(dataResult,  title='Result')

"""
调用2to3.py
"""
def  call_method(fileUrl):
    os.system("python  C:\\Users\\ligc\\AppData\\Local\\Programs\\Python\\Python36\\Tools\\scripts\\2to3.py -w "+fileUrl)


#取字符串中两个符号之间的东东
def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

"""
自定义处理 代码 参数
"""
def custom_Processing(strD):

    if strD != "":
        index = 0
        strdList = strD.split("\r")
        strD = ""
        for obj in strdList:
            if index > 0:
                obj = obj[1:]
            index = index + 1
            strD = strD + obj +"\n"
        parameter = strD.split("####")[1]
        contentCode = strD.split("####")[0]
        contentList = contentCode.split("\n")
        # print(contentList)
        strDy = ""
        for obj in contentList:
            if len(obj)>2:
                if str(obj).find("obj__")>-1:
                    strDy = strDy + obj.replace("obj__",str(parameter)) + "\n"
                else:
                    strDy = strDy + obj+"\n"
        with open("test1.py","w",encoding = "utf-8") as f:
            f.write(strDy)
        command = "cd  "+os.getcwd()+"&python  test1.py"
        actionResult = ""
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            try:
                actionResult = actionResult + str(line.decode('utf-8')) + "\n"
            except Exception as e:
                actionResult = actionResult + str(line.decode('gbk')) + "\n"
            # actionResult = actionResult + line.decode("gbk", "ignore") + "\n"
        pyperclip.copy(actionResult) 


"""
快捷模板
"""
def  python_method():
    std = ''' 
#快捷方法框架
def  fast_Method_Framework(strd):
    strd =strd.replace("\\t","")
    strdL = strd.split("\\n")
    realStrd = ""
    for obj in strdL:
        if obj.replace("\\n","") != "":
            realStrd = realStrd + obj + "\\n"
    strd  = realStrd
    """
    这里写业务处理
    """ 
    return strd

strd = \'\'\'obj__\'\'\'
print(fast_Method_Framework(strd))
####
    '''
    pyperclip.copy(std)



#把列数据转换成sql的in类型
def get_sql_in(word):
    strDList = word.replace("\r\n","\n").replace("\r","\n").split("\n")
    strReult = ""
    for obj in strDList:
        if obj.replace("\n","").replace(" ","")!= "":
            strReult = strReult +'"'+obj.replace("\n","").replace(" ","")+'"'+','
    strReult = strReult[:-1]
    strReult = '('+strReult+')'
    print(strReult)
    return strReult

#取字符串中两个符号之间的东东
def  txt_wrap_by(start_str,  end,  html):
  start  =  html.find(start_str)
  if  start  >=  0:
          start  +=  len(start_str)
          end  =  html.find(end,  start)
          if  end  >=  0:
                  return  html[start:end].strip()


"""
自动生成测试数据
"""
def  automatic_generation_of_test_data(number,sentence):
    # number = g.enterbox("请选择输出参数分割符（默认逗号）：")
    segmentation_character = g.enterbox("请选择输出参数分割符（默认逗号）：")
    if segmentation_character == "," or str(segmentation_character) == None or str(segmentation_character) == " " or str(segmentation_character) == "":
        segmentation_character = ","
    elif str(segmentation_character).find("空格") > -1:
        segmentation_character = " "
    elif str(segmentation_character).find("制表") > -1:
        segmentation_character = "\t"



    strReult = ""
    strList = []
    if len(sentence) > 0:
        defdList = sentence.replace("\t",",").replace("\r","").replace("，",",").split(",")
        for obj in defdList:
            try:
                number1 = int(obj.split("_")[len(obj.split("_"))-1])
                strList.append(obj)
            except Exception as e:
                obj = obj + "_5"
                strList.append(obj)
    # print(strList)
    num = 1
    resultStr = ""
    resultStr = resultStr+sentence.replace("\t",",").replace("\r","").replace('_str','').replace('_time','').replace('_init','')+'\n'
    while num < int(number):
        sObj = {} 
        for  obj in strList:
            if obj != '':
                if  obj.find('_str')>-1:
                    sObj[obj] = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],int(obj.split("_")[len(obj.split("_"))-1])))
                elif obj.find('_time')>-1:
                    sObj[obj] = todayTime + str(random.randint(0,59))
                elif obj.find('_init')>-1:
                    redc = txt_wrap_by("(",")",obj.replace("（","(").replace("）",")"))
                    # print("defergrgt"+  str(redc))
                    if redc != None:
                        # print("werr2222222"+redc)
                        list1 = redc.split("|")
                        number3 = random.randint(0,len(list1)-1)
                        sObj[obj] = list1[number3]
                else:
                    number2 = pow(10,int(obj.split("_")[len(obj.split("_"))-1]))
                    sObj[obj] = random.randint(number2,number2+10*number2)
        txt = ''
        for value in sObj.values():
            txt = txt + str(value)+segmentation_character
        txt = txt + '\n'
        resultStr = resultStr +txt
        num +=1
    # print(resultStr)
    pyperclip.copy(resultStr)
    # g.msgbox("测试数据生成成功")
    # g.msgbox("测试数据生成成功！", title="提醒",ok_button="知道啦") 
    result = pyautogui.confirm(text="测试数据生成成功！",title='提醒')
    
    return  resultStr


"""
数据处理-去重
"""
def data_Reduplication(word):
    strDList = word.replace("\r\n","\n").replace("\r","\n").split("\n")
    strReult = ""
    #非重复数组
    non_repetitive_arrays = []
    for obj in strDList:
        if obj.replace("\n","").replace(" ","")!= "":
            if obj not in non_repetitive_arrays:
                non_repetitive_arrays.append(obj)
                strReult = strReult + obj.replace("\n","").replace(" ","") + "\n"
            else:
                print(obj.replace("\n","").replace(" ",""))
    # print(strReult)
    return strReult

"""
保留两位小数
"""
def keep_two_decimal_places(word):
    strDList = word.replace("\r\n","\n").replace("\r","\n").split("\n")
    strReult = ""
    for obj in strDList:
        if obj.replace("\n","").replace(" ","")!= "":
            stdf = '%.2f' % float(obj)
            strReult = strReult + str(stdf) + "\n"
    return strReult

    


"""
包含关系
"""
def inclusive_relation(word,strd):
    original_string = "只属于原字符串的部分；\n"
    reference_string = "只属于参考字符串的部分；\n"
    public_sector = "公共部分；\n"
    primitive_array = []
    reference_array = []
    wordList = word.replace("\r\n","\n").replace("\r","\n").split("\n")
    for obj in wordList:
        if obj.replace("\n","").replace(" ","")!= "":
            primitive_array.append(obj.replace("\n","").replace(" ",""))
    strdList = strd.replace("\r\n","\n").replace("\r","\n").split("\n")

    for obj in strdList:
        if obj.replace("\n","").replace(" ","")!= "":
            reference_array.append(obj)
    # print(primitive_array)
    # print(reference_array)
    for obj in primitive_array:
        if obj not in reference_array:
            original_string= original_string + obj + "\n"
        else:
            public_sector = public_sector + obj + "\n"

    for obj in reference_array:
        if obj not in primitive_array:
            reference_string= reference_string + obj + "\n"

    return  original_string + "\n----\n"+ reference_string + "\n----\n"+ public_sector








"""
地址映射
"""
def address_mapping(sentence):
    strDList = sentence.replace("\r\n","\n").replace("\r","\n").split("\n")
    strReult = ""
    # 获取基础路径
    for obj in strDList:
        if obj.replace("\n","").replace(" ","")!= "":
            strReult = strReult + "原路径："+obj + "\n"
            if obj.find("/") > -1:
                strReult = strReult + "转winow路径：" + obj.replace("/","\\") + "\n"
            if obj.find("\\\\") > -1:
                strReult = strReult + "转winow路径：" + obj.replace("\\\\","\\") + "\n"
            if obj.find("\\") > -1 and obj.find("\\\\") == -1:
                strReult = strReult + "转linux路径：" + obj.replace("\\","/") + "\n"
                strReult = strReult + "转程序路径：" + obj.replace("\\","\\\\") + "\n"
    print(strReult)
    return strReult


"""
请求头
"""
def  request_header(sentence):
    strDList = sentence.replace("\r\n","\n").replace("\r","\n").split("\n")
    strReult = ""
    # 获取基础路径
    for obj in strDList:
        if obj.replace("\n","").replace(" ","")!= "" and obj.find(":") > -1:
            strReult = strReult + '"'+obj.split(":")[0].strip()+'":"'+obj.split(":")[1].strip()+'"'+",\n"
    return strReult
"""
根据指定的规则，过滤数据源
"""
def  rule_query(sentence,queryType,strModel):
    strDList = sentence.replace("\r\n","\n").replace("\r","\n").split("\n")
    st = ""
    if queryType.find("分割符") > -1:
        st = g.enterbox("请输入要取的列（从0开始）：")
    strReult = ""
    # 获取基础路径
    print("输入参数："+str(strModel))
    for obj in strDList:
        obj = obj.strip()
        if queryType.find("包含输入") > -1:
            if None != obj and obj.find(strModel) > -1:
                strReult = strReult + obj + "\n"
                #分割符
        if queryType.find("分割符") > -1:
            
            if strModel == "空格" or str(strModel) == None or str(strModel) == " " or str(strModel) == "":
                strModel = " "
            if strModel == "制表":
                strModel = "\t"
            if obj.find(strModel) > -1:
                objList = obj.split(strModel)
            lastQList = []
            for obj in objList:
                if obj.replace(" ","") != "":
                    lastQList.append(obj)
            try:
                strReult = strReult + lastQList[int(st)] + "\n"
            except Exception as e:
                strReult = strReult + "出现错误" + "\n"
        if queryType.find("不包含") > -1:
            if None != obj and obj.find(strModel) == -1:
                strReult = strReult + obj + "\n"
            

    return strReult




"""
数据处理
"""
def data_processing(sentence):
    text = ""
    resultStr = ""
    if len(sentence) < 100:
        text = len(sentence)
    result = pyautogui.confirm(text=text,title='快捷功能大全',buttons=['json格式化',"测试数据","规则查询","去重","生成数组","地址映射","请求头","包含关系","四舍五入保留2位"])
    if str(result).find("去重")>-1:
        resultStr = data_Reduplication(sentence)
    if str(result).find("生成数组")>-1:
        resultStr = get_sql_in(sentence)
    if str(result).find("json格式化")>-1:
        resultStr = jsonAction.get_json_format(str(sentence),"")
        with open("json模板.json","w+",encoding = "utf-8") as f:
            f.write(resultStr)
        os.startfile("json模板.json")
    if str(result).find("地址映射")>-1:
        resultStr = address_mapping(sentence)
    if str(result).find("请求头")>-1:
        resultStr = request_header(sentence)
    if str(result).find("测试数据")>-1:
        #这边以弹窗的形式包含进去
        result = pyautogui.confirm(text="变量生成规则，以,或，号分割，默认生成数字，带_str生成字符串，带_time生成时间类型，最后带_+数字表示生成的位数")
        # print("dddd+"+result)
        if result.find("OK") > -1:
            number = g.enterbox("请输入数量：")
            print("dddd+"+str(int(number.replace('\n',""))))
            resultStr = automatic_generation_of_test_data(int(number.replace('\n',"")),sentence)
    if str(result).find("包含关系")>-1:
        #这边以弹窗的形式包含进去
        st = g.enterbox("请输入要参考的字符串：")
        resultStr = inclusive_relation(sentence,st)
    if str(result).find("四舍五入保留2位")>-1:
        resultStr = keep_two_decimal_places(sentence)
    if str(result).find("规则查询")>-1:
        rule = pyautogui.confirm(text=text,title='查询规则',buttons=['包含输入',"不包含","分割符","正则表达","相似查询","生成数组"])
        st = g.enterbox("请输入参数(默认空格)：")
        if st != None:
            resultStr = rule_query(sentence,rule,str(st).replace("\n",""))


    pyperclip.copy(resultStr)

def find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern,"",file)
    return  unchinese


"""
数据处理-测试数据生成
"""
def template_conversion(sentence,model):
    strReult = ""
    if len(sentence) > 0:
        sentenceList = sentence.split("\t")
        print(sentenceList)
        for index in range(0,len(sentenceList)):
            if sentenceList[index] != None and sentenceList[index].replace(" ","") != "":
                strF = sentenceList[index]
                if find_unchinese(sentenceList[index]).replace("\n","") == "":
                    time.sleep(1)
                    print(sentenceList[index])
                    strF = turn_the_space_into_capital_letters(translate.getOriginalResult(sentenceList[index]))
                else:
                    strF = find_unchinese(sentenceList[index]).replace("\n","")
                strReult = strReult + model.replace("【原型】",sentenceList[index]).replace("【翻译】",strF).replace("【序列】",str(index))+"\n"

    return strReult

"""
通用参数填写处理
"""
def  general_assignment(sentence,model):
    sentenceList = sentence.replace("\r","\n").split("\n")
    lastSentencelList = []
    strRlut = ""
    for obj in sentenceList:
        obj = obj.strip()
        arryList = []
        if obj.replace("，",",").find(",")>-1:
            dcd = obj.split(",")
            for obj1 in range(0,len(dcd)):
                arryList.append(dcd[obj1])
        if len(arryList) > 0:
            lastSentencelList.append(arryList)
    # print(lastSentencelList)
    for obj in lastSentencelList:
        modelC = str(model)
        for index in range(0,len(obj)):
            #这里是处理基础判断
            modelC = modelC.replace('【'+str(index)+'】',obj[index])
            #空格转下划线
            modelC = modelC.replace('【'+str(index)+'a】',spatial_variable_underline(obj[index]))
        strRlut = strRlut + modelC + "\n"
    return  strRlut






"""
模板处理
"""
def fast_Template(sentence):
    text = ""
    resultStr = ""
    if len(sentence) < 100:
        text = len(sentence)
    result = pyautogui.confirm(text=text,title='快捷功能大全',buttons=['python方法',"转化模板","通用赋值"])
    if str(result).find("python方法")>-1:
        python_method()
    if str(result).find("转化模板")>-1:
        model = g.enterbox("提供【原型】【翻译】【序列】三个参数：")
        resultStr = template_conversion(sentence,model)
    if str(result).find("通用赋值")>-1:
        strd = '''
【0】:原型
【0a】:空格转下划线
        '''
        pyperclip.copy(strd)
        model = g.enterbox("请输入model：")
        resultStr = general_assignment(sentence,model)
    pyperclip.copy(resultStr)


"""
表情包保存
"""
def expression_pack_save():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        model = g.enterbox("请输入名称:")
        im.save(baseUrl+"emoticon\\"+model.strip()+".png")
        pyautogui.alert(text='图片保存成功',title='',button='OK')
    else:
        pyautogui.alert(text='复制内容并非图片',title='',button='OK')

# import os
def listdirBy(path,list_name):  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path) :  
            listdir(file_path, list_name)  
        else:
            if file_path.find(".png") >-1:
                list_name.append(os.path.basename(file_path))
"""
表情包查询
"""
def  expression_pack_query(objL):
    # strd = []
    url = baseUrl + "emoticon"
    flag = True
    for infile in glob.glob(url+"\\*"+objL.strip()+"*"):
        flag = False
        os.system(infile)
        result = pyautogui.confirm(text="",title='快捷功能大全',buttons=['还要继续',"找到了"])
        if result.find("找到了")>-1:
            flag = False
            break
        else:
            flag = True

    if flag:
        url = "http://www.dbbqb.com/s?w="+objL.strip()
        os.startfile(url)
    # print(strd)




"""
不常用功能集锦
"""
def uncommon_Function_Complete(result,text="",sentence = ""):
    if result == None or result == "":
        return False 
    if text == "":
        # pyautogui.hotkey('ctrl', 'c')
        # sentence = pyperclip.paste()
        # sentence = sentence.replace('\n', ' ')
        text = sentence
    #result = pyautogui.confirm(text=text,title='快捷功能大全',buttons=["翻译",'表情包','pip快捷',"快捷搜索","快捷保存","知识题库","数据处理","通用替换",'2to3.py',"截图识别","快捷模板","取消"])
    if str(result).find("2to3.py")>-1:
        fileUrl = pyautogui.prompt("请输入文件路径：")
        call_method(fileUrl)
    if str(result).find("自定义处理")>-1:
        custom_Processing(str(sentence))
    if str(result).find("快捷模板")>-1:
        fast_Template(str(sentence))
    if str(result).find("pip快捷")>-1:
        #os.system("cd  C:\\Users\\ligc\\Desktop\\脚本\\个人脚本\\个人脚本大整理\\兴趣\\小工具集合&python  后台服务程序.py")
        # os.startfile("http://127.0.0.1:9000/index")
        actionResult = ""
        result = os.popen('pip install  '+str(sentence)+'  -i https://pypi.tuna.tsinghua.edu.cn/simple/')  
        res = result.read()  
        for line in res.splitlines():
            actionResult = actionResult + line+ "\n"
        print(actionResult)
        pyautogui.confirm(text=actionResult,title='执行结果')

    if str(result).find("数据处理")>-1:
        #os.startfile("http://127.0.0.1:9000/code")
        data_processing(str(sentence))
    if str(result).find("本地搜索")>-1:
        strD = intelligent_Tips(str(sentence))
    if str(result).find("百度搜索")>-1:
        if str(sentence).find("http") >-1 and str(sentence).find(":") >-1 and str(sentence).find("/") >-1:
                os.startfile(str(sentence).strip())
        os.startfile("http://www.baidu.com/s?wd="+str(sentence)+"&amp;cl=3&amp;t=12&amp;fr=news")
    if str(result).find("取名器")>-1:
        surnames = []
        if str(sentence) != "" and len(str(sentence)) < 2: 
            surnames.append(str(sentence))
        name = nameNamingDevice.getName(surnames)
        print(name)
        pyperclip.copy(name)
        uncommon_Function_Complete("",name,str(sentence))
    if str(result).find("快捷保存")>-1:
        pyautogui.hotkey('ctrl', 'c')
        sentence = pyperclip.paste()
        sentence = sentence.replace('\n', ' ')
        quick_Preservation(str(sentence))
    if str(result).find("知识题库")>-1:
        title = None
        content = None
        title = g.enterbox("请输入问题：")
        if title != None:
            content = g.enterbox("请输入答案：")
        if title != None and  content != None:
            problem_preservation(title,content)
    if str(result).find("通用替换")>-1:
        strd = '''
【0】:原型
【0a】:空格转下划线
        '''
        pyperclip.copy(strd)
        model = g.enterbox("请输入model：")
        resultStr = general_assignment(sentence,model)
        pyperclip.copy(resultStr)
    if str(result).find("翻译")>-1:
        getMain()
    if str(result).find("表情包")>-1:
        result = pyautogui.confirm(text="",title='搜索方式',buttons=["表情包搜索","表情包保存"])
        if None != result and str(result) == "表情包搜索":
            #请输入相关
            model = g.enterbox("请输入关键字（默认标题）：",title = sentence)
            if model  == None  or  model.replace("\n","").replace("\t","") == "":
                model = sentence
            # print(model)
            resultStr = expression_pack_query(model)
        elif None != result and str(result) == "表情包保存":
            resultStr = expression_pack_save()
    if str(result).find("截图识别")>-1:
        os.system("cd  C:\\Users\\ligc\\Desktop\\脚本\\个人脚本\\个人脚本大整理\\兴趣\\小工具集合&python  screenRecognition.py")



"""
智能提示
"""
def intelligent_Tips(sentence):
    stock_identification = 0   #0：快捷输入库  1：重要信息库  2：代码库， 3 日常记录库
    if str(sentence) != "":
        writing_Template_query_all_sql = "SELECT * from  writing_Template WHERE  title  LIKE '%BBBB%'  ORDER BY  count DESC "
        # 查询数据库 
        all_record = mysqlDB.queryMysql(writing_Template_query_all_sql.replace("BBBB",str(sentence).replace("\n","").replace("\r","").replace(" ","")))
        if None == all_record or all_record == []:
            stock_identification = 1
            writing_Template_query_all_sql = "SELECT *  FROM  record  WHERE  title  LIKE '%BBBB%' order by queryCount desc"
            all_record = mysqlDB.queryMysql(writing_Template_query_all_sql.replace("BBBB",str(sentence).replace("\n","").replace("\r","").replace(" ","")))
        if None == all_record or all_record == []:
            stock_identification = 2
            writing_Template_query_all_sql = "SELECT id,title,code as content  FROM  code  WHERE  title  LIKE '%BBBB%'"
            all_record = mysqlDB.queryMysql(writing_Template_query_all_sql.replace("BBBB",str(sentence).replace("\n","").replace("\r","").replace(" ","")))
        if None == all_record or all_record == []:
            stock_identification = 3
            writing_Template_query_all_sql = "SELECT *  FROM  rotary WHERE  title  LIKE '%BBBB%'"
            all_record = mysqlDB.queryMysql(writing_Template_query_all_sql.replace("BBBB",str(sentence).replace("\n","").replace("\r","").replace(" ","")))
        if None == all_record or all_record == []:
            pyautogui.alert(text='没有查到任何结果',title='',button='OK') 
            return False
        print(all_record)
        print(writing_Template_query_all_sql.replace("BBBB",str(sentence).replace("\n","").replace("\r","")))
        allList = []
        indexList = []
        contentList = []
        for obj in all_record:
            allList.append(obj.get("title"))
            indexList.append(obj.get("id"))
            if None != obj.get("content"):
                contentList.append(obj.get("content"))
            else:
                contentList.append("")
        # print(allList)
        repeated_access(allList,indexList,contentList,stock_identification)

"""
重复访问
"""
def repeated_access(allList,indexList,contentList,stock_identification):
    reply = ""
    msg = "选择最合适的选项"
    title = ""
    reply = g.choicebox(msg,choices=allList)
    if None == reply:
        return False
    strX = "标题为：\n"+ reply+"\n\n内容为："+ contentList[allList.index(reply)]

    strXContent = contentList[allList.index(reply)]
    stdContent = ""
    if strX != None and len(strX) > 1000:
        stdContent = strX[0:1000]
    else:
        stdContent = strX
    print(stdContent)
    #g.buttonbox("大家说嗅嗅可爱吗?",image="C:\\Users\\ligc\\Desktop\\脚本\\个人脚本\\个人脚本大整理\\兴趣\\小工具集合\\aaabbb.png",choices=("可爱","不可爱","财迷"))
    result = pyautogui.confirm(text=stdContent,title='保存内容为',buttons=["ok","cancel","图片展示"])
    if str(result).find("ok")>-1:
        contentId = indexList[allList.index(reply)]
        print(contentId) #测试地址
        writing_Template_save_by_id = "UPDATE writing_Template SET count  = count + 1 WHERE id = " + str(contentId)
        # print(strX)
        if strXContent == "":
            pyperclip.copy(reply+"")
        else:
            pyperclip.copy(strXContent)
        if stock_identification == 0:
            mysqlDB.saveMysql(writing_Template_save_by_id)
    elif str(result).find("图片展示")>-1:
        im = Image.open("image\\"+str(reply).replace("\n",'').replace(" ","").strip())
        im.show()
        result = pyautogui.confirm(text=stdContent,title='保存内容为',buttons=["ok","cancel","图片展示"])
        if str(result).find("ok")>-1:
            pyperclip.copy(reply)
        else:
            repeated_access(allList,indexList,contentList,stock_identification)
    else:
        repeated_access(allList,indexList,contentList,stock_identification)
                    

"""
window 获取指令执行结果
"""
def  get_the_result_of_instruction_execution(command):
    command = command.replace("\t","")
    commandList = command.split("\n")
    strdd = ""
    for obj in commandList:
        if obj.replace("\n","") != "":
            strdd = strdd + obj
    command = strdd
    print(command)
    actionResult = ""
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        try:
            actionResult = actionResult + str(line.decode('utf-8')) + "\n"
        except Exception as e:
            actionResult = actionResult + str(line.decode('gbk')) + "\n"
    return actionResult


            
"""
智能提示
"""
def intelligent_Tips(sentence):
    if str(sentence) != "" and str(sentence).find("'") == -1 and str(sentence).find(" ") == -1:
        try:
            get_the_result_of_instruction_execution("cd  C:\\Users\\ligc\\Desktop\\脚本\\个人脚本\\个人脚本大整理\\兴趣\\小工具集合&python  bulletWindowList.py " + str(sentence)+"")
        except Exception as e:
            raise e
        
     



"""
快捷保存
"""
def  quick_Preservation(std):
    writing_Template_insert_sql = "INSERT INTO writing_Template (title) VALUES ('AAAA')"
    writing_Template_insert_sql1 = "INSERT INTO writing_Template (title,content) VALUES ('AAAA','BBBB')"
    stdContent = ""
    if len(std) > 1000:
        stdContent = std[0:1000]
    else:
        stdContent = std
    result = pyautogui.confirm(text=stdContent,title='保存内容为',buttons=["录入","补充说明","取消"])
    if str(result).find("录入")>-1:
        mysqlDB.saveMysql(writing_Template_insert_sql.replace("AAAA",std.replace("\\", "\\\\").replace("'","\\'")))
        pyautogui.alert(text='录入成功',title='',button='OK') 
    if str(result).find("补充说明")>-1:
        title = pyautogui.prompt(text="请输入补充说明",title="录入")
        mysqlDB.saveMysql(writing_Template_insert_sql1.replace("AAAA",title.replace("\\", "\\\\").replace("'","\\'")).replace("BBBB",title.replace("\\", "\\\\").replace("'","\\'")))
        pyautogui.alert(text='录入成功',title='',button='OK') 



"""
问题保存
"""
def  problem_preservation(title,content):
    itemBank_insert_sql = "INSERT INTO itemBank (title,content) VALUES ('AAAA','BBBB')"
    mysqlDB.saveMysql(itemBank_insert_sql.replace("AAAA",title.replace("\\", "\\\\").replace("'","\\'")).replace("BBBB",content.replace("\\", "\\\\").replace("'","\\'")))
    result = pyautogui.confirm(text="保存成功！",title='提醒')

        


def press(key):
    global second
    global fistD
    print(second,fistD)
    fistD = key
    if second != "":
        oldSecond = second
        second = key
        if str(second).find("Key.spaced")>-1 and oldSecond != "xd":
            try:
                getMain()
            except Exception as e:
                print  (e)
            
            second = ""
            fistD = ""
        elif str(second).find("Key.space")>-1 and str(second).find("\\x") == -1 and oldSecond != "xd":
            try:
                uncommon_Function_Complete()
            except Exception as e:
                print(e) 
            
            second = ""
            fistD = ""
        elif str(second).find("q")>-1 and oldSecond != "xd":
            try:
                pyautogui.hotkey('ctrl', 'c')
                sentence = pyperclip.paste()
                sentence = sentence.replace('\n', ' ')
                # print(sentence)
                intelligent_Tips(sentence)
            except Exception as e:
                print(e)
            
            second = ""
            fistD = ""  
        # elif str(second).find("q")>-1 and oldSecond != "xd":
            # second = ""
            # fistD = ""
            # print("进来了")
        else:
            second = ""
    if str(fistD).find("Key.ctrl_l")>-1:
        second = "dw"
    if str(fistD).find("Key.ctrl_r") > -1 :
        second = "xd"


# with Listener(on_press = press) as listener:
#         listener.join()
