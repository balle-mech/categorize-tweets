### アプリ名

categorize-tweets

#### コンセプト

過去のツイートを分析することによりその人の個性がわかる

#### こだわったポイント

- どんなツイートがどのジャンルに分類されたのか確認できる。
- URLなどの不要なテキスト情報は取り除き学習・予測

### ページ画像

<img width="1440" alt="スクリーンショット 2023-01-03 9 44 32" src="https://user-images.githubusercontent.com/91408297/210290091-36489e7c-d15d-4b79-a485-823ae634a234.png">

<img width="1439" alt="スクリーンショット 2023-01-03 9 43 55" src="https://user-images.githubusercontent.com/91408297/210290115-d63f14ac-c34c-4cda-9253-c1b7253baf7e.png">

<img width="1440" alt="スクリーンショット 2023-01-03 9 46 00" src="https://user-images.githubusercontent.com/91408297/210290127-315c0151-5b26-4cd5-ad2f-8b4a518e6fe7.png">

### 公開したアプリの URL

https://cateorize-tweet.azurewebsites.net
（CDは導入しているのですが、もしかしたらサーバーが落ちてて繋がらないかもしれません）

### ツイートを学習しジャンル分け学習モデルを生成するリポジトリ

- https://github.com/a2c6201/let-Fasttext-learn-tweets

## 開発環境

### 開発環境

virtualenv 20.17.0

### 開発言語

Python 3.10.4

## アプリケーション機能

### 機能一覧

- ツイート分類：　TwitterAPIを使用して、アカウントの過去ツイートをカテゴリ別に分類する。
- 分類されたツイート表示：　分類されたツイートを全て表示する。

### 画面一覧

- 検索画面 ：Twitterアカウント名を入力
- 分類結果画面 ：結果を割合表示
- ツイート表示画面　：分類されたツイートを全て表示

### 使用しているAPI,SDK,ライブラリなど

- Twitter API
- fastText(https://fasttext.cc/) (テキスト分類)
- SudachiPy(https://github.com/WorksApplications/SudachiPy )　
(文章を単語に分ける)

## ローカルでの環境構築手順

.env ファイルを作成し、API key をそれぞれ追加(.env.sample を参照)

ターミナルで以下コマンドを入力し、使用ライブラリをインストール

```
pip install -r requirements.txt
```
