このリポジトリは、2026マルコプ講座資料作成の際に、講師が参考にするドキュメントです。
内容は現在(3/8, 2026)で未完成であり、随時内容を更新することができます。

### ファイル構造

```
.
├── docs
│   └── basic_info.md
├── images
│   ├── axes_rotation.png
│   ├── circuit.drawio.png
│   ├── fig1.drawio.png
│   ├── fig2.drawio.png
│   ├── fig3.drawio.png
│   ├── fig4.drawio.png
│   └── mp.drawio.png
├── img_generator
│   ├── axis_rotation_visualizer.py
│   └── rpy_visualizer.py
└── Readme.md
```
このリポジトリでは、`basic_info.md`にドキュメント本文を記述する。

### 各ディレクトリの役割
#### 1. docs

ここには、ドキュメント本文を記述する`.md`ファイルが存在する。

```
docs
└── basic_info.md 
```

#### 2. images
`images`ディレクトリには`.md`本文に埋め込むための画像が保存されている。

```
images
   ├── axes_rotation.png
   ├──circuit.drawio.png
   ├── fig1.drawio.png
   ├── fig2.drawio.png
   ├── fig3.drawio.png
   ├── fig4.drawio.png
   └── mp.drawio.png
```

これらは`basic_info.md`で埋め込まれる画像である。

画像ファイル形式は`.png`形式が良い(pdf化が安定する)。

#### 3.img_generator
`img_generator`ディレクトリ配下では、`basic_info.md`に埋め込まれている画像を生成する。

```
img_generator
    ├── axis_rotation_visualizer.py
    └── rpy_visualizer.py
```

`img_generator`ディレクトリには、画像を生成するための`.py`ファイルが存在する。

生成した画像の保存先は、`images`ディレクトリになるように設定する。