from googleapiclient.discovery import build
from google_auth import get_google_creds
import re

# ✅ Create a new Google Slides presentation
def create_presentation(title):
    creds = get_google_creds()
    service = build('slides', 'v1', credentials=creds)

    presentation = service.presentations().create(body={'title': title}).execute()
    return presentation.get('presentationId'), presentation.get('title')


# ✅ Create multiple slides from bullet-style text
def create_slides_from_bullets(presentation_id, raw_content):
    creds = get_google_creds()
    service = build('slides', 'v1', credentials=creds)

    # Split the content into sections based on "Slide X:"
    slides = re.split(r"Slide \d+:", raw_content)
    slides = [s.strip() for s in slides if s.strip()]

    for slide in slides:
        lines = slide.splitlines()
        if not lines:
            continue

        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()

        # 1. Create a slide with TITLE_AND_BODY layout
        create_response = service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={
                'requests': [{
                    'createSlide': {
                        'slideLayoutReference': {
                            'predefinedLayout': 'TITLE_AND_BODY'
                        }
                    }
                }]
            }
        ).execute()

        # 2. Get the latest slide's elements
        presentation = service.presentations().get(presentationId=presentation_id).execute()
        latest_slide = presentation.get('slides')[-1]
        elements = latest_slide.get('pageElements')

        title_id = None
        body_id = None

        for elem in elements:
            shape = elem.get('shape')
            if not shape:
                continue
            placeholder_type = shape.get('placeholder', {}).get('type')
            if placeholder_type == 'TITLE':
                title_id = elem['objectId']
            elif placeholder_type == 'BODY':
                body_id = elem['objectId']

        # 3. Insert text into title and body
        requests = []

        if title_id:
            requests.append({
                'insertText': {
                    'objectId': title_id,
                    'text': title
                }
            })

        if body_id:
            requests.append({
                'insertText': {
                    'objectId': body_id,
                    'text': body
                }
            })

        if requests:
            service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()
