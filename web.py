import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Remove deprecated option
# st.set_option('deprecation.showfileUploaderEncoding', False)


@st.cache(allow_output_mutation=True)
def loading_model():
    fp = "model.h5"
    model_loader = load_model(fp)
    return model_loader


cnn = loading_model()
st.write("""
# Prediksi Penyakit Tuberculosis (X-ray) menggunakan metode Convolutional Neural Network
by 22.11.5285 abisakha
""")

temp = st.file_uploader("Upload X-Ray Image :")

if temp is not None:
    # Load the image directly
    img = Image.open(temp)

    # Display the uploaded image
    st.image(img, use_column_width=True)

    # Preprocessing the image
    img = img.convert('L')  # Convert to grayscale
    img = img.resize((500, 500))  # Resize image to fit model input
    pp_img = image.img_to_array(img)
    pp_img = pp_img / 255  # Normalize the image
    pp_img = np.expand_dims(pp_img, axis=0)  # Add batch dimension

    # Predict
    preds = cnn.predict(pp_img)

    if preds >= 0.5:
        out = ('hasil prediksi sebesar {:.2%} persen teridikasi terkena penyakit  Tuberculosis. silahkan berkonsultasi lebih lanjut dengan dokter'.format(preds[0][0]))
    else:
        out = ('hasil prediksi sebesar {:.2%} persen terindikasi bahwa normal. silahkan berkonsultasi lebih lanjut dengan dokter'.format(1 - preds[0][0]))

    st.success(out)

else:
    st.text("Oops! That doesn't look like an image. Try again.")
