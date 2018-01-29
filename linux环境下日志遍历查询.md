配置文件：（.txt）

#日志所在目录
logCotents="/opt/smb/tribelogs/153;/opt/smb/tribelogs/154;/opt/smb/tribelogs/164;/opt/smb/tribelogs/165;/opt/smb/tribelogs/171;/opt/smb/tribelogs/180;/opt/smb/tribelogs/181;/opt/smb/tribelogs/182;/opt/smb/tribelogs/183;/opt/smb/tribelogs/184;/opt/smb/tribelogs/185;/opt/smb/tribelogs/187;/opt/smb/tribelogs/188;/opt/smb/tribelogs/189;/opt/smb/tribelogs/190;/opt/smb/tribelogs/191;"
#日志解压缩需要的目录
remoteWenjian ="/opt/zhj"
#日志文件的名字
fileName = "catalina.2018-01-18.out"
#查询指令集
orderMap = "grep 201801180005159837"
#压缩文件夹名称
fileRar = "catalina.2018-01-18.out.tar.gz"


源码：


#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

try:
	f= open('config.txt','r+')
	list1 =f.readlines()
	# print(list1)
	for i in range(0,len(list1)):
		list1[i] =list1[i].strip('\n')
		logCotentsLine = list1[i].find('logCotents')
		remoteWenjianLine = list1[i].find('remoteWenjian')
		fileNameLine = list1[i].find('fileName')
		orderMapLine = list1[i].find('orderMap')
		fileRarLine = list1[i].find('fileRar')
		# print(logCotentsLine)

		if logCotentsLine>-1:
			start = list1[i].find('"')
			end = list1[i].find('"',start+1)
			logCotents = list1[i][start+1:end]
			print(logCotents)
		if remoteWenjianLine>-1:
			start = list1[i].find('"')
			end = list1[i].find('"',start+1)
			remoteWenjian = list1[i][start+1:end]
			print(remoteWenjian)
		if fileNameLine>-1:
			start = list1[i].find('"')
			end = list1[i].find('"',start+1)
			fileName = list1[i][start+1:end]
			print(fileName)
		if orderMapLine>-1:
			start = list1[i].find('"')
			end = list1[i].find('"',start+1)
			orderMap = list1[i][start+1:end]
			print(orderMap)
		if fileRarLine>-1:
			start = list1[i].find('"')
			end = list1[i].find('"',start+1)
			fileRar = list1[i][start+1:end]
			print(fileRar)
finally:
	if f:
		f.close()




# logCotents = "/opt"

# remoteWenjian ='/opt/ceshi'
# fileName = 'ceshi.txt'

# orderMap = "grep 'FATAL EXCEPTION IN SYSTEM PROCESS'"

# fileRar = 'ceshi.tar.gz'

command2 = 'cp '+fileRar+' '+remoteWenjian
command3 = 'cd '+remoteWenjian
command4 = 'tar -zxvf '+fileRar
command6 = 'rm -rf '+fileRar
command7 = 'rm -rf '+fileName
logCotents = logCotents.split(';')
for obj in logCotents:
	try:
		print(obj)
		command1 = 'cd '+obj
		# command5 = orderMap+" "+fileName+" >"+obj.replace('/','-')+fileName
		command5 = orderMap+" "+fileName+" >>"+'a'+fileName
		commands =command1+';'+command2+';'+command3 +';'+command4 +';'+command5 +';'+command6 +';'+command7  
		subprocess.call(commands, shell=True)
	except:
		print('no find')



