#coding: UTF-8
import serial
import json
import datetime
import urllib
import urllib2

# M2Xの定義
deviceid = "…デバイスIDを記載する…"
streamname = "temperature"
apikey = "…Primary API Keyを記載する…"

# M2XにPOST送信する
def m2xpost(value):
        # POST先のURL
        url = "https://api-m2x.att.com/v2/devices/{0}/streams/{1}/values".format(deviceid, streamname)
        # ヘッダ
        headers = {
                'Content-Type' : 'application/json',
                'X-M2X-KEY' : apikey
        }
        # 現在の日時
        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        # POSTするデータ
        data = {'values' : [{'timestamp' : timestamp, 'value' : value}]}

        # POSTする
        req = urllib2.Request(url, json.dumps(data), headers)
        try:
                res = urllib2.urlopen(req)
                print "Sent Data" + res.read()
        except URLErrir, e:
                print e.reason

# /dev/ttyUSB0を開く
s = serial.Serial("/dev/ttyUSB0", 115200)

while 1:
    # 1行読み取る
    data = s.readline()
    # 「;」で分割する
    m = str(data).split(";")
    if ((len(m) >= 11) and (m[11]=="D")):
        temp = int(m[7]) / 100.0
        m2xpost(temp)
s.close()
