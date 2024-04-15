import streamlit as st
import pyperclip


from modules.generate import generate_image

st.set_page_config(page_title="DALL-E Image Generator", layout="wide")
st.title("DALL-E Image Generator")

# Split the screen into two columns
col1, col2 = st.columns(2)

with col1:
    # Text area for prompt input
    prompt = st.text_area("Prompt", value="A beautiful sunset over the ocean", height=200)
    model = st.selectbox("Model", ["dall-e-2", "dall-e-3"], index=1)
    quality = st.selectbox("Quality", ["standard", "hd"], index=0)
    size = st.selectbox(
        "Size", ["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"], index=2)
    style = st.selectbox("Style", ["vivid", "natural"], index=0)

    # Generate button
    if st.button("Generate Image"):
        if prompt:
            image_url = generate_image(
                input_prompt=prompt,
                model_name=model,
                output_quality=quality,
                image_size=size,
                image_style=style
            )
            st.session_state.image_url = image_url
        else:
            st.warning("Please enter a prompt.")

with col2:
    if "image_url" in st.session_state:
        image_url = st.session_state.image_url
        st.image(image_url, use_column_width=True)

        # Copy link button
        st.code(image_url)
        if st.button("Copy Link"):
            pyperclip.copy(image_url)

        # Download button
        if st.button("Download Image"):
            st.markdown(
                f'<a href="{image_url}" download>Click here to download</a>', unsafe_allow_html=True)
    else:
        st.info("Enter a prompt and click 'Generate Image' to see the result.")
