again = "Y" # Allows entry into the loop
while again == "Y":
    # Ask user for information about the series
    term = float(input("Initial Term: "))
    ratio = float(input("Ratio: "))
    num_terms = int(input("Terms to add: "))
    # Start with the initial term and then loop 'num_terms' times
    # to calculate more terms.
    series_sum = term
    for x in range(num_terms):  # Runs 'num_terms" times.  'x' is not used
        # Calculate the new term and add it to the sum
        term = term * ratio
        series_sum += term
    # Display result and ask if the user wants to do another calculation
    print("Sum = {:.20f}".format(series_sum))
    print()
    again = input("Again (Y/N)? ")
    