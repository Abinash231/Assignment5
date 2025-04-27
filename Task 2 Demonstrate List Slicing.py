def list_slicing():
    numbers = list(range(1, 11))
    print(f"Original list: {numbers}")

    first_five = numbers[0:5]
    print(f"Extracted first five elements: {first_five}")

    first_five.reverse()
    print(f"Reversed extracted elements: {first_five}")

if __name__ == "__main__":
    list_slicing()