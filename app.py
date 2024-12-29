import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up page configuration
st.set_page_config(
    page_title="📊 Tata Project Dashboard",
    page_icon="✨",
    layout="wide",
)

# Function to send feedback via SMTP
def send_feedback(email, feedback):
    try:
        # SMTP server configuration
        smtp_server = "smtp.gmail.com"  # Update with your SMTP server
        smtp_port = 587
        sender_email = "your_email@gmail.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password (use app-specific password for Gmail)

        # Email content
        subject = "New Feedback from Tata Project Dashboard"
        message = f"Feedback from {email}:\n\n{feedback}"

        # Set up email headers
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email  # You can change this to a different recipient
        msg['Subject'] = subject

        # Add email body
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return True, None
    except Exception as e:
        return False, str(e)

# Sidebar navigation menu with icons
menu = ["🏠 Home", "📅 Seasonal Revenue Trends", "🏆 Top 10 Customers", "🌍 Top 10 Countries", "📈 Demand by Country", "💬 Feedback"]
choice = st.sidebar.selectbox("🚀 Navigate", menu)

# Home Page
if choice == "🏠 Home":
    st.title("✨ Welcome to the Tata Project Dashboard! ")
    st.write(
        """
        🔍 **Explore detailed insights** into revenue trends, top-performing customers, and market demands across regions.
        This dashboard provides actionable insights to help you make **data-driven decisions**. 🌟
        """
    )
    st.image("download.png", caption="Tata Logo", width=200)

# Seasonal Revenue Trends
elif choice == "📅 Seasonal Revenue Trends":
    st.title("📅 Seasonal Revenue Trends Analysis 🗓️")
    st.image("tata_project_page-0001.jpg", caption="Seasonal Revenue Trends", use_column_width=True)

# Top 10 Customers
elif choice == "🏆 Top 10 Customers":
    st.title("🏆 Top 10 Customers by Revenue 🏅")
    st.image("tata_project_page-0003.jpg", caption="Top 10 Customers by Revenue", use_column_width=True)

# Top 10 Countries
elif choice == "🌍 Top 10 Countries":
    st.title("🌍 Top 10 Countries by Revenue 🌟")
    st.image("tata_project_page-0002.jpg", caption="Top 10 Countries by Revenue", use_column_width=True)

# Demand by Country
elif choice == "📈 Demand by Country":
    st.title("📈 Demand by Country Insights 📊")
    st.image("tata_project_page-0004.jpg", caption="Demand by Country", use_column_width=True)

# Feedback Page
elif choice == "💬 Feedback":
    st.title("💬 We Value Your Feedback 📝")
    st.write("Your feedback helps us improve and deliver better insights. 💖")

    # Input fields for feedback
    user_email = st.text_input("📧 Your Email:", placeholder="Enter your email address")
    feedback_text = st.text_area("💡 Your Feedback:", placeholder="Share your thoughts, suggestions, or issues")

    # Submit button
    if st.button("📨 Submit Feedback"):
        if user_email.strip() and feedback_text.strip():
            sent, error = send_feedback(user_email, feedback_text)
            if sent:
                st.success("🎉 Thank you for your feedback! We appreciate it. 💖")
            else:
                st.error(f"❌ An error occurred: {error}")
        else:
            st.warning("⚠️ Please fill in both your email and feedback before submitting.")

# Footer
st.sidebar.markdown("---")
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    """
    This dashboard is designed to provide insights into revenue trends and customer contributions. 
    Developed using **Streamlit**. 🚀
    """
)
