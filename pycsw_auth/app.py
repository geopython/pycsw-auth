###################################################################
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2026 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
###################################################################

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from pycsw.wsgi_flask import BLUEPRINT as pycsw_blueprint
from sqlalchemy.ext.declarative import declarative_base

#from models import Scope

MEDIA_TYPE = 'application/json'

Base = declarative_base()
db = SQLAlchemy(model_class=Base)

app = Flask(__name__, static_url_path='/static')
app.url_map.strict_slashes = False
app.register_blueprint(pycsw_blueprint, url_prefix='/')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


try:
    from flask_cors import CORS
    CORS(app)
except ImportError:  # CORS needs to be handled by upstream server
    pass


@app.route('/scopes')
def test():

    return jsonify({'name': 'tom'})
