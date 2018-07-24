# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# other functions should go above the handlers
def get_meme_url(meme_choice):
    # put your code here!
    return url


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())


class ShowMemeHandler(webapp2.RequestHandler):
    def post(self):
        # This is where you should get the values from the user
        # add code to get_meme_url to turn their choice into a url
        # it's tricky, but you'll figure it out!
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(results_template.render())


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler),
], debug=True)
