import re
import json
import base64
import requests

from insurance_claim.llm.prompt import get_prompt
from insurance_claim.llm.payload import get_payload

class LLMExtractor:
    def extract_fields_from_image(self, image_path: str) -> dict:
        try:
            # Encode image to base64
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

            # Build prompt and payload
            prompt = get_prompt()
            payload = get_payload([encoded_image], prompt)  
            # Make API call
            response = requests.post(
                "http://164.52.192.246:11434/api/generate",
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                stream=True,
                timeout=360,
            )

            # Collect streaming response
            full_text = ""
            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    full_text += data.get("response", "")
                    if data.get("done", False):
                        break

            # Clean LLM response
            clean_text = full_text.strip()
            clean_text = re.sub(r"```(?:json)?\n?", "", clean_text)
            clean_text = re.sub(r"\n?```", "", clean_text)

            # parse JSON
            extracted_data = json.loads(clean_text)
            extracted_data["confidence"] = extracted_data.get("confidence", None)

            return extracted_data

        except json.JSONDecodeError as parse_err:
            return {"error": f"JSON parse error: {parse_err}"}
        except requests.Timeout:
            return {"error": "Request timed out"}
        except requests.RequestException as req_err:
            return {"error": f"Request failed: {req_err}"}
        except Exception as e:
            return {"error": f"Extraction failed: {str(e)}"}
