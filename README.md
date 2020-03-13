# Stock my show

app for managing stock for shop owners. 
It is also a solid base for building online shop.

## Features
 * shop administrator can edit, delete and create new products and categories (special permissions required)
 * anonymous users can browse through products and categories 
 * search engine allows to conveniently find product or category 
 * see how many products are in each category
 * see detailed view of product with it's description, VAT amount, price, stock amount and category 
 * see how many items are left in stock


## How to get it up and running

### Before you start

Create virtualenv

If you don't have PostgreSQL installed, install it here:

[Install PostgreSQL and create a user](https://www.postgresql.org/download/)



### Getting Started

Install dependencies to your virtualenv, using requirements.txt

```
pip install -r requirements.txt
```

Create new database in PostgreSQL

Create new .py file in stock_my_shop/stock_my_shop folder and name it local_settings.py

Paste there the below:

```
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'HOST': '',
        'PASSWORD': '',
        'USER': '',
    }
}

```
Fill in missing parameteres with your secret key and your database credentials.


#### Installing

While in directory:

```
stock_my_shop/my_shop
```

Run migrations:

```
python3 manage.py migrate
```
Run server

```
python3 manage.py runserver
```

##### OPTIONAL STEP::

Run this code from "populating_db.py" in interactive Python console to populate database with example data.



## Built With

* [Python 3.6](https://www.python.org/)
* [Django 2.2](https://www.djangoproject.com/)  - high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - lets you control the rendering behavior of your Django forms in a very elegant and DRY way 
* [Bootstrap 4](https://getbootstrap.com/) - open source toolkit for developing with HTML, CSS, and JS.
* [PostgreSQL](https://www.postgresql.org/) -  open source object-relational database system

## Author

[ZuzannaP](https://github.com/ZuzannaP)

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE - see the [LICENSE.md](https://github.com/ZuzannaP/shall_we_meet_app/blob/master/LICENSE) file for details



