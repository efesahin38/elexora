import os

new_html = """<!DOCTYPE html>
<html lang="tr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profesyonel Web Tasarım | Elexora</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <!-- Top Banner -->
    <div class="top-banner">
        <p>İşletmenizi dijitale taşımak için güçlü bir adım atın. <a href="#contact">Hemen Başlayın &rarr;</a></p>
    </div>

    <!-- Navigation -->
    <header class="navbar scrolled" id="navbar">
        <div class="container">
            <a href="index.html" class="logo">Elexora</a>
            <nav class="nav-links">
                <a href="index.html">Ana Sayfa</a>
                <a href="#cozumler">Çözümlerimiz</a>
                <a href="#avantajlar">İşinize Ne Katar?</a>
            </nav>
            <div class="nav-actions">
                <a href="#contact" class="nav-link-subtle">İletişim</a>
            </div>
            <div class="mobile-menu-btn"><i class="fas fa-bars"></i></div>
        </div>
    </header>

    <!-- Page Header (HiBob Style) -->
    <section class="hero bg-pastel-teal" style="padding: 80px 0 100px 0; min-height: auto; position: relative; overflow: hidden;">
        <div class="hero-bg-accent" style="background: radial-gradient(circle, #ccfbf1 0%, transparent 70%);"></div>
        <div class="container text-center" style="position: relative; z-index: 2;">
            <h1 class="fade-in-up" style="font-size: 4rem; letter-spacing: -1.5px; margin-bottom: 1.5rem; color: var(--color-text-main);">
                Profesyonel <span style="color: var(--text-teal);">Web Tasarım</span>
            </h1>
            <p class="fade-in-up delay-1" style="font-size: 1.25rem; color: var(--color-text-muted); max-width: 650px; margin: 0 auto 3rem auto; line-height: 1.6;">
                Sizi ve markanızı anlayan, müşterilerde güven uyandıran ve satışlarınızı doğrudan artıran premium kurumsal web siteleri inşa ediyoruz.
            </p>
            <div class="fade-in-up delay-2" style="display: flex; justify-content: center; gap: 1rem;">
                <a href="#cozumler" class="btn btn-primary" style="background-color: var(--text-teal);">Alt Yapıyı Keşfet</a>
            </div>
        </div>
    </section>

    <!-- Content: Zig Zag Services -->
    <section id="cozumler" class="services-wrapper" style="padding-top: 100px; padding-bottom: 80px; background-color: white;">
        <div class="container">
            
            <!-- Row 1: UI/UX Design -->
            <div class="feature-row">
                <div class="feature-text pr-5 fade-in-up">
                    <span class="tag tag-teal">Modern & Premium</span>
                    <h3>Dijital Vitrininiz Sizin Kimliğinizdir.</h3>
                    <p>Web siteniz artık sadece bir internet adresi değil, işletmenizin dünyaya açılan en önemli kapısıdır. Müşterileriniz sizi ilk olarak orada görür ve <strong>ilk izlenim her şeydir.</strong></p>
                    <ul class="bullet-list mt-4">
                        <li><i class="fas fa-check text-teal"></i> <strong>Marka Değeri:</strong> Ziyaretçilerinize anında kurumsal ve güvenilir bir imaj çizin.</li>
                        <li><i class="fas fa-check text-teal"></i> <strong>Kullanıcı Deneyimi (UX):</strong> Müşterilerinizin aradığını saniyeler içinde bulmasını sağlayan akıllı mimari.</li>
                        <li><i class="fas fa-check text-teal"></i> <strong>Dönüşüm Odaklı:</strong> Ziyaretçileri müşteriye dönüştürmek için özel tasarlanmış yönlendirmeler.</li>
                    </ul>
                </div>
                <div class="feature-image bg-pastel-teal fade-in-up delay-1" style="padding: 0; overflow: hidden; position: relative;">
                    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80" alt="Web Design Workspace" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px;">
                    <div style="position: absolute; bottom: 20px; right: 20px; background: white; padding: 1rem 1.5rem; border-radius: 12px; box-shadow: var(--shadow-hover); font-weight: 600; display: flex; align-items: center; gap: 10px;">
                        <i class="fas fa-paint-brush text-teal"></i> Premium UI / UX
                    </div>
                </div>
            </div>

            <!-- Row 2: Mobile Responsive (Reverse) -->
            <div class="feature-row reverse" style="margin-top: 100px;">
                <div class="feature-text pl-5 fade-in-up">
                    <span class="tag tag-coral">Kusursuz Uyumluluk</span>
                    <h3>Telefonda, Tablette, Bilgisayarda... Her Yerde Mükemmel.</h3>
                    <p>Bugün internet trafiğinin %80'inden fazlası mobil cihazlardan geliyor. Eğer web siteniz telefonda bozuk görünüyorsa, her 10 müşterinizden 8'ini baştan kaybediyorsunuz demektir.</p>
                    <ul class="bullet-list mt-4">
                        <li><i class="fas fa-mobile-alt text-coral"></i> <strong>%100 Mobil Uyum (Responsive):</strong> Tüm ekran boyutlarına otomatik adapte olan esnek tasarım.</li>
                        <li><i class="fas fa-tachometer-alt text-coral"></i> <strong>Işık Hızında Yükleme:</strong> Müşterilerinizin sitenin açılmasını beklerken sıkılıp çıkmasına son.</li>
                        <li><i class="fas fa-fingerprint text-coral"></i> <strong>Dokunmatik Dostu:</strong> Telefondan kolayca tıklanabilen büyük butonlar ve rahat menüler.</li>
                    </ul>
                </div>
                <div class="feature-image bg-pastel-coral fade-in-up delay-1" style="padding: 0; overflow: hidden; position: relative;">
                    <img src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=1200&q=80" alt="Mobile Responsive Design" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px;">
                    <div style="position: absolute; top: 20px; left: 20px; background: white; padding: 1rem 1.5rem; border-radius: 12px; box-shadow: var(--shadow-hover); font-weight: 600; display: flex; align-items: center; gap: 10px;">
                        <i class="fas fa-mobile text-coral"></i> Mobil Öncelikli Kodlama
                    </div>
                </div>
            </div>

            <!-- Row 3: SEO Optimization -->
            <div class="feature-row" style="margin-top: 100px; margin-bottom: 0;">
                <div class="feature-text pr-5 fade-in-up">
                    <span class="tag tag-yellow">Google Dostu</span>
                    <h3>Arama Sonuçlarında İlk Sırada Yer Alın.</h3>
                    <p>Dünyanın en güzel web sitesine sahip olabilirsiniz, ancak Google'da bulunamıyorsa hiçbir anlamı yoktur. Sitenizi en alt yapıdan itibaren SEO (Arama Motoru Optimizasyonu) kurallarına göre inşa ediyoruz.</p>
                    <ul class="bullet-list mt-4">
                        <li><i class="fas fa-search text-yellow"></i> <strong>Temiz Kod Yapısı:</strong> Google botlarının sitenizi kolayca okuyup indekslemesi için optimize edilmiş altyapı.</li>
                        <li><i class="fas fa-chart-line text-yellow"></i> <strong>Rakip Analizi:</strong> Sektörünüzdeki anahtar kelimelere özel içerik mimarisi.</li>
                        <li><i class="fas fa-shield-alt text-yellow"></i> <strong>SSL ve Güvenlik:</strong> Google'ın güvenli site algoritmasına tam uyumluluk sağlayan sertifikalar.</li>
                    </ul>
                </div>
                <div class="feature-image bg-pastel-yellow fade-in-up delay-1" style="padding: 0; overflow: hidden; position: relative;">
                    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80" alt="SEO and Analytics" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px;">
                    <div style="position: absolute; bottom: 20px; left: 20px; background: white; padding: 1rem 1.5rem; border-radius: 12px; box-shadow: var(--shadow-hover); font-weight: 600; display: flex; align-items: center; gap: 10px;">
                        <i class="fas fa-rocket text-yellow"></i> Yüksek SEO Skoru
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Testimonial Block -->
    <section style="padding: 60px 0; background-color: var(--bg-pastel-purple);">
        <div class="container text-center max-w-3xl mx-auto" style="max-width: 800px;">
            <i class="fas fa-quote-left" style="font-size: 3rem; color: var(--text-purple); opacity: 0.3; margin-bottom: 1rem;"></i>
            <p class="fade-in-up" style="font-size: 1.5rem; font-weight: 500; font-style: italic; color: var(--color-text-main); line-height: 1.6;">
                "Eski sitemiz çok yavaştı ve mobilde düzgün görünmüyordu. Elexora baştan sona harika bir kurumsal site hazırladı. Sadece tasarımla kalmayıp müşteri dönüşüm oranlarımız da %40 arttı."
            </p>
            <div class="fade-in-up delay-1 mt-4">
                <p style="font-weight: 700; font-size: 1.1rem; margin: 0;">Cemal V.</p>
                <p style="color: var(--color-text-muted); font-size: 0.9rem;">İnşaat Firması Sahibi</p>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section id="avantajlar" class="benefits-section" style="padding: 5rem 0; background-color: var(--color-bg-light);">
        <div class="container">
            <div class="section-title text-center fade-in-up">
                <h2>Özel Web Tasarım İşinize Ne Katar?</h2>
                <p>Hazır şablonların aksine, markanıza özel kodlanmış bir sitenin avantajları.</p>
            </div>
            <div class="grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <!-- Benefit 1 -->
                <div class="why-card fade-in-up" style="background: white; border-radius: 16px; box-shadow: var(--shadow-soft); text-align: center; padding: 2.5rem 1.5rem;">
                    <i class="fas fa-briefcase text-teal" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
                    <h4 style="font-family: var(--font-heading); margin-bottom: 0.5rem; font-size: 1.2rem;">Kurumsal Prestij</h4>
                    <p style="color: var(--color-text-muted); font-size: 0.95rem; margin: 0;">Müşterilerinizin gözünde "işini ciddiye alan, kurumsal ve güvenilir" bir marka imajı yaratırsınız.</p>
                </div>
                <!-- Benefit 2 -->
                <div class="why-card fade-in-up delay-1" style="background: white; border-radius: 16px; box-shadow: var(--shadow-soft); text-align: center; padding: 2.5rem 1.5rem;">
                    <i class="fas fa-chart-pie text-coral" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
                    <h4 style="font-family: var(--font-heading); margin-bottom: 0.5rem; font-size: 1.2rem;">Artan Satışlar</h4>
                    <p style="color: var(--color-text-muted); font-size: 0.95rem; margin: 0;">Doğru yönlendirmeler (CTA) sayesinde siteye giren kullanıcıların size ulaşma veya satın alma oranı yükselir.</p>
                </div>
                <!-- Benefit 3 -->
                <div class="why-card fade-in-up delay-2" style="background: white; border-radius: 16px; box-shadow: var(--shadow-soft); text-align: center; padding: 2.5rem 1.5rem;">
                    <i class="fas fa-globe text-purple" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
                    <h4 style="font-family: var(--font-heading); margin-bottom: 0.5rem; font-size: 1.2rem;">Sınırları Kaldırın</h4>
                    <p style="color: var(--color-text-muted); font-size: 0.95rem; margin: 0;">Sadece bulunduğunuz mahalleye değil, tüm Türkiye'ye ve hatta dünyaya hizmet/ürün sunma imkanı yakalarsınız.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="bottom-cta" style="padding-top: 50px;">
        <div class="container text-center px-4">
            <div class="cta-inner fade-in-up" style="background-color: var(--bg-pastel-teal);">
                <h2>Dijital Vitrininizi Birlikte İnşa Edelim</h2>
                <p>Rakiplerinizin gerisinde kalmayın. Modern, şık ve hızlı bir web sitesiyle sektöre öncülük edin. Ücretsiz analiz ve fiyatlandırma için hemen bize ulaşın.</p>
                <div class="cta-buttons">
                    <a href="https://wa.me/905555555555" target="_blank" class="btn btn-primary btn-large" style="background-color: var(--text-teal);">
                        <i class="fab fa-whatsapp"></i> WhatsApp'tan Fiyat Alın
                    </a>
                    <a href="mailto:info@elexora.com" class="btn btn-secondary btn-large" style="background: white; color: var(--color-text-main);">
                        <i class="fas fa-envelope"></i> E-Posta Gönderin
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer bg-dark text-white pt-5">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="index.html" class="footer-logo">Elexora</a>
                    <p class="mt-3 text-muted">İşletmenizi dijital dünyada büyütmek için gereken tüm yenilikçi çözümler tek bir çatı altında.</p>
                    <div class="social-links mt-4">
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Hizmetlerimiz</h4>
                    <ul>
                        <li><a href="harita-yonetimi.html">Google Harita Yönetimi</a></li>
                        <li><a href="web-tasarim.html">Profesyonel Web Tasarım</a></li>
                        <li><a href="mobil-uygulama.html">Mobil Uygulama</a></li>
                        <li><a href="personel-takip.html">Personel Takip (PDKS)</a></li>
                        <li><a href="randevu-sistemi.html">Online Randevu Sistemi</a></li>
                        <li><a href="dijital-pazarlama.html">Dijital Pazarlama & Reklam</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>İletişim</h4>
                    <ul>
                        <li><a href="tel:+905555555555">+90 (555) 555 55 55</a></li>
                        <li><a href="mailto:info@elexora.com">info@elexora.com</a></li>
                        <li>Türkiye & Global Hizmet Ağı</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Elexora Dijital Çözümler. Tüm hakları saklıdır.</p>
                <div class="legal-links">
                    <a href="#">Gizlilik Politikası</a>
                    <a href="#">Kullanım Şartları</a>
                </div>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>

</html>"""

with open('/Users/efesahin/Desktop/website/elexora-website/web-tasarim.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("web-tasarim.html rebuilt successfully.")
