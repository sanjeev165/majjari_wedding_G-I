from PIL import Image, ImageOps 
import qrcode


url = "https://majjariwedding-gi.streamlit.app"
qr = qrcode.make(url)
qr.save("invite_qr.png")
#st.image("invite_qr.png", caption="Scan to view this invitation")