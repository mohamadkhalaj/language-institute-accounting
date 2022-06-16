import datetime
import random

from queries import (
    create_category,
    create_class,
    create_class_students,
    create_class_week_days,
    create_class_weekday,
    create_course,
    create_language,
    create_level,
    create_payment,
    create_payment_method,
    create_staff,
    create_staff_account,
    create_student,
    create_student_account,
    create_teacher,
    create_teacher_account,
)

# Test for student creation 10 items.

# first_name sample
first_name = ['John', 'Jane', 'Mary', 'Tom', 'Bob',
              'Alice', 'Sam', 'Tommy', 'Jack', 'Linda']
# last_name sample
last_name = ['Smith', 'Johnson', 'Williams', 'Jones',
             'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
# phone_number sample
phone_number = ['1234567890', '1234567891', '1234567892', '1234567893',
                '1234567894', '1234567895', '1234567896', '1234567897', '1234567898', '1234567899']


def test_student_creation():
    # state sample
    state = ['CA', 'TX', 'NY', 'FL', 'NJ', 'IL', 'GA', 'MA', 'MI', 'OH']
    # city sample
    city = ['San Francisco', 'Houston', 'New York', 'Florida',
            'New Jersey', 'Chicago', 'Atlanta', 'Boston', 'Detroit', 'Washington']
    # street sample
    street = ['123 Main St', '456 Main St', '789 Main St', '1011 Main St', '1213 Main St',
              '1415 Main St', '1617 Main St', '1819 Main St', '2020 Main St', '2222 Main St']
    # zip_code sample
    zip_code = ['12345', '54321', '98765', '12345', '54321',
                '98765', '12345', '54321', '98765', '12345']
    for i in range(10):
        create_student(
            first_name=random.choice(first_name),
            last_name=random.choice(last_name),
            state=random.choice(state),
            city=random.choice(city),
            street=random.choice(street),
            zip_code=random.choice(zip_code),
            phone_number=random.choice(phone_number),
            email='email' + str(i),
            date_birth=datetime.datetime.now() - datetime.timedelta(days=random.randint(4, 60)))

# Test for teacher creation 10 items.


def test_teacher_creation():
    for i in range(10):
        create_teacher(
            description='description' + str(i),
            first_name=random.choice(first_name),
            last_name=random.choice(last_name),
            phone_number=random.choice(phone_number),
            email='email' + str(i))

# Test for staff creation 10 items.


def test_staff_creation():
    # sample for position
    position = ["Administrator", "Financial"]
    for i in range(10):
        create_staff(
            position=random.choice(position),
            first_name=random.choice(first_name),
            last_name=random.choice(last_name),
            phone_number=random.choice(phone_number),
            email='email' + str(i))

# Test for class creation 10 items.


def test_class_creation():
    # sample for past date
    start_date = [datetime.datetime.now(
    ) - datetime.timedelta(days=random.randint(1, 100)) for _ in range(100)]
    # sample for future date
    end_date = [datetime.datetime.now(
    ) + datetime.timedelta(days=random.randint(1, 100)) for _ in range(100)]
    # sample fot price
    price = [random.randint(100, 1000) for _ in range(100)]
    for i in range(10):
        create_class(
            name='name' + str(i),
            start_date=random.choice(start_date),
            end_date=random.choice(end_date),
            price=random.choice(price),
            teacher_id=i+1,
            course_id=i+1)

# Test for course creation 10 items.


def test_course_creation():
    # sample for term
    term = ["Spring", "Summer", "Fall", "Winter"]
    for i in range(10):
        create_course(
            lessons=random.randint(1, 10),
            description='description' + str(i),
            term=random.choice(term),
            category_id=random.randint(1, 4),
            level_id=random.randint(1, 3),
            language_id=random.randint(1, 10))

# Test for student account creation 10 items.


def test_student_account_creation():
    for i in range(10):
        create_student_account(
            login='login' + str(i),
            password='password' + str(i),
            student_id=i+1)

# Test for teacher account creation 10 items.


def test_teacher_account_creation():
    for i in range(10):
        create_teacher_account(
            login='login' + str(i),
            password='password' + str(i),
            teacher_id=i+1)

# Test for staff account creation 10 items.


def test_staff_account_creation():
    for i in range(10):
        create_staff_account(
            login='login' + str(i),
            password='password' + str(i),
            staff_id=i+1)

# Create Test for level all possible values.


def test_level():
    create_level("Beginner", "B")
    create_level("Intermediate", "I")
    create_level("Advanced", "A")


# Create Test for 10 languages.


def test_language():
    create_language("English")
    create_language("German")
    create_language("French")
    create_language("Spanish")
    create_language("Italian")
    create_language("Portuguese")
    create_language("Russian")
    create_language("Japanese")
    create_language("Chinese")
    create_language("Arabic")


# create test for category.
def test_category():
    create_category("adult")
    create_category("child")
    create_category("young")
    create_category("grand")

# Create test for 5 payment methods.


def test_payment_method():
    create_payment_method("Cash")
    create_payment_method("Credit Card")
    create_payment_method("Debit Card")
    create_payment_method("PayPal")
    create_payment_method("Bank Transfer")


# Test for payment creation 10 items.


def test_payment_creation():
    # sample for amount
    amount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    # sample for status
    status = ["Pending", "Completed", "Cancelled"]
    for i in range(10):
        create_payment(
            payment_method_id=random.randint(1, 5),
            amount=random.choice(amount),
            student_id=i+1,
            status=random.choice(status),
            description='description' + str(i))


# create 30 samples for ClassWeekday.
def test_class_weekdays():
    # weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    # hours such: 10:00 - 11:00
    hours = ['10:00 - 11:00', '11:00 - 12:00', '12:00 - 13:00', '13:00 - 14:00',
             '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00']
    for i in range(30):
        create_class_weekday(
            hour=random.choice(hours),
            weekday=random.choice(weekdays))

# create 10 sample for create_class_students.


def test_student_class():
    for i in range(10):
        create_class_students(class_id=random.randint(
            1, 10), student_id=random.randint(1, 10))

# 10 samples for class_week_days.


def test_class_week_days_samples():
    # weekdays
    for i in range(10):
        create_class_week_days(i+1, random.randint(1, 30))


if __name__ == "__main__":

    print("Test for level...")
    test_level()

    print("Test for language...")
    test_language()

    print("Test for category...")
    test_category()

    print("Test for payment_method creation...")
    test_payment_method()

    print("Test for student creation...")
    test_student_creation()

    print("Test for teacher creation...")
    test_teacher_creation()

    print("Test for staff creation...")
    test_staff_creation()

    print("Test for course creation...")
    test_course_creation()

    print("Test for class creation...")
    test_class_creation()

    print("Test for student account creation...")
    test_student_account_creation()

    print("Test for teacher account creation...")
    test_teacher_account_creation()

    print("Test for staff account creation...")
    test_staff_account_creation()

    print("Test for payment creation...")
    test_payment_creation()

    print("Test for ClassWeekday creation...")
    test_class_weekdays()

    print("Test for student class creation...")
    test_student_class()

    print("Test for class_week_days creation...")
    test_class_week_days_samples()
