# OTP_VALIDATION
# Admin Portal for Fee Management

This is a Python-based admin portal designed to manage user details and send emails to users based on their fee payment status. The portal allows the admin to edit user information, send emails to fee-pending users, and send emails to fee-cleared users.

## Features

1. **Admin Login with OTP Verification**:
   - The admin must enter the correct username (`admin`) and a valid OTP sent to the registered email address to log in.

2. **Edit User Information**:
   - The admin can update the fee payment status of users (e.g., change from "pending" to "cleared").

3. **Send Emails to Fee-Pending Users**:
   - The admin can send reminder emails to users who have not cleared their fees.

4. **Send Emails to Fee-Cleared Users**:
   - The admin can send acknowledgment emails to users who have cleared their fees.

5. **Exit Option**:
   - The admin can exit the portal after completing the tasks.

## Prerequisites

- Python 3.x
- External libraries:
  - `feepending` (for sending emails to fee-pending users)
  - `feepaid` (for sending emails to fee-cleared users)
  - `otp` (for OTP generation and verification)

## How to Use

1. **Run the Script**:
   - Execute the Python script in your terminal or IDE.

2. **Admin Login**:
   - Enter the username as `admin`.
   - An OTP will be sent to the registered email address (`shashi2028j@gmail.com`).
   - Enter the OTP to log in successfully.

3. **Choose an Option**:
   - After logging in, the admin can choose from the following options:
     - **Edit Information**: Update the fee payment status of users.
     - **Send mail to Fee Pending users**: Send emails to users with pending fees.
     - **Send mail to Fee Cleared users**: Send emails to users who have cleared their fees.
     - **Exit**: Exit the portal.

4. **Exit the Portal**:
   - Select the "Exit" option to close the portal.

## User Details

The user details are stored in a dictionary with the following structure:

```python
userdetails = {
    101: ["Shashi", "shashikumar2028j@gmail.com", "true"],
    102: ["Manohar", "reddymanohar894@gmail.com", "true"],
    103: ["Poojitha", "kodudhulapoojitha19@gmail.com", "false"],
    104: ["Harshitha", "harshithamudhiraj16@gmail.com", "false"],
    105: ["Bindu Priya", "gardasbindupriya4@gmail.com", "true"],
    106: ["Cherukuri Sahithi", "cherukurisahithi486@gmail.com", "false"]
}
