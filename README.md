# 🔪 Minimal Wastage Bar Cutting App

A simple Streamlit app to calculate the optimal way to cut stock bars into required lengths with minimal wastage.

This app helps users input a stock bar length and a list of required cut lengths, then calculates a cutting plan that minimizes wastage. It's useful for manufacturing, construction, and other fields where material optimization is important.

<img width="1170" height="2532" alt="cutting streamlit app_(iPhone 12 Pro) (1)" src="https://github.com/user-attachments/assets/ba4119ab-2ece-4f77-b6a9-0f38c1e54fdf" />



[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cutting.streamlit.app/)

## Features

- **Input stock bar length** and required cut lengths (comma-separated).
- **Automatic calculation** of a minimal-waste cutting plan using a simple greedy algorithm.
- **Results breakdown**: See how each bar is cut, individual waste, total bars used, and total waste.
- **Error handling**: Warns if a cut exceeds stock length or if input is invalid.

## How to run locally

1. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app**

   ```
   streamlit run streamlit_app.py
   ```

## Example Usage

Enter your stock bar length (e.g., `70.00`) and required cut lengths (e.g., `43.00, 42.50, 35.30, 29.00, 29.00, 25.00, 25.00`). Press "Calculate Cutting Plan" to view the optimal cutting plan and total waste.

## Author

Sharad Rai

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
