from datetime import datetime

from decouple import config as env
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["SECRET_KEY"] = env("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pymssql://{env("DB_USER")}:{env("DB_PASSWORD")}@{env("DB_HOST")}?charset=utf8'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    date_birth = db.Column(db.DateTime, default=datetime.utcnow())
    email = db.Column(db.String(255), nullable=False)

    account = db.relationship("StudentAccount", backref="student", lazy=True)

    payment = db.relationship("Payment", backref="student", lazy=True)


class StudentAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey(
        "student.id"), nullable=False)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    account = db.relationship("TeacherAccount", backref="teacher", lazy=True)

    teacher_class = db.relationship("Class", backref="teacher", lazy=True)


class TeacherAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey(
        "teacher.id"), nullable=False)


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255))

    account = db.relationship("StaffAccount", backref="staff", lazy=True)


class StaffAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    staff_id = db.Column(db.Integer, db.ForeignKey(
        "staff.id"), nullable=False)


class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    sign = db.Column(db.String(2), nullable=False)

    course_id = db.relationship(
        "Course", backref="level", lazy=True)


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    course_id = db.relationship(
        "Course", backref="language", lazy=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    course_id = db.relationship(
        "Course", backref="category", lazy=True)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lessons = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    term = db.Column(db.String(255), nullable=False)

    course_class = db.relationship("Class", backref="course", lazy=True)

    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id"), nullable=False)

    level_id = db.Column(db.Integer, db.ForeignKey(
        "level.id"), nullable=False)

    language_id = db.Column(db.Integer, db.ForeignKey(
        "language.id"), nullable=False)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow())
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(300), nullable=False)

    payment_method_id = db.Column(db.Integer, db.ForeignKey(
        "payment_method.id"), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey(
        "student.id"), nullable=False)


class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    payment_id = db.relationship(
        "Payment", backref="payment_method", lazy=True)


class_week_days = db.Table('class_week_day',
                           db.Column('class_weekday_id', db.Integer, db.ForeignKey(
                               'class_weekday.id'), primary_key=True),
                           db.Column('class_id', db.Integer, db.ForeignKey(
                               'class.id'), primary_key=True),
                           db.Column('hour', db.String(255), nullable=False)
                           )

class_students = db.Table('class_student',
                          db.Column('student_id', db.Integer, db.ForeignKey(
                              'student.id'), primary_key=True),
                          db.Column('class_id', db.Integer, db.ForeignKey(
                              'class.id'), primary_key=True)
                          )


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow())
    end_date = db.Column(db.DateTime, default=datetime.utcnow())
    price = db.Column(db.Float, nullable=False)

    weekdays = db.relationship('ClassWeekday', secondary=class_week_days, lazy='subquery',
                               backref=db.backref('classes', lazy=True))

    students = db.relationship('Student', secondary=class_students, lazy='subquery',
                               backref=db.backref('students', lazy=True))

    teacher_id = db.Column(db.Integer, db.ForeignKey(
        "teacher.id"), nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey(
        "course.id"), nullable=False)


class ClassWeekday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
