# Owner class definition
class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list for owner's pets

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        # Check if the pet is of type Pet
        if not isinstance(pet, Pet):
            raise Exception("The object must be of type Pet")
        pet.owner = self  # Set the owner of the pet
        self._pets.append(pet)  # Add the pet to the owner's list of pets

    def get_sorted_pets(self):
        # Return a sorted list of pets by their names
        return sorted(self._pets, key=lambda pet: pet.name)


# Pet class definition
class Pet:
    # Class variable for allowed pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        # Validate pet_type
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}")
        self.owner = owner  # The owner is optional at initialization
        Pet.all.append(self)  # Add this instance to the list of all Pets
        # Automatically add this pet to the owner's list if an owner is provided
        if owner:
            owner.add_pet(self)


# Test case
def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)

    assert owner.pets() == [pet1, pet2]
