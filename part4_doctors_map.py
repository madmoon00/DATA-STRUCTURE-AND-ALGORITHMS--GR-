# Τεταρτο Μερος
from enum import Enum

# Βήμα 1: Δημιουργία Enum για τις ιατρικές ειδικότητες
class Specialization(Enum):
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    ORTHOPEDICS = "Orthopedics"
    DERMATOLOGY = "Dermatology"
    ONCOLOGY = "Oncology"
    PEDIATRICS = "Pediatrics"

# Βήμα 2: Δημιουργία Dictionary για mapping γιατρών-ειδικοτήτων
doctor_map = {}

# Βήμα 3: CRUD λειτουργίες

# Προσθήκη γιατρού
def add_doctor(name, specialization):
    doctor_map[name] = specialization
    print(f"Προστέθηκε: {name} - {specialization.value}")

# Ενημέρωση ειδικότητας γιατρού
def update_doctor(name, new_specialization):
    if name in doctor_map:
        doctor_map[name] = new_specialization
        print(f"Ενημερώθηκε: {name} -> {new_specialization.value}")
    else:
        print(f"Ο γιατρός {name} δεν υπάρχει.")

# Διαγραφή γιατρού
def delete_doctor(name):
    if name in doctor_map:
        del doctor_map[name]
        print(f"Διαγράφηκε: {name}")
    else:
        print(f"Ο γιατρός {name} δεν βρέθηκε.")

# Αναζήτηση γιατρού
def get_doctor(name):
    if name in doctor_map:
        print(f"{name} - {doctor_map[name].value}")
    else:
        print(f"Ο γιατρός {name} δεν βρέθηκε.")

# Εμφάνιση όλων των γιατρών
def display_all_doctors():
    print("\nΌλοι οι γιατροί:")
    for name, spec in doctor_map.items():
        print(f"  {name}: {spec.value}")

# Βήμα 4: Παραδείγματα χρήσης
if __name__ == "__main__":
    add_doctor("Δρ. Παπαδόπουλος", Specialization.CARDIOLOGY)
    add_doctor("Δρ. Νικολάου", Specialization.NEUROLOGY)
    add_doctor("Δρ. Μητσοπούλου", Specialization.PEDIATRICS)

    display_all_doctors()

    update_doctor("Δρ. Νικολάου", Specialization.DERMATOLOGY)
    get_doctor("Δρ. Νικολάου")

    delete_doctor("Δρ. Παπαδόπουλος")
    get_doctor("Δρ. Παπαδόπουλος")

    display_all_doctors()
