# Beyoğlu Lostra — Web Sitesi

Bakırköy'de bulunan **Beyoğlu Lostra** ayakkabı, çanta, valiz ve kemer tamir dükkanı için geliştirilmiş, FastAPI tabanlı, modern ve responsive (mobil uyumlu) bir web uygulamasıdır.

## 🚀 Özellikler
- **FastAPI Altyapısı**: Hızlı, hafif ve güvenli Python backend.
- **Modern Tasarım**: Koyu renk tonları, altın (gold) detaylar ve akıcı geçiş efektleri ile premium tasarım.
- **Tam Mobil Uyum (Responsive)**: Telefon, tablet ve bilgisayarlarla tam uyumlu arayüz.
- **WhatsApp Fiyat Hattı**: Müşterilerin tamir ettirmek istediği ürünlerin fotoğraflarını çekip doğrudan WhatsApp üzerinden fiyat almalarını kolaylaştıran adım adım yönlendirme.
- **Google Maps Entegrasyonu**: Dükkan konumu harita olarak eklenmiştir ve müşterilerin tek tıkla yol tarifi almasını sağlar.
- **Bakım Rehberi**: Deri, süet ve nubuk ürünlerin bakımı hakkında faydalı bilgiler.

## 🛠️ Kurulum ve Çalıştırma

Local bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Python Kurulumu
Bilgisayarınızda Python 3.8 veya üzeri bir sürümün kurulu olduğundan emin olun.

### 2. Bağımlılıkları Yükleme
Terminal veya komut satırını açıp proje klasörüne gidin ve gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Başlatma
Sunucuyu başlatmak için şu komutu çalıştırın:
```bash
python main.py
```

Uygulama başladıktan sonra tarayıcınızdan aşağıdaki adrese girerek siteyi görüntüleyebilirsiniz:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 📁 Proje Klasör Yapısı
```
beyoglu-lostra/
├── main.py              # FastAPI sunucu kodları
├── requirements.txt     # Python kütüphaneleri listesi
├── README.md            # Kurulum kılavuzu (Bu dosya)
├── templates/
│   └── index.html       # Web sitesi HTML şablonu
└── static/
    ├── css/
    │   └── style.css    # Stil (CSS) dosyası
    └── js/
        └── main.js      # JavaScript dosyası (Animasyonlar ve işlevler)
```
