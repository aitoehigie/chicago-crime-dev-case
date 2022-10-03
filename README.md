
---
# chicago_crime_dev_case
chicago_crime_dev_case created by aitoehigie

## Project Setup

N.B Before building the containers, do ensure that you add your `BigQuery GOOGLE_APPLICATION_CREDENTIALS json` file in the root directory of this project
and set the path to the file in the `default.toml` file found here: `/chicago-crime-dev-case/chicago_crime_dev_case/default.toml`. Then run the build command:


```bash
docker-compose build
```

## Executing

```bash
docker-compose up
```

You can then access the streamlit dashboard here: [Dashboard](http://localhost:8501)
And access the Openapi docs here: [Docs](http://localhost:8000/docs)

## Configuration

This project uses [Dynaconf](https://dynaconf.com) to manage configuration.

```py
from chicago_crime_dev_case.config import settings
```

## Acessing variables

```py
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Defining variables

### On files

settings.toml

```toml
[development]
dynaconf_merge = true

[development.db]
echo = true
```

> `dynaconf_merge` is a boolean that tells if the settings should be merged with the default settings defined in chicago_crime_dev_case/default.toml.

### As environment variables
```bash
export chicago_crime_dev_case_KEY=value
export chicago_crime_dev_case_KEY="@int 42"
export chicago_crime_dev_case_KEY="@jinja {{ this.db.uri }}"
export chicago_crime_dev_case_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Secrets

There is a file `.secrets.toml` where your sensitive variables are stored,
that file must be ignored by git. (add that to .gitignore)

Or store your secrets in environment variables or a vault service, Dynaconf
can read those variables.

