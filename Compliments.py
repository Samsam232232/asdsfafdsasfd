__version__ = (2, 0, 0)

# 	
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
# 	
#                                             © Copyright 2024
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/Compliments.jpg

import asyncio
import logging

from telethon.tl.types import Message

from .. import loader, main, utils

logger = logging.getLogger(__name__)


class ComplimentsMod(loader.Module):
    '''Покажи девушке какая она прекрасная (ну или им, какие они прекрасные)'''

    strings = {
        "name": "Compliments",
        "_cfg_doc_for_one_or_more": (
            "Выберите пожалуйста, комплименты будут для 1 человека женского пола, или"
            " для всех людей женского пола в чате \nЕсли для 1 человека--> one\nЕсли"
            " для всех людей женского пола в чате--> more"
        ),
        "_cfg_doc_command_mode": (
            "Выберите пожалуйста режим команды, какая будет анимация: \n Если вы"
            " хотите, чтобы печатался список комплиментов --> 1 \n Если вы хотите,"
            " чтобы каждую секунду комплимент заменялся на другой и в конце вывелся"
            " полный список --> 2"
        ),
    }


    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "for_one_or_more",
                "one",
                doc=lambda: self.strings("_cfg_doc_for_one_or_more"),
                validator=loader.validators.Choice(["one", "more"]),
            ),
            loader.ConfigValue(
                "command_mode",
                1,
                doc=lambda: self.strings("_cfg_doc_command_mode"),
                validator=loader.validators.Choice([1, 2]),
            ),
        )


    async def inline_compliments(self, message: Message):
        om = self.config["for_one_or_more"]
        mode = self.config["command_mode"]
        if om == "one":
            if mode == 1:
                messages = [
                    "Ты...прекрасный(ая), а еще.... ",
                    "{♡} пидорас 🌺 ",
                    "🪴уебище~~ ",
                    "^0^ сирота 👐 ",
                    "👩🏻‍🎓нищета $>$ ",
                    "~~хуйня 👉👈 ",
                    "🙀 сын хуйни 😍 ",
                    "🤯 сын шлюхи 🤠 ",
                    "🥵 жирный 😜 ",
                    "~♡~ говном воняеш 🌹 ",
                    "😍 заебал 🤭 ",
                    "~~дурак ☁️ ",
                    "💋 тупой 🫂 ",
                    "👥 пробка🗣 ",
                    "😌 лиза из барбоскиных♡ ",
                    "🙈 додик ",
                    "😋 хуиплет) ",
                    "😊 долбень ",
                    "😻 конченый ",
                    "🦄 долбаеп ",
                    "👌 чурка ",
                    "🤔 сучонок ",
                    "🌚 быдло ",
                    "🌸 в харчках плаваешь ",
                    "🤜🤛 долбан ",
                    "✨ сын чингисхана",
                    "🐱 Ахуевший ",
                    "🔮 долбень ",
                    "💘 сын мусорки ",
                    "🤗 и вообще нахуй сходи ",
                ]

                current = ""
                for i in messages:
                    current += i + "\n"
                    message = await utils.answer(message, current)
                    await asyncio.sleep(0.5)

                await utils.answer(message, f"<i>{current}</i>")
            elif mode == 2:
                await utils.answer(message, "<i>Ты......</i>")
                await asyncio.sleep(1)
                await utils.answer(message, "<i>Ты...прекрасная...</i>")
                await asyncio.sleep(1)
                await utils.answer(message, "<i>Ты...прекрасная, а еще....</i>")
                await asyncio.sleep(1)
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "🍬 привлекательная",
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        f"<i>Ты...прекрасная, а еще....\n{m}</i>",
                    )
                    await asyncio.sleep(1)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    f"<b><i>Ты...прекрасная, а еще.... \n{all_}\nИ САМАЯ ЛУЧШАЯ НА"
                    " СВЕТЕ❤️❤️❤️❤️❤️❤️❤️❤️</i></b>",
                )
            else:
                await utils.answer(
                    message,
                    "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                    " потому что в конфиге неправильное значение. \nНапишите"
                    " <code>.complimentscfg</code>",
                )
        elif om == "more":
            if mode == 1:
                await utils.answer(message, "<i>Каждая девушка/девочка/женщина...</i>")
                await asyncio.sleep(0.5)
                await utils.answer(
                    message, "<i>Каждая девушка/девочка/женщина в этом чате...</i>"
                )
                await asyncio.sleep(0.5)
                await utils.answer(
                    message,
                    "<i>ТКаждая девушка/девочка/женщина в этом чате прекрасна...</i>",
                )
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя ♡",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "🍬 привлекательная",
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        "<i>Каждая девушка/девочка/женщина в этом чате прекрасна..."
                        f" еще, каждая из них...\n{m}</i>",
                    )
                    await asyncio.sleep(0.5)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    "<b><i>Каждая девушка/девочка/женщина в этом чате прекрасна.... еще"
                    f" каждая из них: \n{all_}\nИ САМАЯ ЛУЧШАЯ НА"
                    " СВЕТЕ❤️❤️❤️❤️❤️❤️❤️❤️</i></b>",
                )
            elif mode == 2:
                await utils.answer(message, "<i>Каждая девушка/девочка/женщина...</i>")
                await asyncio.sleep(1)
                await utils.answer(
                    message,
                    "<i>Каждая девушка/девочка/женщина в этом чате прекрасна...</i>",
                )
                await asyncio.sleep(1)
                await utils.answer(
                    message,
                    "<i>Каждая девушка/девочка/женщина в этом чате прекрасна... еще"
                    " каждая из них:</i>",
                )
                await asyncio.sleep(1)
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "🍬 привлекательная",
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        "<i>Каждая девушка/девочка/женщина в этом чате прекрасна..."
                        f" еще каждая из них:\n{m}</i>",
                    )
                    await asyncio.sleep(1)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    "<b><i>Каждая девушка/девочка/женщина в этом чате прекрасна... еще"
                    f" каждая из них: \n{all_}\nИ САМАЯ ЛУЧШАЯ НА"
                    " СВЕТЕ❤️❤️❤️❤️❤️❤️❤️❤️</i></b>",
                )
            else:
                await utils.answer(
                    message,
                    "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                    " потому что в конфиге неправильное значение. \nНапишите"
                    " <code>.complimentscfg</code>",
                )
        else:
            await utils.answer(
                message,
                "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                " потому что в конфиге неправильное значение. \nНапишите"
                " <code>.complimentscfg</code>",
            )

    async def complimentscfgcmd(self, message: Message):
        """—>конфиг этого модуля"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    async def ilikecmd(self, message):
        "Инлайн анимация комплиментов(полная настройка в конфиге)"
        await self.inline.form(
            text="Я должен кое-что сказать...",
            reply_markup=[
                [{"text": "🥺", "callback": self.inline_compliments}],
                [{"text": "🚫", "action": "close"}],
            ],
            message=message,
            disable_security=True,
        )