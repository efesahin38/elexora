import os

new_html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Web Design | Elexora</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        .step-card {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .step-card:hover {
            transform: translateY(-10px);
            background: white !important;
            box-shadow: var(--shadow-hover);
        }
        .faq-item {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
        }
        .faq-item:hover {
            border-color: var(--text-teal);
            box-shadow: var(--shadow-soft);
        }
    </style>
</head>

<body class="letter-spacing-tight">
    <!-- Top Banner -->
    <div class="top-banner">
        <p>Elevate your business with a world-class digital presence. <a href="#contact">Start Your Journey &rarr;</a></p>
    </div>

    <!-- Navigation -->
    <header class="navbar scrolled" id="navbar">
        <div class="container">
            <a href="index.html" class="logo">Elexora</a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="#solutions">Solutions</a>
                <a href="#process">Process</a>
                <a href="#contact">Get Quote</a>
            </nav>
            <div class="nav-actions">
                <a href="#contact" class="nav-link-subtle">Consultation</a>
            </div>
            <div class="mobile-menu-btn"><i class="fas fa-bars"></i></div>
        </div>
    </header>

    <!-- Hero Section (Hyper-Aesthetic) -->
    <section class="hero" style="background: white; padding: 120px 0 160px 0; overflow: visible;">
        <!-- Mesh Gradients and Blobs -->
        <div class="shape-blob glow-teal floating" style="top: -100px; left: -50px; width: 600px; height: 600px;"></div>
        <div class="shape-blob glow-purple floating-delayed" style="bottom: -100px; right: -50px; width: 600px; height: 600px; background: radial-gradient(circle, #f3f0ff 0%, transparent 70%);"></div>
        
        <div class="container" style="position: relative; z-index: 10;">
            <div class="hero-content" style="grid-template-columns: 1.1fr 0.9fr;">
                <div class="hero-text">
                    <span class="tag tag-teal floating">World Class Standard</span>
                    <h1 class="fade-in-up" style="font-size: 4.8rem; line-height: 1.1; margin-bottom: 2rem;">
                        Design for the <br>
                        <span class="text-gradient-teal">Next Generation</span>
                    </h1>
                    <p class="fade-in-up delay-1 line-height-relaxed" style="font-size: 1.4rem; color: #4b5563; max-width: 580px; margin-bottom: 3.5rem;">
                        We don't just build websites. We craft immersive digital experiences that captivate your audience and scale your business globally.
                    </p>
                    <div class="hero-buttons fade-in-up delay-2">
                        <a href="#solutions" class="btn btn-primary btn-large" style="background: var(--text-teal); padding: 1.2rem 2.8rem;">View Our Expertise</a>
                        <a href="#contact" class="btn btn-secondary btn-large" style="padding: 1.2rem 2.8rem; border-width: 2px;">Start a Proposal</a>
                    </div>
                </div>
                
                <div class="hero-graphic fade-in-up delay-3" style="position: relative; height: 550px;">
                    <!-- Glassmorphism Cards -->
                    <div class="glass floating" style="position: absolute; top: 10%; right: 0; width: 320px; padding: 2.5rem; border-radius: 32px; z-index: 5; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                            <div style="width: 48px; height: 48px; background: #e6fafa; border-radius: 14px; display: flex; align-items: center; justify-content: center; color: #00A9A5;">
                                <i class="fas fa-chart-line fa-lg"></i>
                            </div>
                            <div>
                                <h4 style="font-size: 1.1rem; margin: 0;">Growth Driven</h4>
                                <p style="font-size: 0.85rem; color: #6b7280; margin: 0;">Conversion Optimized</p>
                            </div>
                        </div>
                        <div style="height: 12px; background: #f3f4f6; border-radius: 10px; margin-bottom: 12px; width: 90%;"></div>
                        <div style="height: 12px; background: #f3f4f6; border-radius: 10px; width: 60%;"></div>
                    </div>

                    <div class="glass-dark floating-delayed" style="position: absolute; bottom: 5%; left: -10%; width: 280px; padding: 2rem; border-radius: 28px; z-index: 6; color: white;">
                        <h4 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;">99.9%</h4>
                        <p style="font-size: 0.9rem; opacity: 0.8; margin: 0;">System Uptime Guaranteed</p>
                    </div>

                    <!-- Main Device Mockup (Pseudo) -->
                    <div style="position: absolute; top: 15%; left: 10%; width: 90%; height: 75%; background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%); border-radius: 24px; border: 1px solid #e5e7eb; padding: 1.5rem; transform: perspective(1000px) rotateY(-10deg) rotateX(5deg);">
                        <div style="width: 100%; height: 100%; background: white; border-radius: 12px; border: 1px solid #e5e7eb; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                            <i class="fas fa-rocket fa-4x" style="color: var(--text-teal); opacity: 0.2;"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services: Elite Zig-Zag -->
    <section id="solutions" class="services-wrapper" style="padding: 120px 0; background: white; position: relative; z-index: 10;">
        <div class="container">
            <div class="section-title text-center" style="margin-bottom: 100px;">
                <span class="tag tag-purple">Our Craft</span>
                <h2 style="font-size: 3.5rem; margin-top: 1rem;">Solutions for Every Dimension</h2>
            </div>

            <!-- UI/UX Section -->
            <div class="feature-row" style="margin-bottom: 160px;">
                <div class="feature-text pr-5 fade-in-up">
                    <h3 style="font-size: 2.8rem; margin-bottom: 2rem;">Unrivaled <br><span class="text-gradient-teal">Visual Identity</span></h3>
                    <p class="line-height-relaxed" style="font-size: 1.25rem; color: #4b5563;">Your digital identity is established in milliseconds. We design high-fidelity interfaces that don't just look stunning—they communicate authority and professionalism.</p>
                    <ul class="bullet-list mt-5">
                        <li style="margin-bottom: 1.2rem;"><i class="fas fa-check-circle text-teal"></i> <strong>Strategic UI:</strong> Layouts built for clarity.</li>
                        <li style="margin-bottom: 1.2rem;"><i class="fas fa-check-circle text-teal"></i> <strong>Elite UX:</strong> Journeys mapped for simplicity.</li>
                    </ul>
                </div>
                <div class="feature-image fade-in-up delay-1" style="background: none; padding: 0;">
                    <div style="width: 100%; border-radius: 40px; overflow: hidden; box-shadow: 0 40px 100px -20px rgba(0,0,0,0.15); border: 12px solid #f8fafc;">
                        <img src="https://images.unsplash.com/photo-1545235617-9465d2a55698?auto=format&fit=crop&w=1200&q=80" alt="UI Design" style="width: 100%; display: block;">
                    </div>
                </div>
            </div>

            <!-- Global Reach Section (Reverse) -->
            <div class="feature-row reverse" style="margin-bottom: 160px;">
                <div class="feature-text pl-5 fade-in-up">
                    <h3 style="font-size: 2.8rem; margin-bottom: 2rem;">Market Dominance <br><span class="text-gradient-coral">Global Scale</span></h3>
                    <p class="line-height-relaxed" style="font-size: 1.25rem; color: #4b5563;">Why settle for local when you can dominate the <strong>entire world?</strong> We build architectures that scale infinitely, ensuring your brand resonates in every corner of the globe.</p>
                    <ul class="bullet-list mt-5">
                        <li style="margin-bottom: 1.2rem;"><i class="fas fa-globe-americas text-coral"></i> <strong>Infinite Reach:</strong> Break free from geographical limits.</li>
                        <li style="margin-bottom: 1.2rem;"><i class="fas fa-bolt text-coral"></i> <strong>Edge Performance:</strong> Fast everywhere, always.</li>
                    </ul>
                </div>
                <div class="feature-image fade-in-up delay-1" style="background: none; padding: 0;">
                    <div style="width: 100%; border-radius: 40px; overflow: hidden; box-shadow: 0 40px 100px -20px rgba(0,0,0,0.15); border: 12px solid #fff5f5;">
                        <img src="https://images.unsplash.com/photo-1551650975-87deedd944c3?auto=format&fit=crop&w=1200&q=80" alt="Global Reach" style="width: 100%; display: block;">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Design Process Section -->
    <section id="process" style="padding: 120px 0; background: #f9f9f8;">
        <div class="container">
            <div class="section-title text-center" style="margin-bottom: 80px;">
                <span class="tag tag-teal">Methodology</span>
                <h2 style="font-size: 3.5rem;">How We Create Perfection</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem;">
                <div class="step-card fade-in-up" style="background: rgba(255,255,255,0.6); padding: 3.5rem 2.5rem; border-radius: 32px; border: 1px solid #eee;">
                    <div style="font-size: 3.5rem; font-weight: 800; color: rgba(0, 169, 165, 0.1); margin-bottom: 1.5rem;">01</div>
                    <h4 style="font-size: 1.4rem; margin-bottom: 1rem;">Discovery</h4>
                    <p style="color: #6b7280;">Deep dive into your brand goals and competitive landscape.</p>
                </div>
                <div class="step-card fade-in-up delay-1" style="background: rgba(255,255,255,0.6); padding: 3.5rem 2.5rem; border-radius: 32px; border: 1px solid #eee;">
                    <div style="font-size: 3.5rem; font-weight: 800; color: rgba(252, 102, 92, 0.1); margin-bottom: 1.5rem;">02</div>
                    <h4 style="font-size: 1.4rem; margin-bottom: 1rem;">Architecture</h4>
                    <p style="color: #6b7280;">Logic-first blueprinting of high-conversion user journeys.</p>
                </div>
                <div class="step-card fade-in-up delay-2" style="background: rgba(255,255,255,0.6); padding: 3.5rem 2.5rem; border-radius: 32px; border: 1px solid #eee;">
                    <div style="font-size: 3.5rem; font-weight: 800; color: rgba(139, 92, 246, 0.1); margin-bottom: 1.5rem;">03</div>
                    <h4 style="font-size: 1.4rem; margin-bottom: 1rem;">Creation</h4>
                    <p style="color: #6b7280;">Translating code and design into a premium final product.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section (Clean) -->
    <section style="padding: 120px 0; background: white;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 5rem;">
                <div>
                    <span class="tag tag-yellow">Q&A</span>
                    <h2 style="font-size: 3.5rem; margin-top: 1.5rem;">Inquiries</h2>
                    <p style="font-size: 1.2rem; color: #4b5563; margin-top: 1.5rem;">Everything you need to know about starting your digital revolution.</p>
                </div>
                <div>
                    <div class="faq-item fade-in-up">
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">How long does a premium build take?</h4>
                        <p style="color: #6b7280; margin: 0;">Typically 4-8 weeks depending on complexity and scale.</p>
                    </div>
                    <div class="faq-item fade-in-up delay-1">
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Do you handle ongoing maintenance?</h4>
                        <p style="color: #6b7280; margin: 0;">We offer comprehensive success management for all our builds.</p>
                    </div>
                    <div class="faq-item fade-in-up delay-2">
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Will my site be SEO ready?</h4>
                        <p style="color: #6b7280; margin: 0;">Every line of code we write is optimized for maximum visibility.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Bottom CTA (Glassmorphism) -->
    <section id="contact" style="padding: 120px 0; background: #fff;">
        <div class="container">
            <div class="glass fade-in-up" style="background: linear-gradient(135deg, #e6fafa 0%, #f3f0ff 100%); padding: 100px 60px; border-radius: 60px; text-align: center; border: none; overflow: hidden; position: relative;">
                <div class="shape-blob glow-teal floating" style="top: -50px; left: -50px;"></div>
                <div class="shape-blob glow-purple floating-delayed" style="bottom: -50px; right: -50px;"></div>
                
                <h2 style="font-size: 4rem; position: relative; z-index: 5; margin-bottom: 1.5rem;">Ready for the Leap?</h2>
                <p style="font-size: 1.5rem; position: relative; z-index: 5; color: #4b5563; max-width: 700px; margin: 0 auto 3.5rem auto;">Join the ranks of elite businesses redefining their industry. Let's create your masterpiece.</p>
                
                <div class="cta-buttons" style="position: relative; z-index: 5; display: flex; justify-content: center; gap: 2rem;">
                    <a href="https://wa.me/905555555555" target="_blank" class="btn btn-primary btn-large" style="background: #111; color: white; padding: 1.2rem 3rem;">
                        <i class="fab fa-whatsapp"></i> Chat via WhatsApp
                    </a>
                    <a href="mailto:info@elexora.com" class="btn btn-white btn-large" style="padding: 1.2rem 3rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <i class="fas fa-envelope"></i> Send an Inquiry
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer (Deep Dark) -->
    <footer class="site-footer" style="padding: 120px 0 60px 0;">
        <div class="container">
            <div class="footer-grid" style="grid-template-columns: 2fr 1fr 1fr;">
                <div class="footer-brand">
                    <a href="index.html" class="footer-logo" style="font-size: 2.5rem;">Elexora</a>
                    <p style="font-size: 1.1rem; color: #9ca3af; margin-top: 1.5rem;">The engine behind next-generation digital leaders.</p>
                    <div class="social-links mt-5">
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Ecosystem</h4>
                    <ul>
                        <li><a href="harita-yonetimi.html">Maps OS</a></li>
                        <li><a href="web-tasarim.html">Web Engine</a></li>
                        <li><a href="mobil-uygulama.html">Mobile Core</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="#">Global HQ</a></li>
                        <li><a href="mailto:info@elexora.com">Email Us</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom mt-5" style="border-top-color: rgba(255,255,255,0.05); padding-top: 40px;">
                <p>&copy; 2026 Elexora Digital Excellence. All rights reserved.</p>
                <div class="legal-links">
                    <a href="#">Security</a>
                    <a href="#">Privacy</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script>
        // Intersection Observer for FAQ animations
        const faqObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.faq-item').forEach(el => faqObserver.observe(el));
    </script>
</body>

</html>"""

with open('/Users/efesahin/Desktop/website/elexora-website/web-tasarim.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("web-tasarim.html upgraded to Hyper-Aesthetic Premium Redesign.")
