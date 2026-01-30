import streamlit as st

st.title("ECOTEK 🌱")

if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    st.write("Select your facility type")

    facility_type = st.radio(
        "You are a:",
        ["Hostel", "Hotel", "Community Apartment"]
    )

    if st.button("Next"):
        st.session_state.facility_type = facility_type
        st.session_state.page = 2
        st.rerun()  


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
        st.rerun()

    
if st.session_state.page == 3:
    st.subheader("Pickup Request Summary")

    details = st.session_state.details

    st.write(f"**Facility Type:** {details['facility_type']}")
    st.write(f"**Name:** {details['name']}")
    st.write(f"**Area:** {details['area']}")
    st.write(f"**Address:** {details['address']}")
    st.write(f"**Food Type:** {details['food_type']}")
    st.write(f"**Quantity:** {details['quantity']}")

    st.markdown("---")

    if st.button("Confirm & Search Handler"):
        st.session_state.page = 4
        st.rerun()

    
if st.session_state.page == 4:
    st.subheader("Searching for available waste handlers...")

    with st.spinner("Matching based on location and food type..."):
        import time
        time.sleep(2)

    handlers = [
        {"name": "GreenGrow Compost", "area": "Anna Nagar", "phone": "9876543210"},
        {"name": "EcoCycle Solutions", "area": "Tambaram", "phone": "9123456789"},
        {"name": "CleanEarth Collective", "area": "Velachery", "phone": "9988776655"}
    ]

    assigned_handler = handlers[0]

    st.session_state.assigned_handler = assigned_handler
    st.session_state.page = 5
    st.rerun()


if st.session_state.page == 5:
    st.subheader("Select Preferred Pickup Time")

    time_slot = st.selectbox(
        "Available time slots",
        [
            "9:00 AM – 11:00 AM",
            "11:00 AM – 1:00 PM",
            "2:00 PM – 4:00 PM",
            "4:00 PM – 6:00 PM"
        ]
    )

    if st.button("Confirm Pickup Time"):
        st.session_state.pickup_time = time_slot
        st.session_state.page = 6
        st.rerun()

    
if st.session_state.page == 6:
    handler = st.session_state.assigned_handler
    details = st.session_state.details
    pickup_time = st.session_state.pickup_time

    st.success("✅ Pickup Confirmed!")

    st.write(f"**Assigned Handler:** {handler['name']}")
    st.write(f"**Contact:** {handler['phone']}")
    st.write(f"**Pickup Time:** {pickup_time}")

    st.markdown("## 🌍 Environmental Impact")

    quantity_str = details["quantity"]
    if "Less than" in quantity_str:
        waste = 0.5
    else:
        waste = float(quantity_str.split("-")[0])

    co2_saved = waste * 0.5
    eco_points = int(waste * 10)

    st.write(f"**Waste diverted:** {waste} kg")
    st.write(f"**Estimated CO₂ emissions avoided:** {co2_saved:.1f} kg")
    st.write(f"**EcoPoints earned:** 🌱 {eco_points}")