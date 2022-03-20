# business_intelligence (Backend)

## Project setup
```
source virtualenv/bin/activate
```

```
pip install -r requirement.txt
```

### Copy your enviroment file
```
copy or create your .flaskenv file for environment config database and application
```

### Add your database like your configuration in .flaskenv file and you can migrate database
```
flask db init
```

```
flask db upgrade
```

## Or you can import database if you have the db dump

### Running your application
```
flask run
```

### Customize configuration
See [Reference](https://flask.palletsprojects.com/en/2.0.x/).
Or [Flask for Restful API](https://kiddyxyz.medium.com/tutorial-restful-api-dengan-flask-python-part-1-pengenalan-instalasi-4836478ce651).
