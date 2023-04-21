from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from App.models import db
from App.controllers import add_user_equipment,get_userData,get_all_exercise_equipment
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from App.models import UserData

userData_views = Blueprint('userData_views', __name__, template_folder='../templates')

@userData_views.route('/equipment', methods=['POST'])
@login_required
def equipment_data():
    selected_options = request.form.getlist('options')
    result = add_user_equipment(current_user.id,selected_options)

    if result == True:
        return redirect('/users')
    else:
        return redirect('/')
    
@userData_views.route('/equipment', methods=['GET'])
@login_required
def print_equipment_data():
    equipments = get_all_exercise_equipment()
    print(equipments)
    return render_template('equipmentSelection.html',equipments = equipments)