def process_scores_v2(scores):
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

process_scores_v2([85, 90, 78, 92, 88])
