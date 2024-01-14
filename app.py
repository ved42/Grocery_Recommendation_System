import streamlit as st
import pandas as pd
import numpy as np
import pickle

food_dict = pickle.load(open('food_dict.pkl','rb'))
foods = pd.DataFrame(food_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Grocery Recommender System')
foods=foods[foods['Health Goals']!='nan']

from collections import Counter

def recommend(health_goals):
    food_index = foods[foods['Health Goals'] == health_goals].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    preferred_foods = []

    for i in food_list:
        preferred_foods.extend(foods.iloc[i[0]].Preferred_Foods.split(', '))

    # Count the occurrences of each food
    food_counts = Counter(preferred_foods)


    top_3_foods = food_counts.most_common(5)
    food_item=[]

    for food, count in top_3_foods:
        food_item.append(food)
    return food_item

selected_health_goals_name = st.selectbox(
 'Please select  from following options',
 foods['Health Goals'].unique())


if st.button('Recommend'):
    recommendations=recommend(selected_health_goals_name)
    for i in recommendations:
        st.write(i)
