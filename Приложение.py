import datetime
import uuid

from models import Users, Products, Orders, Tickets
from peewee import *


db = MySQLDatabase(database="tests", host="127.0.0.1", user="root", password="08november91")


class Users(db.Model):
      username = CharField(max_length=30, unique=True)  # null = False
      password = CharField(max_length=30)  # null = False
      points = IntegerField()

      @staticmethod
      def is_exist(username: str) -> bool:
            try:
                  Users.get(Users.username == username)
            except Users.DoesNotExist:
                  return False
            else:
                  return True


class Tickets(db.Model):
      uuid = CharField(max_length=36, unique=True)  # null = False
      available = CharField(max_length=30)  # null = False
      user = BooleanField()


class Products(db.Model):
      name = CharField(max_length=255, null=False)
      cost = SmallIntegerField()
      count = SmallIntegerField()

      # @property
      # def total_sum(self):
      #     return self.cost * self.count


class Orders(db.Model):
      user_id = ForeignKeyField(Users, field="id", on_delete="CASCADE")
      product_id = ForeignKeyField(Products, field="id")
      count = SmallIntegerField()
      order_datetime = DateTimeField()




hello = '=== Добро пожаловать в "Не магазин" ==='
print(hello.center(len(hello) + 40))
print('Здесь вы можете обменивать тикеты для того, чтобы приобретать товары')

print('> Товары \n'
      '> Зарегистрироваться \n'
      '> Войти')


Products.create(name="Картинка с котиком", cost=50, count=20)
Products.create(name="Наклейка синего цвета", cost=15, count=45)
Products.create(name="Наклейка красного цвета", cost=20, count=50)

Users.create(username="Alex", password='0000', points=20)


prod = Products.get(Products.name == "Картинка с котиком")
prod_2 = Products.get(Products.name == "Наклейка синего цвета")
prod_3 = Products.get(Products.name == "Наклейка красного цвета")



enter = input('')
if enter == 'Товары':
      print(f"{'Название':<30}{'Стоимость':<20}{'Кол-во':<20}")
      print('=' * 60)
      print(f"{prod.name:<30}{prod.count:<20}{prod.cost:<20}")
      print(f"{prod_2.name:<30}{prod_2.count:<20}{prod_2.cost:<20}")
      print(f"{prod_3.name:<30}{prod_3.count:<20}{prod_3.cost:<20}")

#
login = input('')
if login == 'Зарегистрироваться':
      print(input('Ведите логин > '))
      print(input('Ведите пароль > '))




print(hello.center(len(hello) + 40))
print('Здесь вы можете обменивать тикеты для того, чтобы приобретать товары')

print('> товары \n'
      '> Купить \n'
      '> Профиль \n'
      '> Тикет')

new_uuid = str(uuid.uuid4())
print(new_uuid)

