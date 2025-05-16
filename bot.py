#!/usr/bin/env python

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Load token from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a mirror bot. Send me any message and I will echo it back to you.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just send me any message and I will repeat it back to you!')

async def mirror_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.text:
            await update.message.reply_text(update.message.text)
        elif update.message.caption:
            await update.message.reply_text(update.message.caption)
        else:
            await update.message.reply_text("I received your message but it doesn't contain text I can mirror.")
    except Exception as e:
        logger.error(f"Error in mirror_message: {e}")
        await update.message.reply_text("Sorry, I encountered an error processing your message.")

def main():
    logger.info('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Message handler
    app.add_handler(MessageHandler(
        (filters.TEXT | filters.CAPTION) & ~filters.COMMAND,
        mirror_message
    ))

    logger.info('Polling...')
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()