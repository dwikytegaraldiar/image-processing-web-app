import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import io

# Fungsi untuk menampilkan halaman pertama (Tentang Anggota Kelompok)
def page_about():
    st.title("Group 1-Linear Algebra Class 2")
    st.subheader("Nama Anggota:")
    st.write("1. Abigail")
    st.write("2. Dwiky Tegar Aldiar as Developer")
    st.write("3. Kharisma")
    st.write("4. Tugiman")

# Fungsi untuk menampilkan halaman kedua (Aplikasi Image Processing)
def page_image_processing():
    st.title("Aplikasi Image Processing")

    st.subheader("Pilih Gambar")
    uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Membaca gambar yang diunggah
        img = Image.open(uploaded_file)
        img = np.array(img)  # Convert to numpy array untuk diproses lebih lanjut

        # Menampilkan gambar asli
        st.image(img, caption="Gambar Asli", use_container_width=True)

        st.subheader("Pilih Operasi Image Processing")

        # Pilih operasi yang ingin diterapkan pada gambar
        operation = st.selectbox("Pilih operasi:", ["Rotate", "Scale", "Translate", "Skew"])

        processed_image = None  # Variabel untuk menyimpan gambar yang diproses

        if operation == "Rotate":
            angle = st.slider("Pilih sudut rotasi:", min_value=0, max_value=360, value=90)
            processed_image = rotate_image(img, angle)
            st.image(processed_image, caption=f"Rotasi {angle} Derajat", use_container_width=True)
        
        elif operation == "Scale":
            scale_factor = st.slider("Pilih faktor skala:", min_value=0.1, max_value=3.0, value=1.0)
            processed_image = scale_image(img, scale_factor)
            st.image(processed_image, caption=f"Skala {scale_factor}x", use_container_width=True)
        
        elif operation == "Translate":
            x_translation = st.slider("Pilih pergeseran horizontal:", min_value=-100, max_value=100, value=0)
            y_translation = st.slider("Pilih pergeseran vertikal:", min_value=-100, max_value=100, value=0)
            processed_image = translate_image(img, x_translation, y_translation)
            st.image(processed_image, caption="Pergeseran Gambar", use_container_width=True)
        
        elif operation == "Skew":
            skew_x = st.slider("Pilih skew horizontal:", min_value=-50, max_value=50, value=0)
            skew_y = st.slider("Pilih skew vertikal:", min_value=-50, max_value=50, value=0)
            processed_image = skew_image(img, skew_x, skew_y)
            st.image(processed_image, caption="Skew Gambar", use_container_width=True)

        # Fitur Download Gambar
        if processed_image is not None:
            # Download sebagai JPG
            download_jpg = image_to_bytes(processed_image, "JPEG")
            st.download_button("Download JPG", download_jpg, file_name="processed_image.jpg", mime="image/jpeg")

            # Download sebagai PNG
            download_png = image_to_bytes(processed_image, "PNG")
            st.download_button("Download PNG", download_png, file_name="processed_image.png", mime="image/png")

            # Download sebagai PDF
            download_pdf = image_to_pdf(processed_image)
            st.download_button("Download PDF", download_pdf, file_name="processed_image.pdf", mime="application/pdf")

# Fungsi untuk konversi gambar menjadi byte stream untuk diunduh
def image_to_bytes(img, format="PNG"):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    img_byte_arr = io.BytesIO()
    pil_img.save(img_byte_arr, format=format)
    img_byte_arr.seek(0)
    return img_byte_arr.read()

# Fungsi untuk konversi gambar menjadi PDF
def image_to_pdf(img):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    pdf_byte_arr = io.BytesIO()
    pil_img.save(pdf_byte_arr, format="PDF")
    pdf_byte_arr.seek(0)
    return pdf_byte_arr.read()

# Fungsi untuk rotasi gambar
def rotate_image(img, angle):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    rotated = pil_img.rotate(angle)
    return np.array(rotated)

# Fungsi untuk skala gambar
def scale_image(img, factor):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    width, height = pil_img.size
    new_dim = (int(width * factor), int(height * factor))
    scaled = pil_img.resize(new_dim)
    return np.array(scaled)

# Fungsi untuk mentranslasikan gambar
def translate_image(img, x, y):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    translated = ImageOps.offset(pil_img, x, y)
    return np.array(translated)

# Fungsi untuk skew gambar
def skew_image(img, skew_x, skew_y):
    pil_img = Image.fromarray(img)  # Convert numpy array to PIL Image
    width, height = pil_img.size
    skewed = pil_img.transform(
        (width, height), 
        Image.AFFINE, 
        (1, skew_x / 100.0, 0, skew_y / 100.0, 1, 0)
    )
    return np.array(skewed)

# Menentukan halaman mana yang akan ditampilkan
def main():
    st.sidebar.title("Menu")
    menu = ["Tentang Anggota", "Image Processing"]
    choice = st.sidebar.radio("Pilih Menu", menu)

    if choice == "Tentang Anggota":
        page_about()
    elif choice == "Image Processing":
        page_image_processing()

if __name__ == "__main__":
    main()
