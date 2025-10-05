"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
   
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers
numbers = get_numbers_from_user()

def analyze_numbers(numbers):
   
    if not numbers:
        return None

    analysis = {}
    analysis['count'] = len(numbers)
    analysis['sum'] = sum(numbers)
    analysis['average'] = analysis['sum'] / analysis['count']
    analysis['minimum'] = min(numbers)
    analysis['maximum'] = max(numbers)
    # for even and odd
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num.is_integer():
            if int(num) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    analysis['even_count'] = even_count
    analysis['odd_count'] = odd_count
    return analysis


def display_analysis(analysis):
    
    #if there is no dictionary yet
    if not analysis:
        print("No numbers entered to analyze.")
        return

    # using analysis dictionary
    print("\nAnalysis Results:")
    print("-" * 20)

    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']:.2f}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']:.2f}")
    print(f"Maximum: {analysis['maximum']:.2f}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    
    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()