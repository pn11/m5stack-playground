# m5stack-micropython on WSL

## Firmware 選択

M5Stack を MicroPython で動かすには以下の3つ方法がありそう

- [m5stack/M5Cloud](https://github.com/m5stack/M5Cloud)
- [m5stack/M5Stack_MicroPython](https://github.com/m5stack/M5Stack_MicroPython)
- [UIFlow](https://m5stack.github.io/UIFlow_doc/ja/)

公式が推してるのは UIFlow っぽいが、 debug しにくそうだったので上の2つを検討して、2個目の方が GitHub の履歴が新しかったのでこれを使う。

## WSL での USB 通信

WSL2 は USB 使えない。

- [WSL 2 についてよく寄せられる質問 | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-faq#can-i-access-the-gpu-in-wsl-2-are-there-plans-to-increase-hardware-support)

WSL 1では以下のように serial 通信できる。 

- [Serial Support on the Windows Subsystem for Linux | Microsoft Docs](https://docs.microsoft.com/en-us/archive/blogs/wsl/serial-support-on-the-windows-subsystem-for-linux)

CP210X driver は Windows 側に入れれば良い。

- [Download – m5stack-store](https://m5stack.com/pages/download)

## M5Stack_MicroPython Firmware の導入

主に以下2つを見て行う。

- [m5stack/M5Stack_MicroPython](https://github.com/m5stack/M5Stack_MicroPython)
- [build · loboris/MicroPython_ESP32_psRAM_LoBo Wiki](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/build)

また、以下も参考になった。

- [M5Stack用MicroPythonのビルドとカスタマイズ - Qiita](https://qiita.com/ciniml/items/1378d02bc14098b959ef)

まず必要 package を install して、repository を clone してくる。

```sh
sudo apt-get install git wget make libncurses-dev flex bison gperf python python-serial
git clone --depth 1 https://github.com/m5stack/M5Stack_MicroPython
```

次に build の設定。

```sh
./BUILD.sh menuconfig
```

この中で以下の2つを実施

- `Serial Flasher Config` --> `Default serial Port` を変更 (私の場合は `/dev/ttyS3`、以下も同様)
- `MicroPython --> Modules --> Use Display module` を確認

終わったら Exit して

```sh
./BUILD.sh
```

build できたら以下で firmware を書き込む (2行目は通信を確認してるだけ)。port 番号は環境によって異なる。

```sh
sudo chmod 666 /dev/ttyS3
stty -F /dev/ttyS3 -a
./BUILD.sh flash
```

## ampy

[scientifichackers/ampy](https://github.com/scientifichackers/ampy) を使って MicroPython を実機で動かす。日本語の記事では以下などが参考になる。

- [ampy: MicroPythonマイコンとPCとのファイル転送ツール – Ambient](https://ambidata.io/blog/2018/03/15/ampy/)

私の場合は以下のような手順で行った。

```sh
sudo apt-get install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate 
pip install adafruit-ampy
ampy --port /dev/ttyS3 ls
```

## MicroPython でなんかする


```sh
ampy --port /dev/ttyS3 run test.py
```

で実行する。

```sh
ampy --port /dev/ttyS3 put test.py /flash/main.py
```

のようにすると転送する。 `/flash/main.py` は M5Stack が起動したときに実行される。

## M5Cloud をやろうとしたメモ

- [M5StackでセンサーデーターをAmbientに送る (MicroPython編) – Ambient](https://ambidata.io/samples/m5stack/m5stack-micropython/)

を見てやろうとした。v0.3.4 が repository から消えていたので commit 履歴から見つけてきて入れたけど、Wi-Fi は ESSID を登録できなそうだったりしたのでやめた。一応、以下のような手順 (0.4.0 の場合)で firmware 書き込みはできた。

```sh
pip install esptool
wget https://github.com/m5stack/M5Cloud/raw/master/firmwares/OFF-LINE/m5stack-20180516-v0.4.0.bin
esptool.py --chip esp32 --port /dev/ttyS3 erase_flash
esptool.py --chip esp32 --port /dev/ttyS3 write_flash --flash_mode dio -z 0x1000 m5stack-20180516-v0.4.0.bin
```

Medium に転載済み。

- [M5Stack で MicroPython を使う - oka - Medium](https://medium.com/@oka/m5stack-%E3%81%A7-micropython-%E3%82%92%E4%BD%BF%E3%81%86-9a03e8be7ce)
