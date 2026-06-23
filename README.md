# 🏏 IPL Match Winner Predictor using XGBoost

An end-to-end Machine Learning project that predicts the winner of an Indian Premier League (IPL) match using historical IPL data and an XGBoost classification model. The project includes data cleaning, exploratory data analysis, model building, and an interactive Streamlit web application.

---

## 🚀 Features

* Predicts the winner of an IPL match
* Uses XGBoost Machine Learning algorithm
* Displays winning probability
* Interactive Streamlit web application
* Supports only current IPL teams and venues
* User-friendly interface with progress bars and animations

---

## 📊 Dataset

The project uses historical IPL match data containing:

* Team 1
* Team 2
* Toss Winner
* Toss Decision
* Match Venue
* Match Winner

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Streamlit
* Pickle

---

## 📈 Exploratory Data Analysis (EDA)

The project includes:

* Top batting stadiums analysis
* Team performance analysis
* Toss impact analysis
* Venue-based statistics
* Match trends and visualizations
* Data cleaning and preprocessing

---

## 🤖 Machine Learning Pipeline

Data Collection → Data Cleaning → Feature Engineering → Label Encoding → Train-Test Split → XGBoost Model Training → Prediction → Streamlit Deployment

### Input Features

* Team 1
* Team 2
* Toss Winner
* Toss Decision
* Venue

### Target

* Match Winner

---


### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Sample Prediction

Input:

* Team 1: Chennai Super Kings
* Team 2: Mumbai Indians
* Toss Winner: Chennai Super Kings
* Toss Decision: Bat
* Venue: MA Chidambaram Stadium, Chepauk, Chennai

Output:

* Predicted Winner: Chennai Super Kings
* Winning Probability: 68.42%

---

## 📸 Application Preview

<img width="100%" alt="IPL Predictor Screenshot" src="screenshots/app.png">

---

## 🔮 Future Improvements

* Add team logos
* Head-to-head statistics
* Recent form analysis
* Player statistics integration
* Live IPL API integration
* Cloud deployment
* Dark mode interface
* Feature importance visualization

---

## 👨‍💻 Author

**Lionel Haris**

* LinkedIn: https://www.linkedin.com/in/lionel-haris-163b0a2b8/
* GitHub: https://github.com/lionelharis

---

⭐ If you found this project useful, please give it a star.
