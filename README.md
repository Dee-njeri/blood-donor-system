# Blood Donation Management System

This is a **Blood Donation Management System** built using the **Django** framework. It facilitates blood donation and distribution by connecting donors, health facilities, and patients, while focusing on user experience, real-time inventory management, and data security.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Database Design](#database-design)
  - [User Models](#user-models)
  - [Facility Models](#facility-models)
- [Routes](#routes)
  - [User Routes](#user-routes)
  - [Facility Routes](#facility-routes)
- [Contributing](#contributing)
- [License](#license)

---

## Features

1. **Donor Management**

   - User registration and profile completion.
   - Donation eligibility checks and history.
   - Blood donation appointment booking.
   - Request Blood from available facilities.

2. **Facility Management**

   - Health facility registration and approval process.
   - Blood inventory tracking and management.
   - Handling blood requests and donation appointments.
   - Donor management

3. **Notifications**

   - Notifications for updates on requests, donations, and approvals for both patients and facilities.

4. **User Roles**

   - Individual donors.
   - Health facilities (hospitals, clinics, etc.).
   - Superuser for administration and facility approvals.

5. **Secure System**

   - Role-based access controls.
   - Data validation for security and accuracy.

6. **Dynamic Expiry and Blood Type Management**
   - Auto-calculation of blood unit expiration based on donation type.
   - Inventory segregated by blood type and facility.

---

## Technologies Used

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Database**: SQlite
- **Authentication**: Django's built-in authentication system

---

## Dependencies

The following are some key Python packages used in the project:

- **Django**: Web framework for building the application.
- **django-filter**: Provides filtering capabilities for views and querysets.
- **django-tables2**: For rendering data in tabular format.
- **hashlib**: Used for generating unique hashes for IDs.

---

## Setup and Installation

### Prerequisites

- Python 3.9+
- SQLite
- pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Dee-njeri/blood-donor-system.git
   cd blood-donation-system

   ```
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**

   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.


---

## Database Design   

This section provides a detailed explanation of the database models, their fields, validations, and relationships in the system.

## User Models

### 1. CustomUser

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>email</code></td>
    <td><code>EmailField</code></td>
    <td>Unique email address for the user.</td>
  </tr>
  <tr>
    <td><code>role</code></td>
    <td><code>CharField</code></td>
    <td>User role (Individual, Facility); choices are defined in the app.</td>
  </tr>
  <tr>
    <td><code>is_active</code></td>
    <td><code>BooleanField</code></td>
    <td>Indicates if the user account is active; defaults to <code>True</code>.</td>
  </tr>
  <tr>
    <td><code>is_approved</code></td>
    <td><code>BooleanField</code></td>
    <td>Indicates if the user account is approved by an admin; defaults to <code>False</code> for facilities and <code>True</code>.</td>
  </tr>
  <tr>
    <td><code>date_joined</code></td>
    <td><code>DateTimeField</code></td>
    <td>The date and time when the user account was created.</td>
  </tr>
  <tr>
    <td><code>last_login</code></td>
    <td><code>DateTimeField</code></td>
    <td>Tracks the last login date and time for the user.</td>
  </tr>
</table>

### 2. UserProfile

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>user</code></td>
    <td><code>OneToOneField</code></td>
    <td>Links to the CustomUser.</td>
  </tr>
  <tr>
    <td><code>user_uuid</code></td>
    <td><code>UUIDField</code></td>
    <td>Unique identifier for the user.</td>
  </tr>
  <tr>
    <td><code>firstname</code></td>
    <td><code>CharField</code></td>
    <td>User's first name; max length of 50 characters.</td>
  </tr>
  <tr>
    <td><code>lastname</code></td>
    <td><code>CharField</code></td>
    <td>User's last name; max length of 50 characters.</td>
  </tr>
  <tr>
    <td><code>date_of_birth</code></td>
    <td><code>DateField</code></td>
    <td>User's date of birth.</td>
  </tr>
  <tr>
    <td><code>contact_number</code></td>
    <td><code>CharField</code></td>
    <td>Phone number; max length of 50 characters.</td>
  </tr>
  <tr>
    <td><code>county</code></td>
    <td><code>CharField</code></td>
    <td>County of residence.</td>
  </tr>
  <tr>
    <td><code>gender</code></td>
    <td><code>CharField</code></td>
    <td>Gender of the user; choices include Male, Female, Other.</td>
  </tr>
  <tr>
    <td><code>blood_type</code></td>
    <td><code>CharField</code></td>
    <td>User's blood type; choices include A+, A-, B+, etc.</td>
  </tr>
  <tr>
    <td><code>created_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp when the profile was created.</td>
  </tr>
  <tr>
    <td><code>updated_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp for the last profile update.</td>
  </tr>
</table>

### 3. Donation

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>donation_id</code></td>
    <td><code>UUIDField</code></td>
    <td>Unique identifier for the donation.</td>
  </tr>
  <tr>
    <td><code>user</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the UserProfile of the donor.</td>
  </tr>
  <tr>
    <td><code>facility</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the FacilityProfile where the donation occurred.</td>
  </tr>
  <tr>
    <td><code>amount</code></td>
    <td><code>FloatField</code></td>
    <td>Quantity of blood donated in milliliters.</td>
  </tr>
  <tr>
    <td><code>donation_type</code></td>
    <td><code>CharField</code></td>
    <td>Type of donation (e.g., whole blood, plasma); choices defined.</td>
  </tr>
  <tr>
    <td><code>status</code></td>
    <td><code>CharField</code></td>
    <td>Status of the donation (e.g., pending, approved); choices defined.</td>
  </tr>
  <tr>
    <td><code>donation_date</code></td>
    <td><code>DateField</code></td>
    <td>The date the donation occurred.</td>
  </tr>
  <tr>
    <td><code>created_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp when the donation record was created.</td>
  </tr>
</table>

### 4. Request

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>request_id</code></td>
    <td><code>UUIDField</code></td>
    <td>Unique identifier for the request.</td>
  </tr>
  <tr>
    <td><code>user</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the UserProfile of the requester.</td>
  </tr>
  <tr>
    <td><code>facility</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the FacilityProfile where the request is made.</td>
  </tr>
  <tr>
    <td><code>request_type</code></td>
    <td><code>CharField</code></td>
    <td>Type of request (e.g., blood units, plasma).</td>
  </tr>
  <tr>
    <td><code>urgency_level</code></td>
    <td><code>CharField</code></td>
    <td>Indicates urgency (e.g., low, medium, high).</td>
  </tr>
  <tr>
    <td><code>status</code></td>
    <td><code>CharField</code></td>
    <td>Status of the request (e.g., pending, approved, rejected).</td>
  </tr>
  <tr>
    <td><code>requested_date</code></td>
    <td><code>DateField</code></td>
    <td>The date the request was made.</td>
  </tr>
  <tr>
    <td><code>remarks</code></td>
    <td><code>TextField</code></td>
    <td>Additional notes about the request.</td>
  </tr>
</table>

### 5. Notification

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>user</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the CustomUser.</td>
  </tr>
  <tr>
    <td><code>message</code></td>
    <td><code>TextField</code></td>
    <td>Notification message content.</td>
  </tr>
  <tr>
    <td><code>is_read</code></td>
    <td><code>BooleanField</code></td>
    <td>Indicates if the notification has been read; defaults to False.</td>
  </tr>
  <tr>
    <td><code>created_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp when the notification was created.</td>
  </tr>
</table>

---

## Facility Models

### 1. Facility Profile

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>user</code></td>
    <td><code>OneToOneField</code></td>
    <td>Links to the CustomUser account for the facility.</td>
  </tr>
  <tr>
    <td><code>name</code></td>
    <td><code>CharField</code></td>
    <td>Facility name; max length of 50 characters.</td>
  </tr>
  <tr>
    <td><code>contact_number</code></td>
    <td><code>CharField</code></td>
    <td>Phone number for the facility.</td>
  </tr>
  <tr>
    <td><code>facility_type</code></td>
    <td><code>CharField</code></td>
    <td>Type of facility (e.g., hospital, clinic); choices defined.</td>
  </tr>
  <tr>
    <td><code>county</code></td>
    <td><code>CharField</code></td>
    <td>Facility's location (county).</td>
  </tr>
  <tr>
    <td><code>open_days</code></td>
    <td><code>CharField</code></td>
    <td>Days the facility operates (e.g., "Monday to Friday").</td>
  </tr>
  <tr>
    <td><code>opening_time</code></td>
    <td><code>TimeField</code></td>
    <td>Daily opening time.</td>
  </tr>
  <tr>
    <td><code>closing_time</code></td>
    <td><code>TimeField</code></td>
    <td>Daily closing time.</td>
  </tr>
  <tr>
    <td><code>registration_number</code></td>
    <td><code>CharField</code></td>
    <td>Official registration number for the facility.</td>
  </tr>
  <tr>
    <td><code>is_approved</code></td>
    <td><code>BooleanField</code></td>
    <td>Indicates if the facility is approved by a superuser; defaults to False.</td>
  </tr>
  <tr>
    <td><code>created_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp when the profile was created.</td>
  </tr>
  <tr>
    <td><code>updated_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp for the last profile update.</td>
  </tr>
</table>

### 2. Inventory

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>facility</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the FacilityProfile.</td>
  </tr>
  <tr>
    <td><code>blood_type</code></td>
    <td><code>CharField</code></td>
    <td>Blood type (e.g., A+, O-); choices defined.</td>
  </tr>
  <tr>
    <td><code>quantity</code></td>
    <td><code>DecimalField</code></td>
    <td>Quantity of blood available (in units).</td>
  </tr>
  <tr>
    <td><code>units_received</code></td>
    <td><code>IntegerField</code></td>
    <td>Total units received by the facility.</td>
  </tr>
  <tr>
    <td><code>updated_at</code></td>
    <td><code>DateTimeField</code></td>
    <td>Timestamp for the last inventory update.</td>
  </tr>
</table>

### 3. BloodUnit

<table>
  <tr>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>unit_id</code></td>
    <td><code>CharField</code></td>
    <td>Unique identifier for the blood unit.</td>
  </tr>
  <tr>
    <td><code>facility</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the FacilityProfile storing the unit.</td>
  </tr>
  <tr>
    <td><code>donor</code></td>
    <td><code>ForeignKey</code></td>
    <td>Links to the UserProfile of the donor; nullable.</td>
  </tr>
  <tr>
    <td><code>blood_type</code></td>
    <td><code>CharField</code></td>
    <td>Blood type (e.g., A+, O-); choices defined.</td>
  </tr>
  <tr>
    <td><code>quantity</code></td>
    <td><code>DecimalField</code></td>
    <td>Quantity of blood in the unit (in milliliters).</td>
  </tr>
  <tr>
    <td><code>donation_type</code></td>
    <td><code>CharField</code></td>
    <td>Type of donation; choices defined (e.g., whole blood, plasma).</td>
  </tr>
  <tr>
    <td><code>collection_date</code></td>
    <td><code>DateField</code></td>
    <td>Date the blood unit was collected.</td>
  </tr>
  <tr>
    <td><code>expiration_date</code></td>
    <td><code>DateField</code></td>
    <td>Expiration date of the blood unit; calculated automatically.</td>
  </tr>
  <tr>
    <td><code>status</code></td>
    <td><code>CharField</code></td>
    <td>Status of the unit (e.g., available, expired); choices defined.</td>
  </tr>
  <tr>
    <td><code>remarks</code></td>
    <td><code>TextField</code></td>
    <td>Additional notes or observations.</td>
  </tr>
</table>

----

## Routes
### User routes

<table>
  <tr>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>/register/</code></td>
    <td>User registration.</td>
  </tr>
  <tr>
    <td><code>/complete-profile/</code></td>
    <td>Complete user profile.</td>
  </tr>
  <tr>
    <td><code>/profile-settings/</code></td>
    <td>Edit user profile.</td>
  </tr>
  <tr>
    <td><code>/dashboard/</code></td>
    <td>User dashboard.</td>
  </tr>
  <tr>
    <td><code>/donations/</code></td>
    <td>View donation history.</td>
  </tr>
  <tr>
    <td><code>/requests/</code></td>
    <td>View blood requests.</td>
  </tr>
  <tr>
    <td><code>/requests/make-request/facility_id/</code></td>
    <td>Make a blood request to a facility.</td>
  </tr>
  <tr>
    <td><code>/requests/edit/id/</code></td>
    <td>Edit an existing blood request.</td>
  </tr>
  <tr>
    <td><code>/requests/cancel-request/id/</code></td>
    <td>Cancel a blood request.</td>
  </tr>
  <tr>
    <td><code>/donations/check-eligibility/</code></td>
    <td>Check donation eligibility.</td>
  </tr>
  <tr>
    <td><code>/donations/book-donation-appointment/</code></td>
    <td>Book a donation appointment.</td>
  </tr>
</table>

### Facility routes
<table>
  <tr>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>/dashboard/</code></td>
    <td>Facility dashboard.</td>
  </tr>
  <tr>
    <td><code>/register/</code></td>
    <td>Facility registration.</td>
  </tr>
  <tr>
    <td><code>/awaiting-approval/</code></td>
    <td>Facility approval status page.</td>
  </tr>
  <tr>
    <td><code>/complete-profile/</code></td>
    <td>Complete facility profile.</td>
  </tr>
  <tr>
    <td><code>/profile-settings/</code></td>
    <td>Edit facility profile.</td>
  </tr>
  <tr>
    <td><code>/requests/</code></td>
    <td>View blood requests.</td>
  </tr>
  <tr>
    <td><code>/requests/approve-request/id/</code></td>
    <td>Approve a blood request.</td>
  </tr>
  <tr>
    <td><code>/requests/reject-request/id/</code></td>
    <td>Reject a blood request.</td>
  </tr>
  <tr>
    <td><code>/donations/</code></td>
    <td>View blood donations.</td>
  </tr>
  <tr>
    <td><code>/inventory/</code></td>
    <td>View and manage blood inventory.</td>
  </tr>
</table>

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**:
Fork this repository to your GitHub account by clicking the "Fork" button.
2. **Create a new branch**:
Create a new branch for your feature/bugfix. Do not make changes to the `main` branch.
3. **Commit your changes and push to your branch**:
Make your desired changes and commit them to your branch. Push your branch to your GitHub account.
4. **Submit a pull request**:
Submit a pull request to the `main` branch with a detailed explanation of the changes you made.


## License

This project is licensed under the MIT License.