#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: DmTool.py
Author: 吉姆哥
Date: 2023/8/27
Description: 大漠工具类封装
"""
from PyGameAuto32 import PyGameAuto


class DmTool:

    dm = None

    resourcePath = ''

    # 初始化全局大漠对象
    @staticmethod
    def initGlobleDmObj():
        # 初始化全局大漠对象
        dm = PyGameAuto.gl_init("ly901107a81915b5c54de20f31cfa5a0a00ffad8", "lexgeeker01234567890")
        py = PyGameAuto()
        # 设置操作对象
        py.set_win(dm)
        path = py.get_path()
        print('项目路径 %s' % path)
        resourcePath = "\\".join(str(path).split("\\")[:-1]) + "\\" + 'resource'
        # 设置资源文件路径（图片、描述文件等）
        py.set_path(resourcePath)
        print('资源文件路径 %s' % resourcePath)
        py.set_level(0)
        # py.set_dict(0, 'font.txt')
