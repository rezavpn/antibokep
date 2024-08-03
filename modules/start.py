# Copyright 2024 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
An AntiBokep bot Powered by @rezabotlist to protect your groups from Bokep content.
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="Source",url="https://youtu.be/wVmZD4pZ9PE?si=yTBUYGzvAtTOpTfc")
                ]
            ]
        )
    )
