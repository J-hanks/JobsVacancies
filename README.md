

# JobsVacancies
<img src="./coverage.svg">

### Run
#### Clone the repository
```bash
git clone git@github.com:J-hanks/JobsVacancies.git
```
#### Go to repository folder
```bash
cd JobsVacancies
```

#### Install Requirements
```bash
pipenv install
```
#### Start Virtual enviroment
```bash
pipenv shell
```

#### Load data to database
```bash
./resetDB.sh
```

#### Run server 
```bash
python manage.py runserver
```


#### Acesss the site
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Users
#### Common user
email:      webuser@jobsvacancies.com
password:   jobsvacancies

#### Company user
email:      webusercompany@jobsvacancies.com
password:   jobsvacancies


### Test
```bash
python manage.py test
```