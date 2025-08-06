import streamlit as st
from agents import (
    generate_structure,
    write_slide_content,
    generate_speaker_notes,
    generate_image
)
from utils import save_to_pdf
from google_slides import create_presentation, create_slides_from_bullets
from PIL import Image
import os

# Streamlit page setup
st.set_page_config(page_title="Slide Agent", layout="centered")
st.title("AI Slide Generator + Google Slides Export")

# Initialize session state
if "content" not in st.session_state:
    st.session_state.content = ""
if "notes" not in st.session_state:
    st.session_state.notes = ""
if "image_path" not in st.session_state:
    st.session_state.image_path = ""
if "structure" not in st.session_state:
    st.session_state.structure = ""
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "audience" not in st.session_state:
    st.session_state.audience = ""

# Inputs
topic = st.text_input("Enter your topic", value=st.session_state.topic)
audience = st.text_input("Enter your target audience", value=st.session_state.audience)

# Generate slide content
if st.button("Generate Slide Deck"):
    if not topic or not audience:
        st.warning("Please enter both topic and audience.")
    else:
        st.session_state.topic = topic
        st.session_state.audience = audience

        with st.spinner("Generating structure..."):
            st.session_state.structure = generate_structure(topic, audience)

        with st.spinner("Writing slide content..."):
            st.session_state.content = write_slide_content(st.session_state.structure)

        with st.spinner("Generating speaker notes..."):
            st.session_state.notes = generate_speaker_notes(st.session_state.content)

        with st.spinner("Generating image..."):
            st.session_state.image_path = generate_image(topic)

        st.success("Slide deck ready!")

# Show generated content
if st.session_state.content:
    st.subheader("Slide Content")
    st.text_area("Content", st.session_state.content, height=250)

    st.subheader("Speaker Notes")
    st.text_area("Notes", st.session_state.notes, height=200)

    # Show image
    if st.session_state.image_path and os.path.exists(st.session_state.image_path):
        st.image(
            Image.open(st.session_state.image_path),
            caption="AI-generated Image",
            use_container_width=True
        )

    # Export to PDF
    if st.button("Export PDF"):
        save_to_pdf(st.session_state.content, st.session_state.notes)
        st.success("PDF saved to output/presentation.pdf")

    # Export to Google Slides
    if st.button("Export to Google Slides"):
        pres_id, pres_title = create_presentation("Slide Deck: " + st.session_state.topic)
        create_slides_from_bullets(pres_id, st.session_state.content)
        st.success("Uploaded to Google Slides!")
        st.markdown(f"[Open Presentation](https://docs.google.com/presentation/d/{pres_id}/edit)", unsafe_allow_html=True)
