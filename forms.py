from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddPackageForm(FlaskForm):
    product = StringField('Product Name: ')
    submit = SubmitField('Add Package')


class AddCustomerForm(FlaskForm):
    name = StringField("Customer Name: ")
    submit = SubmitField('Add Customer')


class AssignCustomerForm(FlaskForm):
    package_id = IntegerField("Package ID: ")
    customer_id = IntegerField("Customer ID: ")
    submit = SubmitField("Assign Package to Customer")


class DeletePackageForm(FlaskForm):
    id = StringField('Package ID: ')
    submit = SubmitField('Remove Package')
