# Twilio SMS Sending App

This is a Django-based web application for sending SMS messages using the Twilio API.

## **Setup and Run Locally**

### **Prerequisites**
1. Python 3.x installed on your machine.
2. Twilio account and API credentials (Account SID, Auth Token and My Twilio phone number).
![Screenshot](readme_media\screenshot.png)
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
    py -m pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root with the following content:
     ```
     TWILIO_ACCOUNT_SID=your_account_sid_here
     TWILIO_AUTH_TOKEN=your_auth_token_here
     TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
     ```
     ![Screenshot](readme_media\screenshot_2.png)
   - Replace the placeholders with your actual Twilio credentials.

5. **Run the Server**:
    ```bash
    py manage.py runserver
    ```

6. **Access the Application**:
   - Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### **Usage**
1. Enter the recipient's phone number and your message in the form. If you are using a Twilio free trial account, there are specific restrictions and requirements to be aware of:
- You can only send SMS messages to phone numbers that are verified as Caller IDs in your Twilio account.
- Verification involves receiving a one-time passcode (OTP) on the desired number, which must be validated in your Twilio account settings.
- Twilio’s Verified Caller ID service is only available for the US1 data routing region at this time.
2. Click "Send SMS."
3. View the status and details of the message on the response page.

---

### **Dependencies**
- Django
- Twilio Python SDK
- dotenv for environment variables
