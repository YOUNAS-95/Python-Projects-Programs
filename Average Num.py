def average(numbers):
    if not numbers:
        return None  # Handle the case where the list is empty
    return sum(numbers) / len(numbers)

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
result = average(numbers_list)
print("Average:", result)
