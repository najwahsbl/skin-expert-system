import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="SkinGlow Expert System",
    page_icon="✨",
    layout="centered"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #fff5f7, #fffdfd);
}

h1 {
    color: #ff4f8b;
    text-align: center;
    font-size: 50px;
}

h2, h3 {
    color: #ff4f8b;
}

p {
    font-size: 17px;
}

.stSelectbox label,
.stMultiSelect label {
    font-size: 17px;
    font-weight: 600;
}

.stButton>button {
    background-color: #ff4f8b;
    color: white;
    border-radius: 14px;
    border: none;
    height: 55px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #ff2f75;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("✨ SkinGlow Expert System")

st.markdown("""
<center>
Discover skincare ingredients and products tailored to your skin needs.
</center>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------------
# USER INPUT
# -----------------------------------

skin_type = st.selectbox(
    "What is your skin type?",
    ["Oily", "Dry", "Combination", "Sensitive"]
)

skin_concern = st.selectbox(
    "What is your main skin concern?",
    ["Acne", "Dark Spots", "Redness", "Wrinkles", "Large Pores"]
)

routine = st.selectbox(
    "Do you currently use skincare products?",
    ["Yes", "No"]
)

avoid = st.multiselect(
    "Ingredients you would like to avoid",
    ["Alcohol", "Fragrance", "Paraben", "Essential Oils"]
)

budget = st.selectbox(
    "Your budget range",
    ["Budget Friendly", "Mid Range", "Premium"]
)

st.divider()

# -----------------------------------
# CURRENT PRODUCTS
# -----------------------------------

st.subheader("🧴 Current Skincare Products")

cleanser = st.selectbox(
    "Cleanser",
    [
        "None",
        "Oil-Control Gel Cleanser",
        "Hydrating Cream Cleanser",
        "Gentle Foam Cleanser",
        "Soothing Sensitive Cleanser"
    ]
)

toner = st.selectbox(
    "Toner",
    [
        "None",
        "Hydrating Toner",
        "Balancing Toner",
        "Pore Refining Toner",
        "Calming Toner"
    ]
)

serum = st.selectbox(
    "Serum",
    [
        "None",
        "Niacinamide Serum",
        "Vitamin C Serum",
        "Hyaluronic Acid Serum",
        "Centella Serum"
    ]
)

moisturizer = st.selectbox(
    "Moisturizer",
    [
        "None",
        "Oil-Free Moisturizer",
        "Ceramide Moisturizer",
        "Gel Moisturizer",
        "Barrier Repair Moisturizer"
    ]
)

sunscreen = st.selectbox(
    "Sunscreen",
    [
        "None",
        "Matte Sunscreen",
        "Hydrating Sunscreen",
        "Gel Sunscreen",
        "Mineral Sunscreen"
    ]
)

st.divider()

# -----------------------------------
# ANALYSIS
# -----------------------------------

if st.button("✨ Analyze My Skin"):

    st.subheader("🌸 Recommended Ingredients")

    # -----------------------------------
    # OILY
    # -----------------------------------

    if skin_type == "Oily":

        st.success("✨ Salicylic Acid")
        st.write("Controls excess oil, unclogs pores and reduces acne.")

        st.success("✨ Niacinamide")
        st.write("Minimizes pores and balances sebum production.")

        st.subheader("🇲🇾 Malaysian Product Recommendations")

        st.markdown("""
- **SimpleSiti Oil Control Cleanser**
- **Skintific Niacinamide Serum**
- **Safi Acne Solutions Moisturizer**
- **Wardah UV Shield Sunscreen Gel**
        """)

    # -----------------------------------
    # DRY
    # -----------------------------------

    elif skin_type == "Dry":

        st.success("✨ Hyaluronic Acid")
        st.write("Provides deep hydration and keeps skin moisturized.")

        st.success("✨ Ceramide")
        st.write("Strengthens and repairs skin barrier.")

        st.subheader("🇲🇾 Malaysian Product Recommendations")

        st.markdown("""
- **Nano White Hydrating Cleanser**
- **Hada Labo Hydrating Lotion**
- **Aiken Prebiotic Moisturizer**
- **Wardah Hydramild Sunscreen**
        """)

    # -----------------------------------
    # COMBINATION
    # -----------------------------------

    elif skin_type == "Combination":

        st.success("✨ Niacinamide")
        st.write("Balances oily and dry areas of the skin.")

        st.success("✨ Vitamin C")
        st.write("Brightens skin and reduces dark spots.")

        st.subheader("🇲🇾 Malaysian Product Recommendations")

        st.markdown("""
- **Safi Balqis Cleanser**
- **Skintific Vitamin C Serum**
- **SimplySiti Brightening Moisturizer**
- **Biore UV Aqua Sunscreen**
        """)

    # -----------------------------------
    # SENSITIVE
    # -----------------------------------

    elif skin_type == "Sensitive":

        st.success("✨ Centella Asiatica")
        st.write("Calms irritation and reduces redness.")

        st.success("✨ Aloe Vera")
        st.write("Soothes and hydrates sensitive skin gently.")

        st.subheader("🇲🇾 Malaysian Product Recommendations")

        st.markdown("""
- **Aiken Tea Tree Cleanser**
- **Cosmoderm Soothing Toner**
- **Skintific Centella Serum**
- **Wardah Mineral Sunscreen**
        """)

# -----------------------------------
# INGREDIENT GUIDE
# -----------------------------------

st.divider()

st.subheader("📖 Ingredient Reference Guide")

ingredient_data = {
    "Ingredient": [
        "Salicylic Acid",
        "Niacinamide",
        "Hyaluronic Acid",
        "Ceramide",
        "Vitamin C",
        "Centella Asiatica",
        "Aloe Vera"
    ],

    "Best For": [
        "Oily Skin",
        "Oily / Combination",
        "Dry Skin",
        "Dry / Sensitive",
        "Combination Skin",
        "Sensitive Skin",
        "Sensitive Skin"
    ],

    "Benefits": [
        "Controls acne and oil",
        "Balances oil and minimizes pores",
        "Deep hydration",
        "Repairs skin barrier",
        "Brightens dark spots",
        "Calms irritation",
        "Soothes sensitive skin"
    ]
}

st.table(ingredient_data)
