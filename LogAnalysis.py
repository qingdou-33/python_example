#this is for analyzing log data file which is from customer.
#coding:gbk
import re
import xlwt
import os

def set_style(name,height,bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	style.font = font
	return style

Filename = input("Please enter the file name with full path:")
filename = re.findall(r'/[0-9a-zA-Z]+[.][0-9a-zA-Z]+',Filename)[-1].strip('/').replace('.','_')

try:
	Result = os.path.exists(Filename)
	current_dir = os.path.dirname(Filename)
	New_File = current_dir + '/' + filename + '.xls'
except:
	print("No such file in category!")

if Result == True:	
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('rawData',cell_overwrite_ok=True)
	worksheeta = workbook.add_sheet('analysis',cell_overwrite_ok=True)
	f = open(Filename,"r")
	data = f.readlines()
	f.close()
	worksheeta.col(1).width  = 256*15
	worksheeta.col(2).width  = 256*20
	worksheeta.col(3).width  = 256*15
	#write raw data to sheet 1
	i = 0
	for i in range(len(data)):
		worksheet.write(i,0,data[i])

	#write table header to sheet 2	
	row0 = ["Date","Time","delta t/ms","resonse/request","Command/Feedback"]
	i = 0
	for i in range(0,len(row0)):
		worksheeta.write(0,i,row0[i],set_style("Times New Roman",300,True))
	
	#classify the data, 
	j = 0
	k = 1
	while(j<=len(data)):
		try:
			req = re.search(r'data request|data response',data[j])
			ang = re.search(r'<( [a-z0-9A-Z]{2}){2,22}>',data[j])
			day = re.search(r'\d+', data[j])
			time = re.search(r'\d+\.\d+', data[j])
			worksheeta.write(k,0,day.group(0))
			worksheeta.write(k,1,time.group(0))
			worksheeta.write(k,3,req.group(0))
			worksheeta.write(k,4,ang.group(0))
			if k == 1:
				time_past = time.group(0)
			else:		
				worksheeta.write(k,2,str(1000*(float(time.group(0)) - float(time_past))))
				time_past = time.group(0)
			
			k = k+1
			j = j+1
		except:
			j = j+1
	
	workbook.save(New_File)	

	
