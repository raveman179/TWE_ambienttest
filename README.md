# TWE_ambienttest
TWE-liteでambientと通信する ※テスト中※

# ファイルについて
twe_m2x_test.py:

書籍「TWE-Liteではじめるセンサー電子工作」より、AT&TのM2XにADT7410で測定した温度をpythonでパースしてアップロードするスクリプト。

twe_ambient.py:

書籍のスクリプトを参考に、IoTデータ可視化サービスの[Ambient](https://ambidata.io/)にデータをアップロードする目的のスクリプト。
twe_m2x_testで使用しているurllib2がエラーを起こすため、requestsモジュールで書き換えを行っている。

# 概要
zigbee無線マイコンのTWE-liteを使用して、i2c接続の温度センサADT7410から出力されたデータを読み取り、
親機(linuxシングルボードPC + monostick)経由でAmbientにアップロードしたい。

TWE-liteの概要は[こちら。](https://mono-wireless.com/jp/products/index.html)

温度センサーの概要は[こちら。](http://akizukidenshi.com/catalog/g/gM-06675/)

親機：linuxシングルボードPC([orangePizero](https://ja.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?channel=twinner)) + [monostick](https://mono-wireless.com/jp/products/MoNoStick/index.html)



-----------親機と子機の写真-------------











子機(TWE-lite DIP+ソーラー電源管理モジュール+電気二重層コンデンサ)

上記構成の子機において、日の出ている間は外部電源なし動作することを確認できた。



送信されたデータ

-----------ターミナルの写真-------------

子機から送られてくるデータの最後の４桁が温度データなので、pythonで抽出してambientにアップロードする。

#今後の予定

