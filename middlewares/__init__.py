from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .checksub import CheckSubscriptionMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(CheckSubscriptionMiddleware())
