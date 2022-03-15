# URLを登録していく
from controllers import *

# FastAPIのルーティング用の関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
