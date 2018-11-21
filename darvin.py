import win32api
import win32gui
import win32con
import time
import random
import os
import configparser

cur_path=os.path.dirname(os.path.realpath(__file__))
config_path=os.path.join(cur_path,'config.ini')
conf=configparser.ConfigParser()
conf.read(config_path)

#mishu = input("想跑大概多少米?输入整数:")
mishu = conf.get('param','mishu')  #总路程
mishu = int(mishu)
	
minut = conf.get('param','minute')
minut = int(minut)
miao  = minut * 60

speed = conf.get('param','speed')  #米每秒
speed = int(speed)
nameOfp = input("采用默认位置矩形输入y,否则输入自定义举行名:\n")
if(nameOfp=="y"):
	nameOfp="p1"
oriws=conf.get("point",nameOfp+"_wei").split(",")
orijs=conf.get("point",nameOfp+"_jing").split(",")
for i in range(4):
	oriws[i]=float(oriws[i])
	orijs[i]=float(orijs[i])
print(oriws)
print(orijs) 
s1="夜神模拟器"
s2="位置设置"

winName = s2
handle = win32gui.FindWindow(0,winName);
'''
oriws=[30.612583,30.612312,30.614406,30.614701]
orijs=[114.36475,114.36293,114.36250,114.36430]

oriws=[30.612505,30.61245,30.613434,30.613543]
orijs=[114.36240,114.36164,114.36141,114.36220]
'''
ws =[]
js =[]
VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

def genS(th,ts):
	for i in range(len(oriws)):
		w1=oriws[i]
		j1=orijs[i]
		if i!=len(oriws)-1 :
			w2=oriws[i+1]
			j2=orijs[i+1]
		else :
			w2=oriws[0]
			j2=orijs[0]
			
		if (i+1)%2!=0 :
				perw=(w2-w1)/th;
				perj=(j2-j1)/th;
				nPo = th;
		else :
				perw=(w2-w1)/ts;
				perj=(j2-j1)/ts;
				nPo = ts;
		while nPo>0 :
			ws.append(w1)
			js.append(j1)
			w1 = w1 + perw
			j1 = j1 + perj
			nPo = nPo - 1
def cliP(x,y) :
	p = (x,y)
	win32api.SetCursorPos(p)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0); 
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0); 
def cliP1():
	cliP(337,64)
	cliP(337,64)
	cliP(337,64)
	cliP(337,64)
def cliP2():
	cliP(446,64)
	cliP(446,64)
	cliP(446,64)
	cliP(446,64)
def cliP3():
	cliP(412,401)
	cliP(412,401)
	cliP(412,401)
def initi():
	cliP1()
	for i  in range(30):
		win32api.keybd_event(win32con.VK_DELETE,0,0,0);
		win32api.keybd_event(win32con.VK_DELETE,0,win32con.KEYEVENTF_KEYUP,0);
	win32api.keybd_event(win32con.VK_TAB,0,0,0);
	win32api.keybd_event(win32con.VK_TAB,0,win32con.KEYEVENTF_KEYUP,0);
	for i in range(30):
		win32api.keybd_event(win32con.VK_DELETE,0,0,0);
		win32api.keybd_event(win32con.VK_DELETE,0,win32con.KEYEVENTF_KEYUP,0);
def key_input(w,j):
	for p in w:
		win32api.keybd_event(VK_CODE[p], 0, 0, 0)
		win32api.keybd_event(VK_CODE[p], 0, win32con.KEYEVENTF_KEYUP, 0)
	win32api.keybd_event(win32con.VK_TAB,0,0,0);
	win32api.keybd_event(win32con.VK_TAB,0,win32con.KEYEVENTF_KEYUP,0);
	for p in j:
		win32api.keybd_event(VK_CODE[p], 0, 0, 0)
		win32api.keybd_event(VK_CODE[p], 0, win32con.KEYEVENTF_KEYUP, 0)
		
EARTH_REDIUS = 6378.137
import math
pi = math.pi
def rad(d):
    return d * pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return 1000*s   #以米为单位 

def wucha():
	w= random.random()
	if w>0.5 :
		w = (w-0.5)*(-1)
	w = w/100000
	return w


if handle!=0:
	print("已找到 "+winName+" 窗口\n")
	print(winName+" 的窗口句柄:"+str(handle))
	#button = win32gui.FindWindowEx(handle,None,"Button",None)
	#print(button)
	
	win32gui.ShowWindow(handle,win32con.SW_RESTORE)
	win32gui.SetForegroundWindow(handle)
	print("已激活 "+winName+" 窗口\n")
	
	handleDetail = win32gui.GetWindowRect(handle)  # 返回(x1,y2,x2,y2) tuple类型，其中，左上角点为(x1,y1),右下角点(x2,y2)
	
	
	#handleMenu = win32gui.GetMenu(handle)
	#print("菜单句柄:"+str(handleMenu))
	
	wWidth = handleDetail[2]-handleDetail[0]
	wHeight= handleDetail[3]-handleDetail[1]
	print("窗口信息:"+str(handleDetail))
	bili = wWidth/wHeight  
	print("窗口比例:"+str(bili))
	win32gui.MoveWindow(handle,0,0,wWidth,wHeight,1)
	handleDetail = win32gui.GetWindowRect(handle)
	print("窗口信息:"+str(handleDetail)+"\n")
	#handleSubMenu = win32gui.GetSubMenu(handleMenu,0)
	#print(handleSubMenu)
	
	
	px = [337,446,412 ]
	py = [64,64,401]
	
	hDis = getDistance(oriws[0],orijs[0],oriws[1],orijs[1]) 
	sDis = getDistance(oriws[1],orijs[1],oriws[2],orijs[2]) 
	
	hhs = hDis/speed
	sss = sDis/speed
	hhs = round(hhs)
	sss = round(sss)
	genS(hhs,sss)
	cirDis = (hDis + sDis) * 2
	print("当前配置：")
	print("	横向距离为"+str(hDis)+"米")
	print("	竖直距离为"+str(sDis)+"米")
	print("	一圈总长为"+str(cirDis)+"米")
	print("	横向点数为"+str(hhs))
	print("	纵向点数为"+str(sss))
	
	print("	总路程:"+str(mishu)+"米")
	print("	总时间:"+str(minut)+"分钟")
	print("	速度  :"+str(speed)+"米/秒")
	times = 3
	lucheng = 0
	tai = True
	while tai :
		for k in range(len(ws)):
			initi()
			cliP1()
			key_input(str(ws[k]+wucha()),str(js[k]+wucha()))
			cliP2()
			cliP3()
			time.sleep(1)
			lucheng = lucheng + speed
			if lucheng > mishu :
				tai = False
				break;
			
else:
	print("未找到叫做 "+winName+" 的窗口")
	win32api.MessageBox(0,"请打开位置设置","错误",win32con.MB_OK)