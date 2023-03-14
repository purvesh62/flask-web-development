from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import AddPackageForm, AddCustomerForm, DeletePackageForm, AssignCustomerForm

app = Flask(__name__)

# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'
# Required for cookies to work in the preview window that's integrated in the lab IDE
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Package(db.Model):
    __tablename__ = 'packages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    customer = db.relationship('Customer', backref='package', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.customer:
            return f"Package ID is {self.id}, Product is {self.name} and Customer is {self.customer.name} with ID: {self.customer.id}"
        else:
            return f"Package ID is {self.id}, Product is {self.name} and has no customer assigned yet."


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # We use packages.id because __tablename__='packages'
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer Name: {self.name} and ID: {self.id}"


##############################
### BASE VIEW ###############
############################
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_package', methods=['GET', 'POST'])
def add_package():
    form = AddPackageForm()

    if form.validate_on_submit():
        product = form.product.data

        # Add new Package to database
        new_package = Package(product)
        db.session.add(new_package)
        db.session.commit()

        return redirect(url_for('list_packages'))

    return render_template('add_package.html', form=form)


@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = AddCustomerForm()

    if form.validate_on_submit():
        name = form.name.data
        # Add new customer to database
        new_customer = Customer(name)
        db.session.add(new_customer)
        db.session.commit()

        return redirect(url_for('list_customers'))

    return render_template('add_customer.html', form=form)


@app.route('/list_packages')
def list_packages():
    # Grab a list of packages from database.
    packages = Package.query.all()
    return render_template('list_packages.html', packages=packages)


@app.route('/list_customers')
def list_customers():
    # Grab a list of packages from database.
    customers = Customer.query.all()
    return render_template('list_customers.html', customers=customers)


@app.route('/delete_package', methods=['GET', 'POST'])
def delete_package():
    form = DeletePackageForm()

    if form.validate_on_submit():
        id = form.id.data
        package = Package.query.get(id)
        db.session.delete(package)
        db.session.commit()

        return redirect(url_for('list_packages'))
    return render_template('delete_package.html', form=form)


@app.route('/assign_customer', methods=['GET', 'POST'])
def assign_customer():
    form = AssignCustomerForm()
    if form.validate_on_submit():
        package_id = form.package_id.data
        customer_id = form.customer_id.data

        package = Package.query.get(package_id)
        customer = Customer.query.get(customer_id)
        package.customer = customer
        db.session.commit()
        return redirect(url_for('list_packages'))

    return render_template('assign_customer.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
