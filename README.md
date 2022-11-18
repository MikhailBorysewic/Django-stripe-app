# Project run

These steps suppose you have docker-compose installed.

## Env configuration

Go to https://dashboard.stripe.com/test/apikeys, copy your API keys and paste to .env file:

```commandline
SECRET_API_KEY=Your-Secret-key
PUBLIC_API_KEY=Your-Publishable-key
SECRET_KEY=django-insecure-d()wo(_gc(1&n8(#a@s1c&34gv@!q2y_wcc0r0k&q2dh+w*4&+
```

# Build/Run container
```commandline
docker-compose build .
docker-compose up
```

# Get created container Name/ID
Open new terminal and run:
```commandline
docker container ls
```

# Run migrations
```commandline
docker exec -it CREATED_CONTAINER_NAME/ID sh
python manage.py migrate
```

# Create superuser
```commandline
docker exec -it CREATED_CONTAINER_NAME/ID sh
python manage.py createsuperuser
```

Open http://127.0.0.1:8000/admin/ in your browser.

Add items, open http://127.0.0.1:8000/item/{id}/ in yor browser, try make [test](https://stripe.com/docs/testing) purchase.