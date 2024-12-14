class NutrientDeficiency:
    def __init__(self, name, deficiency_syndrome, cure):
        self.name = name
        self.deficiency_syndrome = deficiency_syndrome
        self.cure = cure

    def display_info(self):
        print(f"\nNutrient: {self.name}")
        print(f"Deficiency Syndrome: {self.deficiency_syndrome}")
        print(f"Cure: {self.cure}")

    def edit_info(self):
        print(f"\nEditing information for {self.name}")
        self.deficiency_syndrome = input(f"Enter new deficiency syndrome for {self.name}: ")
        self.cure = input(f"Enter new cure for {self.name}: ")


class PlantNutrientApp:
    def __init__(self):
        self.macro_nutrients = {
            "Nitrogen": NutrientDeficiency(
                "Nitrogen",
                "Yellowing of older leaves, stunted growth.",
                "Add nitrogen-based fertilizers like ammonium nitrate."
            ),
            "Phosphorus": NutrientDeficiency(
                "Phosphorus",
                "Purpling of older leaves, poor root development.",
                "Apply phosphorus-based fertilizers like superphosphate."
            ),
            "Potassium": NutrientDeficiency(
                "Potassium",
                "Yellowing and browning of leaf edges, weak stems.",
                "Add potassium sulfate or potassium chloride."
            ),
            "Calcium": NutrientDeficiency(
                "Calcium",
                "Deformed or necrotic leaf tips, stunted growth.",
                "Apply lime or gypsum."
            ),
            "Magnesium": NutrientDeficiency(
                "Magnesium",
                "Yellowing between leaf veins, leaf curling.",
                "Use magnesium sulfate (Epsom salts)."
            ),
            "Sulfur": NutrientDeficiency(
                "Sulfur",
                "Yellowing of younger leaves, stunted growth.",
                "Apply sulfur or ammonium sulfate."
            )
        }

        self.micro_nutrients = {
            "Iron": NutrientDeficiency(
                "Iron",
                "Yellowing between leaf veins, especially in younger leaves.",
                "Use chelated iron supplements."
            ),
            "Manganese": NutrientDeficiency(
                "Manganese",
                "Chlorosis of leaves, dark green veins with pale tissue.",
                "Apply manganese sulfate."
            ),
            "Zinc": NutrientDeficiency(
                "Zinc",
                "Interveinal chlorosis, reduced leaf size.",
                "Add zinc sulfate or chelated zinc."
            ),
            "Copper": NutrientDeficiency(
                "Copper",
                "Chlorosis, distorted leaves, dieback of younger stems.",
                "Apply copper sulfate."
            ),
            "Boron": NutrientDeficiency(
                "Boron",
                "Poor fruit set, deformed leaves, and roots.",
                "Use borax or boric acid."
            ),
            "Molybdenum": NutrientDeficiency(
                "Molybdenum",
                "Yellowing of leaves, poor growth.",
                "Apply sodium molybdate."
            )
        }

    def choose_nutrient_type(self):
        while True:
            print("\nChoose nutrient type:")
            print("1. Macro Nutrients")
            print("2. Micro Nutrients")
            print("3. Exit")
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                self.select_nutrient(self.macro_nutrients)
            elif choice == "2":
                self.select_nutrient(self.micro_nutrients)
            elif choice == "3":
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def select_nutrient(self, nutrient_dict):
        while True:
            print("\nEnter the nutrient name (e.g., Nitrogen, Iron), or type 'exit' to return:")
            nutrient_name = input("Nutrient name: ").capitalize()

            if nutrient_name == "Exit":
                break
            elif nutrient_name in nutrient_dict:
                nutrient_info = nutrient_dict[nutrient_name]
                nutrient_info.display_info()

                
                edit_choice = input("\nWould you like to edit this information? (yes/no): ").lower()
                if edit_choice == "yes":
                    nutrient_info.edit_info()

            else:
                print(f"\nNo information available for {nutrient_name}. Please try again.")


if __name__ == "__main__":
    app = PlantNutrientApp()
    app.choose_nutrient_type()
