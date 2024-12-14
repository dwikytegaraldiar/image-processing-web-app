import streamlit as st
import cv2
import numpy as np
from PIL import Image

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
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Konversi RGB ke BGR (OpenCV)

        # Menampilkan gambar asli
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Gambar Asli", use_column_width=True)

        st.subheader("Pilih Operasi Image Processing")

        # Pilih operasi yang ingin diterapkan pada gambar
        operation = st.selectbox("Pilih operasi:", ["Rotate", "Scale", "Translate", "Skew"])

        if operation == "Rotate":
            angle = st.slider("Pilih sudut rotasi:", min_value=0, max_value=360, value=90)
            rotated_image = rotate_image(img, angle)
            st.image(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB), caption=f"Rotasi {angle} Derajat", use_column_width=True)

        elif operation == "Scale":
            scale_factor = st.slider("Pilih faktor skala:", min_value=0.1, max_value=3.0, value=1.0)
            scaled_image = scale_image(img, scale_factor)
            st.image(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB), caption=f"Skala {scale_factor}x", use_column_width=True)

        elif operation == "Translate":
            x_translation = st.slider("Pilih pergeseran horizontal:", min_value=-100, max_value=100, value=0)
            y_translation = st.slider("Pilih pergeseran vertikal:", min_value=-100, max_value=100, value=0)
            translated_image = translate_image(img, x_translation, y_translation)
            st.image(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB), caption="Pergeseran Gambar", use_column_width=True)

        elif operation == "Skew":
            skew_x = st.slider("Pilih skew horizontal:", min_value=-50, max_value=50, value=0)
            skew_y = st.slider("Pilih skew vertikal:", min_value=-50, max_value=50, value=0)
            skewed_image = skew_image(img, skew_x, skew_y)
            st.image(cv2.cvtColor(skewed_image, cv2.COLOR_BGR2RGB), caption="Skew Gambar", use_column_width=True)

# Fungsi untuk rotasi gambar
def rotate_image(img, angle):
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    return rotated

# Fungsi untuk skala gambar
def scale_image(img, factor):
    rows, cols = img.shape[:2]
    new_dim = (int(cols * factor), int(rows * factor))
    scaled = cv2.resize(img, new_dim)
    return scaled

# Fungsi untuk mentranslasikan gambar
def translate_image(img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return translated

# Fungsi untuk skew gambar
def skew_image(img, skew_x, skew_y):
    M = np.float32([[1, skew_x / 100, 0], [skew_y / 100, 1, 0]])
    skewed = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return skewed

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