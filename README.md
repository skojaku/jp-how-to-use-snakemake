# Snakemakeのすゝめ~"Re-search"をもっと簡単に~

このレポジトリは、私のノートで紹介した[「Snakemakeのすゝめ~Re-searchをもっと楽に」](https://skojaku.github.io/%E3%83%8E%E3%83%BC%E3%83%88/snakemake%E3%81%AE%E3%81%99%E3%82%9D%E3%82%81/)で使ったコードを保管しています。
コードは章ごとにフォルダに分けて置きました。

- 1章: ワークフローを作ろう
- 2章:ワイルドカードのすゝめ
- 3章:テキスト要約
- 3章:テキスト要約(shell司令文を使った場合)

# インストール

### 1章から2章まで

以下のコードでSnakemakeをインストール。
```bash
conda install -c conda-forge -c bioconda snakemake
```

その他、ノート内のデモを動かすためのライブラリをインストール。
```bash
conda install -c conda-forge -c bioconda numpy seaborn matplotlib pandas wikipedia-api
```

### 3章

テキスト要約に使う[Pytorch](https://pytorch.org/get-started/locally/)及び[transformers](https://huggingface.co/docs/transformers/index)をインストール。
環境によってインストールが異なるので、本サイトを参照してください。私の環境(MAC)では以下のコマンドでインストールしました。
```bash
conda install pytorch torchvision torchaudio -c pytorch # Pytorch
conda install -c huggingface transformers # Transformers
```

# Snakefileの実例
- http://github.com/skojaku/residual2vec
- https://github.com/yy/sex-reporting
