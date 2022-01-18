# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError

engine = Engine()
import os
import redis

r = redis.from_url(os.environ.get("REDIS_URL_impharaon"))

@engine.define
def write_users(**params):
    print(params['id'])
    if params['url'] != None:
        r.hmset('ls_' + params['id'],params)
    else :
        r.hmset('lsp_' + params['id'],params)



@engine.define
def write_users_sent_message_times(**params):
    r.hmset('test','key','value')




@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('Content cannot be empty!')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
