# MQTT Clients Examples
![mqtt-image](https://raw.githubusercontent.com/kobayashiry0/mqtt-clients-examples/refs/heads/main/images/mqttexample.png)

このリポジトリは、**Mosquitto** をブローカーとして使用し、**Python（paho-mqtt）** と **HTML + JavaScript（mqtt.js）** を使って MQTT 通信を始めるためのガイドです。

## Table of Contents

- [Environment](#environment)
- [Mosquitto](#mosquitto)
  - [Installation](#installation)
  - [Usage](#usage-1)
    - [Starting MQTT over TCP](#starting-mqtt-over-tcp)
    - [Starting MQTT over WebSocket](#starting-mqtt-over-websocket)
  - [Usage](#usage)
- [Python（paho-mqtt）](#pythonpaho-mqtt)
  - [Installation](#installation-1)
  - [How to Run](#how-to-run)
- [HTML + JavaScript（mqtt.js）](#html--javascriptmqttjs)
  - [How to Run](#how-to-run-1)
- [References](#references)

## Environment
- OS: macOS Sequoia 15.5 

| library/tool | version  |
| --------- | ------ |
| Homebrew | 4.4.31  |
| Mosquitto | 2.0.21 |
| Python    | 3.12.7 |
| pip       | 24.2   |
| paho-mqtt | 2.1.0  |

## Mosquitto

### Installation
Homebrewを使用してMosquittoをインストールします。
Homebrewはインストール済みとします。

```zsh
brew install mosquitto
````

### Usage

#### Starting MQTT over TCP
```zsh
mosquitto
```

※ デフォルトではポート `1883` でMQTT over TCPが起動します。

> [!Warning]
> セキュリティ上、ブラウザでMQTT over TCPは通信できないため、MQTT over WebSocketを使用する必要があります。


#### Starting MQTT over WebSocket
```zsh
mosquitto -c mosquitto.conf
```
-cオプションで設定ファイルを指定します。
mosquitto.confの内容は以下の通りです。

```conf
listener 1883
listener 9001
protocol websockets
```
ポート `1883` でMQTT over TCP、ポート `9001` でMQTT over WebSocketが起動します。 

## Python（paho-mqtt）

### Installation

```zsh
pip3 install paho-mqtt
```

### How to Run
```zsh
python3 example.py
```
* subscribe: `topicA`
* publish: `topicB`

## HTML + JavaScript（mqtt.js）
### How to Run
ブラウザでexample.htmlを開きます。
* subscribe: `topicB`
* publish: `topicA`
pythonの例と逆になっています。

## References
- [MQTT](https://mqtt.org/)
- [Mosquitto](https://mosquitto.org/)
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)
- [mqtt.js](https://github.com/mqttjs)
