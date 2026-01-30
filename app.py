import streamlit as st

st.title("ECOTEK 🌱")

# initialize page state
if "page" not in st.session_state:
    st.session_state.page = 1

# PAGE 1 — Facility type selection
if st.session_state.page == 1:
    st.write("Select your facility type")

    facility_type = st.radio(
        "You are a:",
        ["Hostel", "Hotel", "Community Apartment"]
    )

    if st.button("Next"):
        st.session_state.facility_type = facility_type
        st.session_state.page = 2


# PAGE 2 — Waste details form
if st.session_state.page == 2:
    st.subheader("Enter Waste Details")

    name = st.text_input("Name of place")
    area = st.text_input("Area / Locality")
    address = st.text_area("Address")

    quantity = st.selectbox(
        "Approximate quantity of waste (kg)",
        ["Less than 1KG", "1-5 KG", "5-10 KG", "10-50KG", "50-100 KG"]
    )

    food_type = st.selectbox(
        "Type of food waste",
        ["Raw", "Cooked", "Mixed"]
    )

    if st.button("Request Pickup"):
        st.session_state.details = {
            "facility_type": st.session_state.facility_type,
            "name": name,
            "area": area,
            "address": address,
            "quantity": quantity,
            "food_type": food_type
        }
        st.session_state.page = 3
    
    if st.session_state.page == 3:
        st.subheader("Pickup Request Summary")

        details = st.session_state.details

        st.write(f"**Facility Type:** {details['facility_type']}")
        st.write(f"**Name:** {details['name']}")
        st.write(f"**Area:** {details['area']}")
        st.write(f"**Address:** {details['address']}")
        st.write(f"**Food Type:** {details['food_type']}")
        st.write(f"**Quantity:** {details['quantity']} kg")

        st.markdown("---")

    if st.button("Confirm & Search Handler"):
        st.session_state.page = 4
