import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ChatMemberHandler

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
GROUP_RULES = """📌 Group Rules:
1. Be respectful.
2. No spam.
3. Only relevant content.
4. No offensive language.
Enjoy your time here!"""

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# خوشامدگویی به کاربران جدید
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        try:
            name = member.full_name
            await context.bot.send_message(
                chat_id=member.id,
                text=f"🌟 Welcome {name}! So happy to have you here!\n\n{GROUP_RULES}"
            )
        except:
            pass

# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 I'm alive and ready!")

# راه‌اندازی ربات
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()

if __name__ == "__main__":
    main()