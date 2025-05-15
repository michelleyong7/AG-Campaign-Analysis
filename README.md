*AG Nick Brown 2024 Campaign - Public Contributions Dashboard*

*Created an end to end data analysis and visualization project exploring public donation trends for the current Washington Attorney General candidiate Nick Brown.*

**Overview**

This project analyzes public donation data for Nick Brown's 2024 Washington State Attorney General campaign, sourced from the Washington State Public Disclosure Commission (PDC). It includes full-cycle data analysis using:

* Python & pandas for data cleaning  
* SQLite for structured querying  
* Tableau for dashboard design & storytelling  

The final dashboard visualizes donation trends, top donor cities, and post-primary fundraising momentum.

**Tools Utilized**

* Python 
* SQLite  
* Tableau  
* VS Code  
* Public campaign finance data (CSV from WA PDC)

**Key Insights**

* October saw the *highest fundraising month* at over **$474,000**, indicating strong pre-election momentum.  
* Donors were concentrated in urban centers like **Seattle, Bellevue, and Olympia**.  
* Post-primary weeks showed a *rapid cumulative growth*, especially between weeks **41–43**.

**Dashboard Preview**

![Campaign Dashboard](tableau/dashboard.png)

**Project Structure**

```
AG-campaign-analysis/
├── data/
│   ├── raw/                # Original data files (e.g., CSVs from PDC)
│   └── processed/          # Cleaned data, database, and analysis outputs
├── scripts/                # Python scripts for cleaning, loading, and querying data
├── sql/                    # Pure SQL scripts for analysis
├── tableau/                # Tableau workbook and dashboard images
├── README.md               # Project documentation (this file)
```

**What I Learned**

* Applied **Python (pandas)** to clean and transform real-world campaign finance data 
* Structured and queried datasets using **SQL (SQLite)** to extract time-based trends and donor insights  
* Built an interactive, insight-driven **Tableau dashboard** that visually communicates key campaign fundraising patterns  
* Practiced **end-to-end analysis** — from raw CSV to visual story — showcasing the complete data analyst workflow  

 **Data Source**

All contribution data was publicly sourced from the [Washington State Public Disclosure Commission](https://www.pdc.wa.gov/).


