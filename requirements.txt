import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐶 TT_PITBULL ONLINE\n\n"
        "Comandi disponibili:\n"
        "/start\n"
        "/analisi"
    )

async def analisi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 ANALISI SETKA CUP\n\n"
        "Sistema TT_PITBULL attivo.\n"
        "Modulo analisi in preparazione."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analisi", analisi))

print("TT_PITBULL avviato")

app.run_polling()
