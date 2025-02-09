# bank.py
# Prompt the user and read in two money amounts
# author Joanna Mnich

def main():
    # Prompt the user to enter the first amount in cents
    amount1 = int(input("Enter amount1 (in cent): "))
    
    # Prompt the user to enter the second amount in cents
    amount2 = int(input("Enter amount2 (in cent): "))
    
    # Calculate the total sum in cents
    total_cents = amount1 + amount2
    
    # Convert to euros and cents
    euros = total_cents // 100
    cents = total_cents % 100
    
    # Print the result in human-readable format
    print(f"The sum of these is €{euros}.{cents:02d}")

if __name__ == "__main__":
    main()
