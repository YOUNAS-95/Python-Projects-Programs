# Get user's credit score as input
credit_score = int(input("Enter your credit score: "))

# Classify the credit score into categories
if 700 <= credit_score <= 749:
    category = "Excellent"
elif 650 <= credit_score <= 699:    
    category = "Poor"
elif credit_score < 600:
    category = "Bad"
else:
    category = "Undefined"

# Display the result
print(f"Your credit score is classified as: {category}")
