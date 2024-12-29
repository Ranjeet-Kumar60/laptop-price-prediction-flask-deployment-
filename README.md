# Laptop Price Prediction Using Machine Learning

## Overview
This project aims to predict the price of laptops based on their specifications using various machine learning algorithms. By analyzing and preprocessing the dataset, we derived insights, handled multicollinearity, and evaluated different models to determine the most accurate predictor.

---

## About the Data
The dataset includes key details about laptops, such as:
- **Brand** (e.g., Apple, Dell)
- **Laptop Type**
- **Screen Size**
- **Screen Resolution**
- **Processor**
- **RAM**
- **Storage**
- **Graphics Card**
- **Operating System**
- **Weight**
- **Price** (Target variable)

---


## Data Preparation and Feature Engineering
1. **New Features Created**:
   - **PPI (Pixels Per Inch)**: To measure screen sharpness.
   - **Touchscreen**: Whether the laptop has a touchscreen (Yes/No).
   - **Dedicated GPU**: Whether the laptop has a dedicated graphics card.
   - **CPU Series**: Extracted CPU type (e.g., Core i5, Core i7).
   - **SSD Capacity**: Storage capacity in GB.
   - **Has HDD**: Whether the laptop has an HDD (Yes/No).


2. **Dropped Redundant Features**:
   - **`ScreenResolution_Width`** and **`ScreenResolution_Height`** due to high correlation (0.94) with **`PPI`**.
   - **`Inches`** due to low correlation with price (0.06) and high multicollinearity with `Weight`.
   - **`Has_HDD`** and **`Has_SSD`** as their predictive power was already covered by `HDD_Capacity_GB` and `SSD_Capacity_GB`.


3. **Dropped Columns**:
   - **Raw Columns**: `ScreenResolution`, `Memory`, `CPU`, `GPU` as they were transformed into more useful metrics.

---

## Algorithms Used
The following algorithms were trained and evaluated:
1. **Linear Regression**
2. **Support Vector Machine (SVR)**
3. **Random Forest**
4. **XGBoost**

---

## Model Evaluation
### R² Scores:
| Model                  | Train R² | Test R² |
|------------------------|----------|---------|
| **Linear Regression**  | 0.84     | 0.82    |
| **SVR**                | 0.93     | 0.86    |
| **Random Forest**      | 0.98     | 0.86   |
| **XGBoost**            | 0.96     | 0.86   |

### Insights:
- **XGBoost** and emerged as the best-performing models with minimal overfitting.
- **Linear Regression** exhibited underfitting and struggled with the dataset's complexity.
- **SVR** showed consistent improvement with larger training data, indicating potential for further tuning.
- **Random Forest** starts high and consistently increase the tarining score as the training size increase.
---

## Visualizations
1. **Feature Correlation**: Heatmap showcasing multicollinearity among features.
2. **Learning Curves**: Insights into model generalization and overfitting/underfitting patterns.
3. **Price Distribution**:
   - Based on `Dedicated GPU` vs `Integrated GPU`.
   - Across different operating systems (Windows, MacOS, Linux).
4. **Model Performance**:
   - Learning curves for all algorithms.

---

## Conclusion
- The project demonstrates that **XGBoost** are optimal models for laptop price prediction.
- Feature engineering and multicollinearity handling were crucial for improving model accuracy and interpretability.

---

## How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
