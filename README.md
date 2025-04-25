# Grocery Store E-commerce Platform

A Django-based e-commerce platform for grocery shopping with multiple user roles including customers, sellers, delivery agents, and administrators.

## Features

- **Multi-User System**
  - Customer Portal
  - Seller Dashboard
  - Delivery Agent Interface
  - Administrator Panel

- **Shopping Features**
  - Product Browsing
  - Shopping Cart
  - Secure Payment Integration
  - Order Tracking

- **Admin Features**
  - User Management
  - Product Management
  - Order Management
  - Dashboard Analytics

## Tech Stack

- **Backend Framework**: Django 5.1
- **Frontend**:
  - HTML/CSS
  - Bootstrap 4
  - jQuery
  - AdminMart Template (Admin Dashboard)
  - DataTables
  - Chartist.js for Analytics

## Prerequisites

- Python 3.x
- Node.js and npm (for admin dashboard assets)
- Django

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install django mathfilters
```

4. Install npm dependencies (for admin dashboard):
```bash
cd Guest/static/admin
npm install
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start development server:
```bash
python manage.py runserver
```

## Project Structure

```
MainProject/
├── Administrator/     # Admin module
├── DeliveryAgent/    # Delivery management
├── Guest/            # Public facing module
├── Seller/          # Seller management
├── User/            # Customer module
└── MainProject/     # Project settings
```

## Environment Variables

Create a `.env` file in the root directory and add:

```
DEBUG=True
SECRET_KEY=your-secret-key
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project uses multiple components with different licenses:
- AdminMart Template: Free for personal and commercial use
- DataTables: MIT License
- Project Code: [Your License]

## Credits

- AdminMart Template
- TemplatesJungle
- Bootstrap
- DataTables
- Other third-party libraries as listed in package.json