# VetNet Microservice API Tester

This Streamlit application is designed to test all endpoints of the VetNet Microservice API. It provides a user-friendly interface to interact with the API for managing master data such as Companies, Certifications, Degrees, Universities, Job Titles, Skills, and Field of Studies.

## Setup Instructions

Follow these steps to set up and run the API Tester application locally:

1. **Create a Virtual Environment**:
   Open a terminal in the `api-tester` directory and create a new virtual environment using Python:
   ```
   python3 -m venv .venv
   ```

2. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```
   - On Windows:
     ```
     .venv\Scripts\activate
     ```

3. **Install Dependencies**:
   Install the required Python packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Application**:
   Start the Streamlit server to launch the API Tester application:
   ```
   streamlit run app.py
   ```
   This will open the application in your default web browser at `http://localhost:8501`.

## Usage Instructions

1. **Select API Category and Operation**:
   - Use the sidebar to choose an API category (e.g., Companies, Certifications) and an operation (GET, POST, PUT, DELETE, DELETE_MANY).

2. **Input Data**:
   - For `PUT` and `DELETE` operations, enter the ID of the item you wish to modify or delete.
   - For `POST` and `PUT` operations, fill in the request body fields like `Name` and `Is Active`.

3. **Execute API Call**:
   - Click the "Execute API Call" button to send the request to the selected endpoint.
   - The application will display the request URL and method for transparency.

4. **View Response**:
   - The response from the API will be shown in JSON format.
   - For `GET` requests returning a list, a table view of the data is also provided for easier readability.

5. **Configuration**:
   - In the sidebar under "Configuration", you can update the API Base URL (default: `http://localhost:4000`) and Static Token if needed.
   - Click "Update Configuration" to apply changes.

## Troubleshooting

- **API Connection Issues**: Ensure the VetNet Microservice is running at the specified API Base URL (default: `http://localhost:4000`). Verify that the Static Token matches the one configured in the microservice.
- **Dependency Installation Errors**: Make sure your virtual environment is activated before running `pip install -r requirements.txt`. If issues persist, check for Python version compatibility (Python 3.8+ recommended).
- **Streamlit Not Launching**: Confirm that the `streamlit` package is installed (`pip show streamlit`). If the browser doesn't open automatically, navigate to `http://localhost:8501` manually.

## Notes

- This application assumes the VetNet Microservice API endpoints follow the structure defined in the `ENDPOINTS` dictionary in `app.py`. If the API structure changes, update the `ENDPOINTS` dictionary accordingly.
- For security, sensitive data like the Static Token can be managed via environment variables or a `.env` file, which the application will load using `python-dotenv`.

If you encounter persistent issues or need additional features, please contact the developer or update the application code as needed.
