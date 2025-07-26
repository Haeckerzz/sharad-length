import streamlit as st


def minimal_waste_bar_cut(stock_length, required_lengths):
    required_lengths = sorted(required_lengths, reverse=True)
    bars = []
    while required_lengths:
        bar = []
        remaining = stock_length
        to_remove = []
        for i, length in enumerate(required_lengths):
            if length <= remaining:
                bar.append(length)
                remaining -= length
                to_remove.append(i)
        bars.append(bar)
        for i in reversed(to_remove):
            required_lengths.pop(i)
    return bars


st.set_page_config(
    layout="centered", page_title="length app", page_icon="🔪")

st.title("🔪 Minimal Wastage Bar Cutting")

st.markdown(
    "<div style='text-align:right'>"
    "Author: Sharad Rai (<a href='tel:+91 93011 97505'>+91 93011 97505</a>)"
    "</div>",
    unsafe_allow_html=True,
)

stock_length = st.number_input(
    "Enter stock bar length", value=100.00, min_value=0.1, format="%.2f")
cut_lengths_input = st.text_area(
    "Enter required cut lengths (comma-separated)",
    value="43.00, 43.00, 43.00, 43.00, 42.50, 42.50, 35.30, 35.30, 35.30, 35.30, 35.00, 35.00, 35.00, 33.30, 33.30, 29.00, 29.00, 25.00, 25.00"
)

if st.button("Calculate Cutting Plan"):
    try:
        required_lengths = [float(x.strip())
                            for x in cut_lengths_input.split(',') if x.strip()]
        if any(l > stock_length for l in required_lengths):
            st.error("❌ A cut length exceeds the stock bar length.")
        elif not required_lengths:
            st.warning("⚠️ Please provide at least one cut length.")
        else:
            bars = minimal_waste_bar_cut(stock_length, required_lengths)
            total_waste = 0

            with st.expander("Click to view detailed breakdown (closed by default)", expanded=False):
                for idx, bar in enumerate(bars, 1):
                    bar_sum = sum(bar)
                    waste = stock_length - bar_sum
                    total_waste += waste
                    bar_cuts = ", ".join(f"{x:.2f}" for x in bar)
                    st.markdown(
                        f"""
                        <div style="background-color:#F0F2F6; border-left:6px solid #4CAF50;
                                    padding:12px; margin-bottom:10px; border-radius:6px;">
                            <span style="font-size:1.1rem; font-weight:bold;">Bar {idx}:</span>
                            <span style="color:#1a237e">cuts = [{bar_cuts}]</span>
                            <span style="font-size:1rem;"> | </span>
                            <span style="color:#c0392b; font-size:1.1rem;"><b>waste:</b> {waste:.2f}</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            st.markdown(
                f"<h3 style='color:#4CAF50;'>Total bars used: {len(bars)}</h3>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<h4 style='color:#FF5722;'>Total waste: {total_waste:.2f}</h4>",
                unsafe_allow_html=True
            )
    except ValueError:
        st.error(
            "Invalid input: Ensure all cut lengths are numbers, separated by commas.")
