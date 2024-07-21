import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('iplwinmodel.pkl','rb'))
st.title('IPL WIN PROBABILITY PREDICTION')
st.markdown("The IPL Win Probability Predictor app uses machine learning to analyze match data, team performance, and player statistics, offering real-time predictions on the likelihood of an IPL team winning. It enhances viewer engagement during matches by providing accurate and insightful forecasts.\n Enter the values of the seccond innings!!")
st.write("## About")
st.write("1. Adjust the input parameters in the sidebar.")
st.write("2. Click the 'Predict Win Probability' button.")
st.write("3. View the predicted win probability in the result section.")


col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.sidebar.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.sidebar.number_input('Score')
with col4:
    overs = st.sidebar.number_input('Overs completed')
with col5:
    wickets = st.sidebar.number_input('Wickets out')


if st.button('Predict Win Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.write("## Win probability predictions")
    st.subheader(f"{batting_team} - {round(win * 100, 2)}%")
    st.subheader(f"{bowling_team} - {round(loss * 100, 2)}%")
    labels = [batting_team, bowling_team]
    sizes = [win, loss]
    colors = ['green', 'coral']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.2f%%', colors=colors, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Add a title
    ax.set_title('Win Probability Prediction')
    fig.patch.set_facecolor('#f0f0f0')

    # Show the chart in Streamlit
    st.pyplot(fig)



