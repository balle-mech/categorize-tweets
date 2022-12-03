### アプリ名
categorize-tweets

#### コンセプト
過去のツイートを分析することによりその人の個性がわかる

#### こだわったポイント
- どんなツイートがどのジャンルに分類されたのか確認できる。
- URLなどの不要なテキスト情報は取り除き学習・予測

### 公開したアプリの URL
https://cateorize-tweet.azurewebsites.net
（CDは導入しているはずなのですが、もしかしたらサーバーが落ちてて繋がらないかもしれません）

### 該当プロジェクトのリポジトリ URL
- https://github.com/a2c6201/categorize-tweets
- https://github.com/a2c6201/let-Fasttext-learn-tweets(ツイートを学習しジャンル分け学習モデルを生成するリポジトリ)

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
- SudachiPy(https://github.com/WorksApplications/SudachiPy)　
(文章を単語に分ける)
