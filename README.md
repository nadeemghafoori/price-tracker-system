# Price Tracker System

This project is a web-based application that helps you monitor product prices across online stores. Just enter an item’s URL and your desired price, and the system will automatically track it and send you an email notification when the price drops to your target. You can track multiple items at once, making it easy to stay updated on the best deals.

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/nadeemghafoori/price-tracker-system.git
   ```
2. Navigate to the project folder:
   ```bash
   cd price-tracker-system
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Update configuration files before running:

   - `src/config.py` → Set `DEBUG` (True/False) and your admin email in `ADMINS`.
   - `src/app.py` → Replace `app.secret_key` with your own secret key.
   - `src/models/alerts/constants.py` → Add your Mailgun `API_KEY`, `FROM email`, and `domain`.
   - `src/common/database.py` → Set `Database.URI` to your MongoDB URI and make sure a database named `PriceTrackerSystem` exists.

6. Run the app:
   ```bash
   python src/run.py
   ```
7. After running, check the terminal output for something like `Running on http://127.0.0.1:5000/`, Open that URL in your browser to view it.
