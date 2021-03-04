#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import src.get_img as gi

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.resize(1000, 800)
        self.setWindowTitle("demo")
        self.label = QLabel(self)
        self.label.setFixedSize(900, 400)
        self.label.move(50, 370)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        # 实例化QComBox对象
        self.site = QtWidgets.QComboBox(self)
        self.site.move(100, 100)
        # 多个添加条目
        self.site_list = ['千岛湖温馨岛', '金华塘雅', '海宁东方学院', '嘉善善西','绍兴滨海新城','绍兴陈蔡水库','杭州湾湿地','宁波奉化滕头村','金华游埠小学', '台州里石门水库', '省中心']
        # self.site.addItems(['千岛湖温馨岛', '金华塘雅', '海宁东方学院', '嘉善善西','绍兴滨海新城','绍兴陈蔡水库','杭州湾湿地','宁波奉化滕头村','金华游埠小学', '台州里石门水库', '省中心'])
        self.site.addItems(self.site_list)

        self.material = QtWidgets.QComboBox(self)
        self.material.move(100, 150)

        # 单个添加条目
        # ['3-甲基戊烷','二溴乙烷(ppb)','正己烷(ppb)','2.4-二甲基戊烷(ppb)','苯(ppb)','2.3-二甲基戊烷(ppb)','3-甲基己烷(ppb)','2.2.4-三甲基戊烷(ppb)','正庚烷(ppb)','2.3.4-三甲基戊烷(ppb)','甲基环己烷(ppb)','甲苯(ppb)','2-甲基庚烷(ppb)','3-甲基庚烷(ppb)','正辛烷(ppb)','乙苯(ppb)','间-对二甲苯(ppb)','苯乙烯(ppb)','邻二甲苯(ppb)','正壬烷(ppb)','异丙苯(ppb)','正丙苯(ppb)','间-乙基甲苯(ppb)','对-乙基甲苯(ppb)','1.3.5-三甲苯(ppb)','邻-乙基甲苯(ppb)','1.2.4-三甲苯(ppb)','正癸烷(ppb)','1.2.3-三甲苯(ppb)','十一烷(ppb)','十二烷(ppb)','丙烷(ppb)','丙烯(ppb)','乙炔(ppb)','异丁烷(ppb)','正丁烷(ppb)','反-2-丁烯(ppb)','1-丁烯(ppb)','顺-2-丁烯(ppb)','环戊烷(ppb)','异戊烷(ppb)','正戊烷(ppb)','1.3-丁二烯(ppb)','反-2-戊烯(ppb)','1-戊烯(ppb)','顺-2-戊烯(ppb)','2.2-二甲基丁烷(ppb)','2.3-二甲基丁烷(ppb)','异戊二烯(ppb)','2-甲基戊烷(ppb)','1-己烯(ppb)','环己烷(ppb)','乙烷(ppb)','乙烯(ppb)','1.2-二氯乙烷(ppb)','四氯化碳(ppb)','氯仿(ppb)','三氯乙烯(ppb)','1.1.2-三氯乙烷(ppb)','四氯乙烯(ppb)','氯苯(ppb)','氯乙烯(ppb)','二氯甲烷(ppb)','顺-1.2-二氯乙烯(ppb)','1.3-二氯苯(ppb)','1.2-二氯苯(ppb)','氯乙烷(ppb)','溴甲烷(ppb)','氯甲烷(ppb)','1,1-二氯乙烷(ppb)','1,4-二氯苯(ppb)','氯化苄(ppb)','丙烯醛(ppb)','丙醛(ppb)','丙酮(ppb)','乙醛(ppb)','乙腈(ppb)','甲基叔丁基醚(ppb)','异丁烯醛(ppb)','正丁醛(ppb)','甲基乙烯基酮(ppb)','丁酮(ppb)','2-戊酮(ppb)','戊醛(ppb)','3-戊酮(ppb)','己醛(ppb)','2-甲基己烷(ppb)','间-二乙苯(ppb)','对-二乙苯(ppb)','氟利昂-114(ppb)','氟利昂11(ppb)','氟利昂113(ppb)','二氯乙烯(ppb)','1,1,1-三氯乙烷(ppb)','1,2-二氯丙烷(ppb)','一溴二氯甲烷(ppb)','顺-1,3-二氯丙烯(ppb)','反-1,3-二氯丙烯(ppb)','甲基环戊烷(ppb)']
        self.material_list = ['3-甲基戊烷(ppb)(3-Methylpentane)', '二溴乙烷(ppb)(Dibromoethane)', '正己烷(ppb)(n-Hexane)', '2.4-二甲基戊烷(ppb)(2,4-Dimethylpentane)', '苯(ppb)(Benzene)', '2.3-二甲基戊烷(ppb)(2,3-Dimethylpentane)', '3-甲基己烷(ppb)(3-Methylhexane)', '2.2.4-三甲基戊烷(ppb)(2,2,4-Trimethylpentane)', '正庚烷(ppb)(n-Heptane)', '2.3.4-三甲基戊烷(ppb)(2,3,4-Trimethylpentane)', '甲基环己烷(ppb)(Methylcyclohexane)', '甲苯(ppb)(Toluene)', '2-甲基庚烷(ppb)(2-Methylheptane)', '3-甲基庚烷(ppb)(3-Methylheptane)', '正辛烷(ppb)(n-Octane)', '乙苯(ppb)(Ethylbenzene)', '间-对二甲苯(ppb)(m,p-Xylene)', '苯乙烯(ppb)(Styrene)', '邻二甲苯(ppb)(o-Xylene)', '正壬烷(ppb)(Nonane)', '异丙苯(ppb)(Isopropylbenzene)', '正丙苯(ppb)(n-Propylbenzene)', '间-乙基甲苯(ppb)(m-Ethyltoluene)', '对-乙基甲苯(ppb)(p-Ethyltoluene)', '1.3.5-三甲苯(ppb)(1,3,5-Trimethylbenzene)', '邻-乙基甲苯(ppb)(o-Ethyltoluene)', '1.2.4-三甲苯(ppb)(1,2,4-Trimethylbenzene)', '正癸烷(ppb)(n-Decane)', '1.2.3-三甲苯(ppb)(1,2,3-Trimethylbenzene)', '十一烷(ppb)(Undecane)', '十二烷(ppb)(n-Dodecane)', '丙烷(ppb)(Propane)', '丙烯(ppb)(Propylene)', '乙炔(ppb)(Acetylene)', '异丁烷(ppb)(iso-Butane)', '正丁烷(ppb)(n-Butane)', '反-2-丁烯(ppb)(trans-2-Butene)', '1-丁烯(ppb)(1-Butene)', '顺-2-丁烯(ppb)(cis-2-Butene)', '环戊烷(ppb)(Cyclopentane)', '异戊烷(ppb)(iso-Pentane)', '正戊烷(ppb)(n-Pentane)', '1.3-丁二烯(ppb)(1,3-Butadiene)', '反-2-戊烯(ppb)(trans-2-Pentene)', '1-戊烯(ppb)(1-Pentene)', '顺-2-戊烯(ppb)(cis-2-Pentene)', '2.2-二甲基丁烷(ppb)(2,2-Dimethylbutane)', '2.3-二甲基丁烷(ppb)(2,3-Dimethylbutane)', '异戊二烯(ppb)(Isoprene)', '2-甲基戊烷(ppb)(2-Methylpentane)', '1-己烯(ppb)(1-Hexene)', '环己烷(ppb)(Cyclohexane)', '乙烷(ppb)(Ethane)', '乙烯(ppb)(Ethylene)', '1.2-二氯乙烷(ppb)(1,2-Dichloroethane)', '四氯化碳(ppb)(CarbonTetrachloride)', '氯仿(ppb)(Chloroform)', '三氯乙烯(ppb)(Trichloroethylene)', '1.1.2-三氯乙烷(ppb)(1,1,2-Trichloroethane)', '四氯乙烯(ppb)(Tetrachloroethylene)', '氯苯(ppb)(Chlorobenzene)', '氯乙烯(ppb)(Vinylchloride)', '二氯甲烷(ppb)(MethyleneChloride)', '顺-1.2-二氯乙烯(ppb)(cis-1,2-Dichloroethene)', '1.3-二氯苯(ppb)(1,3-Dichlorobenzene)', '1.2-二氯苯(ppb)(1,2-Dichlorobenzene)', '氯乙烷(ppb)(Chloroethane)', '溴甲烷(ppb)(Bromomethane)', '氯甲烷(ppb)(Chloromethane)', '1,1-二氯乙烷(ppb)(1,1-Dichloroethane)', '1,4-二氯苯(ppb)(1,4-Dichlorobenzene)', '氯化苄(ppb)(BenzylChloride)', '丙烯醛(ppb)(Acrolein)', '丙醛(ppb)(Propanal)', '丙酮(ppb)(Acetone)', '乙醛(ppb)(Acetaldehyde)', '乙腈(ppb)(Acetonitrile)', '甲基叔丁基醚(ppb)(MTBE)', '异丁烯醛(ppb)(Methacrolein)', '正丁醛(ppb)(n-Butanal)', '甲基乙烯基酮(ppb)(Methyl vinyl ketone)', '丁酮(ppb)(Butanone)', '2-戊酮(ppb)(2-Pentanone)', '戊醛(ppb)(Pentanal)', '3-戊酮(ppb)(3-Pentanone)', '己醛(ppb)(Hexanal)', '2-甲基己烷(ppb)(2-Methylhexane)', '间-二乙苯(ppb)(m-Diethylbenzene)', '对-二乙苯(ppb)(p-Diethylbenzene)', '氟利昂-114(ppb)(Freon-114)', '氟利昂11(ppb)(Freon-11)', '氟利昂113(ppb)(Freon-113)', '二氯乙烯(ppb)(Dichloroethene)', '1,1,1-三氯乙烷(ppb)(1,1,1-Trichloroethane)', '1,2-二氯丙烷(ppb)(1,2-Dichloropropane)', '一溴二氯甲烷(ppb)(Bromodichloromethane)', '顺-1,3-二氯丙烯(ppb)(cis-1,3-Dichloropropene)', '反-1,3-二氯丙烯(ppb)(trans-1,3-Dichloropropene)', '甲基环戊烷(ppb)(Methylcyclopentane)']
        # self.material.addItems(['3-甲基戊烷','二溴乙烷(ppb)','正己烷(ppb)','2.4-二甲基戊烷(ppb)','苯(ppb)','2.3-二甲基戊烷(ppb)','3-甲基己烷(ppb)','2.2.4-三甲基戊烷(ppb)','正庚烷(ppb)','2.3.4-三甲基戊烷(ppb)','甲基环己烷(ppb)','甲苯(ppb)','2-甲基庚烷(ppb)','3-甲基庚烷(ppb)','正辛烷(ppb)','乙苯(ppb)','间-对二甲苯(ppb)','苯乙烯(ppb)','邻二甲苯(ppb)','正壬烷(ppb)','异丙苯(ppb)','正丙苯(ppb)','间-乙基甲苯(ppb)','对-乙基甲苯(ppb)','1.3.5-三甲苯(ppb)','邻-乙基甲苯(ppb)','1.2.4-三甲苯(ppb)','正癸烷(ppb)','1.2.3-三甲苯(ppb)','十一烷(ppb)','十二烷(ppb)','丙烷(ppb)','丙烯(ppb)','乙炔(ppb)','异丁烷(ppb)','正丁烷(ppb)','反-2-丁烯(ppb)','1-丁烯(ppb)','顺-2-丁烯(ppb)','环戊烷(ppb)','异戊烷(ppb)','正戊烷(ppb)','1.3-丁二烯(ppb)','反-2-戊烯(ppb)','1-戊烯(ppb)','顺-2-戊烯(ppb)','2.2-二甲基丁烷(ppb)','2.3-二甲基丁烷(ppb)','异戊二烯(ppb)','2-甲基戊烷(ppb)','1-己烯(ppb)','环己烷(ppb)','乙烷(ppb)','乙烯(ppb)','1.2-二氯乙烷(ppb)','四氯化碳(ppb)','氯仿(ppb)','三氯乙烯(ppb)','1.1.2-三氯乙烷(ppb)','四氯乙烯(ppb)','氯苯(ppb)','氯乙烯(ppb)','二氯甲烷(ppb)','顺-1.2-二氯乙烯(ppb)','1.3-二氯苯(ppb)','1.2-二氯苯(ppb)','氯乙烷(ppb)','溴甲烷(ppb)','氯甲烷(ppb)','1,1-二氯乙烷(ppb)','1,4-二氯苯(ppb)','氯化苄(ppb)','丙烯醛(ppb)','丙醛(ppb)','丙酮(ppb)','乙醛(ppb)','乙腈(ppb)','甲基叔丁基醚(ppb)','异丁烯醛(ppb)','正丁醛(ppb)','甲基乙烯基酮(ppb)','丁酮(ppb)','2-戊酮(ppb)','戊醛(ppb)','3-戊酮(ppb)','己醛(ppb)','2-甲基己烷(ppb)','间-二乙苯(ppb)','对-二乙苯(ppb)','氟利昂-114(ppb)','氟利昂11(ppb)','氟利昂113(ppb)','二氯乙烯(ppb)','1,1,1-三氯乙烷(ppb)','1,2-二氯丙烷(ppb)','一溴二氯甲烷(ppb)','顺-1,3-二氯丙烯(ppb)','反-1,3-二氯丙烯(ppb)','甲基环戊烷(ppb)'])
        self.material.addItems(self.material_list)

        self.year = QtWidgets.QComboBox(self)
        self.year.move(800, 100)
        self.year.addItems(['year', '2016', '2017', '2018','2019', '2020'])

        self.month_start = QtWidgets.QComboBox(self)
        self.month_start.move(800, 150)
        self.month_start.addItems(['month_start', '1', '2', '3','4', '5', '6', '7', '8', '9',  '10', '11', '12'])

        self.month_end = QtWidgets.QComboBox(self)
        self.month_end.move(800, 200)
        self.month_end.addItems(['month_end', '1', '2', '3','4', '5', '6', '7', '8', '9',  '10', '11', '12'])

        self.mode = QtWidgets.QComboBox(self)
        self.mode.move(100, 200)
        self.mode.addItems(['weekend', 'day_night', 'season'])


        btn = QPushButton(self)
        btn.setText("start")
        btn.move(100, 250)
        btn.clicked.connect(self.clike_event)

    def clike_event(self):
        site_index = self.site.currentIndex()
        material_index = self.material.currentIndex()
        year_index = self.year.currentIndex()
        month_start_index = self.month_start.currentIndex()
        month_end_index = self.month_end.currentIndex()
        mode_index = self.mode.currentIndex()
        
        gi.get_img(site_index + 1,material_index+ 1, year_index, month_start_index,month_end_index, mode_index)
        jpg = QtGui.QPixmap(".\\resources\\img\\%s-%s-%d-%d-%d.jpg"%(self.site_list[site_index],self.material_list[material_index] , year_index + 2015, month_start_index, month_end_index)).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = picture()
    w.show()
    sys.exit(app.exec_())
