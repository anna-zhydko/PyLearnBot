async def remove_inline_markup(bot, message):
    try:
        await bot.edit_message_reply_markup(message_id=message.message_id - 1, chat_id=message.chat.id)
    except:
        pass
