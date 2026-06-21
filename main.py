import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

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
    context.user_data["attesa_match"] = True

    await update.message.reply_text(
        "🏓 Inserisci il match Setka Cup\n\n"
        "Esempio:\n"
        "Ivanov vs Petrov"
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
async def ricevi_match(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.user_data.get("attesa_match"):
        return

    match = update.message.text

    context.user_data["attesa_match"] = False

    await update.message.reply_text(
        f"📊 ANALISI MATCH\n\n"
        f"Match: {match}\n\n"
        f"Probabilità:\n"
        f"Giocatore 1: 60%\n"
        f"Giocatore 2: 40%\n\n"
        f"Fiducia: 7/10\n\n"
        f"Pronostico:\n"
        f"Vittoria Giocatore 1"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analisi", analisi))
app.add_handler(CommandHandler("setka", setka))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, ricevi_match)
)
print("TT_PITBULL avviato")

app.run_polling()
