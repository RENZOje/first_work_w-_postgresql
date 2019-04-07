from database import Database
from user import User

Database.initialase(user='postgres',password='123456',database='learning',host='localhost')
user = User('smth@gmail.com', 'Smth', 'Smth', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('smth@gmail.com')
print(user_from_db)
