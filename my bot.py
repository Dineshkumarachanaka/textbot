from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Define a function to handle normal text messages
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create an Updater object with your bot's API token
    updater = Updater(token='6801438098:AAGnKLLBkHr1JKDJ_Tt26VOAZRq7zDHFC5c', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Register a handler for normal text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
