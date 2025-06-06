import json
from insurance_claim.schema.claim_schema import ClaimData

def handle_api_response(response) -> dict:
    if response.status_code != 200:
        return {"error": f"API returned status code {response.status_code}", "raw": response.text}

    try:
        message_content = response.json().get("message", {}).get("content")
        if not message_content:
            return {"error": "No content found in API response", "raw": response.text}

        claim_data_dict = json.loads(message_content)

        validated_data = ClaimData(**claim_data_dict)
        return validated_data.dict(by_alias=True)

    except (json.JSONDecodeError, TypeError) as e:
        return {"error": f"JSON decode error: {str(e)}", "raw": response.text}
    except Exception as e:
        return {"error": f"Validation failed: {str(e)}", "raw": message_content}
