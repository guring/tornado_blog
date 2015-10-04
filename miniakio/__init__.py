#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.web
from tornado.web import StaticFileHandler
from .libs import sqlite3lib
from blogconfig import COOKIE_SECRET, DATABASE, DEBUG
from blog import *


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
    cookie_secret=COOKIE_SECRET,
    login_url="/auth/signin",
    autoescape=None,
    debug=DEBUG,
)

handlers = [
    (r'/static/(.*)', StaticFileHandler, {"path": settings['static_path']}),
    ('/', HomeHandler),  # 主页
    ('/post/([0-9]+)', EntryHandler),  # 获取某篇文章
    # ('/([a-zA-Z0-9-]+)/*', EntryHandler),
    ('/picky/(*+)/*', PickyHandler),  # 展示这篇文章的页面
    ('/picky/(*+.md)', PickyDownHandler),  # 下载这篇文章的md文件
    ('/tag/([^/]+)/*', TagsHandler),  # 获取标签下的文章列表
    ('/category/([^/]+)/*', CategoryHandler),  # 获取分类下的文章列表
    ('/post/new', NewPostHandler),  # 新建文章
    ('/post/delete/([0-9]+)', DeletePostHandler),  # 删除文章
    ('/post/update/([0-9]+)', UpdatePostHandler),  # 更改文章
    ('/post/picky', NewPickyHandler),  # 新建picky
    ('/auth/signin', SigninHandler),  # 登录
    ('/auth/signout', SignoutHandler),  # 登出
    ('/blog/feed', FeedHandler),  # 导出源
    ('/search/all', SearchHandler),  # 全站搜索
    ('/blog/all', ArchiveHandler),  # 所有博客
    ('/blog/tags', TagListHandler),  # 标签列表
    (r'.*', PageNotFound),  # 未找到页面
]


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = sqlite3lib.Connection(DATABASE)
