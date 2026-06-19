"""
Quick prediction script for Spam Email Detection.
Loads saved model and vectorizer to classify new emails.
"""

import pickle

# Load saved model and vectorizer
with open('models/spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


def predict_spam(email_text: str) -> str:
    """
    Predict if an email is spam or not.
    
    Args:
        email_text: Raw email content
        
    Returns:
        'Spam' or 'Not Spam'
    """
    # Transform text using saved vectorizer
    email_vector = vectorizer.transform([email_text])
    
    # Predict using saved model
    prediction = model.predict(email_vector)[0]
    
    return "Spam" if prediction == 1 else "Not Spam"


if __name__ == "__main__":
    # Example usage
    test_email = "Congratulations! You won $1000! Click here now!"
    result = predict_spam(test_email)
    print(f"Email: {test_email}")
    print(f"Prediction: {result}")
