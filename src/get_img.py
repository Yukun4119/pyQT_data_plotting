import csv
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from chinese_calendar import is_workday, is_holiday


def is_run_year(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


def day_count(year, month, day):
	total_day = 0
	mm = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
	if is_run_year(year):
		mm = [31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
	for i in range(month - 1):
		total_day += mm[i]
	total_day += day
	return total_day



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
	
	site_list = ['千岛湖温馨岛', '金华塘雅', '海宁东方学院', '嘉善善西','绍兴滨海新城','绍兴陈蔡水库','杭州湾湿地','宁波奉化滕头村','金华游埠小学', '台州里石门水库', '省中心']
	eng_site_list = ['QianDaoHuWengXingDao', 'JinHuaTangYa', 'HaiNingDongFangXueYuan', 'JiaShanShanXi', 'ShaoXingBingHaiXinCheng', 'ShaoXingChenCaiShuiKu', 'HangZhouWanShiDi', 'NingBoFengHuaTengTouCun', 'JinHuaYouBuXiaoXue', 'TaiZhouLiShiMenShuiKu', 'ShengZhongXin']
	# material_list = ['3-甲基戊烷','二溴乙烷(ppb)','正己烷(ppb)','2.4-二甲基戊烷(ppb)','苯(ppb)','2.3-二甲基戊烷(ppb)','3-甲基己烷(ppb)','2.2.4-三甲基戊烷(ppb)','正庚烷(ppb)','2.3.4-三甲基戊烷(ppb)','甲基环己烷(ppb)','甲苯(ppb)','2-甲基庚烷(ppb)','3-甲基庚烷(ppb)','正辛烷(ppb)','乙苯(ppb)','间-对二甲苯(ppb)','苯乙烯(ppb)','邻二甲苯(ppb)','正壬烷(ppb)','异丙苯(ppb)','正丙苯(ppb)','间-乙基甲苯(ppb)','对-乙基甲苯(ppb)','1.3.5-三甲苯(ppb)','邻-乙基甲苯(ppb)','1.2.4-三甲苯(ppb)','正癸烷(ppb)','1.2.3-三甲苯(ppb)','十一烷(ppb)','十二烷(ppb)','丙烷(ppb)','丙烯(ppb)','乙炔(ppb)','异丁烷(ppb)','正丁烷(ppb)','反-2-丁烯(ppb)','1-丁烯(ppb)','顺-2-丁烯(ppb)','环戊烷(ppb)','异戊烷(ppb)','正戊烷(ppb)','1.3-丁二烯(ppb)','反-2-戊烯(ppb)','1-戊烯(ppb)','顺-2-戊烯(ppb)','2.2-二甲基丁烷(ppb)','2.3-二甲基丁烷(ppb)','异戊二烯(ppb)','2-甲基戊烷(ppb)','1-己烯(ppb)','环己烷(ppb)','乙烷(ppb)','乙烯(ppb)','1.2-二氯乙烷(ppb)','四氯化碳(ppb)','氯仿(ppb)','三氯乙烯(ppb)','1.1.2-三氯乙烷(ppb)','四氯乙烯(ppb)','氯苯(ppb)','氯乙烯(ppb)','二氯甲烷(ppb)','顺-1.2-二氯乙烯(ppb)','1.3-二氯苯(ppb)','1.2-二氯苯(ppb)','氯乙烷(ppb)','溴甲烷(ppb)','氯甲烷(ppb)','1,1-二氯乙烷(ppb)','1,4-二氯苯(ppb)','氯化苄(ppb)','丙烯醛(ppb)','丙醛(ppb)','丙酮(ppb)','乙醛(ppb)','乙腈(ppb)','甲基叔丁基醚(ppb)','异丁烯醛(ppb)','正丁醛(ppb)','甲基乙烯基酮(ppb)','丁酮(ppb)','2-戊酮(ppb)','戊醛(ppb)','3-戊酮(ppb)','己醛(ppb)','2-甲基己烷(ppb)','间-二乙苯(ppb)','对-二乙苯(ppb)','氟利昂-114(ppb)','氟利昂11(ppb)','氟利昂113(ppb)','二氯乙烯(ppb)','1,1,1-三氯乙烷(ppb)','1,2-二氯丙烷(ppb)','一溴二氯甲烷(ppb)','顺-1,3-二氯丙烯(ppb)','反-1,3-二氯丙烯(ppb)','甲基环戊烷(ppb)']
	out_material_list = ['3-甲基戊烷(ppb)(3-Methylpentane)', '二溴乙烷(ppb)(Dibromoethane)', '正己烷(ppb)(n-Hexane)', '2.4-二甲基戊烷(ppb)(2,4-Dimethylpentane)', '苯(ppb)(Benzene)', '2.3-二甲基戊烷(ppb)(2,3-Dimethylpentane)', '3-甲基己烷(ppb)(3-Methylhexane)', '2.2.4-三甲基戊烷(ppb)(2,2,4-Trimethylpentane)', '正庚烷(ppb)(n-Heptane)', '2.3.4-三甲基戊烷(ppb)(2,3,4-Trimethylpentane)', '甲基环己烷(ppb)(Methylcyclohexane)', '甲苯(ppb)(Toluene)', '2-甲基庚烷(ppb)(2-Methylheptane)', '3-甲基庚烷(ppb)(3-Methylheptane)', '正辛烷(ppb)(n-Octane)', '乙苯(ppb)(Ethylbenzene)', '间-对二甲苯(ppb)(m,p-Xylene)', '苯乙烯(ppb)(Styrene)', '邻二甲苯(ppb)(o-Xylene)', '正壬烷(ppb)(Nonane)', '异丙苯(ppb)(Isopropylbenzene)', '正丙苯(ppb)(n-Propylbenzene)', '间-乙基甲苯(ppb)(m-Ethyltoluene)', '对-乙基甲苯(ppb)(p-Ethyltoluene)', '1.3.5-三甲苯(ppb)(1,3,5-Trimethylbenzene)', '邻-乙基甲苯(ppb)(o-Ethyltoluene)', '1.2.4-三甲苯(ppb)(1,2,4-Trimethylbenzene)', '正癸烷(ppb)(n-Decane)', '1.2.3-三甲苯(ppb)(1,2,3-Trimethylbenzene)', '十一烷(ppb)(Undecane)', '十二烷(ppb)(n-Dodecane)', '丙烷(ppb)(Propane)', '丙烯(ppb)(Propylene)', '乙炔(ppb)(Acetylene)', '异丁烷(ppb)(iso-Butane)', '正丁烷(ppb)(n-Butane)', '反-2-丁烯(ppb)(trans-2-Butene)', '1-丁烯(ppb)(1-Butene)', '顺-2-丁烯(ppb)(cis-2-Butene)', '环戊烷(ppb)(Cyclopentane)', '异戊烷(ppb)(iso-Pentane)', '正戊烷(ppb)(n-Pentane)', '1.3-丁二烯(ppb)(1,3-Butadiene)', '反-2-戊烯(ppb)(trans-2-Pentene)', '1-戊烯(ppb)(1-Pentene)', '顺-2-戊烯(ppb)(cis-2-Pentene)', '2.2-二甲基丁烷(ppb)(2,2-Dimethylbutane)', '2.3-二甲基丁烷(ppb)(2,3-Dimethylbutane)', '异戊二烯(ppb)(Isoprene)', '2-甲基戊烷(ppb)(2-Methylpentane)', '1-己烯(ppb)(1-Hexene)', '环己烷(ppb)(Cyclohexane)', '乙烷(ppb)(Ethane)', '乙烯(ppb)(Ethylene)', '1.2-二氯乙烷(ppb)(1,2-Dichloroethane)', '四氯化碳(ppb)(CarbonTetrachloride)', '氯仿(ppb)(Chloroform)', '三氯乙烯(ppb)(Trichloroethylene)', '1.1.2-三氯乙烷(ppb)(1,1,2-Trichloroethane)', '四氯乙烯(ppb)(Tetrachloroethylene)', '氯苯(ppb)(Chlorobenzene)', '氯乙烯(ppb)(Vinylchloride)', '二氯甲烷(ppb)(MethyleneChloride)', '顺-1.2-二氯乙烯(ppb)(cis-1,2-Dichloroethene)', '1.3-二氯苯(ppb)(1,3-Dichlorobenzene)', '1.2-二氯苯(ppb)(1,2-Dichlorobenzene)', '氯乙烷(ppb)(Chloroethane)', '溴甲烷(ppb)(Bromomethane)', '氯甲烷(ppb)(Chloromethane)', '1,1-二氯乙烷(ppb)(1,1-Dichloroethane)', '1,4-二氯苯(ppb)(1,4-Dichlorobenzene)', '氯化苄(ppb)(BenzylChloride)', '丙烯醛(ppb)(Acrolein)', '丙醛(ppb)(Propanal)', '丙酮(ppb)(Acetone)', '乙醛(ppb)(Acetaldehyde)', '乙腈(ppb)(Acetonitrile)', '甲基叔丁基醚(ppb)(MTBE)', '异丁烯醛(ppb)(Methacrolein)', '正丁醛(ppb)(n-Butanal)', '甲基乙烯基酮(ppb)(Methyl vinyl ketone)', '丁酮(ppb)(Butanone)', '2-戊酮(ppb)(2-Pentanone)', '戊醛(ppb)(Pentanal)', '3-戊酮(ppb)(3-Pentanone)', '己醛(ppb)(Hexanal)', '2-甲基己烷(ppb)(2-Methylhexane)', '间-二乙苯(ppb)(m-Diethylbenzene)', '对-二乙苯(ppb)(p-Diethylbenzene)', '氟利昂-114(ppb)(Freon-114)', '氟利昂11(ppb)(Freon-11)', '氟利昂113(ppb)(Freon-113)', '二氯乙烯(ppb)(Dichloroethene)', '1,1,1-三氯乙烷(ppb)(1,1,1-Trichloroethane)', '1,2-二氯丙烷(ppb)(1,2-Dichloropropane)', '一溴二氯甲烷(ppb)(Bromodichloromethane)', '顺-1,3-二氯丙烯(ppb)(cis-1,3-Dichloropropene)', '反-1,3-二氯丙烯(ppb)(trans-1,3-Dichloropropene)', '甲基环戊烷(ppb)(Methylcyclopentane)']
	eng_material_list = ['3-Methylpentane', 'Dibromoethane', 'n-Hexane', '2,4-Dimethylpentane', 'Benzene', '2,3-Dimethylpentane', '3-Methylhexane', '2,2,4-Trimethylpentane', 'n-Heptane', '2,3,4-Trimethylpentane', 'Methylcyclohexane', 'Toluene', '2-Methylheptane', '3-Methylheptane', 'n-Octane', 'Ethylbenzene', 'm,p-Xylene', 'Styrene', 'o-Xylene', 'Nonane', 'Isopropylbenzene', 'n-Propylbenzene', 'm-Ethyltoluene', 'p-Ethyltoluene', '1,3,5-Trimethylbenzene', 'o-Ethyltoluene', '1,2,4-Trimethylbenzene', 'n-Decane', '1,2,3-Trimethylbenzene', 'Undecane', 'n-Dodecane', 'Propane', 'Propylene', 'Acetylene', 'iso-Butane', 'n-Butane', 'trans-2-Butene', '1-Butene', 'cis-2-Butene', 'Cyclopentane', 'iso-Pentane', 'n-Pentane', '1,3-Butadiene', 'trans-2-Pentene', '1-Pentene', 'cis-2-Pentene', '2,2-Dimethylbutane', '2,3-Dimethylbutane', 'Isoprene', '2-Methylpentane', '1-Hexene', 'Cyclohexane', 'Ethane', 'Ethylene', '1,2-Dichloroethane', 'CarbonTetrachloride', 'Chloroform', 'Trichloroethylene', '1,1,2-Trichloroethane', 'Tetrachloroethylene', 'Chlorobenzene', 'Vinylchloride', 'MethyleneChloride', 'cis-1,2-Dichloroethene', '1,3-Dichlorobenzene', '1,2-Dichlorobenzene', 'Chloroethane', 'Bromomethane', 'Chloromethane', '1,1-Dichloroethane', '1,4-Dichlorobenzene', 'BenzylChloride', 'Acrolein', 'Propanal', 'Acetone', 'Acetaldehyde', 'Acetonitrile', 'MTBE', 'Methacrolein', 'n-Butanal', 'Methyl vinyl ketone', 'Butanone', '2-Pentanone', 'Pentanal', '3-Pentanone', 'Hexanal', '2-Methylhexane', 'm-Diethylbenzene', 'p-Diethylbenzene', 'Freon-114', 'Freon-11', 'Freon-113', 'Dichloroethene', '1,1,1-Trichloroethane', '1,2-Dichloropropane', 'Bromodichloromethane', 'cis-1,3-Dichloropropene', 'trans-1,3-Dichloropropene', 'Methylcyclopentane']

# get small csv
	path = "./resources/data/%s-%s-%d-%d-%d.csv"%(site_list[s-1],out_material_list[m-1], year_index + 2015, month_s_index, month_e_index)
	with open(path,'w') as f:
		csv_write = csv.writer(f)
		b = ['time','material']
		csv_write.writerow(b)
		index = 0
		for it in time_list:
			data_flow = [it,material_list[index]]
			csv_write.writerow(data_flow)
			index += 1

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
			year_day = 365
			if is_run_year(int(year)):
				year_day = 366
			ratio = day_count(int(year),int(month),int(day)) / year_day
			# ratio = "%.4f"%ratio
			
			if is_workday(date):
				weekday_x.append(float(ratio) + year)
				weekday_y.append(material_list[i])
			else:
				weekend_x.append(float(ratio) + year)
				weekend_y.append(material_list[i])


		wkd = plt.scatter(weekday_x, weekday_y, s=8.,  color = 'red')
		wke = plt.scatter(weekend_x, weekend_y, s=8., color = 'blue')
		plt.legend(handles=[wkd,wke],labels=['weekday','weekend'],loc='best')

	elif mode_index == 1:
		day_time_x = []
		day_time_y = []
		night_time_x = []
		night_time_y = []
		for i in range(len(material_list)):

			year = int(Year_month[i][0:4])
			month = int(Year_month[i][5:7])
			day = int(Year_month[i][8:10])
			date = datetime.datetime(year, month, day)
			year_day = 365
			if is_run_year(int(year)):
				year_day = 366
			ratio = day_count(int(year),int(month),int(day)) / year_day
			# ratio = "%.4f"%ratio

			hour = int(Year_month[i][12])
			# print(hour)
			if hour >= 6 and hour <= 18:
				day_time_x.append(float(ratio) + year)
				day_time_y.append(material_list[i])
			else:
				night_time_x.append(float(ratio) + year)
				night_time_y.append(material_list[i])

		day = plt.scatter(day_time_x, day_time_y, s=8.,  color = 'green')
		night = plt.scatter(night_time_x, night_time_y, s=8., color = 'black')
		plt.legend(handles=[day,night],labels=['day','night'],loc='best')

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
			year = int(Year_month[i][0:4])
			month = int(Year_month[i][5:7])
			day = int(Year_month[i][8:10])
			date = datetime.datetime(year, month, day)
			year_day = 365
			if is_run_year(int(year)):
				year_day = 366
			ratio = day_count(int(year),int(month),int(day)) / year_day
			# ratio = "%.4f"%ratio
			
			if 3 <= month <= 5:
				spring_x.append(float(ratio) + year)
				spring_y.append(material_list[i])
			elif 6 <= month <= 8:
				summer_x.append(float(ratio) + year)
				summer_y.append(material_list[i])
			elif 9 <= month <= 11:
				fall_x.append(float(ratio) + year)
				fall_y.append(material_list[i])
			else:
				winter_x.append(float(ratio) + year)
				winter_y.append(material_list[i])


		spring = plt.scatter(spring_x, spring_y, s=8.,  color = 'green')
		summer = plt.scatter(summer_x, summer_y, s=8., color = 'red')
		fall = plt.scatter(fall_x, fall_y, s =8., color = 'orange')
		winter = plt.scatter(winter_x, winter_y, s =8., color = 'blue')
		plt.legend(handles=[spring,summer,fall,winter],labels=['spring','summer','fall','winter'],loc='best')


	
	plt.title('%s-(%s)'%(eng_material_list[m-1], eng_site_list[s-1]), fontsize='large',fontweight='bold') 

	plt.ylabel('Concentration(ppb)')
	plt.xlabel('Time')
	plt.savefig("./resources/img/%s-%s-%d-%d-%d.jpg"%(site_list[s-1],out_material_list[m-1], year_index + 2015, month_s_index, month_e_index))
	
	# plt.show()
	plt.cla()
		

if __name__ == '__main__':
	get_img(1,1, "all", "all")




