from recommender import provide_recommendations
from chat_concierge import start_concierge_service
from feedback_analysis import analyze_feedback
from multilingual_support import translate_message

# Sample Guest Profile
guest_profile = {
    "name": "John Doe",
    "preferences": {
        "entertainment": "action movies",
        "diet": "vegan",
        "activities": "hiking"
    },
    "language": "fr"
}

# Sample Feedback
guest_feedback = "Great service but the room was too noisy."

def main():
    print("Welcome to the AI-Powered Guest Experience Platform")

    # Personalized Recommendations
    recommendations = provide_recommendations(guest_profile)
    print("\nPersonalized Recommendations:")
    for category, rec in recommendations.items():
        print(f"{category.capitalize()}: {rec}")

    # Start AI Concierge Service
    start_concierge_service()

    # Feedback Analysis
    sentiment = analyze_feedback(guest_feedback)
    print(f"\nSentiment Analysis of Feedback: {sentiment}")

    # Multilingual Support
    translated_message = translate_message("Welcome to our hotel!", guest_profile['language'])
    print(f"\nTranslated Message: {translated_message}")

if __name__ == "__main__":
    main()
