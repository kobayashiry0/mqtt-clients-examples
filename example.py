import paho.mqtt.client as mqtt
import random
import string

# MQTT configuration
MQTT_BROKER = "localhost"  # MQTTブローカーのアドレス
MQTT_PORT = 9001  # MQTTブローカーのポート
MQTT_KEEPALIVE = 300  # キープアライブ間隔（秒）
MQTT_TOPIC_SUB = "topicA"
MQTT_TOPIC_PUB = "topicB"

# ランダムなクライアントIDを生成する関数
def generate_random_client_id(prefix="python_", length=8):
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return f"{prefix}{random_part}"

# callback関数: 接続時
def on_connect(client, userdata, flags, rc, prop):
    print("connected")
    
# callback関数: 切断時
def on_disconnect(client, userdata, flags, rc, prop):
    print("disconnected")

# callback関数: メッセージ受信時
def on_message(client, userdata, msg):
    print("received message")
    # process message
    process_message(msg.topic, msg.payload.decode("utf-8"))

# callback関数: サブスクライブ時
def on_subscribe(client, userdata, mid, rc, prop):
    print(f"subscribed topic")


def process_message(topic, payload):
    # ここにメッセージを受信した際の処理を実装
    print(f"topic:{topic}")
    print(f"payload:{payload}")


def publish_message(topic, message, qos=0, retain=False):
    client.publish(topic, message, qos, retain)
    print(f"published: {topic} - {message}")


if __name__ == "__main__":
    # initialize MQTT client
    client = mqtt.Client(client_id=generate_random_client_id(), callback_api_version=mqtt.CallbackAPIVersion.VERSION2, transport='websockets')
    
    # set callbacks
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    # client.username_pw_set("username", "password") # if needed
    
    # connect
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    # subscribe
    client.subscribe(MQTT_TOPIC_SUB)
    
    # start loop to process background network traffic
    client.loop_start()
    
    # main loop
    try:
        while True:
            message = input("Enter message to publish (or 'exit' to quit): ")
            if message.lower() == "exit":
                break
            publish_message(MQTT_TOPIC_PUB, message)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client.loop_stop()
        client.disconnect()