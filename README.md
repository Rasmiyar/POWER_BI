# POWER_BI
# Tata Project Dashboard

## Overview
The **Tata Project Dashboard** is a user-friendly web application designed to provide insightful data visualizations and actionable insights into revenue trends, customer contributions, and market demands. Built using **Streamlit**, this dashboard serves as a powerful tool for decision-makers to analyze and optimize business strategies.

## Features

### 📊 Key Modules:
1. **Home**:
   - Overview of the dashboard's purpose and objectives.
   - A welcoming page with the Tata logo and introductory content.

2. **📅 Seasonal Revenue Trends**:
   - Visual representation of revenue trends across seasons.
   - Displays a detailed image/chart illustrating seasonal insights.

3. **🏆 Top 10 Customers**:
   - Highlights the top 10 customers contributing the most to revenue.
   - Uses intuitive visualizations for easy interpretation.

4. **🌍 Top 10 Countries**:
   - Analyzes country-wise revenue contributions.
   - Showcases the top 10 performing countries through a chart or map.

5. **📈 Demand by Country**:
   - Breaks down demand by country for a granular view of market needs.
   - Provides actionable insights with clear visuals.

6. **💬 Feedback**:
   - Collects user feedback to improve the dashboard's features.
   - Allows users to submit their feedback via email using an integrated **SMTP** feature.

### 🌟 Sidebar Navigation:
The sidebar includes a user-friendly navigation menu with emojis to enhance the visual appeal and improve the user experience.

### ✨ Feedback System:
- Integrated **SMTP** email functionality allows users to send feedback directly from the dashboard.
- Users can input their email and feedback, which is then securely sent to the dashboard administrator.

## How to Use
1. **Clone the Repository**:
   
   git clone <repository-url>
   cd tata-project-dashboard


2. **Install Dependencies**:
   Ensure you have Python installed. Run:

   pip install streamlit
 

3. **Run the Application**:
   Start the Streamlit server with the command:
  
   streamlit run app.py
  

4. **Navigate the Dashboard**:
   Use the sidebar to navigate through different sections.

## SMTP Configuration
To enable the feedback feature, update the following details in the `send_feedback` function:
- **SMTP Server**: Update the SMTP server address (default is `smtp.gmail.com`).
- **Email Credentials**: Replace `your_email@gmail.com` and `your_password` with your email and password (use an app-specific password if using Gmail).



## Technologies Used
- **Streamlit**: For building the web application.
- **SMTP**: For feedback email integration.

## Future Enhancements
- Add live data integration for real-time insights.
- Enhance visualizations with interactive charts.
- Implement user authentication for personalized experiences.


Developed by **MOHAMMUDHA RASMIYA** using **Streamlit**. 🚀


