from flask import Flask
from flask import request
from flask import redirect
import subprocess

app = Flask(__name__)

SITE_URL='/var/www/tsundere.me/'

@app.route('/')
def index():
    if len(request.query_string) > 0:
        try:
            if not request.query_string.startswith("http:") and not request.query_string.startswith("https:"):
                return app.send_static_file("invalid.htm")
            tmp_file = subprocess.check_output([SITE_URL + 'bin/tsundere.me', request.query_string]).strip()
            if tmp_file == "no faces":
                return app.send_static_file("noface.htm")
            if not tmp_file.startswith("/static"):
                return app.send_static_file("error.htm")
            return redirect(tmp_file)
        except Exception as e:
            return app.send_static_file("error.htm")
    else:
        return app.send_static_file("index.htm")

