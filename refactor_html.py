import re

with open('/Users/efesahin/Desktop/website/elexora-website/harita-yonetimi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the grid from the before-after-section
grid_match = re.search(r'(<div class="grid"\s*style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(350px, 1fr\)\); gap: 2rem; margin-top: 2rem; text-align: left;">.*?</div>\s*</div>\s*</div>)', content, re.DOTALL)
if not grid_match:
    print("Could not find grid!")
    grid_content = ""
else:
    # Actually, the div class="grid" ends at the second to last </div> before </section>
    # Let's be more precise
    grid_match = re.search(r'(<div class="grid"\s*style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(350px, 1fr\)\); gap: 2rem; margin-top: 2rem; text-align: left;">.*?)\s*</div>\s*</section>', content, re.DOTALL)
    if grid_match:
        grid_content = grid_match.group(1)
    else:
        print("Grid match failed")

# 2. Extract paragraph text
p_text = "Rekabetin yo\u011fun oldu\u011fu g\u00fcn\u00fcm\u00fczde, Google Haritalar'daki birka\u00e7 haks\u0131z veya k\u00f6t\u00fc niyetli (spam) yorum, i\u015fletmenizin prestijini yerle bir edebilir ve potansiyel m\u00fc\u015fterilerinizi rakiplerinize ka\u00e7\u0131rabilir. Elexora olarak, bu haks\u0131zl\u0131\u011fa dur diyoruz."

# 3. Create the new top section
new_top_section = f"""    <section class="services-wrapper" style="padding-top: 80px; padding-bottom: 80px; background-color: var(--bg-pastel-yellow);">
        <div class="container text-center">
            <h2 class="fade-in-up mb-4" style="font-size: 2.5rem; font-weight: 700; color: var(--color-text-main);">Kötü Yorumlara Son Verin.</h2>
            <p class="fade-in-up mx-auto mb-5" style="max-width: 800px; color: var(--color-text-muted); font-size: 1.15rem; line-height: 1.6;">{p_text}</p>
            
{grid_content}
        </div>
    </section>"""

# 4. Replace everything from <section class="services-wrapper"... to the end of <section class="before-after-section"...
# We replace it with new_top_section
pattern = r'<section class="services-wrapper" style="padding-top: 60px;">.*?</section>\s*<section class="before-after-section" style="padding: 5rem 0; background-color: var\(--bg-pastel-yellow\);">.*?</section>'
new_content = re.sub(pattern, new_top_section, content, flags=re.DOTALL)

with open('/Users/efesahin/Desktop/website/elexora-website/harita-yonetimi.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Refactored.")
