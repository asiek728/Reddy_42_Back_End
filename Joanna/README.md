To run the project:

- `cd` into the project on your terminal/Gitbash
- Run `pipenv shell` to activate your virtual environment
- Run `pipenv install -r requirements.txt`
- Make sure to create a `.env` file with the following contents:

```
FLASK_APP=application
FLASK_DEBUG=1
DATABASE_URL=<ELEPHANTSQL_URL>
TEST_DATABASE_URL=<TEST_ELEPHANTSQL_URL>
```

- Run `pipenv run dev`

You're good to go! 
