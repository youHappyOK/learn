#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: LdTool.py
Author: 吉姆哥
Date: 2023/8/27
Description: 雷电模拟器工具类
"""
import os

from practice_part2.common.Container import Container


class LdTool:

    def __init__( self, installation_path:str):
        '''
        【构造方法】
        '''
        # if 模拟器安装路径存在性检测
        if os.path.exists(installation_path) is False:
            print('模拟器安装路径不存在！')
        # 获取模拟器安装路径
        self.ins_path = installation_path
        # Dnconsole程序路径
        self.console_path = self.ins_path + r'\ldconsole.exe '
        # if Dnconsole程序路径检测
        if os.path.exists(self.console_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整或模拟器版本是否不符！')
        # adb程序路径
        self.adb_path = self.ins_path + r'\adb.exe '
        # if adb程序路径检测
        if os.path.exists(self.adb_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整！')
        # 模拟器截屏程序路径
        self.screencap_path = r'/system/bin/screencap'
        # 模拟器截图保存路径
        self.devicess_path = r'/sdcard/autosS.png'
        # 本地图片保存路径
        self.images_path = r'D:\PycharmWorkspace\images'
        # 构造完成
        print('Class-Dnconsole is ready.(%s)' % (self.ins_path))

        Container.set('LdTool',  self)


    def CMD(self, cmd: str):
        '''
        【执行控制台命令语句】
        :param cmd: 命令
        :return: 控制台调试内容
        '''
        CMD = self.console_path + cmd  # 控制台命令
        process = os.popen(CMD)
        result = process.read()
        process.close()
        return result

    def quit(self, index: int = 0):
        '''
        【关闭模拟器】
        :param index: 模拟器序号
        '''
        cmd = 'quit --index %d' % (index)
        self.CMD(cmd)

    def quitall(self):
        '''
        【关闭所有模拟器】
        '''
        cmd = 'quitall'
        self.CMD(cmd)

    def launch(self, index: int = 0):
        '''
        【启动模拟器】
        :param index: 模拟器序号
        :return: True=已启动 / False=不存在
        '''
        cmd = 'launch --index %d' % (index)
        if self.CMD(cmd) == '':
            return True
        else:
            return False

    def reboot(self, index: int = 0):
        '''
        【重启模拟器】
        :param index: 模拟器序号
        :return: 控制台调试内容
        '''
        cmd = 'reboot --index %d' % (index)
        return self.CMD(cmd)

    def list(self):
        '''
        【获取模拟器列表（仅标题）】
        :return: 控制台调试内容
        '''
        cmd = 'list'
        return self.CMD(cmd)

    def runninglist(self):
        '''
        【获取正在运行的模拟器列表（仅标题）】
        :return: 控制台调试内容
        '''
        cmd = 'runninglist'
        return self.CMD(cmd)

    def isrunning(self, index: int = 0):
        '''
        【检测模拟器是否启动】
        :param index: 模拟器序号
        :return: True=已启动 / False=未启动
        '''
        cmd = 'isrunning --index %d' % (index)
        if self.CMD(cmd) == 'running':
            return True
        else:
            return False

    def list2(self):
        '''
        【取模拟器列表】
        :return: 列表（索引、标题、顶层句柄、绑定句柄、是否进入android、进程PID、VBox进程PID）
        '''
        cmd = 'list2'
        return self.CMD(cmd)

    def add(self, name: str):
        '''
        【添加模拟器】
        :param name: 新模拟器标题
        :return: 控制台调试内容
        '''
        cmd = 'add %s' % (name)
        return self.CMD(cmd)

    def copy(self, name: str, index: int):
        '''
        【复制模拟器】
        :param name: 新模拟器标题
        :param index: 原模拟器序号
        :return: 控制台调试内容
        '''
        if not name:
            cmd = 'copy --from %d' % (index)
        else:
            cmd = 'copy --name %s --from %d' % (name, index)
        return self.CMD(cmd)

    def remove(self, index: int):
        '''
        【移除模拟器】
        :param index: 模拟器序号
        :return: 控制台调试内容
        '''
        cmd = 'remove --index %d' % (index)
        return self.CMD(cmd)

    def rename(self, index: int, newtitle: str):
        '''
        【重命名模拟器】
        :param index: 模拟器序号
        :param newtitle: 模拟器新标题
        :return: 控制台调试内容
        '''
        cmd = 'rename --index %d --title %s' % (index, newtitle)
        return self.CMD(cmd)

    def modifyResolution(self, index: int, width, height, dpi):
        '''
        【修改模拟器配置 - 分辨率】
        :param index: 模拟器序号
        :param width: 显示宽度
        :param height: 显示高度
        :param dpi: 每英寸点数
        :return: 控制台调试内容
        '''
        cmd = 'modify --index %d --resolution %s,%s,%s' % (index, width, height, dpi)
        return self.CMD(cmd)

    def modifyCPU(self, index: int, cpu, memory):
        '''
        【修改模拟器配置 - CPU与内存】
        :param index: 模拟器序号
        :param cpu: 模拟器CPU数量（1，2，3，4）
        :param memory: 模拟器内存大小（256，512，768，1024，1536，2048，3072，4096，6144，8192）
        :return: 控制台调试内容
        '''
        cmd = 'modify --index %d --cpu %s --memory %s' % (index, cpu, memory)
        return self.CMD(cmd)

    def modifyManufacturer(self, index: int, manufacturer, model, pnumber):
        '''
        【修改模拟器配置 - 制造商信息】
        :param index: 模拟器序号
        :param manufacturer: 制造商
        :param model: 型号
        :param pnumber: 电话号码
        :return: 控制台调试内容
        '''
        cmd = 'modify --index %d --manufacturer %s --model %s --pnumber %s' % (index, manufacturer, model, pnumber)
        return self.CMD(cmd)

    def modifyOthers(self, index: int, autorotate, lockwindow, root):
        '''
        【修改模拟器配置 - 其他选项】
        :param index: 模拟器序号
        :param autorotate: 自动旋转（1/0）
        :param lockwindow: 锁定窗口（1/0）
        :param root: ROOT（1/0）
        :return: 控制台调试内容
        '''
        cmd = 'modify --index %d --autorotate %s --lockwindow %s --root %s' % (index, autorotate, lockwindow, root)
        return self.CMD(cmd)


    def runApp(self, index: int, packagename: str):
        '''
        【运行App】
        :param index: 模拟器序号
        :param packagename: 包名
        :return: 控制台调试内容
        '''
        cmd = 'runapp --index %d --packagename %s' % (index, packagename)
        return self.CMD(cmd)

    def killApp(self, index: int, packagename: str):
        '''
        【终止App】
        :param index: 模拟器序号
        :param packagename: 包名
        :return: 控制台调试内容
        '''
        cmd = 'killapp --index %d --packagename %s' % (index, packagename)
        return self.CMD(cmd)


    def scan(self, index: int, filepath: str):
        '''
        【扫描二维码】
        :param index: 模拟器序号
        :param filepath: 图片路径
        :return: 控制台调试内容
        '''
        cmd = 'scan  --index %d --file %s' % (index, filepath)
        return self.CMD(cmd)

    def sortWnd(self):
        '''
        【对模拟器窗口排版】
        '''
        cmd = 'sortWnd'
        self.CMD(cmd)