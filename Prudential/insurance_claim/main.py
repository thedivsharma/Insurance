import json
import os
from insurance_claim.llm.llm_extractor import LLMExtractor
from insurance_claim.utils.mysql import insert_into_mysql

def run_pipeline():
    image_dir = "insurance_claim/images"
    output_dir = "insurance_claim/extracted_data"
    os.makedirs(output_dir, exist_ok=True)

    llm = LLMExtractor()

    for file_name in sorted(os.listdir(image_dir)):
        if file_name.lower().endswith(".jpeg"):
            image_path = os.path.join(image_dir, file_name)
            print(f"\n Processing: {file_name}")

            fields = llm.extract_fields_from_image(image_path)

            output_file_name = f"output_{file_name.split('.')[0]}.json"
            output_path = os.path.join(output_dir, output_file_name)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(fields, f, indent=2)

            print(json.dumps(fields, indent=2))
            insert_into_mysql(fields)

if __name__ == "__main__":
    run_pipeline() 

