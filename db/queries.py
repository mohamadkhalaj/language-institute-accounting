import models
from models import db


# Select * from all tables.
def get_all_students():
    return models.Student.query.all()


def get_all_teachers():
    return models.Teacher.query.all()


def get_all_courses():
    return models.Course.query.all()


def get_all_classes():
    return models.Class.query.all()


def get_all_levels():
    return models.Level.query.all()


def get_all_staff():
    return models.Staff.query.all()


def get_all_payment_methods():
    return models.PaymentMethod.query.all()


def get_all_payments():
    return models.Payment.query.all()


def get_all_categories():
    return models.Category.query.all()


def get_all_languages():
    return models.Language.query.all()


def get_all_leveles():
    return models.Level.query.all()

# Get students by part of first_name or last_name.


def get_students_by_name(name):
    return models.Student.query.filter(models.Student.first_name.like(
        '%' + name + '%') | models.Student.last_name.like(
            '%' + name + '%')).all()

# Get teachers by part of first_name or last_name.


def get_teachers_by_name(name):
    return models.Teacher.query.filter(models.Teacher.first_name.like(
        '%' + name + '%') | models.Teacher.last_name.like(
            '%' + name + '%')).all()

# Get staffs by part of first_name or last_name.


def get_staff_by_name(name):
    return models.Staff.query.filter(models.Staff.first_name.like(
        '%' + name + '%') | models.Staff.last_name.like(
            '%' + name + '%')).all()


# serach by first_name and last_name in teachers and staffs and students tables.
def search_by_name_in_all_tables(name):
    return models.Teacher.query.filter(models.Teacher.first_name.like(
        '%' + name + '%') | models.Teacher.last_name.like(
            '%' + name + '%') | models.Staff.first_name.like(
                '%' + name + '%') | models.Staff.last_name.like(
                    '%' + name + '%') | models.Student.first_name.like(
                        '%' + name + '%') | models.Student.last_name.like(
                            '%' + name + '%')).all()


# check student by login and password.
def check_student_login(login, password):
    return models.StudentAccount.query.filter(
        login == login,
        password == password).first()


# check staff by login and password.
def check_staff_login(login, password):
    return models.StaffAccount.query.filter(
        login == login,
        password == password).first()


# check teacher by login and password.
def check_teacher_login(login, password):
    return models.TeacherAccount.query.filter(
        login == login,
        password == password).first()


# Get student classs by student id.
def get_student_classes(student_id):
    return models.Class.query.filter(student_id == student_id).all()

# Get teacher classs by teacher id.


def get_teacher_classes(teacher_id):
    return models.Class.query.filter(teacher_id == teacher_id).all()

# Get class students.


def get_class_students(class_id):
    return models.Student.query.filter(class_id == class_id).all()

# Get class teacher.


def get_class_teachers(class_id):
    return models.Teacher.query.filter(class_id == class_id).all()

# Get class weekdays.


def get_class_weekdays(class_id):
    return models.ClassWeekday.query.filter(class_id == class_id).all()

# Get class courses.


def get_class_courses(class_id):
    return models.Course.query.filter(class_id == class_id).all()

# Get student payments.


def get_student_payments(student_id):
    return models.Payment.query.filter(student_id == student_id).all()

# Get weekday classs by weekday id.


def get_weekday_classes(weekday_id):
    return models.Class.query.filter(weekday_id == weekday_id).all()

# Get classes by hour.


def get_classes_by_hour(hour):
    return models.Class.query.filter(hour == hour).all()

# Get sum of student payments amount.


def get_student_payments_amount(student_id):
    return models.Payment.query.filter(student_id == student_id).sum(models.Payment.amount)

# Get class students count.


def get_class_students_count(class_id):
    return models.Student.query.filter(class_id == class_id).count()

# Get course students count.


def get_course_students_count(course_id):
    return models.Student.query.filter(course_id == course_id).count()

# Get count of students.


def get_students_count():
    return models.Student.query.count()

 # Get count of teachers.


def get_teachers_count():
    return models.Teacher.query.count()

# Get count of staff.


def get_staff_count():
    return models.Staff.query.count()

# Get count of classes.


def get_classes_count():
    return models.Class.query.count()

# Get count of courses.


def get_courses_count():
    return models.Course.query.count()

# Get languages count.


def get_languages_count():
    return models.Language.query.count()

# Get language classes count.


def get_language_classes_count(language_id):
    return models.Class.query.filter(language_id == language_id).count()

# Get language courses count.


def get_language_courses_count(language_id):
    return models.Course.query.filter(language_id == language_id).count()

# Get students cancelled paymentt.


def get_students_cancelled_payments(student_id):
    return models.Payment.query.filter(student_id == student_id, status="Cancelled").all()

# Get students completed payments.


def get_students_completed_payments(student_id):
    return models.Payment.query.filter(student_id == student_id, status="Completed").all()

# Get students pending payments.


def get_students_pending_payments(student_id):
    return models.Payment.query.filter(student_id == student_id, status="Pending").all()

# Get class duration by substracting start_time and end_time.


def get_class_duration(class_id):
    class_ = models.Class.query.filter(class_id == class_id).first()
    return class_.end_time - class_.start_time

# Update student.


def update_student(student_id, first_name, last_name, state, city, street, zip_code, phone_number, email, date_birth):
    model = models.Student.query.filter(id == student_id).first()
    model.first_name = first_name
    model.last_name = last_name
    model.state = state
    model.city = city
    model.street = street
    model.zip_code = zip_code
    model.phone_number = phone_number
    model.email = email
    model.date_birth = date_birth
    db.session.commit()

# Update teacher.


def update_teacher(teacher_id, description, first_name, last_name, phone_number, email):
    model = models.Teacher.query.filter(id == teacher_id).first()
    model.description = description
    model.first_name = first_name
    model.last_name = last_name
    model.phone_number = phone_number
    model.email = email
    db.session.commit()

# Update staff.


def update_staff(staff_id, position, first_name, last_name, phone_number, email):
    model = models.Staff.query.filter(id == staff_id).first()
    model.position = position
    model.first_name = first_name
    model.last_name = last_name
    model.phone_number = phone_number
    model.email = email
    db.session.commit()


# Update student account.
def update_student_account(student_id, login, password):
    model = models.StudentAccount.query.filter(id == student_id).first()
    model.login = login
    model.password = password
    db.session.commit()

# Update teacher account.


def update_teacher_account(teacher_id, login, password):
    model = models.TeacherAccount.query.filter(id == teacher_id).first()
    model.login = login
    model.password = password
    db.session.commit()

# Update staff account.


def update_staff_account(staff_id, login, password):
    model = models.StaffAccount.query.filter(id == staff_id).first()
    model.login = login
    model.password = password
    db.session.commit()

# Update student address.


def update_student_address(student_id, state, city, street, zip_code):
    model = models.Student.query.filter(id == student_id).first()
    model.state = state
    model.city = city
    model.street = street
    model.zip_code = zip_code
    db.session.commit()


# Create accounts.


def create_student_account(login, password, student_id):
    model = models.StudentAccount(
        login=login, password=password, student_id=student_id)
    db.session.add(model)
    db.session.commit()


def create_staff_account(login, password, staff_id):
    model = models.StaffAccount(
        login=login, password=password, staff_id=staff_id)
    db.session.add(model)
    db.session.commit()


def create_teacher_account(login, password, teacher_id):
    model = models.TeacherAccount(
        login=login, password=password, teacher_id=teacher_id)
    db.session.add(model)
    db.session.commit()

# Create staff.


def create_staff(position, first_name, last_name, phone_number, email):
    model = models.Staff(
        position=position,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email)

    db.session.add(model)
    db.session.commit()
# Create student.


def create_student(first_name, last_name, state, city, street, zip_code, phone_number, email, date_birth):
    model = models.Student(
        first_name=first_name,
        last_name=last_name,
        state=state,
        city=city,
        street=street,
        zip_code=zip_code,
        phone_number=phone_number,
        email=email,
        date_birth=date_birth)

    db.session.add(model)
    db.session.commit()
# Create teacher.


def create_teacher(description, first_name, last_name, phone_number, email):
    model = models.Teacher(
        description=description,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email)

    db.session.add(model)
    db.session.commit()
# Create class.


def create_class(name, start_date, end_date, price, teacher_id, course_id):
    model = models.Class(
        name=name,
        start_date=start_date,
        end_date=end_date,
        price=price,
        teacher_id=teacher_id,
        course_id=course_id)

    db.session.add(model)
    db.session.commit()
# Create course


def create_course(lessons, description, term, category_id, level_id, language_id):
    model = models.Course(
        lessons=lessons,
        description=description,
        term=term,
        category_id=category_id,
        level_id=level_id,
        language_id=language_id)

    db.session.add(model)
    db.session.commit()

# Create paymanent method.


def create_payment_method(name):
    model = models.PaymentMethod(
        name=name)

    db.session.add(model)
    db.session.commit()

# Create payment.


def create_payment(payment_method_id, amount, student_id, status, description):
    model = models.Payment(
        payment_method_id=payment_method_id,
        amount=amount,
        student_id=student_id,
        status=status,
        description=description)

    db.session.add(model)
    db.session.commit()

# Create level.


def create_level(name, sign):
    model = models.Level(
        name=name,
        sign=sign)

    db.session.add(model)
    db.session.commit()

# Create category.


def create_category(name):
    model = models.Category(
        name=name)

    db.session.add(model)
    db.session.commit()

# Create language.


def create_language(name):
    model = models.Language(
        name=name)

    db.session.add(model)
    db.session.commit()


# Create ClassWeekday.
def create_class_weekday(hour, weekday):
    model = models.ClassWeekday(
        hour=hour,
        name=weekday)

    db.session.add(model)
    db.session.commit()


# create class_students.
def create_class_students(class_id, student_id):
    statement = models.class_students.insert().values(
        student_id=student_id, class_id=class_id)

    db.session.execute(statement)
    db.session.commit()

# Create class_week_days


def create_class_week_days(class_id, class_week_day_id):
    statement = models.class_week_days.insert().values(
        class_weekday_id=class_week_day_id, class_id=class_id)
    db.session.execute(statement)
    db.session.commit()


def delete_course(course_id):
    models.Course.query.filter(id == course_id).delete()
    db.session.commit()


def delete_class(class_id):
    models.Class.query.filter(id == class_id).delete()
    db.session.commit()


def delete_teacher(teacher_id):
    models.Teacher.query.filter(id == teacher_id).delete()
    db.session.commit()


def delete_student(student_id):
    models.Student.query.filter(id == student_id).delete()
    db.session.commit()


def delete_staff(staff_id):
    models.Staff.query.filter(id == staff_id).delete()
    db.session.commit()
