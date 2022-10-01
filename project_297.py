from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
broker = 'broker.emqx.io'
port = 1883
topic = "topicName/iot"




client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client


@app.route('/')
def index():
	return render_template('index.html')
@app.route('/main', methods = ['POST'])
def main():
	return render_template('main.html')
@app.route('/index', methods = ['POST'])
def release():
	release_test()
	return render_template('1.html')
def release_test():
	client = connect_mqtt()
	client.loop_start()
	send_release_data(client)
@app.route('/2', methods = ['POST'])

def send_release_data(client):
	msg = "1"
	result = client.publish(topic, msg)
	status = results[1]
	if status == 1:
		print("Send `{msg}` to topic `{topic}`")



#Define the Release Orbital Arm button and connect with MQTT server

#Define the Main Engine Test button and connect with MQTT server

#Define the Activate Hydrogen button and connect with MQTT server

#Define the Main Engine Ignite button and connect with MQTT server

#Define the Hydrogen Vent Arm button and connect with MQTT server

#Define the Ignite both SRB's button and connect with MQTT server

if __name__ == "__main__":
    app.run(port=5001)





