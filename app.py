from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SECRET_KEY'] = 'carapp'  

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

csrf = CSRFProtect(app)

from models import Vehicle, Modification, User
from users import users_bp
from forms import VehicleForm, AddModificationForm

app.register_blueprint(users_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', vehicles=vehicles)

@app.route('/add_vehicle', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        name = form.name.data
        make = form.make.data
        model = form.model.data
        year = form.year.data
        new_vehicle = Vehicle(name=name, make=make, model=model, year=year, user_id=current_user.id)
        db.session.add(new_vehicle)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_vehicle.html', form=form)

@app.route('/vehicle/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.user_id != current_user.id:
        flash('You do not have permission to view this vehicle.', 'danger')
        return redirect(url_for('index'))
    form = AddModificationForm()
    if form.validate_on_submit():
        modification = form.modification.data
        status = form.status.data
        new_mod = Modification(name=modification, status=status, vehicle_id=vehicle_id)
        db.session.add(new_mod)
        db.session.commit()
    return render_template('vehicle.html', vehicle=vehicle, form=form)

@app.route('/modify_vehicle/<int:mod_id>', methods=['POST'])
@login_required
def modify_vehicle(mod_id):
    mod = Modification.query.get_or_404(mod_id)
    if mod.vehicle.user_id != current_user.id:
        flash('You do not have permission to modify this vehicle.', 'danger')
        return redirect(url_for('index'))
    mod.status = 'Installed'
    db.session.commit()
    return redirect(url_for('vehicle', vehicle_id=mod.vehicle_id))

@app.route('/edit_vehicle/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def edit_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.user_id != current_user.id:
        flash('You do not have permission to edit this vehicle.', 'danger')
        return redirect(url_for('index'))
    form = VehicleForm()
    if form.validate_on_submit():
        vehicle.name = form.name.data
        vehicle.make = form.make.data
        vehicle.model = form.model.data
        vehicle.year = form.year.data
        db.session.commit()
        return redirect(url_for('vehicle', vehicle_id=vehicle.id))
    elif request.method == 'GET':
        form.name.data = vehicle.name
        form.make.data = vehicle.make
        form.model.data = vehicle.model
        form.year.data = vehicle.year
    return render_template('edit_vehicle.html', form=form)

@app.route('/delete_vehicle/<int:vehicle_id>', methods=['POST'])
@login_required
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.user_id != current_user.id:
        flash('You do not have permission to delete this vehicle.', 'danger')
        return redirect(url_for('index'))
    db.session.delete(vehicle)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)