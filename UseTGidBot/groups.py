#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters


# Groups Welcome
@Client.on_message(filters.new_chat_members)
async def welcome(bot, msg):
    bot_id = (await bot.get_me())["id"]
    if msg.new_chat_members[0].id == bot_id:
        await msg.reply(
            f"Obrigado por me adicionar aqui! \n\nDeste grupo ID é `{msg.chat.id}`"
        )
    else:
        pass
