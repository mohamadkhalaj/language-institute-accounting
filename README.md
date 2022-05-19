# language-institute-accounting

# Run
First make sure that ms sql server is up!
```
pip3 install -r requirements.txt
export FLASK_APP='models.py'
cd db
flask db init && flask db migrate && flask db upgrade
```

# Docker
If you don't have ms sql server installed on your system, you can use container just run below command:
```
docker-compose up
```
default username: sa
default password: Admin12345
port: 1433

# Usage
Some CRUD sample codes are wrote in 'sample-query.py' file.