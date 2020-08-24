from flask import Flask
from flask import request
from RPi import GPIO
'use ifconfig -a to get ip address, to connect easily'

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

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
				$('#btnOff').click(function(){
					$.ajax({
						type: 'POST',
						url: '/off',
						success: function(data){
							$('#txtRespond').text('off requested')
						}
					});
				});
			});
		</script>
	</head>
	<body>
		<p id='txtRespond'></p>
		<button id='btnOn'>ON</button>
		<button id='btnOff'>OFF</button>
	</body>
</html>'''
	except Exception as e:
		print(e)

@app.route('/on', methods=['POST'])
def on():
	if request.method == 'POST':
		GPIO.output(7, GPIO.HIGH)
		return 'OK'
	else:
		return 'NOT OK'
@app.route('/off', methods =['POST'])
def off():
	if request.method == 'POST':
		GPIO.output(7, GPIO.LOW)
		return 'OK'
	else:
		return 'NOT OK'

if __name__ == '__main__':
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7, GPIO.OUT)
		app.run(debug=True, host='0.0.0.0')
	except Exception as e:
		print(e)
