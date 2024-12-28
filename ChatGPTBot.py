import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Masukkan API Key OpenAI dan token Telegram bot di sini
OPENAI_API_KEY = "<your open AI API Key>"
TELEGRAM_BOT_TOKEN = "<your Telegram Bot token>"

# Konfigurasikan OpenAI
openai.api_key = OPENAI_API_KEY

# Fungsi untuk mendapatkan respons dari ChatGPT
async def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Gunakan "gpt-4" jika Anda memiliki akses
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()

# Fungsi untuk menangani pesan pengguna
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chatgpt_response = await get_chatgpt_response(user_message)
    await update.message.reply_text(chatgpt_response)

# Fungsi untuk memulai bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Saya adalah bot AI Punggawa (not really). saya hanya terhubung dengan ChatGPT. saya dapat menganalisa suatu case berdasarkan inputan yang anda berikan dan memberikan saran serta rekomendasi")

# Main function untuk menjalankan bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Menangani perintah /start
    app.add_handler(CommandHandler("start", start))

    # Menangani pesan teks
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()
