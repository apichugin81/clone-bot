# Тексты сообщений

from aiogram.utils.markdown import link


from src.constants.common import URL


class MSG:
    prozero_text = ('Не принимается на акции, но можно сдать в '
                    + link('экоцентре ProZero', url=URL.prozero_tg))