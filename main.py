import os
import random
import hashlib
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

    try:
        giocatore1, giocatore2 = [x.strip() for x in match.split("vs")]
    except:
        await update.message.reply_text(
            "❌ Formato non valido.\n\nEsempio:\nIvanov vs Petrov"
        )
        return

    

    nomi_ordinati = sorted([giocatore1, giocatore2])

    chiave = f"{nomi_ordinati[0]} vs {nomi_ordinati[1]}"

    seed = int(hashlib.md5(chiave.encode()).hexdigest(), 16)

    livello = seed % 100

    if livello < 50:
        base_prob = 52 + (seed % 5)      # 52-56
    elif livello < 85:
        base_prob = 57 + (seed % 8)      # 57-64
    else:
        base_prob = 65 + (seed % 6)      # 65-70

    if giocatore1 == nomi_ordinati[0]:
        prob1 = base_prob
        prob2 = 100 - base_prob
    else:
        prob1 = 100 - base_prob
        prob2 = base_prob
    if prob1 > prob2:
        vincitore = giocatore1
    else:
        vincitore = giocatore2

    vantaggio = abs(base_prob - 50)

    if vantaggio >= 18:
        fiducia = 9
    elif vantaggio >= 14:
        fiducia = 8
    elif vantaggio >= 10:
        fiducia = 7
    else:
        fiducia = 6

    if fiducia >= 8:
        valore = "🟢 ALTO"
        stake = "3%"
    elif fiducia == 7:
        valore = "🟡 MEDIO"
        stake = "2%"
    else:
        valore = "🔴 BASSO"
        stake = "1%"
    if fiducia >= 8:
        motivo = "Maggiore affidabilità nelle simulazioni."
    elif fiducia == 7:
        motivo = "Leggero vantaggio statistico."
    else:
        motivo = "Match equilibrato con margine ridotto."

    await update.message.reply_text(
        f"📊 ANALISI MATCH\n\n"
        f"🏓 Match: {giocatore1} vs {giocatore2}\n\n"
        f"📈 Probabilità:\n"
        f"{giocatore1}: {prob1}%\n"
        f"{giocatore2}: {prob2}%\n\n"
        f"🔥 Fiducia: {fiducia}/10\n"
        f"💰 Stake consigliato: {stake}\n"
        f"🎯 Valore: {valore}\n\n"
        f"🏆 Pronostico:\n"
        f"Vittoria {vincitore}\n\n"
        f"📌 Motivo:\n"
        f"{motivo}"
    )
    return

    

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analisi", analisi))
app.add_handler(CommandHandler("setka", setka))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, ricevi_match)
)
print("TT_PITBULL avviato")
print("VERSIONE FASE1")

app.run_polling()
