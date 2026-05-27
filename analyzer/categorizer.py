import config
from config import category

def assign_category(description):

    description = description.lower()

    for key , values in config.category.items():
        for value in values:
            if value in description:
                return key

    return "Others"

def categ(df):
    df['Category'] = df['Description'].apply(assign_category)
    return df

