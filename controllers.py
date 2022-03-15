# url.pyでURLに基づく関数を定義していく
def index(request: Request):
    # ルートへのリクエストに対してtemplates/index.htmlでレスポンスするようになった
    return templates.TemplateResponse("index.html",{"request":request})
