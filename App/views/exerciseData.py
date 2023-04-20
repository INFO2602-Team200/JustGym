from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json,url_for,flash
from App.models import db
from App.controllers import get_all_exercises_json
from App.controllers import get_all_exercises,get_all_category_exercises,get_exerciseData,get_user_workouts
from.index import index_views
from flask_login import login_required,current_user


exerciseData_views = Blueprint('exerciseData_views', __name__, template_folder='../templates')

@exerciseData_views.route('/exerciseData', methods=['GET'])
def get_exerciseData_page():
    exercises = get_all_exercises_json()
    return jsonify(exercises)

#Categories-exercises  Routes
@exerciseData_views.route('/categories/<string:category>', methods=['GET'])
@exerciseData_views.route('/categories/<string:category>/<int:id>', methods=['GET'])
@login_required
def category_exercise_page(category, id = 0):
  exercises = get_all_category_exercises(category)

  if id == 0:
     selected_exercise = get_exerciseData(exercises[0].id)
  else:
    selected_exercise = get_exerciseData(id)

  if exercises:
    workouts = get_user_workouts(current_user.id)
    return render_template('category-exercises.html', exercises = exercises,category = category, selected_exercise = selected_exercise,workouts = workouts)

  flash('Category Not Found')
  return redirect(url_for('test'))

