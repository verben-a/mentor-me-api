from flask import Flask, render_template, Response, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from getpass import getpass
from werkzeug.security import generate_password_hash, check_password_hash

import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

import json
import os

from . import app
from .database import session  # not known yet.
from .models import User, Profile


@app.route("/")
def home():
    return render_template("home.html")