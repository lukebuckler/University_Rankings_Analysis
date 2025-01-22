# Global University Rankings Analysis Dashboard

An interactive dashboard analyzing worldwide university rankings data, built with Python and Streamlit.

## Overview

This project analyzes global university rankings data to provide insights into:
- Geographic distribution of top universities
- Country and city-wise university concentrations
- Ranking distributions and patterns
- Excellence clusters across different ranking brackets

## Features

- Interactive world map visualization
- Real-time filtering by:
  - Countries
  - Ranking range
  - Number of displayed entries
- Key metrics dashboard
- Multiple visualization types:
  - Choropleth maps
  - Bar charts
  - Histograms
  - Excellence cluster analysis

## Technology Stack

- Python 3.8+
- Streamlit
- Plotly
- Pandas
- Seaborn
- Matplotlib

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/university-rankings-analysis.git

# Navigate to project directory
cd university-rankings-analysis

# Install dependencies
pip install -r requirements.txt
```

## Data Structure

The analysis uses a CSV file with the following columns:
- University: Institution name
- Country: Location country
- City: Location city
- Global Rank: International ranking position

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Access the dashboard at `http://localhost:8501`

3. Use the sidebar filters to:
   - Select specific countries
   - Adjust ranking range
   - Modify number of displayed entries

## Analysis Features

### Geographic Distribution
- Interactive world map showing university density
- Country-wise distribution analysis
- City-level concentration patterns

### Rankings Analysis
- Distribution of rankings across institutions
- Excellence clusters identification
- Comparative analysis across regions

### Performance Metrics
- Total university counts
- Country and city statistics
- Average ranking calculations

## Project Structure

```
university-rankings/
├── app.py                 # Main Streamlit application
├── data/
│   └── universities.csv   # Dataset
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## Future Improvements

1. Additional Analysis Features:
   - Time series analysis of ranking changes
   - Subject-wise rankings
   - Regional performance comparisons

2. Technical Enhancements:
   - Advanced filtering options
   - Export functionality
   - API integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [your.email@example.com]
Project Link: [https://github.com/yourusername/university-rankings-analysis]