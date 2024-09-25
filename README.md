# mksld

A very crappy (dockerized) script written in 10ish mins that scrapes [@MKBHD](https://x.com/MKBHD)'s wallpaper app's (Panels) **public** API and fetches all the images tagged with `dhd` (high-definition image).

> [!NOTE]
> I own none of the content fetched by this script. All rights go to their respective copyright holders.

## Usage

To ensure a clean and isolated environment for this project, it's recommended to use a virtual environment.

### Steps:

1. **Install Python 3** (if not already installed)

   Make sure Python 3 is installed on your system by running:
   ```bash
   python3 --version
   ```
   If it's not installed, follow the instructions on [Python's official website](https://www.python.org/downloads/) to download and install Python 3.

2. **Create a Virtual Environment**

   Navigate to your project directory, and run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

   This will create a `venv` directory with a virtual environment.

3. **Activate the Virtual Environment**

    - **On Linux/Mac:**
      ```bash
      source venv/bin/activate
      ```
    - **On Windows:**
      ```bash
      .\venv\Scripts\activate
      ```

   After activation, your terminal prompt should change to indicate that you are now working inside the virtual environment.

4. **Install Dependencies from `requirements.txt`**

   If your project has a `requirements.txt` file that lists the necessary dependencies, you can install them with the following command:
   ```bash
   pip install -r requirements.txt
   ```

   This will install all the required packages into your virtual environment.

5. **Running the Python Script**

   After setting up the environment and installing the dependencies, you can run your Python script like this:
   ```bash
   python3 src/mksld.py
   ```

6. **Deactivate the Virtual Environment**[Docker_Installation_Guide.md](../../../Desktop/Docker_Installation_Guide.md)

   When you're done working in the virtual environment, you can deactivate it by running:
   ```bash
   deactivate
   ```
## Docker

To run the application in a Docker container you can run the `docker-run.sh` script below. Make sure to install Docker on your OS before.

```sh
./docker-run.sh
```

## Credit
- [@uwukko](https://x.com/uwukko/status/1838640932167503998) for posting about the media API endpoint.
- [@grok](https://x.com/grok) for boiler-plate element traversal with `requests`.
