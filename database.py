from gino import Gino
from aiogram import Dispatcher

from settings import DATABASE_STR

db = Gino()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    telegram_id = db.Column(db.Integer())


async def on_startup(dispatcher: Dispatcher) -> None:
    await db.set_bind(DATABASE_STR)
    await db.gino.create_all()


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await db.pop_bind().close()
