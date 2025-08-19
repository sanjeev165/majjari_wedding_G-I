# streamlit_wedding_app.py
# High-end wedding website built with Streamlit
# To run: pip install streamlit pillow pandas
# Then: streamlit run streamlit_wedding_app.py

import streamlit as st
from PIL import Image, ImageOps
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components

import streamlit.components.v1 as components

components.html("""
<div id="overlay"></div>
<style>
#overlay {
  position: fixed;
  pointer-events: none;
  inset: 0;
  z-index: 9999;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: transparent;
}
.flower {
  position: absolute;
  top: -50px;
  animation: fall linear forwards;
}
@keyframes fall {
  to {
    transform: translateY(110vh) rotate(360deg);
  }
}
</style>
<script>
const overlay = document.getElementById("overlay");
const flowerEmojis = ["🌸", "🌼", "💐", "🌺",];
function spawnFlowers(batchSize) {
    for (let i = 0; i < batchSize; i++) {
        let flower = document.createElement("div");
        flower.className = "flower";
        flower.style.left = Math.random() * 100 + "vw";
        flower.style.fontSize = Math.random() * 24 + 20 + "px";
        flower.style.animationDuration = (Math.random() * 3 + 4) + "s";
        // Randomly select a flower emoji
        flower.innerText = flowerEmojis[Math.floor(Math.random() * flowerEmojis.length)];
        overlay.appendChild(flower);
        setTimeout(() => { flower.remove(); }, 7000);
    }
}
// Spawn a batch of flowers every 2 seconds
setInterval(() => {
    spawnFlowers(5); // 5 flowers per batch
}, 2000);
</script>
""", height=200)


# --- Page config ---
# st.set_page_config(
#     page_title="G&I — Our Wedding",
#     page_icon="assets/logo.png" if os.path.exists("assets/log1.png") else "💍",
#     layout="centered",
#     initial_sidebar_state="auto",
# )

# --- Helpers ---
DATA_DIR = "data"
ASSETS_DIR = "assets"


os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# load image safely
def load_image(path, fallback_shape=(1600, 600), make_round=False):
    if os.path.exists(path):
        img = Image.open(path)
        if make_round:
            size = min(img.size)
            img = ImageOps.fit(img, (size, size))
            mask = Image.new("L", (size, size), 0)
            draw = Image.Draw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
            img.putalpha(mask)
        return img
    else:
        # return a blank placeholder image
        return Image.new("RGB", fallback_shape, color=(245, 245, 245))


# --- Stylish CSS ---st.markdown
# This CSS creates a high-end feel: custom font, glass cards, centered hero text.
HERO_CSS = HERO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');

:root{
  --accent:#a27b5c;
  --muted:#5b5b5b;
}

[data-testid="stAppViewContainer"] {
  background: linear-gradient(180deg, #fffdfa 0%, #f7f5f2 100%);
}

.hero {
  position: relative;
  width: 100%;
  height: 480px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  margin-bottom: 24px;
}
.hero::after{
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0.02) 60%);
}
.hero-content{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  text-align: center;
  color: white;
  font-family: 'Playfair Display', serif;
}
.hero h1{
  font-size: 48px;
  margin: 0 0 6px;
  letter-spacing: 1px;
}
.hero p{
  margin: 0;
  font-size: 18px;
  opacity: 0.95;
}

/* Responsive styles for mobile */
@media (max-width: 600px) {
  .hero {
    height: 260px;
    border-radius: 10px;
  }
  .hero h1 {
    font-size: 28px;
    padding: 0 10px;
  }
  .hero p {
    font-size: 14px;
    padding: 0 10px;
  }
  .hero-content {
    width: 90%;
  }
}

.card {
  background: rgba(255,255,255,0.75);
  backdrop-filter: blur(6px);
  border-radius: 14px;
  padding: 18px;
  box-shadow: 0 6px 28px rgba(16,24,40,0.06);
}

.section-title{
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  margin-bottom: 8px;
  color: var(--muted);
}

.small-muted{
  color: #7b7b7b;
  font-size: 14px;
}

.logo {
  height: 56px;
}

.rsvp-btn{
  background: linear-gradient(90deg, var(--accent), #d2b08a);
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  text-decoration: none;
}

</style>
"""

st.markdown(HERO_CSS, unsafe_allow_html=True)

# st.markdown(
#     """
#     <div class="hero">
#         <img src="https://yourdomain.com/banner.jpg" 
#              style="width:100%; height:100%; object-fit: cover;">
#         <div class="hero-content">
#             <h1>Majjari Wedding Celebrations</h1>
#             <p>Join us for a journey of love and togetherness</p>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # --- Header with logo and names ---
# logo_path = os.path.join(ASSETS_DIR, "logo2.png")
# if os.path.exists(logo_path):
#     logo = Image.open(logo_path)
#     st.image(logo, width=96)
# else:
#     st.markdown("<h3 style='font-family: Playfair Display, serif; m33argin:0;'>G & I</h3>", unsafe_allow_html=True)

# Small tagline
#st.markdown("<div class='small-muted'>We invite you to celebrate our wedding</div>", unsafe_allow_html=True)
st.write("---")

# --- Hero / Banner ---
banner_path = os.path.join(ASSETS_DIR, "banner.png")
# If user provided a banner.jpg in assets, it will be used as a background.
# We render a full-width hero with overlaying text using HTML/CSS.

banner_url = f"{banner_path}" if os.path.exists(banner_path) else ""


    # Streamlit won't allow local file url in CSS background reliably in all deploys.
    # So we render the image and then overlay text using an absolute positioned div.
if os.path.exists(banner_path):
    banner_img = Image.open(banner_path)
    st.image(banner_img, use_container_width=True)
    st.markdown(
        """
        <div style='text-align:center; margin-top:-200px; color:white; font-family: "Playfair Display", serif;'>
            <h1 style='font-size:48px;'>Gnana Sanjeev Weds Indrani</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # fallback: simple image with overlaid text using columns
    st.image(load_image(banner_path), use_container_width=True)
    st.markdown("<div style='text-align:center; margin-top:-160px; color:#111;'><h1 style='font-family: Playfair Display, serif; color:#111;'>Gnana Sanjeev Majjari & Indrani </h1><p style='color:#333;'>Oct 02, 2025 · Villa dei Fiori · Tuscany, Italy</p></div>", unsafe_allow_html=True)

# --- Main content ---
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='section-title'>Our Story</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <p style='font-family: Inter, sans-serif; font-size:16px; color:#333;'>
            We met on a rainy afternoon in Florence and instantly knew we were each other's home. After adventures through mountains and city streets, we invite you to join us as we say "I do" surrounded by family and friends.
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>Event Details</div>", unsafe_allow_html=True)
        st.write("**Ceremony** — 4:00 PM, Garden Terrace")
        st.write("**Reception** — 6:30 PM, Grand Hall")
        st.write("**Dress code** — Black tie optional")

    with col2:
        st.markdown("<div class='section-title'>Quick Info</div>", unsafe_allow_html=True)
        st.markdown("- Venue: Villa dei Fiori\n- Address: Via delle Rose 12, Tuscany\n- Accommodation: See the Travel & Stay tab")
        st.markdown("<br>", unsafe_allow_html=True)
        # RSVP shortcut
        if st.button("RSVP — Let us know"):
            st.switch_page("pages/forms.py")
            st.markdown("<script>window.location.href='#rsvp-section'</script>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.write("\n")

# --- Gallery ---
st.markdown("<div style='display:flex; align-items:center; justify-content:space-between;'><h3 style='margin:0; font-family: Playfair Display, serif;'>Gallery</h3><div class='small-muted'>A few moments we love</div></div>", unsafe_allow_html=True)

gallery_cols = st.columns(3)
sample_images = [
    os.path.join(ASSETS_DIR, f) for f in ["log1.png", "logo2.png", "log3.png", "log4.png",]
]

for i, path in enumerate(sample_images):
    col = gallery_cols[i % 3]
    if os.path.exists(path):
        col.image(load_image(path), use_container_width =True)
    else:
        col.write("(Add image to assets/)")

st.write("---")
RSVP_FILE = os.path.join(DATA_DIR, "rsvps.csv")
# Show a small admin view (only visible locally)
if st.checkbox("Show RSVPs (admin)"):
    df = pd.read_csv(RSVP_FILE)
    st.dataframe(df.sort_values("timestamp", ascending=False))

st.write("---")

# --- Travel & Stay ---
st.markdown("<h3 style='font-family: Playfair Display, serif;'>Travel & Stay</h3>", unsafe_allow_html=True)
st.markdown(
    """
    - Nearest airport: KADAPA (CDP). Shuttle service will be provided from the airport to the venue.
    - Nearest Railway station: Yerraguntla (YA).
    - Nearest Town: Proddutor 
    - Contact our travel coordinator: 9652101998
    """
)

#st.write("---")

# --- Registry ---
# #
st.write("---")

# --- Contact / Footer ---
st.markdown("<h4 style='font-family: Playfair Display, serif;'>Contact</h4>", unsafe_allow_html=True)
st.markdown("If you have questions, email us at hello@wedding-email.example")

st.markdown("<div style='text-align:center; margin-top:30px; color:#7b7b7b;'>Designed with ❤️ · Please replace placeholder assets in the assets/ folder.</div>", unsafe_allow_html=True)

# --- End of app ---

# Optional: Add couple photo
# st.image("your_photo.jpg", width=400)

# Optional: Map location (if you want)
# st.map(latitude, longitude)

# Generate and show QR code
# url = "https://your-streamlit-app.streamlit.app"
# qr = qrcode.make(url)
# qr.save("invite_qr.png")
# st.image("invite_qr.png", caption="Scan to view this invitation")

# st.markdown("---")
# st.markdown("We can't wait to celebrate with you! 🎉")
