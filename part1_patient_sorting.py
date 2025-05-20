# Μέρος Πρώτο 
import random
import string
import time


class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}"

# Δημιουργία παραδειγμάτων ασθενών
patients = [
    Patient(104, "Maria Papadopoulou", 30, "Flu"),
    Patient(101, "Giorgos Katsaros", 45, "Asthma"),
    Patient(106, "Eleni Markou", 27, "Covid-19"),
    Patient(102, "Nikos Panagiotou", 60, "Diabetes"),
    Patient(103, "Anna Georgiou", 35, "Hypertension"),
]


# Δημιουργία bubble sort
def bubble_sort(patients, key=lambda x: x.age):
    n = len(patients)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key(patients[j]) > key(patients[j + 1]):
                patients[j], patients[j + 1] = patients[j + 1], patients[j]


# Δημιουργια Merge sort

def merge_sort(patients, key=lambda x: x.age):
    if len(patients) <= 1:
        return patients

    mid = len(patients) // 2
    left = merge_sort(patients[:mid], key)
    right = merge_sort(patients[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Δημιουργία Quick sort

def quick_sort(patients, key=lambda x: x.age):
    if len(patients) <= 1:
        return patients
    pivot = patients[0]
    less = [x for x in patients[1:] if key(x) <= key(pivot)]
    greater = [x for x in patients[1:] if key(x) > key(pivot)]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

# Δημιουργία linear search

def linear_search(patients, target, key=lambda x: x.patient_id):
    for patient in patients:
        if key(patient) == target:
            return patient
    return None


# Δημιουργία Binary Search

def binary_search(patients, target, key=lambda x: x.patient_id):
    low = 0
    high = len(patients) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = key(patients[mid])

        if mid_value == target:
            return patients[mid]
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Συνάρτηση για δημιουργία τυχαίων ασθενων
def generate_random_patient(patient_id):
    name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
    age = random.randint(1, 100)
    diagnosis = random.choice(["Flu", "Asthma", "Covid-19", "Diabetes", "Hypertension"])
    return Patient(patient_id, name, age, diagnosis)

def generate_patient_list(size):
    return [generate_random_patient(i) for i in range(size)]


def measure_sorting_algorithms(sizes=[100, 500, 1000]):
    for size in sizes:
        print(f"\n--- Sorting Performance for list size: {size} ---")
        patients = generate_patient_list(size)

        # Bubble Sort
        bubble_patients = patients.copy()
        start = time.time()
        bubble_sort(bubble_patients, key=lambda x: x.age)
        end = time.time()
        print(f"Bubble Sort: {end - start:.5f} sec")

        # Merge Sort
        merge_patients = patients.copy()
        start = time.time()
        sorted_merge = merge_sort(merge_patients, key=lambda x: x.age)
        end = time.time()
        print(f"Merge Sort: {end - start:.5f} sec")

        # Quick Sort
        quick_patients = patients.copy()
        start = time.time()
        sorted_quick = quick_sort(quick_patients, key=lambda x: x.age)
        end = time.time()
        print(f"Quick Sort: {end - start:.5f} sec")

def measure_search_algorithms(sizes=[100, 500, 1000]):
    for size in sizes:
        print(f"\n--- Search Performance for list size: {size} ---")
        patients = generate_patient_list(size)
        target_id = random.randint(0, size - 1)

        # Linear search
        start = time.time()
        linear_search(patients, target_id, key=lambda x: x.patient_id)
        end = time.time()
        print(f"Linear Search: {end - start:.5f} sec")

        # Binary search (λίστα πρέπει να είναι ταξινομημένη)
        sorted_patients = merge_sort(patients, key=lambda x: x.patient_id)
        start = time.time()
        binary_search(sorted_patients, target_id, key=lambda x: x.patient_id)
        end = time.time()
        print(f"Binary Search: {end - start:.5f} sec")

        result = linear_search(patients, target_id, key=lambda x: x.patient_id)
        print("Found by Linear Search:", result if result else "Not found")


if __name__ == "__main__":
    measure_sorting_algorithms()
    measure_search_algorithms()

    print("\n--- παραδείγματα αναζήτησης ---")
    # Χρήση της αρχικής μικρής λίστας
    target_id = 103
    result = linear_search(patients, target_id, key=lambda x: x.patient_id)
    print(f"\nLinear Search by ID {target_id}:")
    print(result if result else "Not found")

    sorted_by_id = merge_sort(patients, key=lambda x: x.patient_id)
    result = binary_search(sorted_by_id, target_id, key=lambda x: x.patient_id)
    print(f"\nBinary Search by ID {target_id}:")
    print(result if result else "Not found")

    target_name = "Anna Georgiou"
    result = linear_search(patients, target_name, key=lambda x: x.name)
    print(f"\nLinear Search by Name '{target_name}':")
    print(result if result else "Not found")

    sorted_by_name = merge_sort(patients, key=lambda x: x.name)
    result = binary_search(sorted_by_name, target_name, key=lambda x: x.name)
    print(f"\nBinary Search by Name '{target_name}':")
    print(result if result else "Not found")

