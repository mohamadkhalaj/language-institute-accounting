import models
from models import app, db

app.app_context().push()

# new student object
new_stu1 = models.Student(first_name='nastooh', last_name="javan", state="alborz", city="karaj",
                          street="karaj", zip_code="1111111111", phone_number="+9809121111111", email="test@test.com")

new_stu2 = models.Student(first_name='ali', last_name="khaleghi", state="Qazvin", city="qazvin",
                          street="norouzian", zip_code="2222222222", phone_number="+9809121111111", email="test@test.com")

new_stu3 = models.Student(first_name='shokuh', last_name="kermanshahi", state="tehran", city="tehran",
                          street="enghelab", zip_code="3333333333", phone_number="+9809121111111", email="test@test.com")
db.session.add(new_stu1)
db.session.add(new_stu2)
db.session.add(new_stu3)
db.session.commit()

# print names and last names
print(f"name: {new_stu1.first_name}, last name: {new_stu1.last_name}")
print(f"name: {new_stu2.first_name}, last name: {new_stu2.last_name}")
print(f"name: {new_stu3.first_name}, last name: {new_stu3.last_name}")

# edit Student
stu = models.Student.query.filter_by(first_name="nastooh").first()
stu.last_name = 'Taheri javan'
db.session.commit()
print(f"name: {stu.first_name}, last name: {stu.last_name}")

# number of students
count = models.Student.query.count()
print(f"number of students: {count}")

# remove object
stu = models.Student.query.filter_by(
    first_name="ali", last_name='khaleghi').first()
db.session.delete(stu)
db.session.commit()
count = models.Student.query.count()
print(f"number of students after remove: {count}")


# iterate students
all_stus = models.Student.query.all()
names = [stu.first_name for stu in all_stus]
print('All names: ')
print(*names, sep='\n')
