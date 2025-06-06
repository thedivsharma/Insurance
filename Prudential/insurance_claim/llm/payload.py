from insurance_claim.llm.properties import get_field_properties
from insurance_claim.llm.required import get_required

def get_payload(encoded_images: list[str], prompt: str) -> dict:
    return {
        "model": "gemma3:12b",
        "prompt": prompt,
        "images": encoded_images,
        "stream": False,
        "format": {
            "type": "object",
            "properties": get_field_properties(),
            "required": get_required(),
        },
    } 