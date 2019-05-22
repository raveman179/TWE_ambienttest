# TWE_ambienttest
TWE-liteでambientと通信する ※テスト中※

## ファイルについて
twe_m2x_test.py:

書籍「TWE-Liteではじめるセンサー電子工作」より、AT&TのM2XにADT7410で測定した温度をpythonでパースしてアップロードするスクリプト。

twe_ambient.py:

書籍のスクリプトを参考に、IoTデータ可視化サービスの[Ambient](https://ambidata.io/)にデータをアップロードする目的のスクリプト。
twe_m2x_testで使用しているurllib2がエラーを起こすため、requestsモジュールで書き換えを行っている。

## 概要
zigbee無線マイコンのTWE-liteを子機と親機の計2台使用して、
子機に接続したi2c接続の温度センサADT7410から出力されたデータを読み取り、
親機(linuxシングルボードPC([OrangePi zero](https://ja.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?channel=twinner)) + [monostick](https://mono-wireless.com/jp/products/MoNoStick/index.html))経由でAmbientにアップロードしたい。

TWE-liteの概要は[こちら。](https://mono-wireless.com/jp/products/index.html)

温度センサーの概要は[こちら。](http://akizukidenshi.com/catalog/g/gM-06675/)

------------------------------------

親機の写真

![20935037_930928167064371_3249722347539914507_o](https://user-images.githubusercontent.com/22868285/58178324-f49d9f80-7ce0-11e9-955c-439d41c9f3fb.jpg)

ArmbianをSDカードにセットアップして、SSH経由でログインして操作。
ボード上にwifiモジュールが実装されているが、日本国内で通信すると技適に引っかかるので有線LANで接続している。

子機(TWE-lite DIP+ソーラー電源管理モジュール+電気二重層コンデンサ)

上記構成の子機において、日の出ている間は外部電源なし動作することを確認できた。



送信されたデータはシリアル値で、minicom等のシリアルモニターで表示できる。



最後の４桁が温度データなので、pythonで抽出してambientにアップロードする。


### 今後やりたいこと
+
