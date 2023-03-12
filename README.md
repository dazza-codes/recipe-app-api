# recipe-app-api

Recipe API project from Udemy course

# Configuration and Secrets

Use [python-decouple](https://github.com/HBNetwork/python-decouple) for configuration.

To create a new `SECRET_KEY`:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Sample values for `.env` settings:
```shell
# .env file in the root of the project, could be symlinked to
# another file, such as .environments/.env.local
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY='YOUR_SECRET_KEY'
DATABASE_URL='sqlite:///db.sqlite3'
```
