#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from 装备函数 import *
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import shutil

# 读取yaml文件
def readyaml(file = "../setting/account_other_bonus_attributes.yaml"):
    try:
        fr = open(file, 'r', encoding='utf-8')
        config = yaml.load(fr, Loader=yaml.FullLoader)
    except FileNotFoundError:
        app = QApplication([])
        msgBox = QMessageBox(QMessageBox.Critical, '错误','找不到配置文件!')
        msgBox.exec()
    return(config)

# 向yaml文件中写入配置
def writeyaml(file, data):
    file_bk = file + ".bk"
    if not os.path.isfile(file_bk):
        # 若当前是首次使用配置工具，则写入前备份配置文件
        shutil.copyfile(file, file_bk)

    fr = open(file, 'w', encoding='utf-8')
    yaml.dump(data, fr, default_flow_style=False,encoding='utf-8',allow_unicode=True)
    fr.close()

# 显示yaml文件
def display_info(data_list):
    for tmp in data_list:
        print(tmp)
    return(config)

configItems = readyaml()

# 查找配置名
def find_names(config):
    names = []
    for i in range(len(config)):
        names.append(config[i]["names"][0])
    return(names)

class Config:
    # 动态加载UI文件
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = QUiLoader().load('UI/config.ui')

        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui.saveButton.clicked.connect(self.save_button)
        self.ui.minusButton.clicked.connect(self.minus_button)
        self.ui.nameBox.currentIndexChanged.connect(self.change_config)

        # 打开自动加载配置
        readyaml()
        names = find_names(configItems)
        if len(names) > 0:
            self.ui.nameBox.clear()
            self.ui.nameBox.addItems(names)
            self.read_config(configItems,0)

    def change_config(self):
        readyaml()
        self.read_config(configItems,self.ui.nameBox.currentIndex())

    def read_config(self,config,index):
        if "gui_config" in config[index]:
            gui_config = config[index]["gui_config"]
            x = 0
            while x < len(gui_config):
                # 杂项
                self.ui.attributesBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.attackBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.mythBox.setCurrentIndex(gui_config[x])

                # 武器
                x += 1
                self.ui.weaponType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.weaponBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.weaponAttributes.setText(gui_config[x])
                x += 1
                self.ui.weaponAttack.setText(gui_config[x])
                x += 1
                self.ui.weaponEnh.setText(gui_config[x])
                x += 1
                self.ui.weaponForge.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.type.setCurrentIndex(gui_config[x])

                # 上衣
                x += 1
                self.ui.coatType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.coatBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.coatAttributes.setText(gui_config[x])
                x += 1
                self.ui.coatAttack.setText(gui_config[x])
                x += 1
                self.ui.coatEnh.setText(gui_config[x])
                x += 1
                self.ui.coatSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.coatBadge.setText(gui_config[x])

                # 护肩
                x += 1
                self.ui.neckType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.neckBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.neckAttributes.setText(gui_config[x])
                x += 1
                self.ui.neckAttack.setText(gui_config[x])
                x += 1
                self.ui.neckEnh.setText(gui_config[x])
                x += 1
                self.ui.neckSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.neckBadge.setText(gui_config[x])

                # 下装
                x += 1
                self.ui.pantsType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.pantsBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.pantsAttributes.setText(gui_config[x])
                x += 1
                self.ui.pantsAttack.setText(gui_config[x])
                x += 1
                self.ui.pantsEnh.setText(gui_config[x])
                x += 1
                self.ui.pantsSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.pantsBadge.setText(gui_config[x])

                # 鞋
                x += 1
                self.ui.shoesType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.shoesBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.shoesAttributes.setText(gui_config[x])
                x += 1
                self.ui.shoesAttack.setText(gui_config[x])
                x += 1
                self.ui.shoesEnh.setText(gui_config[x])
                x += 1
                self.ui.shoesSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.shoesBadge.setText(gui_config[x])

                # 腰带
                x += 1
                self.ui.beltType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.beltBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.beltAttributes.setText(gui_config[x])
                x += 1
                self.ui.beltAttack.setText(gui_config[x])
                x += 1
                self.ui.beltEnh.setText(gui_config[x])
                x += 1
                self.ui.beltSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.beltBadge.setText(gui_config[x])

                # 项链
                x += 1
                self.ui.necklaceType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.necklaceBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.necklaceAttributes.setText(gui_config[x])
                x += 1
                self.ui.necklaceAttack.setText(gui_config[x])
                x += 1
                self.ui.necklaceEnh.setText(gui_config[x])
                x += 1
                self.ui.necklaceSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.necklaceBadge.setText(gui_config[x])

                # 手镯
                x += 1
                self.ui.braceletType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.braceletBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.braceletAttributes.setText(gui_config[x])
                x += 1
                self.ui.braceletAttack.setText(gui_config[x])
                x += 1
                self.ui.braceletEnh.setText(gui_config[x])
                x += 1
                self.ui.braceletSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.braceletBadge.setText(gui_config[x])

                # 戒指
                x += 1
                self.ui.ringType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.ringBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.ringAttributes.setText(gui_config[x])
                x += 1
                self.ui.ringAttack.setText(gui_config[x])
                x += 1
                self.ui.ringEnh.setText(gui_config[x])
                x += 1
                self.ui.ringSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.ringBadge.setText(gui_config[x])

                # 辅助装备
                x += 1
                self.ui.supportType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.supportBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.supportAttributes.setText(gui_config[x])
                x += 1
                self.ui.supportAttack.setText(gui_config[x])
                x += 1
                self.ui.supportEnh.setText(gui_config[x])
                x += 1
                self.ui.supportSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.supportBadge.setText(gui_config[x])

                # 魔法石
                x += 1
                self.ui.magicstoneType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.magicstoneBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.magicstoneAttributes.setText(gui_config[x])
                x += 1
                self.ui.magicstoneAttack.setText(gui_config[x])
                x += 1
                self.ui.magicstoneEnh.setText(gui_config[x])
                x += 1
                self.ui.magicstoneSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.magicstoneBadge.setText(gui_config[x])

                # 耳环
                x += 1
                self.ui.earrringType.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.earrringBox.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.earrringAttributes.setText(gui_config[x])
                x += 1
                self.ui.earrringAttack.setText(gui_config[x])
                x += 1
                self.ui.earrringEnh.setText(gui_config[x])
                x += 1
                self.ui.earrringSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.earrringBadge.setText(gui_config[x])

                # 装扮
                x += 1
                self.ui.dressAttributes.setText(gui_config[x])
                x += 1
                self.ui.dressAttack.setText(gui_config[x])
                x += 1
                self.ui.dressEnh.setText(gui_config[x])
                x += 1
                self.ui.dressSkill1.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.dressSkill2.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.dressBadge.setText(gui_config[x])

                # 称号
                x += 1
                self.ui.titleAttributes.setText(gui_config[x])
                x += 1
                self.ui.titleAttack.setText(gui_config[x])
                x += 1
                self.ui.titleEnh.setText(gui_config[x])
                x += 1
                self.ui.titleSkill.setCurrentIndex(gui_config[x])
                x += 1
                self.ui.titleBox.setCurrentIndex(gui_config[x])

                # 其他
                x += 1
                self.ui.groupAttributes.setText(gui_config[x])
                x += 1
                self.ui.guildAttributes.setText(gui_config[x])
                x += 1
                self.ui.trainerAttributes.setText(gui_config[x])
                x += 1
                self.ui.marriageAttributes.setText(gui_config[x])
                x += 1
                self.ui.marriageAttack.setText(gui_config[x])
                x += 1
                self.ui.marriageEnh.setText(gui_config[x])
                x += 1
                self.ui.collectAttributes.setText(gui_config[x])
                x += 1
                self.ui.collectAttack.setText(gui_config[x])
                x += 1
                self.ui.collectEnh.setText(gui_config[x])
                x += 1
                self.ui.medalAttributes.setText(gui_config[x])
                x += 1
                self.ui.medalAttack.setText(gui_config[x])
                x += 1
                self.ui.medalEnh.setText(gui_config[x])
                x += 1
                self.ui.decorationAttributes.setText(gui_config[x])
                x += 1
                self.ui.viceAttack.setText(gui_config[x])

                # 最后一行
                x += 1
                self.ui.grainAttributes.setText(gui_config[x])
                x += 1
                self.ui.grainAttack.setText(gui_config[x])
                x += 1
                self.ui.grainEnh.setText(gui_config[x])
                x += 1
                self.ui.petequipmentAttributes.setText(gui_config[x])
                x += 1
                self.ui.petequipmentAttack.setText(gui_config[x])
                x += 1
                self.ui.petequipmentEnh.setText(gui_config[x])
                x += 1
                self.ui.petAttributes.setText(gui_config[x])
                x += 1
                self.ui.petAttack.setText(gui_config[x])
                x += 1
                self.ui.petEnh.setText(gui_config[x])
                x += 1
                self.ui.petSkill.setText(gui_config[x])
                x += 1
                self.ui.perAttributes.setText(gui_config[x])
                x += 1
                self.ui.addtional.setText(gui_config[x])
                x += 1
                self.ui.finall.setText(gui_config[x])
                x += 1
                self.ui.crit.setText(gui_config[x])
                x += 1
                self.ui.skill.setText(gui_config[x])
                break

    def save_config(self,config):
        gui_dict = {}
        gui_name = []
        # 存档名
        gui_name.append(self.ui.nameBox.currentText())
        gui_dict["names"] = gui_name

        # 主要配置项
        gui_config = []
        gui_config.append(self.ui.attributesBox.currentIndex())
        gui_config.append(self.ui.attackBox.currentIndex())
        gui_config.append(self.ui.mythBox.currentIndex())

        # 武器
        gui_config.append(self.ui.weaponType.currentIndex())
        gui_config.append(self.ui.weaponBox.currentIndex())
        gui_config.append(self.ui.weaponAttributes.text())
        gui_config.append(self.ui.weaponAttack.text())
        gui_config.append(self.ui.weaponEnh.text())
        gui_config.append(self.ui.weaponForge.currentIndex())
        gui_config.append(self.ui.type.currentIndex())

        # 上衣
        gui_config.append(self.ui.coatType.currentIndex())
        gui_config.append(self.ui.coatBox.currentIndex())
        gui_config.append(self.ui.coatAttributes.text())
        gui_config.append(self.ui.coatAttack.text())
        gui_config.append(self.ui.coatEnh.text())
        gui_config.append(self.ui.coatSkill.currentIndex())
        gui_config.append(self.ui.coatBadge.text())

        # 头肩
        gui_config.append(self.ui.neckType.currentIndex())
        gui_config.append(self.ui.neckBox.currentIndex())
        gui_config.append(self.ui.neckAttributes.text())
        gui_config.append(self.ui.neckAttack.text())
        gui_config.append(self.ui.neckEnh.text())
        gui_config.append(self.ui.neckSkill.currentIndex())
        gui_config.append(self.ui.neckBadge.text())

        # 下装
        gui_config.append(self.ui.pantsType.currentIndex())
        gui_config.append(self.ui.pantsBox.currentIndex())
        gui_config.append(self.ui.pantsAttributes.text())
        gui_config.append(self.ui.pantsAttack.text())
        gui_config.append(self.ui.pantsEnh.text())
        gui_config.append(self.ui.pantsSkill.currentIndex())
        gui_config.append(self.ui.pantsBadge.text())

        # 鞋
        gui_config.append(self.ui.shoesType.currentIndex())
        gui_config.append(self.ui.shoesBox.currentIndex())
        gui_config.append(self.ui.shoesAttributes.text())
        gui_config.append(self.ui.shoesAttack.text())
        gui_config.append(self.ui.shoesEnh.text())
        gui_config.append(self.ui.shoesSkill.currentIndex())
        gui_config.append(self.ui.shoesBadge.text())

        # 腰带
        gui_config.append(self.ui.beltType.currentIndex())
        gui_config.append(self.ui.beltBox.currentIndex())
        gui_config.append(self.ui.beltAttributes.text())
        gui_config.append(self.ui.beltAttack.text())
        gui_config.append(self.ui.beltEnh.text())
        gui_config.append(self.ui.beltSkill.currentIndex())
        gui_config.append(self.ui.beltBadge.text())

        #项链
        gui_config.append(self.ui.necklaceType.currentIndex())
        gui_config.append(self.ui.necklaceBox.currentIndex())
        gui_config.append(self.ui.necklaceAttributes.text())
        gui_config.append(self.ui.necklaceAttack.text())
        gui_config.append(self.ui.necklaceEnh.text())
        gui_config.append(self.ui.necklaceSkill.currentIndex())
        gui_config.append(self.ui.necklaceBadge.text())

        # 手镯
        gui_config.append(self.ui.braceletType.currentIndex())
        gui_config.append(self.ui.braceletBox.currentIndex())
        gui_config.append(self.ui.braceletAttributes.text())
        gui_config.append(self.ui.braceletAttack.text())
        gui_config.append(self.ui.braceletEnh.text())
        gui_config.append(self.ui.braceletSkill.currentIndex())
        gui_config.append(self.ui.braceletBadge.text())

        # 戒指
        gui_config.append(self.ui.ringType.currentIndex())
        gui_config.append(self.ui.ringBox.currentIndex())
        gui_config.append(self.ui.ringAttributes.text())
        gui_config.append(self.ui.ringAttack.text())
        gui_config.append(self.ui.ringEnh.text())
        gui_config.append(self.ui.ringSkill.currentIndex())
        gui_config.append(self.ui.ringBadge.text())

        # 辅助装备
        gui_config.append(self.ui.supportType.currentIndex())
        gui_config.append(self.ui.supportBox.currentIndex())
        gui_config.append(self.ui.supportAttributes.text())
        gui_config.append(self.ui.supportAttack.text())
        gui_config.append(self.ui.supportEnh.text())
        gui_config.append(self.ui.supportSkill.currentIndex())
        gui_config.append(self.ui.supportBadge.text())

        # 魔法石
        gui_config.append(self.ui.magicstoneType.currentIndex())
        gui_config.append(self.ui.magicstoneBox.currentIndex())
        gui_config.append(self.ui.magicstoneAttributes.text())
        gui_config.append(self.ui.magicstoneAttack.text())
        gui_config.append(self.ui.magicstoneEnh.text())
        gui_config.append(self.ui.magicstoneSkill.currentIndex())
        gui_config.append(self.ui.magicstoneBadge.text())

        # 耳环
        gui_config.append(self.ui.earrringType.currentIndex())
        gui_config.append(self.ui.earrringBox.currentIndex())
        gui_config.append(self.ui.earrringAttributes.text())
        gui_config.append(self.ui.earrringAttack.text())
        gui_config.append(self.ui.earrringEnh.text())
        gui_config.append(self.ui.earrringSkill.currentIndex())
        gui_config.append(self.ui.earrringBadge.text())

        # 装扮
        gui_config.append(self.ui.dressAttributes.text())
        gui_config.append(self.ui.dressAttack.text())
        gui_config.append(self.ui.dressEnh.text())
        gui_config.append(self.ui.dressSkill1.currentIndex())
        gui_config.append(self.ui.dressSkill2.currentIndex())
        gui_config.append(self.ui.dressBadge.text())

        # 称号
        gui_config.append(self.ui.titleAttributes.text())
        gui_config.append(self.ui.titleAttack.text())
        gui_config.append(self.ui.titleEnh.text())
        gui_config.append(self.ui.titleSkill.currentIndex())
        gui_config.append(self.ui.titleBox.currentIndex())

        # 其他
        gui_config.append(self.ui.groupAttributes.text())
        gui_config.append(self.ui.guildAttributes.text())
        gui_config.append(self.ui.trainerAttributes.text())
        gui_config.append(self.ui.marriageAttributes.text())
        gui_config.append(self.ui.marriageAttack.text())
        gui_config.append(self.ui.marriageEnh.text())
        gui_config.append(self.ui.collectAttributes.text())
        gui_config.append(self.ui.collectAttack.text())
        gui_config.append(self.ui.collectEnh.text())
        gui_config.append(self.ui.medalAttributes.text())
        gui_config.append(self.ui.medalAttack.text())
        gui_config.append(self.ui.medalEnh.text())
        gui_config.append(self.ui.decorationAttributes.text())
        gui_config.append(self.ui.viceAttack.text())

        gui_config.append(self.ui.grainAttributes.text())
        gui_config.append(self.ui.grainAttack.text())
        gui_config.append(self.ui.grainEnh.text())
        gui_config.append(self.ui.petequipmentAttributes.text())
        gui_config.append(self.ui.petequipmentAttack.text())
        gui_config.append(self.ui.petequipmentEnh.text())
        gui_config.append(self.ui.petAttributes.text())
        gui_config.append(self.ui.petAttack.text())
        gui_config.append(self.ui.petEnh.text())
        gui_config.append(self.ui.petSkill.text())
        gui_config.append(self.ui.perAttributes.text())
        gui_config.append(self.ui.addtional.text())
        gui_config.append(self.ui.finall.text())
        gui_config.append(self.ui.crit.text())
        gui_config.append(self.ui.skill.text())


        # 主属性词条
        entries = []
        if self.ui.attributesBox.currentIndex() in [0, 1]:
            attributes = "strength_and_intelligence"
        else:
            attributes = "physical_and_mental_strength"
        attack = "physical_magical_independent_attack_power"
        # 装备计算增幅强化
        
        ## 武器
        # 强化
        if self.ui.attackBox.currentIndex() in [1, 2]:
            if self.ui.weaponBox.currentIndex() != 0:
                weapon_dict = {attack : 武器计算(100,"史诗",self.ui.weaponBox.currentIndex(),self.ui.type.currentText(),self.ui.attackBox.currentText())}
                entries.append(weapon_dict)
        # 锻造
        elif self.ui.attackBox.currentIndex() == 3:
            weapon_dict = {attack : 锻造计算(100,"史诗",self.ui.weaponForge.currentIndex())}
            entries.append(weapon_dict)
        else:
            pass
        # 增幅
        if self.ui.weaponType.currentIndex() == 0:
            weapon_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.weaponBox.currentIndex())}
            entries.append(weapon_dict1)
        # 附魔
        if self.ui.weaponAttributes.text() != "":
            weapon_dict2 = {attributes : int(self.ui.weaponAttributes.text())}
            entries.append(weapon_dict2)
        if self.ui.weaponAttack.text() != "":
            weapon_dict3 = {attack : int(self.ui.weaponAttack.text())}
            entries.append(weapon_dict3)
        if self.ui.weaponEnh.text() != "":
            weapon_dict4 = {"extra_all_element_strength" : int(self.ui.weaponEnh.text())}
            entries.append(weapon_dict4)

        ## 上衣
        # 增幅
        if self.ui.coatType.currentIndex() == 0:
            if self.ui.mythBox.currentIndex() == 1:
                coat_dict1 = {attributes : 增幅计算(100,"神话",self.ui.coatBox.currentIndex())}
                entries.append(coat_dict1)
            else:
                coat_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.coatBox.currentIndex())}
                entries.append(coat_dict1)
        # 附魔
        if self.ui.coatAttributes.text() != "":
            coat_dict2 = {attributes : int(self.ui.coatAttributes.text())}
            entries.append(coat_dict2)
        if self.ui.coatAttack.text() != "":
            coat_dict3 = {attack : int(self.ui.coatAttack.text())}
            entries.append(coat_dict3)
        if self.ui.coatEnh.text() != "":
            coat_dict4 = {"extra_all_element_strength" : int(self.ui.coatEnh.text())}
            entries.append(coat_dict4)
        if self.ui.coatSkill.currentIndex() == 1:
            coat_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(coat_dict5)
        elif self.ui.coatSkill.currentIndex() == 2:
            coat_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(coat_dict5)
        if self.ui.coatBadge.text() != "":
            coat_dict6 = {attributes : int(self.ui.coatBadge.text())}
            entries.append(coat_dict6)

        ## 头肩
        # 增幅
        if self.ui.neckType.currentIndex() == 0:
            neck_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.neckBox.currentIndex())}
            entries.append(neck_dict1)
        # 附魔
        if self.ui.neckAttributes.text() != "":
            neck_dict2 = {attributes : int(self.ui.neckAttributes.text())}
            entries.append(neck_dict2)
        if self.ui.neckAttack.text() != "":
            neck_dict3 = {attack : int(self.ui.neckAttack.text())}
            entries.append(neck_dict3)
        if self.ui.neckEnh.text() != "":
            neck_dict4 = {"extra_all_element_strength" : int(self.ui.neckEnh.text())}
            entries.append(neck_dict4)
        if self.ui.neckSkill.currentIndex() == 1:
            neck_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(neck_dict5)
        elif self.ui.neckSkill.currentIndex() == 2:
            neck_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(neck_dict5)
        if self.ui.neckBadge.text() != "":
            neck_dict6 = {attributes : int(self.ui.neckBadge.text())}
            entries.append(neck_dict6)

        ## 下装
        # 增幅
        if self.ui.pantsType.currentIndex() == 0:
            pants_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.pantsBox.currentIndex())}
            entries.append(pants_dict1)
        # 附魔
        if self.ui.pantsAttributes.text() != "":
            pants_dict2 = {attributes : int(self.ui.pantsAttributes.text())}
            entries.append(pants_dict2)
        if self.ui.pantsAttack.text() != "":
            pants_dict3 = {attack : int(self.ui.pantsAttack.text())}
            entries.append(pants_dict3)
        if self.ui.pantsEnh.text() != "":
            pants_dict4 = {"extra_all_element_strength" : int(self.ui.pantsEnh.text())}
            entries.append(pants_dict4)
        if self.ui.pantsSkill.currentIndex() == 1:
            pants_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(pants_dict5)
        elif self.ui.pantsSkill.currentIndex() == 2:
            pants_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(pants_dict5)
        if self.ui.pantsBadge.text() != "":
            pants_dict6 = {attributes : int(self.ui.pantsBadge.text())}
            entries.append(pants_dict6)

        ## 鞋
        # 增幅
        if self.ui.shoesType.currentIndex() == 0:
            shoes_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.shoesBox.currentIndex())}
            entries.append(shoes_dict1)
        # 附魔
        if self.ui.shoesAttributes.text() != "":
            shoes_dict2 = {attributes : int(self.ui.shoesAttributes.text())}
            entries.append(shoes_dict2)
        if self.ui.shoesAttack.text() != "":
            shoes_dict3 = {attack : int(self.ui.shoesAttack.text())}
            entries.append(shoes_dict3)
        if self.ui.shoesEnh.text() != "":
            shoes_dict4 = {"extra_all_element_strength" : int(self.ui.shoesEnh.text())}
            entries.append(shoes_dict4)
        if self.ui.shoesSkill.currentIndex() == 1:
            shoes_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(shoes_dict5)
        elif self.ui.shoesSkill.currentIndex() == 2:
            shoes_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(shoes_dict5)
        if self.ui.shoesBadge.text() != "":
            shoes_dict6 = {attributes : int(self.ui.shoesBadge.text())}
            entries.append(shoes_dict6)

        ## 腰带
        # 增幅
        if self.ui.beltType.currentIndex() == 0:
            belt_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.beltBox.currentIndex())}
            entries.append(belt_dict1)
        # 附魔
        if self.ui.beltAttributes.text() != "":
            belt_dict2 = {attributes : int(self.ui.beltAttributes.text())}
            entries.append(belt_dict2)
        if self.ui.beltAttack.text() != "":
            belt_dict3 = {attack : int(self.ui.beltAttack.text())}
            entries.append(belt_dict3)
        if self.ui.beltEnh.text() != "":
            belt_dict4 = {"extra_all_element_strength" : int(self.ui.beltEnh.text())}
            entries.append(belt_dict4)
        if self.ui.beltSkill.currentIndex() == 1:
            belt_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(belt_dict5)
        elif self.ui.beltSkill.currentIndex() == 2:
            belt_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(belt_dict5)
        if self.ui.beltBadge.text() != "":
            belt_dict6 = {attributes : int(self.ui.beltBadge.text())}
            entries.append(belt_dict6)

        ## 项链
        # 增幅
        if self.ui.necklaceType.currentIndex() == 0:
            necklace_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.necklaceBox.currentIndex())}
            entries.append(necklace_dict1)
        # 附魔
        if self.ui.necklaceAttributes.text() != "":
            necklace_dict2 = {attributes : int(self.ui.necklaceAttributes.text())}
            entries.append(necklace_dict2)
        if self.ui.necklaceAttack.text() != "":
            necklace_dict3 = {attack : int(self.ui.necklaceAttack.text())}
            entries.append(necklace_dict3)
        if self.ui.necklaceEnh.text() != "":
            necklace_dict4 = {"extra_all_element_strength" : int(self.ui.necklaceEnh.text())}
            entries.append(necklace_dict4)
        if self.ui.necklaceSkill.currentIndex() == 1:
            necklace_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(necklace_dict5)
        elif self.ui.necklaceSkill.currentIndex() == 2:
            necklace_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(necklace_dict5)
        if self.ui.necklaceBadge.text() != "":
            necklace_dict6 = {attributes : int(self.ui.necklaceBadge.text())}
            entries.append(necklace_dict6)

        ## 手镯
        # 增幅
        if self.ui.braceletType.currentIndex() == 0:
            if self.ui.mythBox.currentIndex() == 2:
                bracelet_dict1 = {attributes : 增幅计算(100,"神话",self.ui.braceletBox.currentIndex())}
                entries.append(bracelet_dict1)
            else:
                bracelet_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.braceletBox.currentIndex())}
                entries.append(bracelet_dict1)
        # 附魔
        if self.ui.braceletAttributes.text() != "":
            bracelet_dict2 = {attributes : int(self.ui.braceletAttributes.text())}
            entries.append(bracelet_dict2)
        if self.ui.braceletAttack.text() != "":
            bracelet_dict3 = {attack : int(self.ui.braceletAttack.text())}
            entries.append(bracelet_dict3)
        if self.ui.braceletEnh.text() != "":
            bracelet_dict4 = {"extra_all_element_strength" : int(self.ui.braceletEnh.text())}
            entries.append(bracelet_dict4)
        if self.ui.braceletSkill.currentIndex() == 1:
            bracelet_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(bracelet_dict5)
        elif self.ui.braceletSkill.currentIndex() == 2:
            bracelet_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(bracelet_dict5)
        if self.ui.braceletBadge.text() != "":
            bracelet_dict6 = {attributes : int(self.ui.braceletBadge.text())}
            entries.append(bracelet_dict6)

        ## 戒指
        # 增幅
        if self.ui.ringType.currentIndex() == 0:
            ring_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.ringBox.currentIndex())}
            entries.append(ring_dict1)
        # 附魔
        if self.ui.ringAttributes.text() != "":
            ring_dict2 = {attributes : int(self.ui.ringAttributes.text())}
            entries.append(ring_dict2)
        if self.ui.ringAttack.text() != "":
            ring_dict3 = {attack : int(self.ui.ringAttack.text())}
            entries.append(ring_dict3)
        if self.ui.ringEnh.text() != "":
            ring_dict4 = {"extra_all_element_strength" : int(self.ui.ringEnh.text())}
            entries.append(ring_dict4)
        if self.ui.ringSkill.currentIndex() == 1:
            ring_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(ring_dict5)
        elif self.ui.ringSkill.currentIndex() == 2:
            ring_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(ring_dict5)
        if self.ui.ringBadge.text() != "":
            ring_dict6 = {attributes : int(self.ui.ringBadge.text())}
            entries.append(ring_dict6)

        ## 辅助装备
        # 强化
        if self.ui.supportBox.currentIndex() != 0:
            support_dict = {attributes : 左右计算(100,"史诗",self.ui.supportBox.currentIndex())}
            entries.append(support_dict)
        # 增幅
        if self.ui.supportType.currentIndex() == 0:
            support_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.supportBox.currentIndex())}
            entries.append(support_dict1)
        # 附魔
        if self.ui.supportAttributes.text() != "":
            support_dict2 = {attributes : int(self.ui.supportAttributes.text())}
            entries.append(support_dict2)
        if self.ui.supportAttack.text() != "":
            support_dict3 = {attack : int(self.ui.supportAttack.text())}
            entries.append(support_dict3)
        if self.ui.supportEnh.text() != "":
            support_dict4 = {"extra_all_element_strength" : int(self.ui.supportEnh.text())}
            entries.append(support_dict4)
        if self.ui.supportSkill.currentIndex() == 1:
            support_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(support_dict5)
        elif self.ui.supportSkill.currentIndex() == 2:
            support_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(support_dict5)
        if self.ui.supportBadge.text() != "":
            support_dict6 = {attributes : int(self.ui.supportBadge.text())}
            entries.append(support_dict6)

        ## 魔法石
        # 强化
        if self.ui.magicstoneBox.currentIndex() != 0:
            magicstone_dict = {attributes : 左右计算(100,"史诗",self.ui.magicstoneBox.currentIndex())}
            entries.append(magicstone_dict)
        # 增幅
        if self.ui.magicstoneType.currentIndex() == 0:
            magicstone_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.magicstoneBox.currentIndex())}
            entries.append(magicstone_dict1)
        # 附魔
        if self.ui.magicstoneAttributes.text() != "":
            magicstone_dict2 = {attributes : int(self.ui.magicstoneAttributes.text())}
            entries.append(magicstone_dict2)
        if self.ui.magicstoneAttack.text() != "":
            magicstone_dict3 = {attack : int(self.ui.magicstoneAttack.text())}
            entries.append(magicstone_dict3)
        if self.ui.magicstoneEnh.text() != "":
            magicstone_dict4 = {"extra_all_element_strength" : int(self.ui.magicstoneEnh.text())}
            entries.append(magicstone_dict4)
        if self.ui.magicstoneSkill.currentIndex() == 1:
            magicstone_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(magicstone_dict5)
        elif self.ui.magicstoneSkill.currentIndex() == 2:
            magicstone_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(magicstone_dict5)
        if self.ui.magicstoneBadge.text() != "":
            magicstone_dict6 = {attributes : int(self.ui.magicstoneBadge.text())}
            entries.append(magicstone_dict6)

        ## 耳环
        # 强化
        if self.ui.earrringBox.currentIndex() != 0:
            if self.ui.mythBox.currentIndex() == 3:
                earrring_dict = {attributes : 耳环计算(100,"神话",self.ui.earrringBox.currentIndex())}
                entries.append(earrring_dict)
            else:
                earrring_dict = {attributes : 耳环计算(100,"史诗",self.ui.earrringBox.currentIndex())}
                entries.append(earrring_dict)
        # 增幅
        if self.ui.earrringType.currentIndex() == 0:
            if self.ui.mythBox.currentIndex() == 3:
                earrring_dict1 = {attributes : 增幅计算(100,"神话",self.ui.earrringBox.currentIndex())}
                entries.append(earrring_dict1)
            else:
                earrring_dict1 = {attributes : 增幅计算(100,"史诗",self.ui.earrringBox.currentIndex())}
                entries.append(earrring_dict1)
        # 附魔
        if self.ui.earrringAttributes.text() != "":
            earrring_dict2 = {attributes : int(self.ui.earrringAttributes.text())}
            entries.append(earrring_dict2)
        if self.ui.earrringAttack.text() != "":
            earrring_dict3 = {attack : int(self.ui.earrringAttack.text())}
            entries.append(earrring_dict3)
        if self.ui.earrringEnh.text() != "":
            earrring_dict4 = {"extra_all_element_strength" : int(self.ui.earrringEnh.text())}
            entries.append(earrring_dict4)
        if self.ui.earrringSkill.currentIndex() == 1:
            earrring_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(earrring_dict5)
        elif self.ui.earrringSkill.currentIndex() == 2:
            earrring_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(earrring_dict5)
        if self.ui.earrringBadge.text() != "":
            earrring_dict6 = {attributes : int(self.ui.earrringBadge.text())}
            entries.append(earrring_dict6)

        # 装扮
        if self.ui.dressAttributes.text() != "":
            dress_dict2 = {attributes : int(self.ui.dressAttributes.text())}
            entries.append(dress_dict2)
        if self.ui.dressAttack.text() != "":
            dress_dict3 = {attack : int(self.ui.dressAttack.text())}
            entries.append(dress_dict3)
        if self.ui.dressEnh.text() != "":
            dress_dict4 = {"extra_all_element_strength" : int(self.ui.dressEnh.text())}
            entries.append(dress_dict4)
        if self.ui.dressSkill1.currentIndex() == 1:
            dress_dict = {"extra_deal_passive_transfer_skill" : 1}
            entries.append(dress_dict)
        elif self.ui.dressSkill1.currentIndex() == 2:
            dress_dict = {"extra_bless_skill" : 1}
            entries.append(dress_dict)
        elif self.ui.dressSkill1.currentIndex() == 3:
            dress_dict = {"extra_taiyang_skill" : 1}
            entries.append(dress_dict)
        if self.ui.dressSkill2.currentIndex() == 1:
            dress_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(dress_dict5)
        elif self.ui.dressSkill2.currentIndex() == 2:
            dress_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(dress_dict5)
        if self.ui.dressBadge.text() != "":
            dress_dict6 = {attributes : int(self.ui.dressBadge.text())}
            entries.append(dress_dict6)

        ## 称号
        if self.ui.titleAttributes.text() != "":
            title_dict2 = {attributes : int(self.ui.titleAttributes.text())}
            entries.append(title_dict2)
        if self.ui.titleAttack.text() != "":
            title_dict3 = {attack : int(self.ui.titleAttack.text())}
            entries.append(title_dict3)
        if self.ui.titleEnh.text() != "":
            title_dict4 = {"extra_all_element_strength" : int(self.ui.titleEnh.text())}
            entries.append(title_dict4)
        if self.ui.titleSkill.currentIndex() == 1:
            title_dict5 = {"extra_all_job_all_active_skill_lv_1_50" : 1}
            entries.append(title_dict5)
        elif self.ui.titleSkill.currentIndex() == 2:
            title_dict5 = {"extra_all_job_all_skill_lv_15_20" : 1}
            entries.append(title_dict5)
        elif self.ui.titleSkill.currentIndex() == 3:
            title_dict5 = {"extra_all_job_all_skill_lv_20_25" : 1}
            entries.append(title_dict5)
        elif self.ui.titleSkill.currentIndex() == 4:
            title_dict5 = {"extra_all_job_all_skill_lv_25_30" : 1}
            entries.append(title_dict5)
        elif self.ui.titleSkill.currentIndex() == 5:
            title_dict5 = {"extra_all_job_all_skill_lv_30_35" : 1}
            entries.append(title_dict5)

        if self.ui.titleBox.currentIndex() == 1:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 1}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 2:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 2}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 3:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 3}
            entries.append(title_dict6)        
        elif self.ui.titleBox.currentIndex() == 4:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 1}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 5:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 2}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 6:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 3}
            entries.append(title_dict6)

        ## 其他
        if self.ui.groupAttributes.text() != "":
            group_dict = {attributes : int(self.ui.groupAttributes.text())}
            entries.append(group_dict)

        if self.ui.guildAttributes.text() != "":
            guild_dict = {attributes : int(self.ui.guildAttributes.text())}
            entries.append(guild_dict)

        if self.ui.trainerAttributes.text() != "":
            trainer_dict = {attributes : int(self.ui.trainerAttributes.text())}
            entries.append(trainer_dict)

        # 婚房婚戒
        if self.ui.marriageAttributes.text() != "":
            marriage_dict = {attributes : int(self.ui.marriageAttributes.text())}
            entries.append(marriage_dict)
        if self.ui.marriageAttack.text() != "":
            marriage_dict2 = {attack : int(self.ui.marriageAttack.text())}
            entries.append(marriage_dict2)            
        if self.ui.marriageEnh.text() != "":
            marriage_dict3 = {"extra_all_element_strength" : int(self.ui.marriageEnh.text())}
            entries.append(marriage_dict3)   

        # 收集箱
        if self.ui.collectAttributes.text() != "":
            collect_dict = {attributes : int(self.ui.collectAttributes.text())}
            entries.append(collect_dict)
        if self.ui.collectAttack.text() != "":
            collect_dict2 = {attack : int(self.ui.collectAttack.text())}
            entries.append(collect_dict2)            
        if self.ui.collectEnh.text() != "":
            collect_dict3 = {"extra_all_element_strength" : int(self.ui.collectEnh.text())}
            entries.append(collect_dict3)

        # 勋章
        if self.ui.medalAttributes.text() != "":
            medal_dict = {attributes : int(self.ui.medalAttributes.text())}
            entries.append(medal_dict)
        if self.ui.medalAttack.text() != "":
            medal_dict2 = {attack : int(self.ui.medalAttack.text())}
            entries.append(medal_dict2)            
        if self.ui.medalEnh.text() != "":
            medal_dict3 = {"extra_all_element_strength" : int(self.ui.medalEnh.text())}
            entries.append(medal_dict3)

        if self.ui.decorationAttributes.text() != "":
            decoration_dict = {attributes : int(self.ui.decorationAttributes.text())}
            entries.append(decoration_dict)

        if self.ui.viceAttack.text() != "":
            vice_dict = {attack : int(self.ui.viceAttack.text())}
            entries.append(vice_dict)

        # 纹章
        if self.ui.grainAttributes.text() != "":
            grain_dict = {attributes : int(self.ui.grainAttributes.text())}
            entries.append(grain_dict)
        if self.ui.grainAttack.text() != "":
            grain_dict2 = {attack : int(self.ui.grainAttack.text())}
            entries.append(grain_dict2)            
        if self.ui.grainEnh.text() != "":
            grain_dict3 = {"extra_all_element_strength" : int(self.ui.grainEnh.text())}
            entries.append(grain_dict3)

        # 宠物装备
        if self.ui.petequipmentAttributes.text() != "":
            petequipment_dict = {attributes : int(self.ui.petequipmentAttributes.text())}
            entries.append(petequipment_dict)
        if self.ui.petequipmentAttack.text() != "":
            petequipment_dict2 = {attack : int(self.ui.petequipmentAttack.text())}
            entries.append(petequipment_dict2)            
        if self.ui.petequipmentEnh.text() != "":
            petequipment_dict3 = {"extra_all_element_strength" : int(self.ui.petequipmentEnh.text())}
            entries.append(petequipment_dict3)

        # 宠物
        if self.ui.petAttributes.text() != "":
            pet_dict = {attributes : int(self.ui.petAttributes.text())}
            entries.append(pet_dict)
        if self.ui.petAttack.text() != "":
            pet_dict2 = {attack : int(self.ui.petAttack.text())}
            entries.append(pet_dict2)            
        if self.ui.petEnh.text() != "":
            pet_dict3 = {"extra_all_element_strength" : int(self.ui.petEnh.text())}
            entries.append(pet_dict3)
        if self.ui.petSkill.text() != "":
            pet_dict4 = {"creature_increase_owner_attack_power" : int(self.ui.petSkill.text())}
            entries.append(pet_dict4)
        
        # 补正
        if self.ui.perAttributes.text() != "":
            per_dict = {"extra_percent_strength_and_intelligence" : int(self.ui.perAttributes.text())}
            entries.append(per_dict)
        if self.ui.addtional.text() != "":
            per_dict2 = {"extra_percent_addtional_damage" : int(self.ui.addtional.text())}
            entries.append(per_dict2)        
        if self.ui.finall.text() != "":
            per_dict3 = {"extra_percent_final_damage" : int(self.ui.finall.text())}
            entries.append(per_dict3)   
        if self.ui.crit.text() != "":
            per_dict4 = {"extra_percent_crit_damage" : int(self.ui.crit.text())}
            entries.append(per_dict4)
        if self.ui.skill.text() != "":
            per_dict5 = {"other_rate_like_extra_percent_skill_attack_power" : int(self.ui.skill.text())}
            entries.append(per_dict5)

        hasnames = 0
        for i in range(len(config)):
            if self.ui.nameBox.currentText() in config[i]["names"]:
                hasname = 1
                index = i
            else:
                hasname = 0
            hasnames += hasname
        if hasnames:
            config[index]["gui_config"] = gui_config
            config[index]["entries"] = entries
            writeyaml("../setting/account_other_bonus_attributes.yaml",config)
        else:
            name_list = []
            new_config = {}
            name_list.append(self.ui.nameBox.currentText())
            new_config["names"] = name_list
            new_config["gui_config"] = gui_config
            new_config["entries"] = entries
            config.append(new_config)
            writeyaml("../setting/account_other_bonus_attributes.yaml",config)
            names = find_names(configItems)
            self.ui.nameBox.clear()
            self.ui.nameBox.addItems(names)
            self.ui.nameBox.setCurrentIndex(len(names)-1)

        # 通知用户保存完成
        msgBox = QMessageBox()
        msgBox.setWindowTitle('通知')
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('保存成功')
        ok = msgBox.addButton(QMessageBox.Ok)
        msgBox.setDefaultButton(ok)
        msgBox.exec()

    def save_button(self):
        self.save_config(configItems)

    def find_index(self,config):
                    for i in range(len(config)):
                        if self.ui.nameBox.currentText() in config[i]["names"]:
                            index = i
                    return(index)

    def minus_button(self):
        readyaml()
        if len(configItems) > 0:
            # reply = QMessageBox.warning(self,'警告','这是一个警告消息对话框', QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
            msgBox = QMessageBox()
            msgBox.setWindowTitle('警告')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText('删除后无法恢复！')
            msgBox.setInformativeText('确认删除?')
            Save = msgBox.addButton('删除', QMessageBox.AcceptRole)
            Cancel = msgBox.addButton('取消', QMessageBox.DestructiveRole)
            msgBox.setDefaultButton(Cancel)
            reply = msgBox.exec()
            if reply == QMessageBox.AcceptRole:
                readyaml()
                names = find_names(configItems)
                num = self.find_index(configItems)
                del configItems[num]
                readyaml()
                names = find_names(configItems)
                self.ui.minusButton.setEnabled(True)
                self.ui.nameBox.clear()
                self.ui.nameBox.addItems(names)

        else:
            self.ui.minusButton.setEnabled(False)
        
        writeyaml("../setting/account_other_bonus_attributes.yaml",configItems)
       
if __name__ == "__main__":
    app = QApplication([])
    config = Config()
    config.ui.show()
    app.exec_()
