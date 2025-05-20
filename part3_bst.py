# Τριτο Μερος

# Κλάση Ασθενή
class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}"


# Κόμβος του BST
class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None


# Κλάση Binary Search Tree
class PatientBST:
    def __init__(self):
        self.root = None

    # Εισαγωγή ασθενή στο δέντρο
    def insert(self, patient):
        def _insert(root, patient):
            if not root:
                return BSTNode(patient)
            if patient.patient_id < root.patient.patient_id:
                root.left = _insert(root.left, patient)
            else:
                root.right = _insert(root.right, patient)
            return root
        self.root = _insert(self.root, patient)

    # Αναζήτηση ασθενή με ID
    def search(self, patient_id):
        def _search(root, patient_id):
            if not root:
                return None
            if patient_id == root.patient.patient_id:
                return root.patient
            elif patient_id < root.patient.patient_id:
                return _search(root.left, patient_id)
            else:
                return _search(root.right, patient_id)
        return _search(self.root, patient_id)

    # Διαγραφή ασθενή από το δέντρο
    def delete(self, patient_id):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, patient_id):
            if not root:
                return root
            if patient_id < root.patient.patient_id:
                root.left = _delete(root.left, patient_id)
            elif patient_id > root.patient.patient_id:
                root.right = _delete(root.right, patient_id)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _min_value_node(root.right)
                root.patient = temp.patient
                root.right = _delete(root.right, temp.patient.patient_id)
            return root

        self.root = _delete(self.root, patient_id)

    # Inorder Traversal (Left - Root - Right)
    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.patient)
                _inorder(node.right)
        _inorder(self.root)

    # Preorder Traversal (Root - Left - Right)
    def preorder(self):
        def _preorder(node):
            if node:
                print(node.patient)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)

    # Postorder Traversal (Left - Right - Root)
    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.patient)
        _postorder(self.root)

    # Level-order Traversal (BFS)
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.patient)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Τεστ με 10 ασθενείς και εμφάνιση traversals
if __name__ == "__main__":
    bst = PatientBST()

    # Δημιουργία 10 ασθενών
    patients = [
        Patient(5, "Anna", 30, "Flu"),
        Patient(2, "Bob", 40, "Asthma"),
        Patient(8, "Charlie", 35, "Covid-19"),
        Patient(1, "Dora", 28, "Flu"),
        Patient(3, "Eleni", 50, "Diabetes"),
        Patient(6, "Frank", 60, "Cancer"),
        Patient(9, "Georgia", 32, "Allergy"),
        Patient(4, "Haris", 41, "Hypertension"),
        Patient(7, "Iris", 22, "Covid-19"),
        Patient(10, "John", 33, "Injury")
    ]

    # Εισαγωγή όλων στο BST
    for p in patients:
        bst.insert(p)

    # Εμφάνιση των traversals
    print("\nInorder Traversal:")
    bst.inorder()

    print("\nPreorder Traversal:")
    bst.preorder()

    print("\nPostorder Traversal:")
    bst.postorder()

    print("\nLevel-order Traversal:")
    bst.level_order()
