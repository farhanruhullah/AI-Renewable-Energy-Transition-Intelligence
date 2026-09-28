# =====================================================
# PART 1/4
# AI Renewable Energy Transition Intelligence
# =====================================================


import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import shap



# =====================================================
# PAGE CONFIGURATION
# =====================================================


st.set_page_config(

    page_title="AI Energy Transition Intelligence",

    page_icon="🌍",

    layout="wide"

)



# =====================================================
# UI POLISH STYLE
# =====================================================


st.markdown(

    """

<style>


.kpi-card {

    background-color: white;

    padding: 18px;

    border-radius: 12px;

    border: 1px solid #e5e7eb;

    text-align: center;

    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);

}



.kpi-title {

    font-size: 14px;

    color: #666;

}



.kpi-value {

    font-size: 30px;

    font-weight: 700;

    color: #111827;

}



.section-title {

    font-size: 22px;

    font-weight: 700;

    margin-top: 20px;

}


</style>


""",

unsafe_allow_html=True

)



# =====================================================
# HEADER
# =====================================================


st.title(
    "🌍 AI Renewable Energy Transition Intelligence"
)


st.markdown(

    """

### AI-powered energy analytics, transition assessment, and decision support


**Machine Learning • Explainable AI • Energy Analytics • Scenario Simulation**


"""

)



# =====================================================
# LOAD DATA AND MODEL
# =====================================================



@st.cache_data

def load_data():

    return pd.read_csv(

        "data/renewable_energy_transition_ENHANCED_FINAL.csv"

    )



df = load_data()



model = joblib.load(

    "models/co2_emission_model_enhanced_time_validated.pkl"

)

policy_db = pd.DataFrame({

    "Risk": [
        "Fossil Reduction",
        "Renewable Adoption",
        "Clean Infrastructure",
        "Transition Momentum"
    ],

    "Strategy": [

        "Reduce fossil electricity dependency and accelerate renewable deployment.",

        "Increase renewable energy capacity and improve renewable integration.",

        "Strengthen clean energy infrastructure and low-carbon technologies.",

        "Improve long-term transition planning and energy system flexibility."

    ],

    "Impact": [

        "Lower CO₂ emissions and improve transition readiness.",

        "Increase renewable electricity contribution.",

        "Support sustainable energy development.",

        "Improve future transition performance."

    ]

})



# =====================================================
# FEATURE LIST
# =====================================================



features = [

    c for c in [

        "renew_share",

        "gdp_pc",

        "population",

        "electricity_access",

        "energy_use_per_capita",


        "fossil_fuel_energy_share",

        "urban_population",


        "renewable_growth_rate",


        "fossil_dependency_index",

        "energy_transition_score",


        "renewables_share_elec",

        "solar_share_elec",

        "wind_share_elec",

        "hydro_share_elec",


        "fossil_share_elec",

        "coal_share_elec",

        "gas_share_elec",


        "low_carbon_share_elec"


    ]

    if c in df.columns

]





# =====================================================
# USER FRIENDLY FEATURE NAMES
# =====================================================



FEATURE_LABELS = {


    "renew_share":

    "Renewable Energy Share (%)",


    "gdp_pc":

    "GDP per Capita",


    "population":

    "Population",


    "electricity_access":

    "Electricity Access (%)",


    "energy_use_per_capita":

    "Energy Use per Capita",


    "fossil_fuel_energy_share":

    "Fossil Fuel Energy Share (%)",


    "urban_population":

    "Urban Population (%)",


    "renewable_growth_rate":

    "Renewable Growth Rate (%)",


    "fossil_dependency_index":

    "Fossil Dependency Index",


    "energy_transition_score":

    "Energy Transition Score",


    "renewables_share_elec":

    "Renewable Electricity Share (%)",


    "solar_share_elec":

    "Solar Electricity Share (%)",


    "wind_share_elec":

    "Wind Electricity Share (%)",


    "hydro_share_elec":

    "Hydro Electricity Share (%)",


    "fossil_share_elec":

    "Fossil Electricity Share (%)",


    "coal_share_elec":

    "Coal Electricity Share (%)",


    "gas_share_elec":

    "Gas Electricity Share (%)",


    "low_carbon_share_elec":

    "Low Carbon Electricity Share (%)"

}







# =====================================================
# ANALYSIS SCOPE
# =====================================================



scope = st.sidebar.selectbox(

    "🌍 Analysis Scope",

    [

        "All Countries"

    ]

    +

    sorted(

        df["Country Name"].unique()

    )

)



if scope == "All Countries":


    active_df = df.copy()



else:


    active_df = df[

        df["Country Name"] == scope

    ].copy()




profile = (

    active_df

    .sort_values("year")

    .iloc[-1]

)






# =====================================================
# ETRI FUNCTIONS
# =====================================================



def etri_components(row):


    return {


        "Renewable Adoption":

        (

            row.renewables_share_elec

            +

            row.solar_share_elec

            +

            row.wind_share_elec

            +

            row.hydro_share_elec

        ) / 4,



        "Fossil Reduction":

        100 -

        (

            row.fossil_share_elec

            +

            row.coal_share_elec

            +

            row.fossil_dependency_index

        ) / 3,



        "Clean Infrastructure":

        (

            row.low_carbon_share_elec

            +

            row.energy_transition_score

        ) / 2,



        "Transition Momentum":

        row.renewable_growth_rate


    }




def calculate_etri(row):


    c = etri_components(row)


    return (

        0.35 * c["Renewable Adoption"]

        +

        0.30 * c["Fossil Reduction"]

        +

        0.20 * c["Clean Infrastructure"]

        +

        0.15 * c["Transition Momentum"]

    )



# =====================================================
# NAVIGATION
# =====================================================


page = st.sidebar.radio(

    "Module",

    [

        "🌍 Intelligence Dashboard",

        "🤖 Prediction",

        "🔍 Explainable AI",

        "📊 ETRI Assessment",

        "🔮 Scenario Simulator",

        "🏛 Policy Support",

        "📘 About"

    ]

)





# =====================================================
# 🌍 INTELLIGENCE DASHBOARD
# =====================================================



if page == "🌍 Intelligence Dashboard":



    st.subheader(

        f"🌍 {scope} Energy Intelligence Overview"

    )



    # =================================================
    # KPI CARDS
    # =================================================


    c1, c2, c3, c4, c5 = st.columns(5)



    kpi_values = [


        (

            "🌍 Countries Analyzed",

            active_df["Country Name"].nunique()

        ),


        (

            "🌱 Renewable Electricity",

            f"{active_df.renewables_share_elec.mean():.2f}%"

        ),


        (

            "🌫 CO₂ Emissions per Capita",

            f"{active_df.co2_pc.mean():.2f}"

        ),


        (

            "📊 ETRI",

            f"{active_df.apply(calculate_etri, axis=1).mean():.2f}"

        ),


        (

            "🔥 Fossil Dependency",

            f"{active_df.fossil_dependency_index.mean():.2f}%"

        )

    ]




    for col, (title, value) in zip(

        [c1,c2,c3,c4,c5],

        kpi_values

    ):


        col.markdown(

            f"""

            <div class="kpi-card">


            <div class="kpi-title">

            {title}

            </div>


            <div class="kpi-value">

            {value}

            </div>


            </div>


            """,

            unsafe_allow_html=True

        )




    st.divider()





    # =================================================
    # INDICATOR TABLE
    # =================================================


    st.subheader(

        "📋 Energy Transition Indicator Summary"

    )



    indicator_table = pd.DataFrame({


        "Indicator":[


            "Renewable Electricity Share",

            "Solar Share",

            "Wind Share",

            "Hydro Share",

            "Low Carbon Electricity",

            "Fossil Electricity",

            "Coal Share",

            "Gas Share",

            "CO₂ Emissions per Capita",

            "ETRI"


        ],



        "Value":[


            active_df.renewables_share_elec.mean(),


            active_df.solar_share_elec.mean(),


            active_df.wind_share_elec.mean(),


            active_df.hydro_share_elec.mean(),


            active_df.low_carbon_share_elec.mean(),


            active_df.fossil_share_elec.mean(),


            active_df.coal_share_elec.mean(),


            active_df.gas_share_elec.mean(),


            active_df.co2_pc.mean(),


            active_df.apply(

                calculate_etri,

                axis=1

            ).mean()


        ]

    })



    st.dataframe(

        indicator_table,

        use_container_width=True

    )



    st.divider()





    # =================================================
    # CO2 TREND
    # =================================================



    co2_trend = (

        active_df

        .groupby("year")

        ["co2_pc"]

        .mean()

        .reset_index()

    )



    st.plotly_chart(


        px.line(


            co2_trend,


            x="year",


            y="co2_pc",


            title="🌫 CO₂ Emissions per Capita Trend",


            labels={


                "year":

                "Year",


                "co2_pc":

                "CO₂ Emissions per Capita (tons/person/year)"


            }


        ),


        use_container_width=True


    )





    # =================================================
    # RENEWABLE TREND
    # =================================================



    renewable_trend = (

        active_df

        .groupby("year")

        ["renewables_share_elec"]

        .mean()

        .reset_index()

    )



    st.plotly_chart(


        px.line(


            renewable_trend,


            x="year",


            y="renewables_share_elec",


            title="🌱 Renewable Electricity Share Trend",


            labels={


                "year":

                "Year",


                "renewables_share_elec":

                "Renewable Electricity Share (%)"


            }


        ),


        use_container_width=True


    )





    # =================================================
    # ELECTRICITY MIX EVOLUTION
    # =================================================



    mix = (

        active_df

        .groupby("year")


        [

            [

                "renewables_share_elec",

                "coal_share_elec",

                "gas_share_elec"

            ]

        ]

        .mean()

        .reset_index()

    )



    st.plotly_chart(


        px.area(


            mix,


            x="year",


            y=[


                "renewables_share_elec",

                "coal_share_elec",

                "gas_share_elec"


            ],


            title="⚡ Electricity Generation Mix Evolution",


            labels={


                "year":

                "Year",


                "value":

                "Electricity Generation Share (%)",


                "variable":

                "Energy Source",


                "renewables_share_elec":

                "Renewable Electricity",


                "coal_share_elec":

                "Coal Electricity",


                "gas_share_elec":

                "Gas Electricity"


            }


        ),


        use_container_width=True


    )


# =====================================================
# 🤖 PREDICTION
# =====================================================


elif page == "🤖 Prediction":


    st.subheader(

        "🤖 Carbon Emission Prediction"

    )



    st.info(

        f"Baseline values loaded from: {scope}"

    )



    st.markdown(

        """

        Adjust energy and socioeconomic variables

        to explore possible CO₂ emission outcomes.

        """

    )



    user_input = {}



    for feature in features:


        user_input[feature] = st.number_input(


            FEATURE_LABELS.get(

                feature,

                feature

            ),


            value=float(

                profile[feature]

            )

        )





    st.divider()



    if st.button(

        "🚀 Predict CO₂ Emissions"

    ):



        prediction = model.predict(


            pd.DataFrame(

                [

                    user_input

                ]

            )


        )[0]



        st.success(


            f"""

            🌫 Predicted CO₂ Emissions per Capita:

            **{prediction:.3f} tons/person/year**

            """

        )







# =====================================================
# 🔍 EXPLAINABLE AI (SHAP)
# =====================================================


elif page == "🔍 Explainable AI":


    st.subheader(

        "🔍 Explainable AI — CO₂ Driver Analysis"

    )


    st.info(

        "SHAP explains which factors influence the model prediction."

    )



    input_data = pd.DataFrame(

        [

            profile[features]

        ]

    )



    explainer = shap.TreeExplainer(

        model

    )



    shap_values = explainer.shap_values(

        input_data

    )



    shap_df = pd.DataFrame(


        {


            "Feature":

            [

                FEATURE_LABELS.get(

                    f,

                    f

                )

                for f in features

            ],



            "Impact":

            shap_values[0]


        }


    )




    shap_df["Impact Type"] = shap_df["Impact"].apply(


        lambda x:

        "Positive CO₂ Contribution"

        if x > 0

        else

        "Negative CO₂ Contribution"


    )





    st.plotly_chart(



        px.bar(


            shap_df,


            x="Impact",


            y="Feature",


            color="Impact Type",


            orientation="h",


            title=

            "🔍 Key Factors Influencing CO₂ Emissions",


            labels={


                "Impact":

                "SHAP Contribution Value",


                "Feature":

                "Energy and Socioeconomic Factors",


                "Impact Type":

                "Contribution Type"


            }


        ),



        use_container_width=True


    )



    st.markdown(


        """

        🔴 **Positive CO₂ Contribution**

        : Factors associated with higher predicted CO₂ emissions



        🟢 **Negative CO₂ Contribution**

        : Factors associated with lower predicted CO₂ emissions

        """

    )







# =====================================================
# 📊 ETRI ASSESSMENT
# =====================================================


elif page == "📊 ETRI Assessment":



    st.subheader(

        "📊 Energy Transition Readiness Assessment"

    )



    score = calculate_etri(

        profile

    )



    st.metric(


        "Energy Transition Readiness Index",

        f"{score:.2f}/100"


    )




    if score >= 80:


        category = "🟢 Transition Leader"



    elif score >= 50:


        category = "🟡 Transition in Progress"



    else:


        category = "🔴 Transition Beginning"




    st.success(

        category

    )



    st.divider()



    st.subheader(

        "📊 ETRI Component Profile"

    )



    components = etri_components(

        profile

    )



    etri_chart = pd.DataFrame(


        {


            "Component":

            list(

                components.keys()

            ),



            "Score":

            list(

                components.values()

            )


        }


    )



    st.plotly_chart(



        px.bar(


            etri_chart,


            x="Component",


            y="Score",


            title="ETRI Component Profile",


            labels={


                "Component":

                "ETRI Components",



                "Score":

                "Readiness Score"


            }


        ),



        use_container_width=True


    )



# =====================================================
# 🔮 SCENARIO SIMULATOR
# =====================================================


elif page == "🔮 Scenario Simulator":


    st.subheader(

        "🔮 Future Energy Pathway Simulator"

    )



    st.info(

        f"Scenario baseline: {scope}"

    )



    st.markdown(

        """

        Adjust future energy conditions and explore

        possible CO₂ emission outcomes.

        """

    )



    future_profile = profile[features].copy()



    renewable_future = st.slider(


        "🌱 Future Renewable Electricity Share (%)",


        min_value=0.0,


        max_value=100.0,


        value=float(

            profile["renewables_share_elec"]

        )

    )




    coal_future = st.slider(


        "🔥 Future Coal Electricity Share (%)",


        min_value=0.0,


        max_value=100.0,


        value=float(

            profile["coal_share_elec"]

        )

    )





    future_profile[

        "renewables_share_elec"

    ] = renewable_future




    future_profile[

        "coal_share_elec"

    ] = coal_future





    current_prediction = model.predict(


        pd.DataFrame(

            [

                profile[features]

            ]

        )


    )[0]





    future_prediction = model.predict(


        pd.DataFrame(

            [

                future_profile

            ]

        )


    )[0]





    reduction = (


        (

            current_prediction

            -

            future_prediction

        )

        /

        current_prediction


    ) * 100




    st.divider()



    c1, c2, c3 = st.columns(3)



    c1.metric(

        "Current CO₂",

        f"{current_prediction:.3f}"

    )



    c2.metric(

        "Future CO₂",

        f"{future_prediction:.3f}"

    )



    c3.metric(

        "CO₂ Reduction",

        f"{reduction:.2f}%"

    )




    scenario_chart = pd.DataFrame(


        {


            "Scenario":

            [

                "Current",

                "Future"

            ],



            "CO₂ Emissions per Capita":

            [

                current_prediction,

                future_prediction

            ]

        }


    )




    st.plotly_chart(



        px.bar(


            scenario_chart,


            x="Scenario",


            y="CO₂ Emissions per Capita",


            title="🔮 Current vs Future CO₂ Scenario",


            labels={


                "Scenario":

                "Scenario Type",


                "CO₂ Emissions per Capita":

                "CO₂ Emissions (tons/person/year)"


            }


        ),


        use_container_width=True


    )




# =====================================================
# 🏛 POLICY SUPPORT
# =====================================================


elif page == "🏛 Policy Support":


    st.subheader(
        "🏛 AI Dynamic Policy Decision Support"
    )


    st.info(
        f"Policy analysis scope: {scope}"
    )


    # =================================================
    # ETRI-BASED RISK IDENTIFICATION
    # =================================================


    components = etri_components(
        profile
    )


    weakest = min(
        components,
        key=components.get
    )



    st.error(
        f"🔴 Main Transition Risk: {weakest}"
    )



    # =================================================
    # SHAP-BASED EVIDENCE
    # =================================================


    input_data = pd.DataFrame(
        [
            profile[features]
        ]
    )


    explainer = shap.TreeExplainer(
        model
    )


    shap_values = explainer.shap_values(
        input_data
    )


    shap_df = pd.DataFrame(

        {

            "Feature":
            [
                FEATURE_LABELS.get(
                    f,
                    f
                )

                for f in features
            ],


            "Impact":
            shap_values[0]

        }

    )



    shap_df["Importance"] = (

        shap_df["Impact"]

        .abs()

    )



    top_factor = (

        shap_df

        .sort_values(

            "Importance",

            ascending=False

        )

        .iloc[0]["Feature"]

    )



    st.write(

        f"🔍 Most influential factor from SHAP: **{top_factor}**"

    )



    st.divider()



    # =================================================
    # DYNAMIC POLICY RECOMMENDATION
    # =================================================


    if weakest == "Fossil Reduction":


        recommendation = """

### 🟢 Recommended Strategy


Reduce fossil electricity dependency,

accelerate renewable deployment,

and improve clean energy infrastructure.


### 📈 Expected Impact


- Lower CO₂ emissions per capita

- Improved transition readiness

- Cleaner electricity generation

        """



    elif weakest == "Renewable Adoption":


        recommendation = """

### 🟢 Recommended Strategy


Increase renewable energy deployment,

strengthen renewable integration,

and improve clean energy investment.


### 📈 Expected Impact


- Higher renewable electricity contribution

- Reduced fossil dependency

- Improved transition performance

        """



    elif weakest == "Clean Infrastructure":


        recommendation = """

### 🟢 Recommended Strategy


Strengthen clean energy infrastructure,

expand low-carbon technologies,

and improve electricity system flexibility.


### 📈 Expected Impact


- Improved clean energy capacity

- Better long-term transition performance

- Increased system resilience

        """



    else:


        recommendation = """

### 🟢 Recommended Strategy


Improve energy efficiency,

strengthen long-term transition planning,

and accelerate renewable energy pathways.


### 📈 Expected Impact


- Better future transition performance

- Improved energy system flexibility

- Higher transition readiness

        """



    st.success(

        recommendation

    )



    st.divider()



    # =================================================
    # POLICY EVIDENCE TABLE
    # =================================================


    st.subheader(

        "🔵 Evidence Supporting Recommendation"

    )



    evidence = pd.DataFrame(

        {

            "Evidence Source":

            [

                "ETRI Assessment",

                "SHAP Analysis",

                "Energy Indicators"

            ],


            "Finding":

            [

                f"Weakest transition component: {weakest}",

                f"Important prediction factor: {top_factor}",

                "Current energy profile used for assessment"

            ]

        }

    )



    st.dataframe(

        evidence,

        use_container_width=True

    )

# =====================================================
# 📘 ABOUT SECTION
# =====================================================


elif page == "📘 About":



    st.subheader(

        "🌍 AI Renewable Energy Transition Intelligence"

    )



    st.markdown(


        """

### AI-powered energy analytics,

transition assessment, and decision support platform


**Machine Learning • Explainable AI • Energy Analytics • Scenario Simulation**


        """

    )



    st.divider()



    st.subheader(

        "🌍 Intelligent Framework for Energy Transition Assessment"

    )



    st.write(


        """

This platform develops an AI-driven energy transition

intelligence system that analyzes energy patterns,

predicts CO₂ emissions per capita, explains important

emission drivers, evaluates transition readiness,

and explores future energy pathways.



The system combines machine learning, explainable AI,

transition assessment, and scenario simulation to

transform complex energy data into interpretable insights.

        """

    )



    st.subheader(

        "⚡ Core Capabilities"

    )



    st.markdown(


        """

### 🤖 Carbon Emission Intelligence


Predicts CO₂ emissions per capita using energy,

socioeconomic, renewable, and fossil dependency indicators.



### 🔍 Explainable AI Analysis


Uses SHAP-based interpretation to understand

important factors influencing predictions.



### 📊 Energy Transition Readiness Assessment


Uses ETRI to evaluate:


- Renewable adoption

- Fossil dependency reduction

- Clean infrastructure

- Transition momentum



### 🔮 Scenario Simulation


Explores alternative energy pathways

and evaluates possible future impacts.



### 🏛 Policy Decision Support


Converts analytical findings into

transition insights.

        """

    )



    st.subheader(

        "🧠 Model Information"

    )



    st.table(


        pd.DataFrame(


            {


                "Component":

                [

                    "Algorithm",

                    "Validation Strategy",

                    "Training Period",

                    "Testing Period"

                ],



                "Details":

                [

                    "Random Forest Regression",

                    "Time-based split",

                    "2000-2019",

                    "2020-2022"

                ]

            }

        )


    )



    st.subheader(

        "🔄 System Workflow"

    )



    st.code(


        """

Energy Data Sources

        ↓

Data Processing & Feature Engineering

        ↓

Machine Learning Prediction

        ↓

CO₂ Emissions per Capita Forecasting

        ↓

SHAP Explainability

        ↓

Energy Transition Readiness Assessment

        ↓

Future Scenario Simulation

        ↓

Policy Decision Support

        ↓

AI Energy Transition Dashboard

        """

    )



    st.subheader(

        "🎯 Project Objective"

    )



    st.write(


        """

To provide an interpretable AI-based platform

for understanding energy transition challenges,

evaluating sustainability progress, and exploring

cleaner energy pathways through data-driven analysis.

        """

    )







# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:15px;
        margin-top:40px;
        color:#666;
        border-top:1px solid #e5e7eb;
        font-size:14px;
    ">

    <strong>
    🌍 AI Renewable Energy Transition Intelligence Platform
    </strong>

    <br>


    Built with Python | Machine Learning | SHAP | Streamlit

    </div>
    """,
    unsafe_allow_html=True
)
