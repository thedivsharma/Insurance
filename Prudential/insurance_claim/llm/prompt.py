def get_prompt() -> str:
    return """
Extract the following fields in JSON format from the document.
Do NOT guess or fabricate values. If a field is missing or not clearly readable, set it to null.

Fields:
- Patient's full Name
- Hospital Name with the city
- Admission Date 
- Discharge Date 
- What is it that the amount has been paid for ?
- Total Amount 

Return ONLY valid JSON. BY the way , I am sending multiple images , extract one by one sequentially
"""