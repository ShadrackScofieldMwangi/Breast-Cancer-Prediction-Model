Breast Cancer Prediction Model

A supervised machine learning classification project that predicts the likelihood of breast cancer based on patient clinical data. This repository demonstrates the full modeling pipeline—from data preprocessing and visualization to model training and evaluation—using Python and scikit‑learn.

🎯 Project Overview

Early detection of breast cancer can significantly improve treatment outcomes. This project uses a machine learning model to analyze patient features (such as mean radius, texture, perimeter, area, smoothness, etc.) and predict whether a tumor is benign or malignant.

The model was developed using the well‑known Breast Cancer Wisconsin (Diagnostic) Dataset, and classification performance is evaluated using metrics like accuracy and confusion matrix.

📁 Repository Structure

├── Breast Cancer Prediction Model.ipynb   # Main Jupyter Notebook

├── data.csv                              # Breast cancer dataset

├── README.md                             # Project documentation

└── (Optional) requirements.txt           # Python dependencies

🧰 Tools & Libraries

This project uses:

Python

pandas – Data manipulation and loading

NumPy – Numerical operations

scikit‑learn – Machine learning modeling and evaluation

Matplotlib & Seaborn – Visualization

Jupyter Notebook – Interactive development

🔍 How It Works

The notebook implements the complete workflow:

1. Data Loading

Load the breast cancer dataset (data.csv) into a pandas DataFrame.

2. Exploratory Data Analysis (EDA)

Inspect the dataset structure, feature distributions, and class balance between benign and malignant cases.

3. Feature Selection

Separate the input features from the target label (diagnosis).

4. Data Preprocessing

Encode categorical labels into numeric form.

Split the data into training and testing sets.

5. Model Training

Train a classification algorithm (e.g., Logistic Regression, Random Forest, etc.) using the training set.

6. Evaluation

Evaluate the model using:

Accuracy score

Confusion matrix

Classification report (Precision, Recall, F1‑Score)

7. Prediction

Use the trained model to make predictions on new patient data.

🛠️ Getting Started
1. Clone the Repository
   
git clone https://github.com/ShadrackScofieldMwangi/Breast-Cancer-Prediction-Model.git

cd Breast-Cancer-Prediction-Model

3. Install Dependencies

Make sure you have Python 3.7+ installed. Then install required packages:

pip install pandas numpy scikit-learn matplotlib seaborn notebook

3. Run the Notebook

Start Jupyter Notebook:

jupyter notebook "Breast Cancer Prediction Model.ipynb"

Follow the notebook steps to:

Explore and understand the dataset

Train the classifier

Visualize performance metrics

Predict cancer status for new samples

📊 Example Output

The notebook includes:

Accuracy score showing overall predictive performance

Confusion matrix illustrating prediction vs. truth

Classification metrics (precision, recall, F1‑score)

These help you assess how well the model distinguishes between benign and malignant tumors.

📈 Results & Insights

You’ll find:

Clear visualizations of feature distributions

Understanding of class separability

Evaluation summaries that explain model strengths and limitations

These make the model practical for educational and exploratory purposes.

🤝 Contributing

Your contributions are welcome! You can:

⭐ Star the repository

📥 Open issues for bugs or feature ideas

✨ Submit pull requests
