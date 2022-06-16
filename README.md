# language-institute-accounting

# Run
First make sure that ms sql server is up!\n
If you dont have sql sever, make sure DEBUG='True' is set in '.env' file, then app will connect to sqlite.
```
pip3 install -r requirements.txt
export FLASK_APP='models.py'
cd db
flask db init && flask db migrate && flask db upgrade
```

# Docker
If you don't have ms sql server installed on your system, you can use container \n
run below command:
```
docker-compose up
```
```
default username: sa
default password: Admin12345
port: 1433
```

# Usage
After migrating database run below command for inserting sample records:
```
python3 sample_data.py
```
All of possible queries are in 'queries.py' file.