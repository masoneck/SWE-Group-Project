from src.model.database import Database

def get_users():
    db = Database('data/database.db')
    users = db.select_all_users()
    table = []
    for user in users:
        table.append([
            str(user.user_id), str(user.email), str(user.first_name),
            str(user.last_name), str(user.orders)
        ])
    db.close()
    return table if len(table) > 1 else table + []

def get_items():
    db = Database('data/database.db')
    items = db.select_all_sales_items()
    table = []
    for item in items:
        table.append([
            str(item.item_id), str(item.name), str(item.stock), '$'+str(item.price),
            str(item.department_id)
        ])
    db.close()
    return table if len(table) > 1 else table + []

def get_orders():
    db = Database('data/database.db')
    orders = db.select_all_orders()
    table = []
    for order in orders:
        table.append([
            str(order.order_id), str(order.date), str(order.customer_id), '$'+str(order.total),
            str(order.is_complete), str(order.sales_items)
        ])
    db.close()
    return table

# def update_sales_item(sales_item_id, **kwargs):
#     try:
#         sales_item = SalesItem.query.get(sales_item_id)
#         if not sales_item:
#             print(f"Sales item with id {sales_item_id} not found")
#             return None

#         for key, value in kwargs.items():
#             if hasattr(sales_item, key):
#                 setattr(sales_item, key, value)
#             else:
#                 print(f"Sales item does not have attribute {key}")
#         db.session.commit()
#     except Exception as e:
#         print(f"An error occurred while updating sales item: {str(e)}")
#         return None

# def update_user(user_id, **kwargs):
#     try:
#         user = User.query.get(user_id)
#         if not user:
#             print(f"User with id {user_id} not found")
#             return None

#         for key, value in kwargs.items():
#             if hasattr(user, key):
#                 setattr(user, key, value)
#             else:
#                 print(f"User does not have attribute {key}")
#         db.session.commit()
#     except Exception as e:
#         print(f"An error occurred while updating user: {str(e)}")
#         return None

# def create_discount_code(code, discount_amount):
#     try:
#         discount_code = DiscountCode(code=code, discount_amount=discount_amount)
#         db.session.add(discount_code)
#         db.session.commit()
#         return discount_code.id
#     except Exception as e:
#         print(f"An error occurred while creating discount code: {str(e)}")
#         return None

# def create_sales_item(name, price, image, quantity):
#     try:
#         sales_item = SalesItem(name=name, price=price, image=image, quantity=quantity)
#         db.session.add(sales_item)
#         db.session.commit()
#         return sales_item.id
#     except Exception as e:
#         print(f"An error occurred while creating sales item: {str(e)}")
#         return None
