# 温度・湿度・気圧モニター

- UIFlow のサンプルに NTP での時刻同期と Ambient のデータ送信、SD card へのデータ保存を加えたもの。
- Wi-Fi 接続情報と Ambient の channel 情報は `settings.json` に書く。
- UIFlow の firmware じゃないとセンサーの値を読み取れないため動かない。
- UIFlow は多分 v.1.5.2 で動くのを確認している。
