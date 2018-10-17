#!/usr/bin/python

from flask import Flask
from flask_admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

class TestView(BaseView):
    @expose('/')
    def test(self):
        return self.render('test.html')


app=Flask(__name__)
admin=Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(MyView(name='Hello'))
admin.add_view(TestView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(TestView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(TestView(name='Hello 3', endpoint='test3', category='Test'))

if __name__=='__main__':
    app.run()

