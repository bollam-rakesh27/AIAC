import random

# Sample product catalog with brands and categories
products = [
    {"id": 1, "name": "UltraClean Detergent", "brand": "CleanCo", "category": "Detergent"},
    {"id": 2, "name": "Sparkle Detergent", "brand": "Sparkle", "category": "Detergent"},
    {"id": 3, "name": "FreshBite Cereal", "brand": "MorningStar", "category": "Cereal"},
    {"id": 4, "name": "Crunchy Oats", "brand": "Oaty", "category": "Cereal"},
    {"id": 5, "name": "SmoothShave Razor", "brand": "SharpEdge", "category": "Razor"},
    {"id": 6, "name": "GentleGlide Razor", "brand": "SmoothCo", "category": "Razor"},
    {"id": 7, "name": "PureSpring Water", "brand": "AquaPure", "category": "Water"},
    {"id": 8, "name": "CrystalClear Water", "brand": "Crystal", "category": "Water"},
]

# User purchase history and feedback
user_history = []
user_feedback = {}  # product_id: 'like' or 'dislike'

def get_recommendations(history, feedback, n=2):
    # Find categories the user bought before
    bought_categories = set()
    bought_brands = set()
    for pid in history:
        prod = next((p for p in products if p["id"] == pid), None)
        if prod:
            bought_categories.add(prod["category"])
            bought_brands.add(prod["brand"])
    # Avoid recommending disliked products
    disliked_ids = {pid for pid, fb in feedback.items() if fb == 'dislike'}
    # Recommend products from same categories, but different brands
    recs = []
    for cat in bought_categories:
        # Get products in this category, not bought, not disliked, and not from the same brand as last purchase
        last_brand = None
        for pid in reversed(history):
            prod = next((p for p in products if p["id"] == pid), None)
            if prod and prod["category"] == cat:
                last_brand = prod["brand"]
                break
        candidates = [p for p in products if p["category"] == cat and p["id"] not in history and p["id"] not in disliked_ids and p["brand"] != last_brand]
        if candidates:
            # Randomly pick to ensure fairness
            rec = random.choice(candidates)
            recs.append(rec)
    # If not enough recommendations, suggest from new categories
    if len(recs) < n:
        unused = [p for p in products if p["category"] not in bought_categories and p["id"] not in disliked_ids]
        random.shuffle(unused)
        recs.extend(unused[:n - len(recs)])
    return recs[:n]

def explain_recommendation(product, history):
    # Explain why this product is suggested
    for pid in reversed(history):
        prev = next((p for p in products if p["id"] == pid), None)
        if prev and prev["category"] == product["category"]:
            if prev["brand"] != product["brand"]:
                return f"We noticed you bought {prev['name']} ({prev['brand']}) in the {prev['category']} category. To give you variety, we suggest {product['name']} from a different brand ({product['brand']})."
            else:
                return f"You previously bought {prev['name']} in the {prev['category']} category. Here's another option from the same brand."
    return f"This is a popular product in a category you haven't tried yet: {product['category']}."

def get_user_feedback(product):
    # Ask user for feedback on the recommendation
    while True:
        fb = input(f"Do you like the recommendation '{product['name']}' by {product['brand']}? (like/dislike): ").strip().lower()
        if fb in ('like', 'dislike'):
            return fb
        print("Please type 'like' or 'dislike'.")

def main():
    print("Welcome to the Product Recommender!")
    # Simulate user purchase history
    while True:
        print("\nYour purchase history:")
        if user_history:
            for pid in user_history:
                prod = next((p for p in products if p["id"] == pid), None)
                if prod:
                    print(f"- {prod['name']} ({prod['brand']}, {prod['category']})")
        else:
            print("No purchases yet.")
        # Recommend products
        recs = get_recommendations(user_history, user_feedback)
        if not recs:
            print("No new recommendations available.")
            break
        for rec in recs:
            print(f"\nRecommended: {rec['name']} ({rec['brand']}, {rec['category']})")
            print("Reason:", explain_recommendation(rec, user_history))
            fb = get_user_feedback(rec)  # Get feedback from user
            user_feedback[rec["id"]] = fb  # Store feedback
            if fb == 'like':
                user_history.append(rec["id"])  # Add to history if liked
        # Ask if user wants more recommendations
        cont = input("\nWould you like more recommendations? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the Product Recommender!")
            break

if __name__ == "__main__":
    main()

