import sys
sys.path.append('/home/thedivsharma/Desktop/Prudential')

from insurance_claim.llm.llm_extractor import LLMExtractor
import os
import uuid
import json
import threading

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Constants
IMAGE_DIR = "/home/thedivsharma/Desktop/Prudential/insurance_claim/images"
EXTRACTED_RESULT_PATH = "/home/thedivsharma/Desktop/Prudential/insurance_claim/extracted_data/output.json"


# Function to run LLM in background
def run_llm_extraction(image_path):
    extractor = LLMExtractor()
    result = extractor.extract_fields_from_image(image_path)

    with open(EXTRACTED_RESULT_PATH, "w") as f:
        json.dump(result, f, indent=2)


# Upload view
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # Save file with UUID
        file_ext = os.path.splitext(uploaded_file.name)[1]
        filename = f"{uuid.uuid4()}{file_ext}"
        image_path = os.path.join(IMAGE_DIR, filename)

        # Write file
        with open(image_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Run LLM in background
        threading.Thread(target=run_llm_extraction, args=(image_path,)).start()

        # Redirect to buffer page
        return redirect("buffer_page")

    return render(request, "extractor/upload.html")


# Buffer page — acts like a loading screen
def buffer_page(request):
    return render(request, "extractor/buffer.html")


# Final output
def show_output(request):
    if os.path.exists(EXTRACTED_RESULT_PATH):
        with open(EXTRACTED_RESULT_PATH, "r") as f:
            data = json.load(f)
    else:
        data = {"error": "Data is not ready yet. Please wait or try again."}

    return render(request, "extractor/output.html", {"data": data})
