from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
from App.models import db
from App.controllers import get_all_exercises_json
from App.controllers import get_all_exercises
from.index import index_views



exerciseData_views = Blueprint('exerciseData_views', __name__, template_folder='../templates')

@exerciseData_views.route('/exerciseData', methods=['GET'])
def get_exerciseData_page():
    exercises = get_all_exercises_json()
    return jsonify(exercises)