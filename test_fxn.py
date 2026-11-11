from fitting_functions import *


if linear(2, 3, 4) == 10:
    print("Linear : Passed")

else:
    print("Linear : Failed")


if slope_units("Meters", "kg") == "kg/Meters":
    print("Slope Units : Passed")

else:
    print("Slope Units : Failed")


print_equation(4, 1, "Meters", "kg")

