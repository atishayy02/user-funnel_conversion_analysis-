import pandas as pd
import random

def generate_data():
    data = []

    for i in range(300):
        search = 1
        view = 1 if random.random() > 0.1 else 0
        plan = 1 if view == 1 and random.random() > 0.2 else 0
        book = 1 if plan == 1 and random.random() > 0.5 else 0

        budget = random.choice(["Low", "Medium", "High"])
        group_size = random.choice([2, 3, 4, 5])

        data.append([i, search, view, plan, book, budget, group_size])

    df = pd.DataFrame(data, columns=[
        "user_id", "search", "view", "plan", "book", "budget", "group_size"
    ])

    df.to_csv("funnel_dataset.csv", index=False)
    print("Dataset created!")

if __name__ == "__main__":
    generate_data()