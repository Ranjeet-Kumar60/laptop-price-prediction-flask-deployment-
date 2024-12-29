import pandas as pd
from flask import Flask, render_template
from forms import InputForm
import joblib
import numpy as np

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Load the trained model
model = joblib.load("model.joblib")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    prediction = None
    if form.validate_on_submit():
        # Extract the selected resolution and size
        resolution_and_size = form.ScreenResolution.data
        resolution, inches = resolution_and_size.split("_")
        screen_width, screen_height = map(int, resolution.split("x"))
        inches = float(inches)

        # Calculate PPI
        ppi = np.sqrt(screen_width**2 + screen_height**2) / inches

        # Prepare input data for prediction
        input_data = pd.DataFrame({
            "Company": [form.Company.data],
            "TypeName": [form.TypeName.data],
            "Ram": [form.Ram.data],
            "OpSys": [form.OpSys.data],
            "Weight": [form.Weight.data],
            "Touchscreen": [form.Touchscreen.data],
            "PPI": [ppi],
            "Cpu_Series": [form.Cpu_Series.data],
            "SSD_Capacity_GB": [form.SSD_Capacity_GB.data],
            "Has_HDD": [form.Has_HDD.data],
            "Dedicated_GPU": [form.Dedicated_GPU.data],
        })

        # Predict the log-transformed price
        log_prediction = model.predict(input_data)[0]

        # Reverse the log-transformation
        prediction = np.expm1(log_prediction)

        # Format the price for display
        prediction = f"Predicted Price: ₹{prediction:,.0f}"

        

    return render_template(
        "predict.html",
        title="Predict",
        form=form,
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
