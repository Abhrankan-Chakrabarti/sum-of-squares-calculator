import sys

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sum_of_squares.py n")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer value for n")
        sys.exit(1)
    
    result = sum_of_squares(n)
    print(f"The sum of the squares of the first {n} natural numbers is: {result}")
