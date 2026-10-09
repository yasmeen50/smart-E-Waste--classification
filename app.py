import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

from rag_agent import get_information

model = tf.keras.models.load_model("model/ewaste_model.h5")
labels = np.load("model/labels.npy", allow_pickle=True)

st.title("♻️ Smart E-Waste Classification")

st.write("Upload an e-waste image to identify its category.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        caption="Uploaded Image"
    )

    image = cv2.resize(image, (128, 128))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    predicted_class = labels[np.argmax(prediction)]

    st.success(
        f"Predicted E-Waste Category: {predicted_class}"
    )

    information = get_information(predicted_class)

    st.subheader("📚 E-Waste Information")
    st.write(information)