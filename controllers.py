from operator import imod
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import db
from models import User, Task

app = FastAPI(
    title= "FastAPIで作るToDoアプリケーション",
    description="FastAPIチュートリアル:FastAPI(とstarlette)でシンプルなアプリケーションを作りましょう",
    version="0.9 beta"
)

# テンプレート関連の設定(jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env



# url.pyでURLに基づく関数を定義していく
def index(request: Request):
    # ルートへのリクエストに対してtemplates/index.htmlでレスポンスするようになった
    return templates.TemplateResponse("index.html",{"request":request})

def admin(request:Request):
    
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()
    
    return templates.TemplateResponse("admin.html",{"request":request,
                                                    "user":user,"task":task})