#------https://github.com/AmbientDataInc/ambient-python-lib
#------ADT7410から拾った温度データを-----------------------------
#------TWElite→orangepi_zero_gatewayからambientにpostする-------
#------親機TWElite→orangepi_zero_gateway間はUARTで通信する------


#coding: UTF-8

import serial
import datetime
import requests
import ambient

#チャンネルid、ライトキー等の定義
ChannelId = 1673
WriteKey = "b554d27b8388a608"
ReadKey = "759af17441058580"
UserKey = "	bceae53ba3d778fee0"

#インスタンス作成
am = ambient.Ambient(ChannelId, WriteKey)

#シリアルポートを開く
s = serial.Serial("/dev/ttyUSB0",115200)

#ambientにpostする
dt = datetime.datetime.now()

while True:
    #TWEのシリアル値を一行読む
    data = s.readline()
    #:で分割する
    m = str(data).split(":")
    if ((len(m) >= 11) and (m[11 == "D"])):
        ADT_temp = int(m[7]) / 100
    post_ambidata = [{'created' : dt, 'd1': ADT_temp}]

#requestsモジュールで例外処理
try:
    ret = am.send(post_ambidata)
    print('sent to Ambient (ret = %d)' % ret.status_code)
except requests.exceptions.RequestException as e:
    print('request failed: ', e)

