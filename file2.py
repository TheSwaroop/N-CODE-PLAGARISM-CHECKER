def sort_numbers(numbers):
    """
    Implements bubble sort to arrange the list of numbers in ascending order.
    """
    count = len(numbers)
    for i in range(count):
        for j in range(count - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap the elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    result = sort_numbers(data)
    print("Sorted Data:", result)
