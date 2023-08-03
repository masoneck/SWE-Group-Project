from models import User, SalesItem, Order, DiscountCode 
from db import db 

def get_users():
    try:
        users = User.query.all()
        return users
    except Exception as e:
        print(f"An error occurred while fetching users: {str(e)}")
        return None

def get_sales_items():
    try:
        sales_items = SalesItem.query.all()
        return sales_items
    except Exception as e:
        print(f"An error occurred while fetching sales items: {str(e)}")
        return None

def get_previous_orders():
    try:
        previous_orders = Order.query.filter_by(completed=True).all()
        return previous_orders
    except Exception as e:
        print(f"An error occurred while fetching previous orders: {str(e)}")
        return None

def get_current_orders():
    try:
        current_orders = Order.query.filter_by(completed=False).all()
        return current_orders
    except Exception as e:
        print(f"An error occurred while fetching current orders: {str(e)}")
        return None

def update_sales_item(sales_item_id, **kwargs):
    try:
        sales_item = SalesItem.query.get(sales_item_id)
        if not sales_item:
            print(f"Sales item with id {sales_item_id} not found")
            return None

        for key, value in kwargs.items():
            if hasattr(sales_item, key):
                setattr(sales_item, key, value)
            else:
                print(f"Sales item does not have attribute {key}")
        db.session.commit()
    except Exception as e:
        print(f"An error occurred while updating sales item: {str(e)}")
        return None

def update_user(user_id, **kwargs):
    try:
        user = User.query.get(user_id)
        if not user:
            print(f"User with id {user_id} not found")
            return None

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                print(f"User does not have attribute {key}")
        db.session.commit()
    except Exception as e:
        print(f"An error occurred while updating user: {str(e)}")
        return None

def create_discount_code(code, discount_amount):
    try:
        discount_code = DiscountCode(code=code, discount_amount=discount_amount)
        db.session.add(discount_code)
        db.session.commit()
        return discount_code.id
    except Exception as e:
        print(f"An error occurred while creating discount code: {str(e)}")
        return None

def create_sales_item(name, price, image, quantity):
    try:
        sales_item = SalesItem(name=name, price=price, image=image, quantity=quantity)
        db.session.add(sales_item)
        db.session.commit()
        return sales_item.id
    except Exception as e:
        print(f"An error occurred while creating sales item: {str(e)}")
        return None
