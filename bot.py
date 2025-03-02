from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7681957954:AAHNv7K4oyjaUsXShouNMopsvM9i17qJ5OE").build()

app.add_handler(CommandHandler("hi", hello))

app.run_polling()