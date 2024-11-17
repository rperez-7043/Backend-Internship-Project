# Twilio SMS Sending App

This is a Django-based web application for sending SMS messages using the Twilio API.

## **Setup and Run Locally**

### **Prerequisites**
1. Python 3.x installed on your machine.
2. Twilio account and API credentials (Account SID, Auth Token and My Twilio phone number).
3. Install `pip` (Python package installer) if not already installed.

---

### **Installation Steps**
1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    py -m venv .venv
    .venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root with the following content:
     ```
     TWILIO_ACCOUNT_SID=your_account_sid_here
     TWILIO_AUTH_TOKEN=your_auth_token_here
     TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
     ```
   - Replace the placeholders with your actual Twilio credentials.

5. **Run Database Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the Server**:
    ```bash
    py manage.py runserver
    ```

7. **Access the Application**:
   - Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### **Usage**
1. Enter the recipient's phone number and your message in the form.
2. Click "Send SMS."
3. View the status and details of the message on the response page.

---

### **Dependencies**
- Django
- Twilio Python SDK
- dotenv for environment variables

---

### **License**
This project is licensed under [your license here].

---

### **Contributing**
Feel free to submit pull requests or open issues to improve the project.
