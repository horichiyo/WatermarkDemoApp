# WatermarkDemoApp
簡単な画像電子透かしを体感することができるアプリケーションです。

### 環境構築
- Python3系がインストールされている前提です。
- Kivyのインストールは[公式](https://pyky.github.io/kivy-doc-ja/installation/installation-osx.html)を参考にしました。
- 公式の方にも書いてありますが，MacであればHomebrewとpipを使うのが一番簡単だと思います。
- Cythonを先にインストールしないと入らないので注意。

### 使い方
- 画面上部のテキストボックスに埋め込みたい文字を入力します。
- `Embed`ボタンを押すと表示されているカバー画像に情報が埋め込まれ，右側にステゴ画像が表示されます。
- `Extract`ボタンを押すと埋め込まれた情報を抽出して，画面に文字を表示します。
- `Change`ボタンを押すとカバー画像を変更することができます。
- `Mode:XXX`ボタンを押すと埋め込み，抽出に使うアルゴリズムを変更することができます。

### ディレクトリ構成
```
.
├── images
│   ├── QRの画像とかカバー画像とか
│   ├── result
│   │   └── ステゴ画像とか
│   └── stegosaurus.png（初期ステゴ画像用）
├── src
│   ├── __pycache__
│   ├── dwt.py
│   ├── imageInImageWatermarking.py
│   ├── makeqr.py
│   ├── watermarkDemoApp.kv
│   └── watermarkDemoApp.py
└── tools
    └── fonts
        └── ipaexg.ttf
```

### 
