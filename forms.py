import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

# Load dataset to populate dropdown choices
data = pd.read_csv("few_laptop_data_clean.csv")

class InputForm(FlaskForm):
    Company = SelectField(
        "Company",
        choices=[(c, f"Choose {c}") for c in sorted(data["Company"].unique())],
        validators=[DataRequired()]
    )
    TypeName = SelectField(
        "Type Name",
        choices=[(t, f"Type: {t}") for t in sorted(data["TypeName"].unique())],
        validators=[DataRequired()]
    )
    Ram = SelectField(
        "RAM (GB)",
        choices=[(str(r), f"{r} GB") for r in sorted(data["Ram"].unique())],
        validators=[DataRequired()]
    )
    OpSys = SelectField(
        "Operating System",
        choices=[(o, f"OS: {o}") for o in sorted(data["OpSys"].unique())],
        validators=[DataRequired()]
    )
    Weight = SelectField(
        "Weight (kg)",
        choices=[(str(w), f"{w} kg") for w in sorted([1.0, 1.1, 1.3, 1.5, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0])],
        validators=[DataRequired()]
    )
    Touchscreen = SelectField(
        "Touchscreen",
        choices=[(0, "No (Touchscreen Disabled)"), (1, "Yes (Touchscreen Enabled)")],
        validators=[DataRequired()]
    )
    ScreenResolution = SelectField(
        "Screen Resolution and Size",
        choices=[
            ("1920x1080_15.6", "1920x1080, 15.6 Inches (Full HD)"),
            ("1366x768_14.0", "1366x768, 14.0 Inches (HD)"),
            ("2560x1440_13.3", "2560x1440, 13.3 Inches (Quad HD)"),
            ("3840x2160_17.3", "3840x2160, 17.3 Inches (4K UHD)"),
            ("1280x720_11.6", "1280x720, 11.6 Inches (HD)"),
            ("2560x1600_16.0", "2560x1600, 16.0 Inches (WQXGA)"),
            ("3440x1440_34.0", "3440x1440, 34.0 Inches (UltraWide)"),
            ("2560x1600_14.0", "2560x1600,14.0 Inches(2.5K)"),
        ],
        validators=[DataRequired()]
    )
    Cpu_Series = SelectField(
        "CPU Series",
        choices=[(cpu, f"CPU: {cpu}") for cpu in sorted(data["Cpu_Series"].unique())],
        validators=[DataRequired()]
    )
    
    SSD_Capacity_GB = SelectField(
        "SSD Capacity (GB)",
        choices=[(str(ssd), f"{ssd} GB SSD") for ssd in sorted(data["SSD_Capacity_GB"].unique())],
        validators=[DataRequired()]
    )
    Has_HDD = SelectField(
        "Has HDD",
        choices=[(0, "No (No HDD)"), (1, "Yes (Includes HDD)")],
        validators=[DataRequired()]
    )
    Dedicated_GPU = SelectField(
        "Dedicated GPU",
        choices=[(0, "No (Integrated GPU)"), (1, "Yes (Dedicated GPU)")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
