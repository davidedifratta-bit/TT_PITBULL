import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐶 TT_PITBULL ONLINE\n\n"
        "Comandi disponibili:\n"
        "/start\n"
        "/analisin"
        "/setka"
    )

async def analisi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 ANALISI SETKA CUP\n\n"
        "Sistema TT_PITBULL attivo.\n"
        "Modulo analisi in preparazione."
    )
async def setka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏓 SETKA CUP\n\n"
        "Match demo:\n"
        "Ivanov vs Petrov\n\n"
        "Probabilità:\n"
        "Ivanov 62%\n"
        "Petrov 38%\n\n"
        "Fiducia: 7/10\n\n"
        "Pronostico:\n"
        "Vittoria Ivanov"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analisi", analisi))
app.add_handler(CommandHandler("setka", setka))

print("TT_PITBULL avviato")

app.run_polling()
