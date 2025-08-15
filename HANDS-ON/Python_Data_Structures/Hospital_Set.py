#Equipment Tracking & Sterilization -Unique items for contamination control
# Sterilized equipment sets
sterile_lab_equipment = {"Microscope", "Centrifuge", "Pipettes"}
sterile_er_equipment = {"Stethoscope", "Defibrillator", "Sutures"}

# Contaminated items
contaminated = {"Defibrillator", "Sutures", "Scalpel"}

# Sterilize ER equipment
sterile_lab_equipment -= contaminated
print("Sterile Lab Equipment:", sterile_lab_equipment)  
# Output: {'Microscope', 'Centrifuge', 'Pipettes'}

# Combine all sterile tools
all_sterile = sterile_lab_equipment | sterile_er_equipment
print("All Sterile Equipment:", all_sterile)  
# Output: {'Microscope', 'Centrifuge', 'Pipettes', 'Stethoscope'}

#CONTAMINATED ITEMS
contaminated_items = contaminated
print("Contaminated Items:", contaminated_items)
# Output: {'Defibrillator', 'Sutures'}