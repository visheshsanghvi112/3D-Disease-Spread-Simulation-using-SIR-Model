3D Disease Spread Simulation using SIR Model

This project is a Streamlit-based interactive simulation of disease spread using the SIR (Susceptible-Infected-Recovered) model. It visualizes how infections propagate within a network of individuals based on real-world contact data.

Features

✅ User-adjustable Parameters: Control infection probability, recovery probability, and recovery time.✅ CSV Input Support: Upload a dataset with person-to-person contact data.✅ SIR Model Simulation: Tracks disease progression over time.✅ 3D Visualization: Interactive Plotly-based 3D network graph of infection spread.✅ Time-Series Analysis: Line plot showing SIR population dynamics.

How It Works

Upload a CSV file containing columns: Person_ID, Contact_ID, Infection_Status, and Days_Infected.

Graph Creation: A network is built where nodes represent individuals and edges represent contacts.

Disease Spread Simulation: The infection propagates based on the SIR model, updating status dynamically.

Visualize Results:

A time-series plot shows how Susceptible, Infected, and Recovered populations evolve.

3D Network Graphs depict the disease spread in real-time.

Installation

Clone the repository:

git clone https://github.com/yourusername/3d-disease-simulation.git
cd 3d-disease-simulation

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Usage

Open the Streamlit UI in your browser.

Adjust parameters using the sidebar controls.

Upload a CSV dataset and start the simulation.

View the 3D infection spread visualization and SIR model time-series graph.

Technologies Used

🔹 Python | Streamlit | NetworkX | Plotly | Pandas | NumPy

Use Cases

Epidemiology research & analysis

Educational purposes for understanding disease dynamics

Simulating the impact of infection control strategies

Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository, make changes, and submit a pull request.

License

This project is licensed under the MIT License.

