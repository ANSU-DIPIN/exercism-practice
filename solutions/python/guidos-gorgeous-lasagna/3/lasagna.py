"""Functions to calculate preparation and bake times for Guido's gorgeous lasagna.

Learn about Guido, the creator of Python:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Constants
EXPECTED_BAKE_TIME: int = 40  # minutes
PREPARATION_TIME_PER_LAYER: int = 2  # minutes per layer


def bake_time_remaining(elapsed_minutes: int) -> int:
    """Return the remaining bake time in minutes.

    :param elapsed_minutes: Minutes the lasagna has already baked.
    :return: Remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_minutes


def preparation_time_in_minutes(layers: int) -> int:
    """Return the total preparation time for the given number of layers.

    :param layers: Number of lasagna layers.
    :return: Total preparation time in minutes.
    """
    return layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(layers: int, elapsed_minutes: int) -> int:
    """Return the total time spent preparing and baking the lasagna.

    :param layers: Number of lasagna layers.
    :param elapsed_minutes: Minutes the lasagna has already baked.
    :return: Total elapsed time in minutes.
    """
    return preparation_time_in_minutes(layers) + elapsed_minutes


# Optional interactive test block
if __name__ == "__main__":
    layers_input: int = int(input("Enter number of layers: "))
    baked_input: int = int(input("Enter elapsed bake time (minutes): "))

    print("Preparation time:", preparation_time_in_minutes(layers_input), "minutes")
    print("Remaining bake time:", bake_time_remaining(baked_input), "minutes")
    print("Total elapsed time:", elapsed_time_in_minutes(layers_input, baked_input), "minutes")