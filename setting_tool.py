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
        self.ui.addButton.clicked.connect(self.add_button)
        self.ui.minusButton.clicked.connect(self.minus_button)
        self.ui.nameBox.currentIndexChanged.connect(self.change_config)
        self.ui.attributesBox.currentIndexChanged.connect(self.change_attributes)
        self.ui.attackBox.currentIndexChanged.connect(self.change_attack)
        self.ui.categoryBox.currentIndexChanged.connect(self.change_category)
        self.ui.funcBox.currentIndexChanged.connect(self.change_func)
        self.ui.lvBox.currentIndexChanged.connect(self.change_lv)

        # 打开自动加载配置
        names = find_names(configItems)
        if len(names) > 0:
            self.ui.nameBox.clear()
            self.ui.nameBox.addItems(names)
            self.read_config(readyaml(),self.ui.nameBox.currentIndex())

    def change_config(self): 
        try:
            if self.ui.nameBox.currentText() in readyaml()[self.ui.nameBox.currentIndex()]["names"]:
                self.read_config(readyaml(),self.ui.nameBox.currentIndex())
        except IndexError:
            self.clear_config()

    def change_attributes(self):
        if self.ui.attributesBox.currentIndex() == 0:
            attributes = "力量"
        elif self.ui.attributesBox.currentIndex() == 1:
            attributes = "智力"
        elif self.ui.attributesBox.currentIndex() == 2:
            attributes = "体力"
        elif self.ui.attributesBox.currentIndex() == 3:
            attributes = "精神"

        self.ui.weaponAttributes.setPlaceholderText(attributes)
        self.ui.coatAttributes.setPlaceholderText(attributes)
        self.ui.coatBadge.setPlaceholderText(attributes)
        self.ui.neckAttributes.setPlaceholderText(attributes)
        self.ui.neckBadge.setPlaceholderText(attributes)
        self.ui.pantsAttributes.setPlaceholderText(attributes)
        self.ui.pantsBadge.setPlaceholderText(attributes)
        self.ui.shoesAttributes.setPlaceholderText(attributes)
        self.ui.shoesBadge.setPlaceholderText(attributes)
        self.ui.beltAttributes.setPlaceholderText(attributes)
        self.ui.beltBadge.setPlaceholderText(attributes)
        self.ui.necklaceAttributes.setPlaceholderText(attributes)
        self.ui.necklaceBadge.setPlaceholderText(attributes)
        self.ui.braceletAttributes.setPlaceholderText(attributes)
        self.ui.braceletBadge.setPlaceholderText(attributes)
        self.ui.ringAttributes.setPlaceholderText(attributes)
        self.ui.ringBadge.setPlaceholderText(attributes)
        self.ui.supportAttributes.setPlaceholderText(attributes)
        self.ui.supportBadge.setPlaceholderText(attributes)
        self.ui.magicstoneAttributes.setPlaceholderText(attributes)
        self.ui.magicstoneBadge.setPlaceholderText(attributes)
        self.ui.earrringAttributes.setPlaceholderText(attributes)
        self.ui.earrringBadge.setPlaceholderText(attributes)

        self.ui.dressAttributes.setPlaceholderText(attributes)
        self.ui.dressBadge.setPlaceholderText(attributes)
        self.ui.titleAttributes.setPlaceholderText(attributes)
        self.ui.groupAttributes.setPlaceholderText(attributes)
        self.ui.guildAttributes.setPlaceholderText(attributes)
        self.ui.trainerAttributes.setPlaceholderText(attributes)
        self.ui.marriageAttributes.setPlaceholderText(attributes)
        self.ui.collectAttributes.setPlaceholderText(attributes)
        self.ui.medalAttributes.setPlaceholderText(attributes)
        self.ui.decorationAttributes.setPlaceholderText(attributes)
        self.ui.grainAttributes.setPlaceholderText(attributes)
        self.ui.petequipmentAttributes.setPlaceholderText(attributes)
        self.ui.petAttributes.setPlaceholderText(attributes)

        self.ui.perAttributes.setPlaceholderText(attributes + "%")

    def change_attack(self):
        if self.ui.attackBox.currentIndex() == 0:
            attack = "无"
        elif self.ui.attackBox.currentIndex() == 1:
            attack = "物攻"
        elif self.ui.attackBox.currentIndex() == 2:
            attack = "魔攻"
        elif self.ui.attackBox.currentIndex() == 3:
            attack = "独立"
        
        self.ui.weaponAttack.setPlaceholderText(attack)
        self.ui.coatAttack.setPlaceholderText(attack)
        self.ui.coatBadgeAttack.setPlaceholderText(attack)
        self.ui.neckAttack.setPlaceholderText(attack)
        self.ui.neckBadgeAttack.setPlaceholderText(attack)
        self.ui.pantsAttack.setPlaceholderText(attack)
        self.ui.pantsBadgeAttack.setPlaceholderText(attack)
        self.ui.shoesAttack.setPlaceholderText(attack)
        self.ui.shoesBadgeAttack.setPlaceholderText(attack)
        self.ui.beltAttack.setPlaceholderText(attack)
        self.ui.beltBadgeAttack.setPlaceholderText(attack)
        self.ui.necklaceAttack.setPlaceholderText(attack)
        self.ui.necklaceBadgeAttack.setPlaceholderText(attack)
        self.ui.braceletAttack.setPlaceholderText(attack)
        self.ui.braceletBadgeAttack.setPlaceholderText(attack)
        self.ui.ringAttack.setPlaceholderText(attack)
        self.ui.ringBadgeAttack.setPlaceholderText(attack)
        self.ui.supportAttack.setPlaceholderText(attack)
        self.ui.supportBadgeAttack.setPlaceholderText(attack)
        self.ui.magicstoneAttack.setPlaceholderText(attack)
        self.ui.magicstoneBadgeAttack.setPlaceholderText(attack)
        self.ui.earrringAttack.setPlaceholderText(attack)
        self.ui.earrringBadgeAttack.setPlaceholderText(attack)

        self.ui.dressAttack.setPlaceholderText(attack)
        self.ui.dressBadgeAttack.setPlaceholderText(attack)
        self.ui.titleAttack.setPlaceholderText(attack)
        self.ui.trainerAttack.setPlaceholderText(attack)
        self.ui.marriageAttack.setPlaceholderText(attack)
        self.ui.collectAttack.setPlaceholderText(attack)
        self.ui.medalAttack.setPlaceholderText(attack)
        self.ui.viceAttack.setPlaceholderText(attack)
        self.ui.grainAttack.setPlaceholderText(attack)
        self.ui.petequipmentAttack.setPlaceholderText(attack)
        self.ui.petAttack.setPlaceholderText(attack)

        self.ui.petSkill.setPlaceholderText(attack + "%")

    def change_func(self):
        self.ui.weaponType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.coatType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.neckType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.pantsType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.shoesType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.beltType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.necklaceType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.braceletType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.ringType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.supportType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.magicstoneType.setCurrentIndex(self.ui.funcBox.currentIndex())
        self.ui.earrringType.setCurrentIndex(self.ui.funcBox.currentIndex())

    def change_lv(self):
        self.ui.weaponBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.coatBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.neckBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.pantsBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.shoesBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.beltBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.necklaceBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.braceletBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.ringBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.supportBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.magicstoneBox.setCurrentIndex(self.ui.lvBox.currentIndex())
        self.ui.earrringBox.setCurrentIndex(self.ui.lvBox.currentIndex())

    def change_category(self):
        if self.ui.categoryBox.currentText() == "鬼剑士/黑暗武士":
            self.ui.type.clear()
            self.ui.type.addItems(["短剑","光剑","巨剑","太刀","钝器"])
        elif self.ui.categoryBox.currentText() == "神枪手":
            self.ui.type.clear()
            self.ui.type.addItems(["左轮枪","手炮","步枪","手弩","自动手枪"])
        elif self.ui.categoryBox.currentText() == "魔法师/缔造者":
            self.ui.type.clear()
            self.ui.type.addItems(["法杖","魔杖","棍棒","矛","扫把"])
        elif self.ui.categoryBox.currentText() == "格斗家":
            self.ui.type.clear()
            self.ui.type.addItems(["手套","臂铠","爪","拳套","东方棍"])
        elif self.ui.categoryBox.currentText() == "圣职者":
            self.ui.type.clear()
            self.ui.type.addItems(["十字架","念珠","图腾","镰刀","战斧"])
        elif self.ui.categoryBox.currentText() == "魔枪士":
            self.ui.type.clear()
            self.ui.type.addItems(["战戟","长枪","光枪","暗矛"])
        elif self.ui.categoryBox.currentText() == "枪剑士":
            self.ui.type.clear()
            self.ui.type.addItems(["长刀","小太刀","重剑","源力剑"])
        elif self.ui.categoryBox.currentText() == "守护者":
            self.ui.type.clear()
            self.ui.type.addItems(["短剑","巨剑","太刀","钝器"])
        elif self.ui.categoryBox.currentText() == "暗夜使者":
            self.ui.type.clear()
            self.ui.type.addItems(["匕首","双剑","手杖","苦无"])

    def read_config(self,config,index):
        if "gui_config" in config[index]:
            gui_config = config[index]["gui_config"]
            x = 0
            y = len(gui_config)
            if x < y:
                # 杂项
                self.ui.attributesBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.attackBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.mythBox.setCurrentIndex(gui_config[x])
                # 武器
                x += 1
            if x < y:
                self.ui.weaponType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.weaponBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.weaponAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.weaponAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.weaponEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.weaponForge.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.type.setCurrentIndex(gui_config[x])
                # 上衣
                x += 1
            if x < y:
                self.ui.coatType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.coatBadgeAttack.setText(gui_config[x])
                # 护肩
                x += 1
            if x < y:
                self.ui.neckType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.neckBadgeAttack.setText(gui_config[x])
                # 下装
                x += 1
            if x < y:
                self.ui.pantsType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.pantsBadgeAttack.setText(gui_config[x])
                # 鞋
                x += 1
            if x < y:
                self.ui.shoesType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.shoesBadgeAttack.setText(gui_config[x])
                # 腰带
                x += 1
            if x < y:
                self.ui.beltType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.beltBadgeAttack.setText(gui_config[x])
                # 项链
                x += 1
            if x < y:
                self.ui.necklaceType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.necklaceBadgeAttack.setText(gui_config[x])
                # 手镯
                x += 1
            if x < y:
                self.ui.braceletType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.braceletBadgeAttack.setText(gui_config[x])
                # 戒指
                x += 1
            if x < y:
                self.ui.ringType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.ringBadgeAttack.setText(gui_config[x])
                # 辅助装备
                x += 1
            if x < y:
                self.ui.supportType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.supportBadgeAttack.setText(gui_config[x])
                # 魔法石
                x += 1
            if x < y:
                self.ui.magicstoneType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.magicstoneBadgeAttack.setText(gui_config[x])
                # 耳环
                x += 1
            if x < y:
                self.ui.earrringType.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringBadge.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.earrringBadgeAttack.setText(gui_config[x])
                # 装扮
                x += 1
            if x < y:
                self.ui.dressAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressSkill1.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressSkill2.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressBadge.setText(gui_config[x])
                # 称号
                x += 1
            if x < y:
                self.ui.titleAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.titleAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.titleEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.titleSkill.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.titleBox.setCurrentIndex(gui_config[x])
                # 其他
                x += 1
            if x < y:
                self.ui.groupAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.guildAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.trainerAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.marriageAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.marriageAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.marriageEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.collectAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.collectAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.collectEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.medalAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.medalAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.medalEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.decorationAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.viceAttack.setText(gui_config[x])
                # 最后一行
                x += 1
            if x < y:
                self.ui.grainAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.grainAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.grainEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petequipmentAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petequipmentAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petequipmentEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petEnh.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.petSkill.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.perAttributes.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.addtional.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.finall.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.crit.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.skill.setText(gui_config[x])
                # 职业、训练官攻击力、装扮徽章攻击力，因考虑兼容问题单独写
                x += 1
            if x < y:
                self.ui.categoryBox.setCurrentIndex(gui_config[x])
                x += 1
            if x < y:
                self.ui.dressBadgeAttack.setText(gui_config[x])
                x += 1
            if x < y:
                self.ui.trainerAttack.setText(gui_config[x])
                # 晶体契约
                x += 1
            if x < y:
                self.ui.contractCheck.setChecked(gui_config[x])
                # 暗抗
                x += 1
            if x < y:
                self.ui.darkResistance.setText(gui_config[x])
                # 移速
                x += 1
            if x < y:
                self.ui.movingSpeed.setText(gui_config[x])
                x += 1

    def clear_config(self):
        # 杂项
        self.ui.attributesBox.setCurrentIndex(0)
        self.ui.attackBox.setCurrentIndex(0)
        self.ui.mythBox.setCurrentIndex(0)
        # 武器
        self.ui.weaponType.setCurrentIndex(0)
        self.ui.weaponBox.setCurrentIndex(0)
        self.ui.weaponAttributes.setText("")
        self.ui.weaponAttack.setText("")
        self.ui.weaponEnh.setText("")
        self.ui.weaponForge.setCurrentIndex(0)
        self.ui.type.setCurrentIndex(0)
        # 上衣
        self.ui.coatType.setCurrentIndex(0)
        self.ui.coatBox.setCurrentIndex(0)
        self.ui.coatAttributes.setText("")
        self.ui.coatAttack.setText("")
        self.ui.coatEnh.setText("")
        self.ui.coatSkill.setCurrentIndex(0)
        self.ui.coatBadge.setText("")
        self.ui.coatBadgeAttack.setText("")
        # 护肩
        self.ui.neckType.setCurrentIndex(0)
        self.ui.neckBox.setCurrentIndex(0)
        self.ui.neckAttributes.setText("")
        self.ui.neckAttack.setText("")
        self.ui.neckEnh.setText("")
        self.ui.neckSkill.setCurrentIndex(0)
        self.ui.neckBadge.setText("")
        self.ui.neckBadgeAttack.setText("")
        # 下装
        self.ui.pantsType.setCurrentIndex(0)
        self.ui.pantsBox.setCurrentIndex(0)
        self.ui.pantsAttributes.setText("")
        self.ui.pantsAttack.setText("")
        self.ui.pantsEnh.setText("")
        self.ui.pantsSkill.setCurrentIndex(0)
        self.ui.pantsBadge.setText("")
        self.ui.pantsBadgeAttack.setText("")
        # 鞋
        self.ui.shoesType.setCurrentIndex(0)
        self.ui.shoesBox.setCurrentIndex(0)
        self.ui.shoesAttributes.setText("")
        self.ui.shoesAttack.setText("")
        self.ui.shoesEnh.setText("")
        self.ui.shoesSkill.setCurrentIndex(0)
        self.ui.shoesBadge.setText("")
        self.ui.shoesBadgeAttack.setText("")
        # 腰带
        self.ui.beltType.setCurrentIndex(0)
        self.ui.beltBox.setCurrentIndex(0)
        self.ui.beltAttributes.setText("")
        self.ui.beltAttack.setText("")
        self.ui.beltEnh.setText("")
        self.ui.beltSkill.setCurrentIndex(0)
        self.ui.beltBadge.setText("")
        self.ui.beltBadgeAttack.setText("")
        # 项链
        self.ui.necklaceType.setCurrentIndex(0)
        self.ui.necklaceBox.setCurrentIndex(0)
        self.ui.necklaceAttributes.setText("")
        self.ui.necklaceAttack.setText("")
        self.ui.necklaceEnh.setText("")
        self.ui.necklaceSkill.setCurrentIndex(0)
        self.ui.necklaceBadge.setText("")
        self.ui.necklaceBadgeAttack.setText("")
        # 手镯
        self.ui.braceletType.setCurrentIndex(0)
        self.ui.braceletBox.setCurrentIndex(0)
        self.ui.braceletAttributes.setText("")
        self.ui.braceletAttack.setText("")
        self.ui.braceletEnh.setText("")
        self.ui.braceletSkill.setCurrentIndex(0)
        self.ui.braceletBadge.setText("")
        self.ui.braceletBadgeAttack.setText("")
        # 戒指
        self.ui.ringType.setCurrentIndex(0)
        self.ui.ringBox.setCurrentIndex(0)
        self.ui.ringAttributes.setText("")
        self.ui.ringAttack.setText("")
        self.ui.ringEnh.setText("")
        self.ui.ringSkill.setCurrentIndex(0)
        self.ui.ringBadge.setText("")
        self.ui.ringBadgeAttack.setText("")
        # 辅助装备
        self.ui.supportType.setCurrentIndex(0)
        self.ui.supportBox.setCurrentIndex(0)
        self.ui.supportAttributes.setText("")
        self.ui.supportAttack.setText("")
        self.ui.supportEnh.setText("")
        self.ui.supportSkill.setCurrentIndex(0)
        self.ui.supportBadge.setText("")
        self.ui.supportBadgeAttack.setText("")
        # 魔法石
        self.ui.magicstoneType.setCurrentIndex(0)
        self.ui.magicstoneBox.setCurrentIndex(0)
        self.ui.magicstoneAttributes.setText("")
        self.ui.magicstoneAttack.setText("")
        self.ui.magicstoneEnh.setText("")
        self.ui.magicstoneSkill.setCurrentIndex(0)
        self.ui.magicstoneBadge.setText("")
        self.ui.magicstoneBadgeAttack.setText("")
        # 耳环
        self.ui.earrringType.setCurrentIndex(0)
        self.ui.earrringBox.setCurrentIndex(0)
        self.ui.earrringAttributes.setText("")
        self.ui.earrringAttack.setText("")
        self.ui.earrringEnh.setText("")
        self.ui.earrringSkill.setCurrentIndex(0)
        self.ui.earrringBadge.setText("")
        self.ui.earrringBadgeAttack.setText("")
        # 装扮
        self.ui.dressAttributes.setText("")
        self.ui.dressAttack.setText("")
        self.ui.dressEnh.setText("")
        self.ui.dressSkill1.setCurrentIndex(0)
        self.ui.dressSkill2.setCurrentIndex(0)
        self.ui.dressBadge.setText("")
        # 称号
        self.ui.titleAttributes.setText("")
        self.ui.titleAttack.setText("")
        self.ui.titleEnh.setText("")
        self.ui.titleSkill.setCurrentIndex(0)
        self.ui.titleBox.setCurrentIndex(0)
        # 其他
        self.ui.groupAttributes.setText("")
        self.ui.guildAttributes.setText("")
        self.ui.trainerAttributes.setText("")
        self.ui.marriageAttributes.setText("")
        self.ui.marriageAttack.setText("")
        self.ui.marriageEnh.setText("")
        self.ui.collectAttributes.setText("")
        self.ui.collectAttack.setText("")
        self.ui.collectEnh.setText("")
        self.ui.medalAttributes.setText("")
        self.ui.medalAttack.setText("")
        self.ui.medalEnh.setText("")
        self.ui.decorationAttributes.setText("")
        self.ui.viceAttack.setText("")
        # 最后一行
        self.ui.grainAttributes.setText("")
        self.ui.grainAttack.setText("")
        self.ui.grainEnh.setText("")
        self.ui.petequipmentAttributes.setText("")
        self.ui.petequipmentAttack.setText("")
        self.ui.petequipmentEnh.setText("")
        self.ui.petAttributes.setText("")
        self.ui.petAttack.setText("")
        self.ui.petEnh.setText("")
        self.ui.petSkill.setText("")
        self.ui.perAttributes.setText("")
        self.ui.addtional.setText("")
        self.ui.finall.setText("")
        self.ui.crit.setText("")
        self.ui.skill.setText("")
        # 职业、训练官攻击力、装扮徽章攻击力，因考虑兼容问题单独写
        self.ui.categoryBox.setCurrentIndex(0)
        self.ui.dressBadgeAttack.setText("")
        self.ui.trainerAttack.setText("")
        # 晶体契约
        self.ui.contractCheck.setChecked(False)

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
        gui_config.append(self.ui.coatBadgeAttack.text())

        # 头肩
        gui_config.append(self.ui.neckType.currentIndex())
        gui_config.append(self.ui.neckBox.currentIndex())
        gui_config.append(self.ui.neckAttributes.text())
        gui_config.append(self.ui.neckAttack.text())
        gui_config.append(self.ui.neckEnh.text())
        gui_config.append(self.ui.neckSkill.currentIndex())
        gui_config.append(self.ui.neckBadge.text())
        gui_config.append(self.ui.neckBadgeAttack.text())

        # 下装
        gui_config.append(self.ui.pantsType.currentIndex())
        gui_config.append(self.ui.pantsBox.currentIndex())
        gui_config.append(self.ui.pantsAttributes.text())
        gui_config.append(self.ui.pantsAttack.text())
        gui_config.append(self.ui.pantsEnh.text())
        gui_config.append(self.ui.pantsSkill.currentIndex())
        gui_config.append(self.ui.pantsBadge.text())
        gui_config.append(self.ui.pantsBadgeAttack.text())

        # 鞋
        gui_config.append(self.ui.shoesType.currentIndex())
        gui_config.append(self.ui.shoesBox.currentIndex())
        gui_config.append(self.ui.shoesAttributes.text())
        gui_config.append(self.ui.shoesAttack.text())
        gui_config.append(self.ui.shoesEnh.text())
        gui_config.append(self.ui.shoesSkill.currentIndex())
        gui_config.append(self.ui.shoesBadge.text())
        gui_config.append(self.ui.shoesBadgeAttack.text())

        # 腰带
        gui_config.append(self.ui.beltType.currentIndex())
        gui_config.append(self.ui.beltBox.currentIndex())
        gui_config.append(self.ui.beltAttributes.text())
        gui_config.append(self.ui.beltAttack.text())
        gui_config.append(self.ui.beltEnh.text())
        gui_config.append(self.ui.beltSkill.currentIndex())
        gui_config.append(self.ui.beltBadge.text())
        gui_config.append(self.ui.beltBadgeAttack.text())

        #项链
        gui_config.append(self.ui.necklaceType.currentIndex())
        gui_config.append(self.ui.necklaceBox.currentIndex())
        gui_config.append(self.ui.necklaceAttributes.text())
        gui_config.append(self.ui.necklaceAttack.text())
        gui_config.append(self.ui.necklaceEnh.text())
        gui_config.append(self.ui.necklaceSkill.currentIndex())
        gui_config.append(self.ui.necklaceBadge.text())
        gui_config.append(self.ui.necklaceBadgeAttack.text())

        # 手镯
        gui_config.append(self.ui.braceletType.currentIndex())
        gui_config.append(self.ui.braceletBox.currentIndex())
        gui_config.append(self.ui.braceletAttributes.text())
        gui_config.append(self.ui.braceletAttack.text())
        gui_config.append(self.ui.braceletEnh.text())
        gui_config.append(self.ui.braceletSkill.currentIndex())
        gui_config.append(self.ui.braceletBadge.text())
        gui_config.append(self.ui.braceletBadgeAttack.text())

        # 戒指
        gui_config.append(self.ui.ringType.currentIndex())
        gui_config.append(self.ui.ringBox.currentIndex())
        gui_config.append(self.ui.ringAttributes.text())
        gui_config.append(self.ui.ringAttack.text())
        gui_config.append(self.ui.ringEnh.text())
        gui_config.append(self.ui.ringSkill.currentIndex())
        gui_config.append(self.ui.ringBadge.text())
        gui_config.append(self.ui.ringBadgeAttack.text())

        # 辅助装备
        gui_config.append(self.ui.supportType.currentIndex())
        gui_config.append(self.ui.supportBox.currentIndex())
        gui_config.append(self.ui.supportAttributes.text())
        gui_config.append(self.ui.supportAttack.text())
        gui_config.append(self.ui.supportEnh.text())
        gui_config.append(self.ui.supportSkill.currentIndex())
        gui_config.append(self.ui.supportBadge.text())
        gui_config.append(self.ui.supportBadgeAttack.text())

        # 魔法石
        gui_config.append(self.ui.magicstoneType.currentIndex())
        gui_config.append(self.ui.magicstoneBox.currentIndex())
        gui_config.append(self.ui.magicstoneAttributes.text())
        gui_config.append(self.ui.magicstoneAttack.text())
        gui_config.append(self.ui.magicstoneEnh.text())
        gui_config.append(self.ui.magicstoneSkill.currentIndex())
        gui_config.append(self.ui.magicstoneBadge.text())
        gui_config.append(self.ui.magicstoneBadgeAttack.text())

        # 耳环
        gui_config.append(self.ui.earrringType.currentIndex())
        gui_config.append(self.ui.earrringBox.currentIndex())
        gui_config.append(self.ui.earrringAttributes.text())
        gui_config.append(self.ui.earrringAttack.text())
        gui_config.append(self.ui.earrringEnh.text())
        gui_config.append(self.ui.earrringSkill.currentIndex())
        gui_config.append(self.ui.earrringBadge.text())
        gui_config.append(self.ui.earrringBadgeAttack.text())

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

        # 职业、训练官攻击力、装扮徽章攻击力，因考虑兼容问题单独写
        gui_config.append(self.ui.categoryBox.currentIndex())
        gui_config.append(self.ui.dressBadgeAttack.text())
        gui_config.append(self.ui.trainerAttack.text())

        # 晶体契约
        gui_config.append(int(self.ui.contractCheck.isChecked()))

        #暗抗移速
        gui_config.append(self.ui.darkResistance.text())
        gui_config.append(self.ui.movingSpeed.text())

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
        if self.ui.coatBadgeAttack.text() != "":
            coat_dict7 = {attack : int(self.ui.coatBadgeAttack.text())}
            entries.append(coat_dict7)

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
        if self.ui.neckBadgeAttack.text() != "":
            neck_dict7 = {attack : int(self.ui.neckBadgeAttack.text())}
            entries.append(neck_dict7)

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
        if self.ui.pantsBadgeAttack.text() != "":
            pants_dict7 = {attack : int(self.ui.pantsBadgeAttack.text())}
            entries.append(pants_dict7)

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
        if self.ui.shoesBadgeAttack.text() != "":
            shoes_dict7 = {attack : int(self.ui.shoesBadgeAttack.text())}
            entries.append(shoes_dict7)

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
        if self.ui.beltBadgeAttack.text() != "":
            belt_dict7 = {attack : int(self.ui.beltBadgeAttack.text())}
            entries.append(belt_dict7)

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
        if self.ui.necklaceBadgeAttack.text() != "":
            necklace_dict7 = {attack : int(self.ui.necklaceBadgeAttack.text())}
            entries.append(necklace_dict7)

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
        if self.ui.braceletBadgeAttack.text() != "":
            bracelet_dict7 = {attack : int(self.ui.braceletBadgeAttack.text())}
            entries.append(bracelet_dict7)

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
        if self.ui.ringBadgeAttack.text() != "":
            ring_dict7 = {attack : int(self.ui.ringBadgeAttack.text())}
            entries.append(ring_dict7)

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
        if self.ui.supportBadgeAttack.text() != "":
            support_dict7 = {attack : int(self.ui.supportBadgeAttack.text())}
            entries.append(support_dict7)

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
        if self.ui.magicstoneBadgeAttack.text() != "":
            magicstone_dict7 = {attack : int(self.ui.magicstoneBadgeAttack.text())}
            entries.append(magicstone_dict7)

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
        if self.ui.earrringBadgeAttack.text() != "":
            earrring_dict7 = {attack : int(self.ui.earrringBadgeAttack.text())}
            entries.append(earrring_dict7)

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
            dress_dict5 = {"extra_all_job_all_skill_lv_1_50" : 1}
            entries.append(dress_dict5)
        elif self.ui.dressSkill2.currentIndex() == 2:
            dress_dict5 = {"extra_all_job_all_active_skill_lv_1_30" : 1}
            entries.append(dress_dict5)
        if self.ui.dressBadge.text() != "":
            dress_dict6 = {attributes : int(self.ui.dressBadge.text())}
            entries.append(dress_dict6)
        if self.ui.dressBadgeAttack.text() != "":
            dress_dict7 = {attack : int(self.ui.dressBadgeAttack.text())}
            entries.append(dress_dict7)

        ## 称号附魔
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
        elif self.ui.titleSkill.currentIndex() == 6:
            title_dict5 = {"extra_taiyang_skill" : 2}
            entries.append(title_dict5)

        if self.ui.titleBox.currentIndex() == 1:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 1}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 2:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 1}
            title_dict7 = {"extra_bless_skill" : 1}
            entries.append(title_dict6)
            entries.append(title_dict7)
        elif self.ui.titleBox.currentIndex() == 3:
            title_dict6 = {"extra_all_job_all_skill_lv_25_30_in_buff_dress_up" : 1}
            title_dict7 = {"extra_bless_skill" : 2}
            entries.append(title_dict6)
            entries.append(title_dict7)  
        elif self.ui.titleBox.currentIndex() == 4:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 1}
            entries.append(title_dict6)
        elif self.ui.titleBox.currentIndex() == 5:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 1}
            title_dict7 = {"extra_bless_skill" : 1}
            entries.append(title_dict6)
            entries.append(title_dict7)
        elif self.ui.titleBox.currentIndex() == 6:
            title_dict6 = {"extra_all_job_all_skill_lv_30_35_in_buff_dress_up" : 1}
            title_dict7 = {"extra_bless_skill" : 2}
            entries.append(title_dict6)
            entries.append(title_dict7)

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
        if self.ui.trainerAttack.text() != "":
            trainer_dict1 = {attack : int(self.ui.trainerAttack.text())}
            entries.append(trainer_dict1)

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

        # 晶体契约
        if self.ui.contractCheck.isChecked():
            contract_dict = {attack : 40}
            entries.append(contract_dict)

        #移速暗抗
        if self.ui.darkResistance.text() != "":
            dark_dict = {"extra_dark_resistance" : int(self.ui.darkResistance.text())}
            entries.append(dark_dict)
        if self.ui.movingSpeed.text() != "":
            moving_dict = {"extra_percent_moving_speed" : int(self.ui.movingSpeed.text())}
            entries.append(moving_dict)

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
        msgBox.setText('保存成功，在主程序中点击重载配置后存档生效。')
        ok = msgBox.addButton(QMessageBox.Ok)
        msgBox.setDefaultButton(ok)
        msgBox.exec()

    def save_button(self):
        self.save_config(configItems)

    def find_index(self,config):
                    for i in range(len(config)):
                        if self.ui.nameBox.currentText() == config[i]["names"][0]:
                            index = i
                    return(index)

    def add_button(self):
        if self.ui.nameBox.findText("新存档") == -1:
            names = find_names(readyaml())
            names.append("新存档")
            self.ui.nameBox.clear()
            self.ui.nameBox.addItems(names)
            self.ui.nameBox.setCurrentIndex(self.ui.nameBox.findText("新存档"))
            msgBox = QMessageBox(QMessageBox.Information, '提示','已建立新的存档，修改完毕后保存即可。')
            msgBox.exec()
        else:
            msgBox = QMessageBox(QMessageBox.Critical, '错误','已有新的存档，如需建立更新的存档，请删除或将新存档命名为其他名称后再建立新存档。')
            msgBox.exec()

    def minus_button(self):
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
            if self.ui.nameBox.currentText() in find_names(readyaml()):
                num = self.find_index(readyaml())
                del configItems[num]
                self.ui.nameBox.removeItem(self.ui.nameBox.currentIndex())
                writeyaml("../setting/account_other_bonus_attributes.yaml",configItems)
            else:
                self.ui.nameBox.removeItem(self.ui.nameBox.currentIndex())
       
if __name__ == "__main__":
    app = QApplication([])
    config = Config()
    config.ui.show()
    app.exec_()
