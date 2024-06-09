# WebToPavlov

This is a Flask application that allows users to manage files on an SFTP server. Users can log in, view, and update files stored on the server. The application reads user credentials and SFTP credentials from a `config.json` file.

!! This was created to be used as a Simple Website File loader that would load files from a STFP server and then would edit those files for people using Unreal Engine Blueprints to create a Whuitelist system for certain things. !!

## Features

- User authentication
- SFTP connection for file management
- View and update files on the SFTP server

## Requirements

- Python 3.6+
- Flask
- Paramiko

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/WebToPavlov.git
    cd WebToPavlov
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `config.json` file in the root directory:**

    ```json
    {
        "users": {
            "test": "test",
            "tester2": "test1",
            "user2": "password2",
            "user3": "password3"
        },
        "sftp": {
            "host": "your-sftp-host",
            "port": 2022,
            "username": "your-sftp-username",
            "password": "your-sftp-password"
        }
    }
    ```

    - Replace `"your-sftp-host"`, `"your-sftp-username"`, and `"your-sftp-password"` with your actual SFTP credentials.

## Running the Application

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

## Application Structure

- `app.py`: The main Flask application.
- `config.json`: Configuration file for user credentials and SFTP credentials.
- `templates/`: Directory containing HTML templates for the web pages.

## Usage

1. **Login:**

    - Navigate to the login page and log in with one of the users specified in the `config.json` file.

2. **Home Page:**

    - After logging in, you will be redirected to the home page where you can manage files.

3. **View a File:**

    - Enter the filename you want to view and click "Get File".

4. **Update a File:**

    - Enter the filename you want to update and the new content, then click "Update File".

## Security

- **Secret Key:**
  - Ensure that the `app.secret_key` in `app.py` is changed to a random and secure value.

- **Config File:**
  - Do not expose your `config.json` file to the public. Keep it secure and restrict its access.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Feel free to fork this repository, create a new branch, and make improvements. Pull requests are welcome!

## Support

If you encounter any issues or have questions, please join our discord @ [Discord Here](https://discord.gg/JxF4hGaxc2)

