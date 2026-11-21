# Textile Mill Energy Cost Calculator

**AI234 Capstone Project | Textile Engineering | Roll No. 25TE090**  
Mehran University of Engineering and Technology (MUET), Jamshoro

## Project overview
This Streamlit web application estimates the electricity consumption and cost of a textile machine. It uses the machine power rating, operating hours, electricity tariff, and number of operating days.

## Features
- Enter machine power in kW
- Enter operating hours per day
- Enter electricity tariff in PKR per kWh
- Set the number of days for the monthly estimate
- Calculate daily and monthly energy use (kWh)
- Calculate daily and monthly estimated cost (PKR)
- Display a results table and cost chart
- Show a limitations and responsible-use note

## Formulae
- Daily energy (kWh) = Power (kW) × Hours per day
- Monthly energy (kWh) = Daily energy × Days per month
- Cost (PKR) = Energy (kWh) × Tariff (PKR/kWh)

## Run locally
1. Install Python 3.9 or later.
2. Download or clone this repository.
3. In the project folder, install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud
1. Push `app.py`, `requirements.txt`, and `README.md` to a public GitHub repository.
2. Open Streamlit Community Cloud and connect your GitHub account.
3. Choose the repository and `app.py` as the main file.
4. Deploy, then test your public app URL.

## Limitations
The result is an estimate. Actual usage and bills may vary due to load changes, machine condition, power factor, tariff structure, taxes, and other charges. The app assumes the entered power is representative of average operating power.
