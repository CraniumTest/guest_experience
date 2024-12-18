def provide_recommendations(profile):
    recommendations = {}

    entertainment_options = {
        "action movies": "Die Hard series",
        "comedy": "The Office"
    }
    dining_options = {
        "vegan": "Glazed Tofu with Quinoa",
        "gluten-free": "Rice and Bean Bowl"
    }
    activity_options = {
        "hiking": "Local Mountain Trails",
        "relaxation": "Spa Day Package"
    }

    preferences = profile.get('preferences', {})

    recommendations['entertainment'] = entertainment_options.get(preferences.get('entertainment'), "Standard Package")
    recommendations['dining'] = dining_options.get(preferences.get('diet'), "Chef's Special")
    recommendations['activities'] = activity_options.get(preferences.get('activities'), "City Tour")

    return recommendations
