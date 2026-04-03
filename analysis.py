def run_analysis(df):
    print("\n--- Funnel Conversion ---")

    search = df['search'].sum()
    view = df['view'].sum()
    plan = df['plan'].sum()
    book = df['book'].sum()

    print("Search → View:", view / search)
    print("View → Plan:", plan / view)
    print("Plan → Book:", book / plan)

    print("\n--- Conversion by Budget ---")
    print(df.groupby('budget')['book'].mean())

    print("\n--- Conversion by Group Size ---")
    print(df.groupby('group_size')['book'].mean())