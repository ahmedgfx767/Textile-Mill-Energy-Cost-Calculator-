import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Mill Energy Cost Calculator",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ Textile Mill Energy Cost Calculator")
st.caption("AI234 Capstone Project | Textile Engineering | Roll No. 25TE090")

st.write(
    "Estimate electricity consumption and cost for a textile machine "
    "using its power rating, operating hours, and electricity tariff."
)

st.subheader("Enter machine details")
machine_name = st.text_input("Machine name (optional)", value="Textile machine")
power_kw = st.number_input("Machine power (kW)", min_value=0.0, value=50.0, step=1.0)
hours_per_day = st.number_input(
    "Operating hours per day", min_value=0.0, max_value=24.0, value=16.0, step=0.5
)
tariff = st.number_input(
    "Electricity rate (PKR per kWh)", min_value=0.0, value=40.0, step=1.0
)
days_per_month = st.number_input(
    "Days used for monthly estimate", min_value=1, max_value=31, value=30, step=1
)

if st.button("Calculate energy and cost", type="primary", use_container_width=True):
    daily_energy = power_kw * hours_per_day
    monthly_energy = daily_energy * days_per_month
    daily_cost = daily_energy * tariff
    monthly_cost = monthly_energy * tariff

    st.subheader("Estimated results")
    col1, col2 = st.columns(2)
    col1.metric("Daily energy", f"{daily_energy:,.2f} kWh")
    col2.metric("Monthly energy", f"{monthly_energy:,.2f} kWh")
    col3, col4 = st.columns(2)
    col3.metric("Daily cost", f"Rs. {daily_cost:,.2f}")
    col4.metric("Monthly cost", f"Rs. {monthly_cost:,.2f}")

    results = pd.DataFrame(
        {
            "Period": ["Daily", "Monthly"],
            "Energy (kWh)": [daily_energy, monthly_energy],
            "Estimated Cost (PKR)": [daily_cost, monthly_cost],
        }
    )
    st.dataframe(results, use_container_width=True, hide_index=True)
    st.bar_chart(results.set_index("Period")[["Estimated Cost (PKR)"]])

    st.success(f"Estimate for: {machine_name or 'Textile machine'}")
    st.info(
        "Formula: Energy (kWh) = Power (kW) × Operating hours. "
        "Cost (PKR) = Energy (kWh) × Electricity rate."
    )

st.divider()
st.subheader("Limitations & Responsible Use")
st.write(
    "This calculator provides an approximate estimate, not an actual electricity bill. "
    "It assumes the entered power is the average operating power and does not account "
    "for changing machine loads, power factor, taxes, peak/off-peak tariffs, or other "
    "billing charges. Results depend on the accuracy of user inputs."
)
