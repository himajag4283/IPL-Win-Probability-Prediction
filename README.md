## IPL WIN PROBABILITY PREDICTION

Cricket enthusiasts often find it challenging to gauge the potential outcomes of Indian Premier 
League (IPL) matches, given the dynamic nature of the sport. The lack of a user-friendly and 
data-driven tool for predicting win probabilities hinders their ability to make informed 
predictions. This project aims to address this gap by developing an IPL Win Probability 
Predictor using machine learning and Streamlit, offering users a seamless and interactive 
platform to anticipate match results based on historical data, team dynamics, and player 
performances. The goal is to provide cricket fans with a reliable and accessible tool that 
enhances their engagement with IPL matches through real-time win probability predictions.

### Dataset Description:

Two subsets of data are employed in the IPL dataset sourced from Kaggle, namely the 
"matches" dataset and the "deliveries" dataset. These subsets provide distinct sets of 
information, where the "matches" dataset  has the overall match attributes such as teams, toss 
outcomes, and results, while the "deliveries" dataset focuses on granular information at the 
level of individual deliveries, offering insights into ball-by-ball occurrences during matches. 

<img width="473" alt="image" src="https://github.com/HimajaGgithub/Project4-IPL-Win-Probability-Prediction/assets/106176277/f5a39e43-3dca-4c2f-822a-e19db23135a7">
<img width="487" alt="image" src="https://github.com/HimajaGgithub/Project4-IPL-Win-Probability-Prediction/assets/106176277/b94474fb-b590-4749-bcbe-41c0e8ba7208">


### Implementation:

<img width="339" alt="image" src="https://github.com/HimajaGgithub/Project4-IPL-Win-Probability-Prediction/assets/106176277/355ecf0e-7a0e-4ff8-8d6f-fe72ec4551ee">
This System Architecture gives the Basic Implementation of the Project.

Data Preparation and Insight: 
The dataset, eloquently encapsulated in final_df, is a harmonious amalgamation of 
information distilled from both the "matches" and "deliveries" datasets. A glimpse into 
the data, as presented by final_df.sample(), reveals a symphony of columns like 
'batting_team,' 'bowling_team,' 'city,' 'runs_left,' 'balls_left,' 'wickets,' 'total_runs_x,' 
'crr' (current run rate), 'rrr' (required run rate), and the pivotal 'result.' 

• Feature and Target Selection: 
➢ The precursor to model building involves the strategic selection of features (X). 
All columns, except 'result,' play a pivotal role here. 
➢ Meanwhile, the target variable (y) is meticulously designated as the 'result' 
column, anchoring our predictive ambitions. 

• Train-Test Split: 
Prudent model building necessitates a methodical division of our dataset into training and 
testing sets. Enter the venerable train_test_split function, judiciously segregating 80% of 
the data for model training and reserving the remaining 20% for testing our model's mettle.

Model Training: 
The model was trained using the training dataset, learning from the nuances of past 
matches. The fit method is called on the pipeline, allowing the entire process to be executed 
on the training set (X_train, y_train). 
During this phase, the model learns from the transformed features and corresponding 
labels, adjusting its parameters to make accurate predictions.

Model Prediction: 
With training complete, the model was ready to predict outcomes for the test dataset, 
offering insights into potential match results.

Model Evaluation: 
Model evaluation is the process of assessing a machine learning model's performance    
using metrics or criteria, typically involving comparisons between predicted and actual 
outcomes on a separate dataset. It aims to gauge the model's accuracy, generalization, and 
suitability for a given task.
Accuracy score: A metric measuring the proportion of correctly predicted instances, 
by comparing the predicted labels (y_pred) with the actual labels (y_test). It provides a 
single numeric value indicating the model's overall accuracy in making correct 
predictions on the test dataset. This project gave an accuracy of 81%.

Frontend development 
The front-end of the project is developed using Streamlit. Streamlit is an open-source Python 
library that simplifies the process of creating web applications for data science and machine 
learning. It is designed to be beginner-friendly, allowing users to transform data scripts into 
shareable web apps with minimal effort. 
The Streamlit frontend code represents a user-friendly interface for predicting the win 
probability of IPL matches based on key match parameters.

<img width="479" alt="image" src="https://github.com/HimajaGgithub/Project4-IPL-Win-Probability-Prediction/assets/106176277/505a2706-4095-4f79-b1b6-9af3b48af0c3">
<img width="480" alt="image" src="https://github.com/HimajaGgithub/Project4-IPL-Win-Probability-Prediction/assets/106176277/70ff3494-fa5e-4f89-aaf9-cac1d4c57bda">

