from faker import Faker

# from test_reqres_microservice.Models.Users import User
from app.models.User import User

fake = Faker()

user_token = 'QpwL5tke4Pnpja7X4'

# new_user_0 = User(
#     email=fake.email(),
#     first_name=fake.name(),
#     last_name=fake.last_name(),
#     avatar=f'https://reqres.in/img/faces/{fake.random_number()}-image_n.jp'
# )
new_user_0 = User(
    email=fake.email(),
    first_name=fake.name(),
    last_name=fake.last_name(),
    avatar=f'https://reqres.in/img/faces/{fake.random_number()}-image_n.jp'
)

new_user_1 = {
    "email": f"{fake.email()}",
    "first_name": f"{fake.name()}",
    "last_name": f"{fake.last_name()}",
    "avatar": f"https://reqres.in/img/faces/{fake.random_number()}-image_n.jpg"
  }
new_user_2 = {
    "email": f"{fake.email()}",
    "first_name": f"{fake.name()}",
    "last_name": f"{fake.last_name()}",
    "avatar": f"https://reqres.in/img/faces/{fake.random_number()}-image_n.jpg"
  }