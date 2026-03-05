# Software Developer Salary Prediction

A Machine Learning web application that predicts software developer salaries based on country, education level, and years of professional experience. Built with Python and Streamlit, using data from the **Stack Overflow Developer Survey 2023**.

---

##  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [How It Works](#how-it-works)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Training](#model-training)
  - [Web Application](#web-application)
- [Usage](#usage)
  - [Predict Page](#predict-page)
  - [Explore Page](#explore-page)
- [Dataset](#dataset)
- [Model](#model)

---

## Overview

This project uses real-world survey data to build a regression model capable of estimating annual salaries for software developers around the globe. The trained model is served through an interactive Streamlit dashboard that offers two modes:

1. **Predict** — enter your country, education level, and years of experience to get a salary estimate.
2. **Explore** — visualise salary trends across countries and experience levels using interactive charts.

---

## Features

-  Supports **80+ countries** from the Stack Overflow Developer Survey
-  Accounts for **4 education levels** (Less than a Bachelor's, Bachelor's, Master's, Post-grad)
-  Years of experience slider (0 – 30 years)
-  Interactive **pie chart** showing the distribution of survey respondents by country
-  Interactive **bar chart** showing mean salary per country
-  Interactive **line chart** showing mean salary by years of professional experience
-  Fast predictions served by a pre-trained, serialised model (`saved_steps.pkl`)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | [Streamlit](https://streamlit.io/) |
| Data Processing | [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| Visualisation | [Matplotlib](https://matplotlib.org/) |
| Machine Learning | [Scikit-learn](https://scikit-learn.org/) |
| Model Serialisation | `pickle` (built-in) |
| Notebook | [Jupyter](https://jupyter.org/) |

---

## Project Structure

```
MlProject-for-Salary-Pediction/
├── app.py                    # Main Streamlit entry point
├── predict_page.py           # Salary prediction UI and inference logic
├── explore_page.py           # Data exploration and visualisation UI
├── SalaryPrediction.ipynb    # Jupyter notebook: EDA, preprocessing & model training
├── saved_steps.pkl           # Serialised model + label encoders
└── README.md
```

> **Note:** The raw dataset file `survey_results_public.csv` (Stack Overflow Developer Survey 2023) is **not** included in this repository due to its size. See the [Dataset](#dataset) section for download instructions.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RH2004/MlProject-for-Salary-Pediction.git
   cd MlProject-for-Salary-Pediction
   ```

2. **Install dependencies**

   ```bash
   pip install streamlit pandas numpy matplotlib scikit-learn
   ```

3. **Download the dataset** *(only needed to re-train the model or use the Explore page)*

   Download `survey_results_public.csv` from the [Stack Overflow Annual Developer Survey](https://survey.stackoverflow.co/) and place it in the project root directory.

### Running the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## How It Works

### Data Preprocessing

The raw Stack Overflow survey data is cleaned and filtered in both the Jupyter notebook and `explore_page.py`:

- Only the columns `Country`, `EdLevel`, `YearsCodePro`, `Employment`, and `ConvertedCompYearly` are retained.
- Rows with missing values are dropped.
- Only **full-time employed** respondents are kept.
- Salary outliers are removed (keeping salaries between **$10,000** and **$250,000**).
- Countries with fewer than **400 respondents** are grouped into an **"Other"** category.
- `YearsCodePro` edge values (`"Less than 1 year"` → `0.5`, `"More than 50 years"` → `50`) are normalised to numeric values.
- `EdLevel` is mapped to four clean categories: `Less than a Bachelors`, `Bachelor's degree`, `Master's degree`, `Post grad`.

### Model Training

The model training workflow is documented in `SalaryPrediction.ipynb`:

1. Categorical features (`Country`, `EdLevel`) are encoded with `LabelEncoder`.
2. A regression model is trained on the preprocessed features.
3. The trained model and label encoders are serialised to `saved_steps.pkl` using `pickle`.

### Web Application

`app.py` uses Streamlit's sidebar to let the user switch between two pages:

- **Predict** → `predict_page.py` loads the saved model, collects user inputs, and outputs the predicted annual salary.
- **Explore** → `explore_page.py` loads and visualises the survey data with three charts.

---

## Usage

### Predict Page

1. Select your **Country** from the dropdown.
2. Choose your **Education Level**.
3. Drag the **Years of Experience** slider.
4. Click **"Calculate Salary"** to see the estimated annual salary in USD.

### Explore Page

The Explore page displays three visualisations derived from the Stack Overflow Developer Survey 2023:

| Chart | Description |
|---|---|
| Pie chart | Share of survey respondents by country |
| Bar chart | Mean annual salary by country |
| Line chart | Mean annual salary by years of professional experience |

---

## Dataset

This project uses the publicly available **Stack Overflow Annual Developer Survey 2023**.

- 🔗 Download: [https://survey.stackoverflow.co/](https://survey.stackoverflow.co/)
- File required: `survey_results_public.csv`
- Place the file in the **project root directory** before running the Explore page or re-training the model.

---

## Model

The pre-trained model is stored in `saved_steps.pkl` and contains:

| Key | Description |
|---|---|
| `model` | Trained regression model (scikit-learn) |
| `le_country` | `LabelEncoder` fitted on country labels |
| `le_education` | `LabelEncoder` fitted on education level labels |

To retrain the model, open and run `SalaryPrediction.ipynb` after placing the dataset in the project root. The notebook will overwrite `saved_steps.pkl` with the newly trained artefacts.
