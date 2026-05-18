# ============================================
# LOAN APPROVAL PREDICTION SYSTEM
# ============================================

# Import Libraries

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)

# ============================================
# LOAD DATASET
# ============================================

df = pd.read_csv(
    "processed_loan_dataset.csv"
)

# ============================================
# FEATURES AND TARGET
# ============================================

X = df.drop(
    "LoanApproved",
    axis=1
)

y = df["LoanApproved"]

# ============================================
# TRAIN MODEL
# ============================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ============================================
# USER INPUT SECTION
# ============================================

try:

    print("\n===== Loan Approval Prediction =====")

    gender = int(input(
        "Enter Gender (0=Female, 1=Male): "
    ))

    age = float(input(
        "Enter Age: "
    ))

    monthly_income = float(input(
        "Enter Monthly Income: "
    ))

    loan_amount = float(input(
        "Enter Loan Amount: "
    ))

    credit_score = float(input(
        "Enter Credit Score: "
    ))

    employment_status = int(input(
        "Employment Status "
        "(0=Employed,1=Self-Employed,2=Unemployed): "
    ))

    existing_loans = float(input(
        "Existing Loans Count: "
    ))

    loan_term = float(input(
        "Loan Term (months): "
    ))

    property_area = int(input(
        "Property Area "
        "(0=Rural,1=Semi-Urban,2=Urban): "
    ))

    # ========================================
    # INPUT VALIDATION
    # ========================================

    if age < 18 or age > 65:
        raise ValueError(
            "Age must be between 18 and 65."
        )

    if monthly_income <= 0:
        raise ValueError(
            "Income must be positive."
        )

    if loan_amount <= 0:
        raise ValueError(
            "Loan Amount must be positive."
        )

    if credit_score < 300 or credit_score > 900:
        raise ValueError(
            "Credit Score must be between 300 and 900."
        )

    # ========================================
    # CREATE INPUT DATAFRAME
    # ========================================

    input_data = pd.DataFrame([{

        "ApplicantID": 9999,

        "Gender": gender,

        "Age": age,

        "MonthlyIncome": monthly_income,

        "LoanAmount": loan_amount,

        "CreditScore": credit_score,

        "EmploymentStatus": employment_status,

        "ExistingLoans": existing_loans,

        "LoanTerm": loan_term,

        "PropertyArea": property_area
    }])

    # ========================================
    # PREDICTION
    # ========================================

    prediction = model.predict(
        input_data
    )

    # ========================================
    # OUTPUT RESULT
    # ========================================

    print("\n===== Prediction Result =====")

    if prediction[0] == 1:

        print(
            "Loan Approved"
        )

    else:

        print(
            "Loan Rejected"
        )

# ============================================
# ERROR HANDLING
# ============================================

except ValueError as ve:

    print("\nInput Error:", ve)

except Exception as e:

    print("\nUnexpected Error:", e)