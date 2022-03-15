# 概要
FastAPIを使ったToDoアプリの作成

## 背景
- fastAPIの理解が弱いと感じている
- APIとしてよりもWEBフレームワークとしてfastAPIをどう作ったら良いのか？と言う素朴な疑問があった

## 参考
- やってるのはこれ：https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment

## 起動方法
- 前準備
```
    source venv/bin/activate
    pip install -r requirements.txt
```
- 起動
```
    uvicorn run:app --reload
```
 
## ファイル説明
- run.py
    - サーバー起動用
- urls.py
    - ルーティング用
- controllers.py
    - ルーティングに関連した処理を実装
- templatesフォルダ
    - Viewの管理