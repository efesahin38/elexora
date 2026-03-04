import os

with open('/Users/efesahin/Desktop/website/elexora-website/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Simple translation mapping for demo/screenshot purposes
translations = {
    'lang="tr"': 'lang="en"',
    'İşletmeniz İçin Dijital Çözümler': 'Digital Solutions for Your Business',
    'İşletmeniz için profesyonel web tasarımı, mobil uygulama, Google Haritalar yönetimi ve İK donanım çözümleri.': 'Professional web design, mobile apps, Google Maps management, and HR hardware solutions for your business.',
    'İşletmenizi geleceğe taşıyacak dijital sistemlerle tanışın.': 'Meet the digital systems that will carry your business into the future.',
    'Bize Ulaşın &rarr;': 'Contact Us &rarr;',
    'Ana Sayfa': 'Home',
    'Hizmetlerimiz': 'Services',
    'Neden Biz?': 'Why Us?',
    'İletişime Geçin': 'Get in Touch',
    'İşletmenizi Büyüten,<br><span>Modern Dijital</span> Çözümler Merkezi': 'The Center of <br><span>Modern Digital</span> Solutions That Grow Your Business',
    'Web sitesinden mobil uygulamaya, personel takibinden itibar yönetimine kadar tüm ihtiyaçlarınız için tek ve güvenilir adresiniz.': 'Your single and reliable address for all your needs from websites to mobile apps, personnel tracking to reputation management.',
    'Hemen Bilgi Alın': 'Get Info Now',
    'Hizmetleri İncele': 'Explore Services',
    'Sektörünün öncü şirketleri dijital dönüşüm için Elexora\'ya güveniyor': 'Industry leaders trust Elexora for digital transformation',
    'Tüm Hizmetlerimiz': 'Our Services',
    'İşinizin her alanında verimliliği ve satışı artıracak çözümler üretiyoruz.': 'We produce solutions that will increase efficiency and sales in every area of your business.',
    'İtibar Yönetimi': 'Reputation Management',
    'Google Haritalar Yönetimi': 'Google Maps Management',
    'Haksız ve kötü niyetli harita yorumlarını siliyor, işletmenizin gerçek kalitesini internete yansıtıyoruz.': 'We delete unfair and malicious map reviews and reflect the true quality of your business to the internet.',
    'Detaylı Bilgi &rarr;': 'Detailed Info &rarr;',
    'Kurumsal Kimlik': 'Corporate Identity',
    'Profesyonel Web Tasarım': 'Professional Web Design',
    'Markanızın vizyonunu yansıtan premium, mobil uyumlu ve hızlı web siteleri tasarlıyoruz.': 'We design premium, mobile-compatible, and fast websites that reflect your brand\'s vision.',
    'Yazılım & Teknoloji': 'Software & Technology',
    'Özel Mobil Uygulama Geliştirme': 'Custom Mobile App Development',
    'Fikrinize özel; iOS ve Android platformları için hızlı, güvenilir ve çarpıcı tasarımlara sahip özel mobil uygulamalar üretiyoruz.': 'We create custom mobile apps for iOS and Android platforms with fast, reliable, and stunning designs tailored to your idea.',
    'İK & Yönetim': 'HR & Management',
    'Personel Takip Sistemi (PDKS)': 'Personnel Tracking System',
    'Çalışan mesailerini, giriş çıkış saatlerini otomatize edin.': 'Automate employee shifts, entry, and exit times.',
    'Operasyon & Yönetim': 'Operation & Management',
    'Online Randevu Sistemi': 'Online Appointment System',
    'Telefon trafiğinden kurtulun. Müşterileriniz 7/24 kendilerine uygun saatte web siteniz veya uygulamanız üzerinden randevu oluştursun.': 'Get rid of phone traffic. Let your customers create appointments 7/24 at their convenience through your website or app.',
    'Büyüme & Reklam': 'Growth & Advertising',
    'Dijital Pazarlama & Reklam': 'Digital Marketing & Advertising',
    'Instagram, Facebook ve Google Ads reklamlarınızı uzman ekibimiz yönetsin.': 'Let our expert team manage your Instagram, Facebook, and Google Ads advertisements.',
    'Bespoke Teknoloji': 'Bespoke Technology',
    'Özel Yazılım & Mail Otomasyonu': 'Custom Software & Mail Automation',
    'Siz probleminizi anlatın, biz ihtiyacınızı tam çözecek otomasyonları': 'Tell us your problem, and we will develop automations that solve your needs perfectly',
    'Neden Elexora?': 'Why Elexora?',
    'Biz sadece bir ajans değil, dijital dünyadaki büyüme ortağınızız.': 'We are not just an agency, we are your growth partner in the digital world.',
    'Sonuç Odaklılık': 'Result Oriented',
    'Uçtan Uca Çözüm': 'End-to-End Solution',
    '7/24 Kesintisiz Destek': '24/7 Continuous Support',
    'Özelleştirilebilir Yapı': 'Customizable Structure',
    'Müşteri Memnuniyeti': 'Customer Satisfaction',
    'Tamamlanan Proje': 'Completed Project',
    'Ortalama Puan Artışı': 'Average Rating Increase',
    'Şeffaf İletişim': 'Transparent Communication',
    'Sıkça Sorulan Sorular': 'Frequently Asked Questions',
    'Aklınızdaki Projeyi Konuşalım': 'Let\'s Talk About Your Project',
    'Modern işletmelerin güvenilir <br>dijital çözüm ortağı.': 'Reliable digital solution partner for modern businesses.',
    'Tüm hakları saklıdır.': 'All rights reserved.'
}

for tr, en in translations.items():
    content = content.replace(tr, en)

with open('/Users/efesahin/Desktop/website/elexora-website/index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created index-en.html")
