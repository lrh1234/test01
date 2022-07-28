import threading
import subprocess
import time
import datetime
import re

# 支持多个手机同时执行上滑操作刷视频
class myThread(threading.Thread):
    def __init__(self, did):
        threading.Thread.__init__(self)
        self.did = did

    def run(self):
        swipePhone(self.did)

# 执行shell命令
def ShellExecute(shellString):
    print(shellString,end=':::' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+'\n')
    subprocess.Popen(shellString, shell=True, stdout=subprocess.PIPE)

# 执行shell命令并拿到返回数据
def getShellExecuteReturn(shellString):
    print(shellString)
    sub = subprocess.Popen(shellString, shell=True, stdout=subprocess.PIPE)
    string = sub.stdout.read()
    results = string.decode().split('\n')
    results1 = []
    for i in results:
        if i is not None and i != '':
            results1.append(i)
    return results1

# 获取手机屏幕尺寸 x和y
def getFull(did):
    lenWig = []
    result = getShellExecuteReturn('adb -s ' + did + ' shell getevent -p | grep -e "0035" -e "0036"')
    for i in result:
        regex = 'max .*?(.*?),.*?'
        results = re.findall(regex, i, re.S)
        if len(results) > 0:
            lenWig.append(int(results[0]))
    return lenWig

# 滑动屏幕
def swipePhone(did):
    full = getFull(did)
    startx = str(full[0]/2)
    endx = str(full[0] / 2)
    starty = str(full[1]/10 * 8)
    endy = str(full[1] / 10)

    while True:
        shellString = 'adb -s ' + did + ' shell input swipe ' + startx + ' ' + starty + ' ' + endx + ' ' + endy + ' 500'
        ShellExecute(shellString)
        time.sleep(20)

didList = []
#荣耀x7
didList.append('M7TCS4LVWC9P7HJV')


for i in didList:
    thread = myThread(i)
    thread.start()
