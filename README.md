![mqtt-image](https://github.com/kobayashiry0/mqtt-clients-examples/blob/main/images/mqttexample.png)

# MQTT Clients Examples

このリポジトリは、**Mosquitto** をブローカーとして使用し、**Python（paho-mqtt）** と **HTML + JavaScript（mqtt.js）** を使って MQTT 通信を始めるためのガイドです。

## Table of Contents

- [動作環境](#動作環境)
- [Mosquitto](#mosquitto)
  - [インストール方法](#インストール方法)
  - [起動方法](#起動方法)
- [Python（paho-mqtt）](#pythonpaho-mqtt)
  - [インストール方法](#インストール方法-1)
  - [実行方法](#実行方法)
  - [バージョン情報](#バージョン情報)
- [HTML + JavaScript（mqtt.js）](#html--javascriptmqttjs)

## 動作環境

- MacBook Air
- macOS Sequoia 15.5
- Apple M3  
- 16GB RAM  

## Mosquitto

### インストール方法

```zsh
brew install mosquitto
````
バージョン2.0.21

### 起動方法

```zsh
mosquitto
```

※ デフォルトではポート `1883` でブローカーが起動する。

## Python（paho-mqtt）

### インストール方法

```zsh
pip3 install paho-mqtt
```

### 実行方法
```zsh
python3 example.py
```
topicAをsubscribeし、publishするときは、topicBで送信する。

### バージョン情報

| library/tool | version  |
| --------- | ------ |
| Python    | 3.12.7 |
| pip       | 24.2   |
| paho-mqtt | 2.1.0  |

## HTML + JavaScript（mqtt.js）
ブラウザでexample.htmlを開く。
topicBをsubscribeし、publishするときは、topicAで送信する（Pythonの逆）。