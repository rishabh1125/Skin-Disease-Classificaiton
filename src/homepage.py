import streamlit as st
from streamlit_image_select import image_select
from image_predict import ImageClassification
import pandas as pd
# Set page configuration to widen the Streamlit page
st.set_page_config(layout="wide")

# Create a container to hold the main content
main_container = st.container()

# Use the container to set the width of the content
with main_container:
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container {
            max-width: 80%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Image Classification")

st.write("This is a simple image classification app that uses a pre-trained model to classify images.")

# Image upload
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Sample images
st.write("Or select a sample image:")
sample_images = [
    "data/sample1.jpg", "data/sample2.jpg", 
    "data/sample3.jpg","data/sample4.jpg"]
selected_sample = image_select("Sample images", sample_images)
# Display the selected or uploaded image
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", width=800)

elif selected_sample:
    st.image(selected_sample, caption="Selected Sample Image", width=800)

# Model selection dropdown
models = ["CNN trained", "Finetuned ResNet50"]
selected_model = st.selectbox("Select a model", models)

# Add a submit button for classification
if st.button("Classify Image"):
    if uploaded_image is not None or selected_sample:
        # Placeholder for classification logic
        st.write("Classification in progress...")
        # Here you would add the actual classification code
        # based on the selected model and the image (uploaded or sample)
        
        # Example placeholder result
        st.write(f"Model used: {selected_model}")
        image_predict = ImageClassification()
        # Get the prediction from the image classification
        if uploaded_image is not None:
            prediction = image_predict.classify_image(uploaded_image, selected_model)
        else:
            if selected_sample is None:
                 # Case where no sample is selected and point is at the first sample
                selected_sample = sample_images[0]
            prediction = image_predict.classify_image(selected_sample, selected_model)
        
        # Define class labels (replace with actual labels for your model)
        
        # Display the prediction results
        st.subheader("Classification Results:")
        st.write(f"Predicted disease: {prediction[0][0]}")
        prediction = pd.DataFrame(prediction, columns=['disease', 'confidence'])
        # Visualize the results with a bar chart
        st.bar_chart(prediction, x='disease', y='confidence (in %)')
    else:
        st.warning("Please upload an image or select a sample image before classifying.")
