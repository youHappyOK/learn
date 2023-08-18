import pyautogui

# # 分辨率
# print(pyautogui.size())
#
# 鼠标位置
# print(pyautogui.position())
#
# # 查看像素是否存在屏幕上
# print(pyautogui.onScreen(1439, 10))
#
# # 当前位置移动鼠标到绝对位置，持续时间秒
# pyautogui.moveTo(800, 700, 2)
#
# # 当前位置移动鼠标到相对位置
# pyautogui.move(0, -300, 2)

# 当前位置左键拖动鼠标到绝对位置，持续时间秒
# pyautogui.dragTo(100, 100, button='left', duration=1)

# 当前位置拖动鼠标到相对位置，持续时间秒
# pyautogui.drag(100, 100, button='left', duration=2)

# # 鼠标点击绝对位置
# pyautogui.click(x=1248, y=59)
# # 鼠标当前位置左击
# pyautogui.click()
# # 鼠标右击
# pyautogui.click(x=1248, y=59, button='right', duration=3)
# # 鼠标点几次
# pyautogui.click(clicks=2)
# # 点击间隔秒, mac不支持双击打开文件
# pyautogui.click(x=1248, y=59, button='left', clicks=2, interval=0.1, duration=1)
# # 双击，mac不支持
# pyautogui.doubleClick(x=1248, y=59)
# # 三击
# pyautogui.tripleClick()

# # 按住鼠标左键不放, mac无效
# pyautogui.mouseDown(button='left')
# pyautogui.move(-100, 0)
# # 放开鼠标左键
# pyautogui.mouseUp(button='left')

# 鼠标向上滚动(负数代表向下)
# pyautogui.scroll(10, x=700, y=700)

# 控制键盘输入
# x, y = pyautogui.position()
# pyautogui.click(x, y)
# pyautogui.write("i am stupid", interval=0.25)

# 摁下一个键后释放
# x, y = pyautogui.position()
# pyautogui.click(x, y)
# pyautogui.press('enter')
# pyautogui.press('F1')
# pyautogui.press('left')

# # 按住shift的同时按三次左箭头
# pyautogui.keyDown('shift')
# # 或者写成pyautogui.press(['left', 'left', 'left'])或pyautogui.press('left', presses=3)
# pyautogui.press('left')
# pyautogui.press('left')
# pyautogui.press('left')
# pyautogui.keyUp('shift')

# 组合键按顺序摁下，然后按反方向释放（mac好像没用？）
# pyautogui.hotkey('command', 'option', 'escape')

# 截图名字(mac不生效)
#pyautogui.screenshot('jieping1.png')
#pyautogui.screenshot(region=((0, 0, 300, 400)))

# 图像定位（用子图像文件在整个桌面找，不适用,很慢，精确度低）

# 像素匹配

