# 3D Disease Spread Simulation using SIR Model  

This project is a **Streamlit-based interactive simulation** of disease spread using the **SIR (Susceptible-Infected-Recovered) model**. It visualizes how infections propagate within a network of individuals based on **real-world contact data**.  

## **Features**  
✅ **User-adjustable Parameters:** Control infection probability, recovery probability, and recovery time.  
✅ **CSV Input Support:** Upload a dataset with person-to-person contact data.  
✅ **SIR Model Simulation:** Tracks disease progression over time.  
✅ **3D Visualization:** Interactive Plotly-based 3D network graph of infection spread.  
✅ **Time-Series Analysis:** Line plot showing SIR population dynamics.  

## **How It Works**  
1. **Upload a CSV file** containing columns:  
   - `Person_ID` (Unique ID of the individual)  
   - `Contact_ID` (Person they were in contact with)  
   - `Infection_Status` (Susceptible, Infected, or Recovered)  
   - `Days_Infected` (Days since infection)  

2. **Graph Creation:** A network is built where nodes represent individuals and edges represent contacts.  
3. **Disease Spread Simulation:** The infection propagates based on the **SIR model**, updating status dynamically.  
4. **Visualize Results:**  
   - A **time-series plot** shows how Susceptible, Infected, and Recovered populations evolve.  
   - **3D Network Graphs** depict the disease spread in real-time.  

## **Installation & Usage**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/3d-disease-simulation.git
cd 3d-disease-simulation
2. Install Dependencies
Ensure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Simulation
bash
Copy
Edit
streamlit run app.py
Technologies Used
🔹 Python
🔹 Streamlit
🔹 NetworkX
🔹 Plotly
🔹 Pandas
🔹 NumPy

Use Cases
Epidemiology research & analysis
Educational purposes for understanding disease dynamics
Simulating the impact of infection control strategies
Contribute
If you'd like to improve this project, feel free to fork the repository, enhance the code, and submit a pull request!

🚀 Let's simulate and understand disease spread better!

typescript
Copy
Edit

Save this as `README.md` in your GitHub repository. Let me know if you need any modifications! 🚀
