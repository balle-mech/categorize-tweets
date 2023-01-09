import json
import re
from glob import glob
from os import remove
from random import choice

import fasttext as ft
import tweepy
from flask import Flask, render_template, request
from sudachipy import dictionary, tokenizer

import config

COUNT = 700    # ツイート取得上限数
model = ft.load_model('./model-1.bin')  # 分類器

# flask初期設定
app = Flask(__name__)


# 指定したユーザーのツイートを取得
def get_tweet(id):
    api = config.authTwitter()  # config.pyを使ってAPI認証
    tweets = [
        tweet
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=id).items(COUNT)
        if list(tweet.text)[0] != '@'  # リプライを除外
    ]
    return tweets


# 正規表現を使ってツイートから不要な情報を削除
def format_text(text):
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)  # 外部リンクURL
    text = re.sub(r'@[\w/:%#\$&\?\(\)~\. = \+\-…]+', "", text)  # リツイート元のユーザーID
    text = re.sub(r'＼', "", text)
    text = re.sub(r'／', "", text)
    text = re.sub(r'RT', "", text)
    text = re.sub(r'\n', " ", text)    # 改行文字
    return text


# SudachiPyで分かち書きする関数
def wakati(sentence):
    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C
    return " ".join([m.surface() for m in tokenizer_obj.tokenize(sentence, mode)])


# 文書を分かち書きし単語単位に分割
def separate_tweet(tweets):
    results = []

    for tweet in tweets:
        content = format_text(tweet.text)
        content = wakati(content)
        results.append(content)
    return results


# ツイートを学習モデルに分類させて辞書に格納
def categorize(results, raw_tweets):
    print('取得ツイート' + str(len(results)) + '件')
    category_dic = {}
    # ツイートをカテゴリに分類し、カテゴリごとのツイート数をカウント
    for result in results:
        raw_tweet = raw_tweets[results.index(result)]  # ツイート原文を取得
        result = result.replace('\n', ' ')
        ret = model.predict(result)  # ツイートをカテゴリ別に分類
        cname = ret[0][0].replace('__label__', '')
        # カテゴリ名をkeyに、ツイート原文をvalueとして辞書に格納
        category_dic.setdefault(cname, []).append(raw_tweet.text)
    return category_dic


# 辞書をもとに分類されたツイートとその割合をjsonファイルに書き込み
def get_json(dic, results, id):
    categorydic = {}
    for key in dic:
        tweet_num = len(dic[key])  # カテゴリごとのツイート数
        ratio = tweet_num / len(results) * 100
        ratio = round(ratio, 1)
        categorydic[key] = {}
        categorydic[key]['ratio'] = ratio
        categorydic[key]['content'] = dic[key]
    with open('./json_dir/categorized-' + id + '.json', 'w') as f:
        json.dump(categorydic, f, ensure_ascii=False, indent=2)


def get_result_data(id):
    """result画面で使う辞書型データを作成する関数
    分類された整形前のツイートから一件のツイートをランダム抽出し辞書に格納
    """
    with open('./json_dir/categorized-' + id + '.json', 'r') as j:
        json_data = json.load(j)
        for key in json_data:
            json_data[key]['content'] = choice(json_data[key]['content'])
            json_data[key] = [json_data[key]['ratio'], json_data[key]['content']]
        return json_data


def get_detail_data(category):
    """detail画面で使うデータを作成する関数

    jsonファイルから'ratio'キーの要素を削除し
    指定されたカテゴリーのツイートを格納した辞書を作成
    """
    detail_data = []
    file = glob('./json_dir/*.json')
    with open(file[0], 'r') as j:
        json_data = json.load(j)
        for key in json_data:
            del json_data[key]['ratio']
        detail_data = json_data[category]['content']
        return detail_data


@app.route('/')
def index():
    # jsonディレクトリ内のファイルを削除
    json_files = glob('json_dir/*.json')
    if json_files:
        for file in json_files:
            remove(file)
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    id = request.form.get('id')
    error = None
    if not id:
        error = 'IDを入力してください。'
        return render_template('index.html', error=error)

    # メイン処理
    try:
        get_tweet(id)
    except Exception:
        error = 'ユーザーが見つかりませんでした。'
        return render_template('index.html', error=error)
    tweets = get_tweet(id)
    results = separate_tweet(tweets)
    num = len(results)
    category_dic = categorize(results, tweets)
    get_json(category_dic, results, id)
    result_data = get_result_data(id)
    return render_template('result.html', id=id, num=num, data=result_data)


@app.route('/detail/<category>')
def detail(category):
    detail_data = get_detail_data(category)
    return render_template('detail.html', category=category, data=detail_data)


if __name__ == "__main__":
    app.run()
