# E-Com-Web_Backend-Mitti_Bazaar
This repository contains the backend code for Mitti Bazaar, a Django-powered e-commerce web application. It supports user registration and login, product listing and filtering, cart and checkout operations, order management, and third-party payment integration. Designed with scalability, security, and modularity in mind.
Auther = Debapriyo Pal Chowdhury

# Mitti Bazaar - Django E-commerce Platform
```markdown


![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Template Tags Reference](#template-tags-reference)
- [Database Models](#database-models)
- [Admin Customization](#admin-customization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Mitti Bazaar is a full-featured e-commerce platform built with Django, specializing in pottery and clay products. The application includes user authentication, product catalog, shopping cart functionality, and order management.

## Features
- User authentication (login, logout, registration)
- Product catalog with categories
- Shopping cart with session management
- Wishlist functionality
- Order history tracking
- Responsive design
- Admin dashboard for product management

## Installation Guide

### Prerequisites
- Python 3.8+
- MySQL Server
- Git (optional)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mitti-bazaar.git
   cd mitti-bazaar
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**
   - Install MySQL and create a database named `second_e_com`
   - Configure database settings in `myproject/settings.py`

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Project Structure
```
myproject/
├── myapp/                  # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Database models
│   ├── urls.py             # App URL routing
│   └── views.py            # View functions
├── myproject/              # Project configuration
│   ├── settings.py         # Project settings
│   └── urls.py             # Main URL routing
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User-uploaded files
├── requirements.txt        # Python dependencies
└── manage.py               # Django management script
```

## Configuration
Key settings in `myproject/settings.py`:

```python
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'second_e_com',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
## Database Models
Key models in `myapp/models.py`:

```python
class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    about_cat = models.TextField(max_length=2000)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img/')
    available = models.BooleanField(default=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
```

## Admin Customization
Admin interface features in `myapp/admin.py`:

```python
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    inlines = [ProductImageInline]

admin.site.register(Products, ProductAdmin)
admin.site.register(Category)

# Custom admin branding
admin.site.site_header = "Mitti Bazaar Administration"
admin.site.site_title = "Mitti Bazaar Admin Portal"
admin.site.index_title = "Welcome to Mitti Bazaar Admin"
```

