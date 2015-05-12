import os
import webapp2
import jinja2
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates'))
)

class Notes(ndb.Model):
    note = ndb.StringProperty(required=True)

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
        items = Notes.query().fetch()
        self.render("Add_Notes.html", items=items)

    def post(self):
        items = self.request.get("note")
        if not items:
            self.response.out.write('<b>Please add a note before hitting add!</b>')
        else:
            note = Notes(note=items)
            note.put()
        items = Notes.query().fetch()
        self.render("Add_Notes.html", items=items)
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)