# Heritage
# Property Management System

This project is a property management system featuring a backend implemented with Django REST framework and a frontend built with React. It allows users to view property listings, place bids, and manage property details.

## Features

- **Property Listings**: View a list of properties with details and images.
- **Property Details**: View detailed information and images for each property.
- **Bidding**: Place bids on properties, view current highest bids.
- **User Roles**: 
  - **Admin**: Manage users, properties, and oversee bidding activities.
  - **Bidder**: Place bids and view property details.
  - **Property Owner**: List properties and monitor bids.
- **Testimonials**: Submit and view reviews and ratings for properties.
- **Team Information**: View information about team members.
- **Search and Filter**: Search and filter properties by various criteria.

## Backend Setup

### Requirements

- Python 3.10
- Django
- Django REST framework

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd /backend
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

7. **Ensure media files are served**: In `settings.py`, configure `MEDIA_URL` and `MEDIA_ROOT`, and update `urls.py` to serve media files during development.

### API Endpoints

- `GET /api/properties/`: List all properties.
- `GET /api/properties/<id>/`: Get details for a specific property.
- `POST /api/properties/`: Create a new property.
- `GET /api/bids/`: List all bids.
- `POST /api/bids/`: Place a new bid.
- `GET /api/team/`: List all team members.
- `GET /api/testimonials/`: List all testimonials.
- `POST /api/testimonials/`: Submit a new testimonial.

## Frontend Setup

### Requirements

- Node.js
- npm or yarn

### Installation

1. **Navigate to the frontend directory**:
    ```bash
    cd your-repo/frontend
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Start the React development server**:
    ```bash
    npm start
    ```

### Components

- **PropertyList**: Displays a list of properties with images.
- **PropertyDetails**: Shows detailed information and images for a selected property.
- **BidForm**: Allows users to place bids on properties.
- **TeamMembers**: Displays information about team members.

### Axios Configuration

Configure Axios to point to your Django backend:

**`src/axiosConfig.js`**:
```javascript
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/',
});

export default instance;
