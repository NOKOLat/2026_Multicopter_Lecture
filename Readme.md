このリポジトリは、2026マルコプ講座資料作成の際に、講師が参考にするドキュメントです。

### ファイル構造

```
.
├── docs
│   └── basic_info.md
├── images
│   ├── circuit.drawio.png
│   ├── fig1.drawio.png
│   ├── fig2.drawio.png
│   ├── fig3.drawio.png
│   ├── fig4.drawio.png
│   └── mp.drawio.png
├── img_generator
│   ├── axis_rotation_visualizer.py
│   └── rpy_visualizer.py
├── axes_rotation.png
└── Readme.md
```

### 各ディレクトリの役割
#### 1. docs

ここには、ドキュメント本文を記述する`.md`ファイルが存在する。
このリポジトリでは、`basic_info.md`にドキュメント本文を記述する。

```
docs
└── basic_info.md 
```

#### 2. images
`images`ディレクトリには`.md`本文に埋め込むための画像を保存する。

```
images
   ├──circuit.drawio.png
   ├── fig1.drawio.png
   ├── fig2.drawio.png
   ├── fig3.drawio.png
   ├── fig4.drawio.png
   └── mp.drawio.png
```

これらは`basic_info.md`で埋め込まれる画像である。

#### 3.img_generator
`img_generator`ディレクトリには、画像を生成するための`.py`ファイルが存在する。

```
img_generator
    ├── axis_rotation_visualizer.py
    └── rpy_visualizer.py
```

`img_generator`ディレクトリ配下では、`basic_info.md`で埋め込まれている画像を生成する。

