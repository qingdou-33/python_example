#-*-coding:utf-8-*-
import xlwt
import re
import os
import matplotlib.pyplot as plt

filepath = 'D:/shanshan/pythoncode/data/ceshi/data'
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('rawData', cell_overwrite_ok=True)
i = 0
for item in os.listdir(filepath):
    #read raw data
    f = open(filepath + '/' + item, "r")
    data = f.readlines()
    f.close()
    #write raw data to worksheet
    row0 = item
    worksheet.write(0,i,row0)
    j = 0
    for j in range(len(data)):
        worksheet.write(j+1,i,data[j])
    i = i+1

worksheet1 = workbook.add_sheet('3-1',cell_overwrite_ok=True)
f = open(filepath + '/' + '3-1-35_Strain.txt')
data = f.readlines()
f.close()
f = open(filepath + '/' + '3-1-325_Strain.txt')
data2 = f.readlines()
f.close()
j = 0
worksheet1.write(0,8,'3-1-35')
worksheet1.write(0,9,'3-1-325')
distance = []
distance2 = []
strain = []
strain2 = []
for j in range(len(data)):
    if j < 13:
        worksheet1.write(j+1,8,data[j])
        worksheet1.write(j+1, 9, data2[j])
    else:
        time_data = data[j].split('\t')
        time_data2 = data2[j].split('\t')
        k = 0
        for k in range(len(time_data)):
            worksheet1.write(j-13,k,time_data[k])
            if k > 0:
                if time_data2[0] == time_data[0]:
                    worksheet1.write(j - 13, 2, time_data2[k])
                else:
                    worksheet1.write(j-13,2,"Not match!")
            #convert string to float
            distance.append(float(time_data[0]))
            distance2.append(float(time_data2[0]))
            strain.append(float(time_data[1]))
            strain2.append(float(time_data2[1]))

#make a plot
fig = plt.figure()
plt.plot(distance,strain,distance,strain2)
fig.savefig('data.jpg')




#     #classify the case
# files = os.listdir(path)
# for file in files:
#     case = re.search(r'[0-9]-[0-9]',filename).group(0)
#     if not os.path.exists(case):
#         os.mkdir(path + '/' + case)



workbook.save('dataAnalysis.xls')


