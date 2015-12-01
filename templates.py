import cgi
import urllib 
#import os

from google.appengine.api import users
from google.appengine.ext import ndb 

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        author = self.request.get_all("author_name")
        comment = self.request.get_all("comments")
        self.render("comment.html", author = author, comment = comment)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<body>You wrote:<pre>')
        author = self.request.get_all("author_name")
        author = cgi.escape(self.request.get('author_name'))
        #self.render("comment.html")
        #self.response.write('<br>')
        #self.response.write(cgi.escape(self.request.get('commments')))
        #self.response.write('</pre></body>')


    
    	
    	

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)import cgi
import urllib 
#import os

from google.appengine.api import users
from google.appengine.ext import ndb 

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        author = self.request.get_all("author_name")
        comment = self.request.get_all("comments")
        self.render("comment.html", author = author, comment = comment)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<body>You wrote:<pre>')
        author = self.request.get_all("author_name")
        author = cgi.escape(self.request.get('author_name'))
        #self.render("comment.html")
        #self.response.write('<br>')
        #self.response.write(cgi.escape(self.request.get('commments')))
        #self.response.write('</pre></body>')


    
    	
    	

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
