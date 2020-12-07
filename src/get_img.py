import csv
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from chinese_calendar import is_workday, is_holiday

# from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def get_img(s = 1, m = 1, year_index = 0, month_s_index = 0, month_e_index = 0, mode_index = 0):
	with open('../pyQT_data/data/%d.csv'%(int(s)),'r') as csvfile:
	    data = csv.reader(csvfile)
	    time_list = [row[2] for row in data]
	with open('../pyQT_data/data/%d.csv'%(int(s)),'r') as csvfile:
		data = csv.reader(csvfile)
		material_list = [row[3+int(m)] for row in data]

	print("y_label: ", material_list[0])
	print("x_label: ", time_list[0])


	index = 0
	for i in range(len(material_list)):
		if not is_number(material_list[i]):
			continue
		else:
			material_list[index] = float(material_list[i])
			time_list[index] = time_list[i]
			index += 1

	material_list = material_list[:index]
	time_list = time_list[:index]

	# choose time
	query = ""
	if year_index != 0:
		query += str(year_index + 2015)

	index = 0
	if month_s_index == 0 or month_e_index == 0:
		for i in range(len(time_list)):
			if query in time_list[i]:
					time_list[index] = time_list[i]
					material_list[index] = float(material_list[i])
					index += 1

	else:
		year_query = query
		for i in range(len(time_list)):
			for month in range(month_s_index, month_e_index + 1):
				if month < 10:
					year_month_query = year_query + '-0'+ str(month)
				else:
					year_month_query = year_query + '-'+ str(month)
				if year_month_query in time_list[i]:
					time_list[index] = time_list[i]
					material_list[index] = float(material_list[i])
					index += 1

	time_list = time_list[:index]
	material_list = material_list[:index]


	Year_month = []
	for i in time_list:
		Year_month.append(i)

	
	if mode_index == 0:
		weekday_x = []
		weekday_y = []
		weekend_x = []
		weekend_y = []
		for i in range(len(material_list)):
			year = int(Year_month[i][0:4])
			month = int(Year_month[i][5:7])
			day = int(Year_month[i][8:10])
			date = datetime.datetime(year, month, day)
			if is_workday(date):
				weekday_x.append(i)
				weekday_y.append(material_list[i])
			else:
				weekend_x.append(i)
				weekend_y.append(material_list[i])


		plt.scatter(weekday_x, weekday_y, s=8.,  color = 'red')
		plt.scatter(weekend_x, weekend_y, s=8., color = 'blue')
		


	elif mode_index == 1:
		day_time_x = []
		day_time_y = []
		night_time_x = []
		night_time_y = []
		for i in range(len(material_list)):
			hour = int(Year_month[i][12])
			# print(hour)
			if hour >= 6 and hour <= 18:
				day_time_x.append(i)
				day_time_y.append(material_list[i])
			else:
				night_time_x.append(i)
				night_time_y.append(material_list[i])

		plt.scatter(day_time_x, day_time_y, s=8.,  color = 'green')
		plt.scatter(night_time_x, night_time_y, s=8., color = 'black')

	elif mode_index == 2:
		spring_x = []
		spring_y = []
		summer_x = []
		summer_y = []
		fall_x = []
		fall_y = []
		winter_x = []
		winter_y = []

		for i in range(len(material_list)):
			month = int(Year_month[i][5:7])
			print(month)
			if 1 <= month <= 3:
				spring_x.append(i)
				spring_y.append(material_list[i])
			elif 4 <= month <= 6:
				summer_x.append(i)
				summer_y.append(material_list[i])
			elif 7 <= month <= 9:
				fall_x.append(i)
				fall_y.append(material_list[i])
			else:
				winter_x.append(i)
				winter_y.append(material_list[i])


		plt.scatter(spring_x, spring_y, s=8.,  color = 'green')
		plt.scatter(summer_x, summer_y, s=8., color = 'red')
		plt.scatter(fall_x, fall_y, s =8., color = 'orange')
		plt.scatter(winter_x, winter_y, s =8., color = 'blue')


	site_list = ['千岛湖温馨岛', '金华塘雅', '海宁东方学院', '嘉善善西','绍兴滨海新城','绍兴陈蔡水库','杭州湾湿地','宁波奉化滕头村','金华游埠小学', '台州里石门水库', '省中心']
	# material_list = ['3-甲基戊烷','二溴乙烷(ppb)','正己烷(ppb)','2.4-二甲基戊烷(ppb)','苯(ppb)','2.3-二甲基戊烷(ppb)','3-甲基己烷(ppb)','2.2.4-三甲基戊烷(ppb)','正庚烷(ppb)','2.3.4-三甲基戊烷(ppb)','甲基环己烷(ppb)','甲苯(ppb)','2-甲基庚烷(ppb)','3-甲基庚烷(ppb)','正辛烷(ppb)','乙苯(ppb)','间-对二甲苯(ppb)','苯乙烯(ppb)','邻二甲苯(ppb)','正壬烷(ppb)','异丙苯(ppb)','正丙苯(ppb)','间-乙基甲苯(ppb)','对-乙基甲苯(ppb)','1.3.5-三甲苯(ppb)','邻-乙基甲苯(ppb)','1.2.4-三甲苯(ppb)','正癸烷(ppb)','1.2.3-三甲苯(ppb)','十一烷(ppb)','十二烷(ppb)','丙烷(ppb)','丙烯(ppb)','乙炔(ppb)','异丁烷(ppb)','正丁烷(ppb)','反-2-丁烯(ppb)','1-丁烯(ppb)','顺-2-丁烯(ppb)','环戊烷(ppb)','异戊烷(ppb)','正戊烷(ppb)','1.3-丁二烯(ppb)','反-2-戊烯(ppb)','1-戊烯(ppb)','顺-2-戊烯(ppb)','2.2-二甲基丁烷(ppb)','2.3-二甲基丁烷(ppb)','异戊二烯(ppb)','2-甲基戊烷(ppb)','1-己烯(ppb)','环己烷(ppb)','乙烷(ppb)','乙烯(ppb)','1.2-二氯乙烷(ppb)','四氯化碳(ppb)','氯仿(ppb)','三氯乙烯(ppb)','1.1.2-三氯乙烷(ppb)','四氯乙烯(ppb)','氯苯(ppb)','氯乙烯(ppb)','二氯甲烷(ppb)','顺-1.2-二氯乙烯(ppb)','1.3-二氯苯(ppb)','1.2-二氯苯(ppb)','氯乙烷(ppb)','溴甲烷(ppb)','氯甲烷(ppb)','1,1-二氯乙烷(ppb)','1,4-二氯苯(ppb)','氯化苄(ppb)','丙烯醛(ppb)','丙醛(ppb)','丙酮(ppb)','乙醛(ppb)','乙腈(ppb)','甲基叔丁基醚(ppb)','异丁烯醛(ppb)','正丁醛(ppb)','甲基乙烯基酮(ppb)','丁酮(ppb)','2-戊酮(ppb)','戊醛(ppb)','3-戊酮(ppb)','己醛(ppb)','2-甲基己烷(ppb)','间-二乙苯(ppb)','对-二乙苯(ppb)','氟利昂-114(ppb)','氟利昂11(ppb)','氟利昂113(ppb)','二氯乙烯(ppb)','1,1,1-三氯乙烷(ppb)','1,2-二氯丙烷(ppb)','一溴二氯甲烷(ppb)','顺-1,3-二氯丙烯(ppb)','反-1,3-二氯丙烯(ppb)','甲基环戊烷(ppb)']
	material_list = ['3-甲基戊烷(ppb)(3-Methylpentane)', '二溴乙烷(ppb)(Dibromoethane)', '正己烷(ppb)(n-Hexane)', '2.4-二甲基戊烷(ppb)(2,4-Dimethylpentane)', '苯(ppb)(Benzene)', '2.3-二甲基戊烷(ppb)(2,3-Dimethylpentane)', '3-甲基己烷(ppb)(3-Methylhexane)', '2.2.4-三甲基戊烷(ppb)(2,2,4-Trimethylpentane)', '正庚烷(ppb)(n-Heptane)', '2.3.4-三甲基戊烷(ppb)(2,3,4-Trimethylpentane)', '甲基环己烷(ppb)(Methylcyclohexane)', '甲苯(ppb)(Toluene)', '2-甲基庚烷(ppb)(2-Methylheptane)', '3-甲基庚烷(ppb)(3-Methylheptane)', '正辛烷(ppb)(n-Octane)', '乙苯(ppb)(Ethylbenzene)', '间-对二甲苯(ppb)(m,p-Xylene)', '苯乙烯(ppb)(Styrene)', '邻二甲苯(ppb)(o-Xylene)', '正壬烷(ppb)(Nonane)', '异丙苯(ppb)(Isopropylbenzene)', '正丙苯(ppb)(n-Propylbenzene)', '间-乙基甲苯(ppb)(m-Ethyltoluene)', '对-乙基甲苯(ppb)(p-Ethyltoluene)', '1.3.5-三甲苯(ppb)(1,3,5-Trimethylbenzene)', '邻-乙基甲苯(ppb)(o-Ethyltoluene)', '1.2.4-三甲苯(ppb)(1,2,4-Trimethylbenzene)', '正癸烷(ppb)(n-Decane)', '1.2.3-三甲苯(ppb)(1,2,3-Trimethylbenzene)', '十一烷(ppb)(Undecane)', '十二烷(ppb)(n-Dodecane)', '丙烷(ppb)(Propane)', '丙烯(ppb)(Propylene)', '乙炔(ppb)(Acetylene)', '异丁烷(ppb)(iso-Butane)', '正丁烷(ppb)(n-Butane)', '反-2-丁烯(ppb)(trans-2-Butene)', '1-丁烯(ppb)(1-Butene)', '顺-2-丁烯(ppb)(cis-2-Butene)', '环戊烷(ppb)(Cyclopentane)', '异戊烷(ppb)(iso-Pentane)', '正戊烷(ppb)(n-Pentane)', '1.3-丁二烯(ppb)(1,3-Butadiene)', '反-2-戊烯(ppb)(trans-2-Pentene)', '1-戊烯(ppb)(1-Pentene)', '顺-2-戊烯(ppb)(cis-2-Pentene)', '2.2-二甲基丁烷(ppb)(2,2-Dimethylbutane)', '2.3-二甲基丁烷(ppb)(2,3-Dimethylbutane)', '异戊二烯(ppb)(Isoprene)', '2-甲基戊烷(ppb)(2-Methylpentane)', '1-己烯(ppb)(1-Hexene)', '环己烷(ppb)(Cyclohexane)', '乙烷(ppb)(Ethane)', '乙烯(ppb)(Ethylene)', '1.2-二氯乙烷(ppb)(1,2-Dichloroethane)', '四氯化碳(ppb)(CarbonTetrachloride)', '氯仿(ppb)(Chloroform)', '三氯乙烯(ppb)(Trichloroethylene)', '1.1.2-三氯乙烷(ppb)(1,1,2-Trichloroethane)', '四氯乙烯(ppb)(Tetrachloroethylene)', '氯苯(ppb)(Chlorobenzene)', '氯乙烯(ppb)(Vinylchloride)', '二氯甲烷(ppb)(MethyleneChloride)', '顺-1.2-二氯乙烯(ppb)(cis-1,2-Dichloroethene)', '1.3-二氯苯(ppb)(1,3-Dichlorobenzene)', '1.2-二氯苯(ppb)(1,2-Dichlorobenzene)', '氯乙烷(ppb)(Chloroethane)', '溴甲烷(ppb)(Bromomethane)', '氯甲烷(ppb)(Chloromethane)', '1,1-二氯乙烷(ppb)(1,1-Dichloroethane)', '1,4-二氯苯(ppb)(1,4-Dichlorobenzene)', '氯化苄(ppb)(BenzylChloride)', '丙烯醛(ppb)(Acrolein)', '丙醛(ppb)(Propanal)', '丙酮(ppb)(Acetone)', '乙醛(ppb)(Acetaldehyde)', '乙腈(ppb)(Acetonitrile)', '甲基叔丁基醚(ppb)(MTBE)', '异丁烯醛(ppb)(Methacrolein)', '正丁醛(ppb)(n-Butanal)', '甲基乙烯基酮(ppb)(Methyl vinyl ketone)', '丁酮(ppb)(Butanone)', '2-戊酮(ppb)(2-Pentanone)', '戊醛(ppb)(Pentanal)', '3-戊酮(ppb)(3-Pentanone)', '己醛(ppb)(Hexanal)', '2-甲基己烷(ppb)(2-Methylhexane)', '间-二乙苯(ppb)(m-Diethylbenzene)', '对-二乙苯(ppb)(p-Diethylbenzene)', '氟利昂-114(ppb)(Freon-114)', '氟利昂11(ppb)(Freon-11)', '氟利昂113(ppb)(Freon-113)', '二氯乙烯(ppb)(Dichloroethene)', '1,1,1-三氯乙烷(ppb)(1,1,1-Trichloroethane)', '1,2-二氯丙烷(ppb)(1,2-Dichloropropane)', '一溴二氯甲烷(ppb)(Bromodichloromethane)', '顺-1,3-二氯丙烯(ppb)(cis-1,3-Dichloropropene)', '反-1,3-二氯丙烯(ppb)(trans-1,3-Dichloropropene)', '甲基环戊烷(ppb)(Methylcyclopentane)']
	# plt.title('%s-%s'%(site_list[s-1], material_list[m-1]),fontproperties = 'SimHei', fontsize='large',fontweight='bold') 
	plt.savefig("./resources/img/%s-%s-%d-%d-%d.jpg"%(site_list[s-1],material_list[m-1], year_index + 2015, month_s_index, month_e_index))
	
	# plt.show()
	plt.cla()
		

if __name__ == '__main__':
	get_img(1,1, "all", "all")




