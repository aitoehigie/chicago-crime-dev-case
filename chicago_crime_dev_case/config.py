import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="chicago_crime_dev_case",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="chicago_crime_dev_case_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from chicago_crime_dev_case.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export chicago_crime_dev_case_KEY=value
export chicago_crime_dev_case_KEY="@int 42"
export chicago_crime_dev_case_KEY="@jinja {{ this.db.uri }}"
export chicago_crime_dev_case_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
chicago_crime_dev_case_ENV=production chicago_crime_dev_case run
```

Read more on https://dynaconf.com
"""
