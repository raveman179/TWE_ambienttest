# TWE_ambienttest
ソーラーパネルを使用して発電し、TWE-liteを外部電源を使用せずにセンサーから値を取得して、ambientと通信する。 

※テスト中※

## ファイルについて
twe_m2x_test.py:

書籍「TWE-Liteではじめるセンサー電子工作」より、
AT&TのIoTデータ可視化サービスM2XにADT7410で測定した温度をpythonでパースしてアップロードするスクリプト。

twe_ambient.py:

書籍のスクリプトを参考に、IoTデータ可視化サービスの[Ambient](https://ambidata.io/)に測定した温度データをアップロードする目的のスクリプト。
twe_m2x_testで使用しているurllib2がエラーを起こすため、requestsモジュールで書き換えを行っている。

## 概要
zigbee無線マイコンのTWE-liteを子機と親機の計2台使用して、
子機に接続したi2c接続の温度センサADT7410から出力されたデータを読み取り、親機経由でAmbientにアップロードしたい。

また、ソーラーパネルを活用して外部電源を使用しないメンテナンスフリーなシステムを目指す。

TWE-liteの概要は[こちら。](https://mono-wireless.com/jp/products/index.html)

温度センサーの概要は[こちら。](http://akizukidenshi.com/catalog/g/gM-06675/)

------------------------------------

親機(linuxシングルボードPC([OrangePi zero](https://ja.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?channel=twinner)) + [monostick](https://mono-wireless.com/jp/products/MoNoStick/index.html))

![20935037_930928167064371_3249722347539914507_o](https://user-images.githubusercontent.com/22868285/58178324-f49d9f80-7ce0-11e9-955c-439d41c9f3fb.jpg)

ArmbianをSDカードにセットアップして、SSH経由でログインして操作。

ボード上にwifiモジュールが実装されているが、日本国内で通信すると技適に引っかかるので有線LANで接続している。

------------------------------------

子機(TWE-lite DIP+ソーラー電源モジュール+電気二重層コンデンサ)


![20934670_930928170397704_4337454563326426358_o](https://user-images.githubusercontent.com/22868285/58179696-a9d15700-7ce3-11e9-8803-04cfc4c37a2d.jpg)

動作するまでに時間がかかり(5〜6分程度)ソーラー電源モジュールの故障を疑ったが、サポートに問い合わせたところ仕様らしいことが分かった。

~~接続するだけで動作するって説明書には書いてあるので結構紛らわしい。~~

上の構成の子機で日中は外部電源なし動作することを確認できたが、部屋の中ではLEDライトで直接照らしてもほとんど発電しない。
室内での使用は付属のソーラーパネルではなく、もっと発電容量の大きい物を使わないと厳しいと思われる。

------------------------------------

子機から送信されるデータはシリアル値で、minicomやteratermのシリアルモニターで表示できる。

![20934724_930928173731037_6607849671194165715_o](https://user-images.githubusercontent.com/22868285/58179697-a9d15700-7ce3-11e9-8d06-83b16810ef54.jpg)

最後の４桁が温度データなので、これをpythonで抽出してambientにアップロードしてグラフにプロットする。

------------------------------------

### 今後やること、やりたいこと
- pythonスクリプトの動作確認と改良 ex.ambient以外のサービスへのアップロードや、IFTTTと連携させて通知を出す
- 親機のサーバー化、外部公開
- ADT7410以外のセンサーの利用。ex.湿度センサー、土壌水分センサ
- 発電方法の改善
- ユニバーサル基板への実装orPCB作成
