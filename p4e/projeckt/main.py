import os
import time
import requests
from dotenv import load_dotenv

# .env dosyasındaki gizli verileri yükle
load_dotenv()

# Değişkenleri sistemden çek
MODEM_IP = os.getenv('MODEM_IP')
MODEM_PASS = os.getenv('MODEM_PASS')
# O2 modemlerde genelde reboot yolu budur, giriş yaptıktan sonra adresi kontrol etmelisin
REBOOT_URL = f"http://{MODEM_IP}/cgi-bin/reboot" 

def internet_var_mi():
    """İnternet bağlantısını Google üzerinden kontrol eder."""
    try:
        # 5 saniye içinde cevap gelmezse internet yok sayılır
        requests.get("https://8.8.8.8", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def modemi_resetle():
    """Modeme giriş yapar ve reset komutu gönderir."""
    print("⚠️ İnternet koptu! Modeme reset emri gönderiliyor...")
    try:
        # Kullanıcı adı boş (''), sadece şifre ile giriş yapıyoruz
        response = requests.post(REBOOT_URL, auth=('', MODEM_PASS), timeout=10)
        
        if response.status_code == 200:
            print("✅ Reset emri başarıyla iletildi.")
        else:
            print(f"❌ Modem hata döndürdü. Durum kodu: {response.status_code}")
            
    except Exception as e:
        print(f"🚨 Modeme ulaşılamadı! Hata: {e}")

# --- ANA DÖNGÜ ---
if __name__ == "__main__":
    print("🚀 İnternet Bekçisi başlatıldı...")
    while True:
        if internet_var_mi():
            print(f"🌐 [{time.strftime('%H:%M:%S')}] İnternet aktif. 5 dakika sonra tekrar bakılacak.")
            time.sleep(300) # 5 dakika bekle
        else:
            modemi_resetle()
            print("⏳ Modemin açılması için 5 dakika bekleniyor (Döngü durduruldu)...")
            time.sleep(300) # Modem kendine gelene kadar bekle