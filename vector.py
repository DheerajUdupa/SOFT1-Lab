class Vector:
    """Represents a matematical vector as a list of floats."""
    def __init__(self, data = None): # Sets data to None if nothing is passed in
        """Initialises a Vector from a list of floats.
        
        Args:
            data: a list of floats representing the vector elements.
            If no list is provided, the vector is empty.
            """
        if data == None:
            self._vector = []
        else:
            self._vector = list(data) # list(data) makes a copy of data, so no change to _vector affects data

    def __str__(self):
        return_string = ""
        for dimension in self._vector:
            return_string += str(dimension) + ", "
        return_string = return_string[:-2]
        return f"<{return_string}>"

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]

    def set(self, index, value):
        self._vector[index] = value

    def scalar_product(self, scalar):
        """Performs the matematical scalar product operation on a vector
        
        Args:
        scalar: a float representing the number the vector should be multiplied by.
        """
        new_vector = []
        for dimension in self._vector:
            new_vector.append(dimension*scalar)
        return Vector(new_vector)

    def add(self, other_vector: Vector):
        new_vector = []
        for i in range(len(self._vector)):
            new_vector.append(self._vector[i] + other_vector.get(i))
        return Vector(new_vector)

    def equals(self, other_vector: Vector):
        equals_flag = True
        for i in range(len(self._vector)):
            if self._vector[i] != other_vector.get(i):
                equals_flag = False
        return equals_flag

# my_vector = Vector([1, 2, 3])
# print(my_vector)
# empty_vector = Vector()
# print(empty_vector)

# vector1 = Vector([1, 2, 3])
# vector2 = Vector([0, 1, 3])
# added = vector1.add(vector2)
# print(added)

vector1 = Vector([1, 2, 3])
vector2 = Vector([1, 2, 3])
print(vector1.equals(vector2))
vector3 = Vector([0, 2, 0])
print(vector3.equals(vector1))
print(vector1 == vector2)