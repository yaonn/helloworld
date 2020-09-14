from flask import Flask
from flask import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import led 

MONITOR_PAGE_URL = 'http://127.0.0.1:5010/'
RESET_QRCODE_URL = 'http://127.0.0.1:5010/reset/' #/<key>

options = Options()
options.add_argument("--kiosk")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver =  webdriver.Chrome(options=options)
        
app = Flask(__name__)

@app.route('/')
def index():
    try:
        return '''<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            $(document).ready(function(){
                $('#btnOn').click(function(){
                    $.ajax({
                        type: 'POST',
                        url: '/on',
                        success: function(data){
                            $('#txtRespond').text('On requested')
                        }
                    });
                });
            });
        </script>
    </head>
    <body>
        <p id='txtRespond'></p>
        <button id='btnOn'>ON</button>
    </body>
</html>'''
    except Exception as e:
        print(e)

@app.route('/on/', methods=['POST'])
def on():
    try:
        if request.method == 'POST':
            led.on()
            if driver:
                driver.get(MONITOR_PAGE_URL)
                print('driver get {}'.format(MONITOR_PAGE_URL))#debug
            return 'OK'
        else:
            return 'NOT OK'
    except Exception as e:
        print(e)
    finally:
        return 'RPi has gotten the on request but something goes wrong'

if __name__ == '__main__':
    try:
        driver.get(MONITOR_PAGE_URL)
        app.run(debug=False, host='0.0.0.0', port=5000) #True
    except Exception as e:
        print(e)
