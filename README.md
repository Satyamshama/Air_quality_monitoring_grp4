# Air Quality Monitoring

## Overview
Air Quality Monitoring is a software tool designed to detect and analyze air quality. It collects air quality data, processes it, and displays meaningful insights through a graphical user interface (GUI).

## Features
- **Real-time Data Collection**: Retrieves air quality data from sensors or external sources.
- **Graphical User Interface (GUI)**: User-friendly interface to display air quality metrics.
- **Data Analysis**: Computes relevant statistics such as AQI (Air Quality Index).
- **Alerts & Notifications**: Warns users when air quality levels are hazardous.
- **Data Logging**: Stores historical air quality data for future analysis.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries (install using the command below)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Air_quality_monitoring_grp4.git
   cd Air_quality_monitoring_grp4
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python mainGUI.py
   ```

## Usage
1. Start the application by running `mainGUI.py`.
2. The GUI will display real-time air quality data.
3. View alerts when air quality is poor.
4. Save and analyze past air quality records.

## Project Structure
```
Air_quality_monitoring_grp4/  <br>
│── README.md            # Project documentation <br>
│── getData.py           # Script to collect air quality data  <br>
│── mainGUI.py           # GUI application  <br>

```

## Dependencies
The project uses the following libraries:
- `tkinter` (for GUI)
- `requests` (for fetching data from external sources, if applicable)
- `matplotlib` (for data visualization)
- `pandas` (for data handling and analysis)

To install these dependencies manually, run:
```bash
pip install tkinter requests matplotlib pandas
```

## Contributing
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and push to GitHub.
4. Open a Pull Request.


## Contact
For any queries, reach out to **Satyam Sharma** at satyamsharma0@gmail.com.

