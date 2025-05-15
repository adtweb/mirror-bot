import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load token from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a mirror bot. Send me any message and I will echo it back to you.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just send me any message and I will repeat it back to you!')

async def mirror_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mirror the received message back to the user
    await update.message.reply_text(update.message.text)

def main():
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mirror_message))

    print('Polling...')
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()