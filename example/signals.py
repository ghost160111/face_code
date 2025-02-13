import os, requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_telegram_message(text: str) -> None:
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML",
        }
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
        except Exception as e:
            print("Ошибка отправки сообщения в Telegram:", e)
    else:
        print("Telegram Bot Token или Chat ID не заданы.")

@receiver(post_save, sender=Contact)
def notify_new_contact(sender, instance, created, **kwargs):
    if created:
        message = (
            "✦ 𝒩𝑜𝒷𝒶я 𝓏𝒶я𝓋ка ✦\n\n"
            f"👤 <b>Имя:</b> {instance.fullname}\n"
            f"📞 <b>Телефон:</b> {instance.phone}\n"
            f"💬 <b>Сообщение:</b>\n{instance.text}\n\n"
            "📩 <i>Свяжитесь с клиентом как можно скорее!</i>"
        )
        send_telegram_message(message)
