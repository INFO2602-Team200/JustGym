from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user

from.index import index_views

from App.controllers import (
    get_all_exercises,
    get_all_exercises_json,
)

exerciseData_views = Blueprint('exerciseData_views', __name__, template_folder='../templates')

@exerciseData_views.route('/exerciseData', methods=['GET'])
def get_exerciseData_page():
    exercises = get_all_exercises()
    return render_template('exerciseData.html', exercises = exercises)