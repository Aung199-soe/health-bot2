import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging
from my_chatbot import get_chatbot_response  # Import from your chatbot module

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get Telegram token from environment
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_TOKEN:
    logger.error("No TELEGRAM_BOT_TOKEN found in .env file!")
    exit(1)

async def start(update: Update, context):
    """Send welcome message when /start is issued"""
    welcome_msg = """
    🩺 Welcome to Health Helper Bot!
    
    Ask me any medical question like:
    - What are COVID symptoms?
    - How to treat a headache?
    - Is fever dangerous?
    """
    await update.message.reply_text(welcome_msg)

async def handle_message(update: Update, context):
    """Handle incoming messages"""
    try:
        user_message = update.message.text
        logger.info(f"User asked: {user_message}")
        
        # Get response from your chatbot logic
        bot_response = get_chatbot_response(user_message)
        
        await update.message.reply_text(bot_response)
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("Sorry, I encountered an error. Please try again.")

def main():
    """Start the bot"""
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Command handlers
    application.add_handler(CommandHandler('start', start))
    
    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()