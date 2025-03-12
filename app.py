import streamlit as st   
import networkx as nx
import numpy as np
import pandas as pd
import random
import plotly.graph_objects as go
import plotly.express as px
import time

# -------------------- Streamlit UI Setup --------------------
st.title("3D Disease Spread Simulation using SIR Model")
st.sidebar.header("Simulation Settings")

# User-adjustable parameters
P_INFECT = st.sidebar.slider("Infection Probability", 0.0, 1.0, 0.2, 0.01)
P_RECOVER = st.sidebar.slider("Recovery Probability", 0.0, 1.0, 0.1, 0.01)
DAYS_TO_RECOVER = st.sidebar.slider("Days to Recover", 1, 14, 7, 1)

# File uploader for CSV input
uploaded_file = st.sidebar.file_uploader("Upload CSV file (Person_ID, Contact_ID, Infection_Status, Days_Infected)", type=["csv"])

# Option to use predefined dataset
use_predefined = st.sidebar.checkbox("Use Predefined Dataset")

# Predefined dataset
def get_predefined_data():
    data = {
        "Person_ID": ["1", "2", "3", "4", "5", "6"],
        "Name": ["A", "B", "C", "D", "E", "F"],
        "Age": [25, 30, 35, 40, 45, 50],
        "City": ["NY", "LA", "SF", "TX", "MI", "FL"],
        "Contact_ID": ["2", "3", "4", "5", "6", "1"],
        "Infection_Status": ["Infected", "Susceptible", "Susceptible", "Susceptible", "Susceptible", "Susceptible"],
        "Days_Infected": [0, 0, 0, 0, 0, 0]
    }
    return pd.DataFrame(data)

# Function to create graph
def create_graph_from_data(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Person_ID'], row['Contact_ID'])
    return G

# Function to run the simulation
def run_simulation(G, df):
    status = {node: 'S' for node in G.nodes()}
    days_infected = {node: 0 for node in G.nodes()}

    for _, row in df.iterrows():
        if row['Infection_Status'] == 'Infected':
            status[row['Person_ID']] = 'I'
            days_infected[row['Person_ID']] = row['Days_Infected']

    simulation_data = []
    sir_counts = []
    
    while 'I' in status.values():
        new_status = status.copy()
        new_days_infected = days_infected.copy()
        
        for node in G.nodes():
            if status[node] == 'I':
                new_days_infected[node] += 1
                if new_days_infected[node] >= DAYS_TO_RECOVER or random.random() < P_RECOVER:
                    new_status[node] = 'R'
                for neighbor in G.neighbors(node):
                    if status[neighbor] == 'S' and random.random() < P_INFECT:
                        new_status[neighbor] = 'I'
                        new_days_infected[neighbor] = 0
        
        status = new_status
        days_infected = new_days_infected
        simulation_data.append(status.copy())
        sir_counts.append({
            "Day": len(sir_counts),
            "Susceptible": list(status.values()).count('S'),
            "Infected": list(status.values()).count('I'),
            "Recovered": list(status.values()).count('R')
        })
        time.sleep(0.2)
    
    return simulation_data, sir_counts

# Function to plot time series
def plot_sir_dynamics(sir_counts):
    df_sir = pd.DataFrame(sir_counts)
    fig = px.line(df_sir, x="Day", y=["Susceptible", "Infected", "Recovered"],
                  labels={"value": "Population Count", "variable": "State"}, title="SIR Model Over Time")
    return fig

# Function to plot 3D graph
def plot_3d_network(G, status):
    pos = nx.spring_layout(G, dim=3, seed=42)
    x_vals, y_vals, z_vals, colors = [], [], [], []
    for node in G.nodes():
        x_vals.append(pos[node][0])
        y_vals.append(pos[node][1])
        z_vals.append(pos[node][2])
        colors.append("red" if status[node] == 'I' else "green" if status[node] == 'R' else "blue")
    
    fig = go.Figure(data=[go.Scatter3d(x=x_vals, y=y_vals, z=z_vals,
                                       mode='markers',
                                       marker=dict(size=6, color=colors, opacity=0.8))])
    fig.update_layout(title="3D Infection Spread Visualization", scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))
    return fig

# Main app logic
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = ["Person_ID", "Name", "Age", "City", "Contact_ID", "Infection_Status", "Days_Infected"]
    df["Person_ID"] = df["Person_ID"].astype(str)
    df["Contact_ID"] = df["Contact_ID"].astype(str)
elif use_predefined:
    df = get_predefined_data()
    st.sidebar.success("Using predefined dataset")
else:
    st.sidebar.info("Please upload a dataset or select the predefined dataset to start the simulation.")
    df = None

if df is not None:
    G = create_graph_from_data(df)
    
    if st.sidebar.button("Start Simulation"):
        simulation_data, sir_counts = run_simulation(G, df)
        st.plotly_chart(plot_sir_dynamics(sir_counts))
        
        for day, status in enumerate(simulation_data):
            st.subheader(f"Day {day+1}")
            st.plotly_chart(plot_3d_network(G, status), key=f"day_{day}")
            time.sleep(0.5)
