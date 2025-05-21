# MQTT Clients Examples

このリポジトリは、**Mosquitto** をブローカーとして使用し、**Python（paho-mqtt）** と **HTML + JavaScript（mqtt.js）** を使って MQTT 通信を始めるためのガイドです。

---

## 📚 目次

- [動作環境](#動作環境)
- [Mosquitto](#mosquitto)
  - [インストール方法](#インストール方法)
  - [起動方法](#起動方法)
- [Python（paho-mqtt）](#pythonpaho-mqtt)
  - [インストール方法](#インストール方法-1)
  - [バージョン情報](#バージョン情報)
- [HTML + JavaScript（mqtt.js）](#html--javascriptmqttjs)

---

## 💻 動作環境

- MacBook Air  
- Apple M3  
- 16GB RAM  

---

## 🐝 Mosquitto

### インストール方法

```bash
brew install mosquitto
````

### 起動方法

```bash
mosquitto
```

※ デフォルトではポート `1883` でブローカーが起動します。

---

## 🐍 Python（paho-mqtt）

### インストール方法

```bash
pip3 install paho-mqtt
```

### バージョン情報

| ライブラリ/ツール | バージョン  |
| --------- | ------ |
| Python    | 3.12.7 |
| pip       | 24.2   |
| paho-mqtt | 2.1.0  |

---

## HTML + JavaScript（mqtt.js）
