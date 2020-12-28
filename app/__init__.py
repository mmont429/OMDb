from flask import Flask
import os

package_dir = os.path.dirname(
    os.path.abspath(__file__)
)

templates = os.path.join(
    package_dir, "templates"
)

app = Flask(__name__, template_folder=templates)

