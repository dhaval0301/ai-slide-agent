import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_structure(topic, audience):
    prompt = f"""
    You are a presentation strategist. Generate a slide outline for the topic: "{topic}", tailored for the audience: "{audience}".
    Include 6–8 slide titles with brief descriptions.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def write_slide_content(structure):
    prompt = f"""
    You're an AI presenter. Based on the following slide outline, generate detailed bullet-point content for each slide:
    \n{structure}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_speaker_notes(content):
    prompt = f"""
    Create speaker notes for each slide based on the following content. Include helpful delivery tips where relevant:
    \n{content}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_image(prompt, filename="output/slide_image_dalle.png"):
    dalle_prompt = f"An illustration in flat vector style for a presentation slide about: {prompt}"
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=dalle_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        img_data = requests.get(image_url).content
        with open(filename, 'wb') as f:
            f.write(img_data)
        return filename
    except Exception as e:
        print("Image generation failed:", e)
        return None
