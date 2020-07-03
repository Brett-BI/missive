from flask import Blueprint

services_bp = Blueprint("services_bp", __name__, static_folder="app.static", template_folder="app.templates")

from . import Data, Messager, Scheduler