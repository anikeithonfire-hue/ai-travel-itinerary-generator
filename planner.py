import random
from data import activity_data

def generate_plan(destination, days, interests):
    interests = [i.strip().lower() for i in interests.split(",")]
    plan = []

    for day in range(1, days + 1):
        activities = []

        for interest in interests:
            if interest in activity_data:
                activity = random.choice(activity_data[interest])
                activities.append(activity)

        if not activities:
            activities.append("City Exploration")

        plan.append((day, activities))

    return plan