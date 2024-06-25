from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SECRET_KEY'] = 'carapp'
db = SQLAlchemy(app)

from models import Vehicle, Modification

@app.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)

@app.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        name = request.form['name']
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        new_vehicle = Vehicle(name=name, make=make, model=model, year=year)
        db.session.add(new_vehicle)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_vehicle.html')

@app.route('/vehicle/<int:vehicle_id>', methods=['GET', 'POST'])
def vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if request.method == 'POST':
        modification = request.form['modification']
        status = request.form['status']
        new_mod = Modification(name=modification, status=status, vehicle_id=vehicle_id)
        db.session.add(new_mod)
        db.session.commit()
    return render_template('vehicle.html', vehicle=vehicle)

@app.route('/modify_vehicle/<int:mod_id>', methods=['POST'])
def modify_vehicle(mod_id):
    mod = Modification.query.get_or_404(mod_id)
    mod.status = 'Installed'
    db.session.commit()
    return redirect(url_for('vehicle', vehicle_id=mod.vehicle_id))

if __name__ == '__main__':
    app.run(debug=True)
