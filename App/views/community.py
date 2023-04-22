from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json,url_for,flash
from App.models import db
from App.controllers import get_community
from.index import index_views
from flask_login import login_required,current_user


community_views = Blueprint('community_views', __name__, template_folder='../templates')

@community_views.route('/community', methods=['GET'])
@login_required
def home_page():
    community = get_community(1) # there is only 1 active community
    return render_template('users.html',community = community)


