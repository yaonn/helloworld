import os
import datetime
import requests
from random import *
import socket
import qrcode
from flask import Flask, render_template, request, send_from_directory

RPI_IP_ON = 'http://220.134.231.172:5000/on/'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#HOST_NAME = socket.gethostname() 
HOST_IP = '220.134.231.172'#socket.gethostbyname(HOST_NAME)
PORT = 5010
KEY = 0

app = Flask(__name__)

# response to request from RPi
# setup a link 
# create a qrcode picture
# return the qrcode picture to RPi
@app.route('/')
def index():
    try:
        # 二維碼內容
        global KEY
        KEY = randint(1, 100)    # Pick a random number between 1 and 100.
        data = 'http://{ip}:{port}/{key}/login/'.format(ip=HOST_IP, port=PORT,key=KEY)
        print(data)#debug
        # 生成二維碼
        img = qrcode.make(data)
        # 直接顯示二維碼
        #img.show()
        # 保存二維碼為文件
        target = os.path.join(APP_ROOT, 'images/')
        if not os.path.isdir(target):
            os.mkdir(target)
        time = datetime.datetime.now()
        time = time.strftime('%H%M%S')
        print(time) #debug
        filename = '{}.jpg'.format(time)
        destination = os.path.join(target, filename)
        print(destination)
        img.save(destination)
        return render_template('index.html', qrcode_name=filename)
    except Exception as e:
        print(e)
    
@app.route('/qrcode/<filename>/')
def getQRcode(filename):
    return send_from_directory('images', filename)

@app.route('/<key>/login/')
def openLED(key):
    print('openled:hello')
    if int(key)==KEY:
        print('KEY={};clientkey={};open led'.format(KEY,key))
        respond = requests.post(RPI_IP_ON)
        print('openLED')#debug
        print(respond)#debug
        return 'OK'
    else:
        print('KEY={};clientkey={}'.format(KEY,key))
        return 'failed'
    
# process client login request
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)