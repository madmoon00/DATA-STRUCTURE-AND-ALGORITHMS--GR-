# Πεμπτο Μερος
import copy

# Κλάση Ασθενή
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __str__(self):
        return f"{self.street}, {self.city}"

class Patient:
    def __init__(self, name, age, diagnosis, address):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.address = address 

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, "
                f"Address: {self.address}")

if __name__ == "__main__":
    # Αρχικός ασθενής
    original_address = Address("Ερμού 15", "Αθήνα")
    patient1 = Patient("Γιώργος Παπαδόπουλος", 45, "Υπέρταση", original_address)

    print("Αρχικός Ασθενής:")
    print(patient1)

    # Shallow Copy
    shallow_copied = copy.copy(patient1)
    shallow_copied.address.street = "Σταδίου 22"  # Τροποποίηση μόνο στη διεύθυνση

    print("\nΜετά από SHALLOW COPY και αλλαγή διεύθυνσης στο αντίγραφο:")
    print("Αντίγραφο:", shallow_copied)
    print("Αρχικός:", patient1)  # Θα έχει επηρεαστεί

    # Deep Copy
    deep_copied = copy.deepcopy(patient1)
    deep_copied.address.street = "Πατησίων 100"  # Αλλαγή σε deep copy

    print("\nΜετά από DEEP COPY και αλλαγή διεύθυνσης στο αντίγραφο:")
    print("Αντίγραφο:", deep_copied)
    print("Αρχικός:", patient1)  # Δεν έχει αλλάξει
