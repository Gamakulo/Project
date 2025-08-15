#Staff & Patient Records -Key-value pairs for instant lookups
# Staff Directory (ID → Details)
staff = {
    101: {"name": "Dr. Smith", "role": "Cardiologist", "station": "ER"},
    202: {"name": "Nurse Lee", "role": "ICU", "station": "Ward 3B"},
    303: {"name": "Dr. Patel", "role": "Radiologist", "station": "Lab 2"}
}

# Patient Records (ID → Medical History)
patients = {
    "P881": {"name": "John Munae", "allergies": ["Penicillin"], "ward": "ICU"},
    "P882": {"name": "Maria Garcia", "allergies": ["Smoke"], "ward": "Ward 4A"}
}

# Access data
print("Cardiologist on duty:", staff[101]['name'])  # Dr. Smith
print("Maria's allergies:", patients["P882"]["allergies"])  # ['Smoke']
print("Nurse in Ward 3B:", staff[202]['name'])  # Nurse Lee

# Add new patient
patients["P883"] = {"name": "Alex Kim", "allergies": ["Latex"], "ward": "ER"}
patients["P884"] = {"name": "Emily Chen", "allergies": ["Nuts"], "ward": "Ward 4A"}
print("New Patient Added:", patients["P883"])  # Alex Kim
print("New Patient Added:", patients["P884"])  # Emily Chen