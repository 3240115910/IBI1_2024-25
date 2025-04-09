#Start a function to calculate the volume
def calculate_paracetamol_dose(weight, strength):
    # Check if weight is within the valid range
    weight = int (weight)
    print (f'The weigth of the child is:{weight}')
    if not 10 <= weight <= 100:
        raise ValueError("Weight must be between 10 and 100 kg")
    # Check if strength is within the valid range
    valid_strengths = {"120 mg/5 ml": 120, "250 mg/5 ml": 250}
    print (f'The strengths is:{strength}')
    if strength not in valid_strengths:
        raise ValueError("Invalid strength which must be either '120 mg/5 ml' or '250 mg/5 ml'")
    # Calculate the required dose in mg and it 15 mg/kg.
    dose_mg = 15 * weight  
    # Calculate the volume required
    mg_per_ml = valid_strengths[strength] / 5
    volume_ml = dose_mg / mg_per_ml
    print(f"The required volume of paracetamol is {volume_ml:.2f} ml")
    return volume_ml
#an example
try:
    weight = 30  # Example weight in kg
    strength = '250 mg/5 ml' # Example strength
    volume = calculate_paracetamol_dose(weight, strength)
except ValueError as e:
    print(e)