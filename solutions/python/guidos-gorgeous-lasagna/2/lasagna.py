"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Constants
EXPECTED_BAKE_TIME = 40  # Expected bake time in minutes
PREPARATION_TIME = 2     # Preparation time per layer in minutes


def bake_time_remaining(elapsed_minutes):
    """Calculate the bake time remaining.

    :param elapsed_minutes: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_minutes


def preparation_time_in_minutes(layers):
    """Calculate the preparation time based on number of layers.

    :param layers: int - number of lasagna layers.
    :return: int - total preparation time in minutes.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_minutes):
    """Calculate total elapsed cooking time.

    :param layers: int - number of lasagna layers.
    :param elapsed_minutes: int - baking time already elapsed.
    :return: int - total time spent in minutes (preparation + baking).
    """
    return preparation_time_in_minutes(layers) + elapsed_minutes


# Example usage (optional)
if __name__ == "__main__":
    layers_input = int(input("Enter number of layers: "))
    baked_input = int(input("Enter elapsed bake time (minutes): "))

    print("Preparation time:", preparation_time_in_minutes(layers_input), "minutes")
    print("Remaining bake time:", bake_time_remaining(baked_input), "minutes")
    print("Total elapsed time:", elapsed_time_in_minutes(layers_input, baked_input), "minutes")