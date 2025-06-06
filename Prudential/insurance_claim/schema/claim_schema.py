from typing import Optional
from pydantic import BaseModel, Field

class ClaimData(BaseModel):
    patient_name: str = Field(..., alias="Patient Name")
    hospital_name: str = Field(..., alias="Hospital Name")
    admission_date: Optional[str] = Field(None, alias="Admission Date")
    discharge_date: Optional[str] = Field(None, alias="Discharge Date")
    diagnosis: str = Field(..., alias="Diagnosis") 
    total_amount: float = Field(..., alias="Total Amount")
    confidence: Optional[float] = Field(None, alias="confidence")
