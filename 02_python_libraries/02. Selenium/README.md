# Selenium Web Scraping with Python

This repository is a structured learning path for mastering **Selenium** from the perspective of **web scraping**.  
Each script in this repo demonstrates one concept, moving step by step from setup to real-world scraping projects.  

---

## 📂 Repository Structure

SELENIUM/
│── README.md # Overview of this repository
│── requirements.txt # Dependencies
│
├── 01_setup_driver.py # Install, configure, and launch browser
├── 02_navigate_pages.py # Opening pages, navigating back/forward, refresh
├── 03_find_elements.py # Locating elements (id, name, xpath, css)
├── 04_extract_text.py # Extracting text and attributes
├── 05_interact_elements.py # Clicking, sending keys, dropdowns, checkboxes
├── 06_waits.py # Implicit vs Explicit waits
├── 07_scroll_load.py # Handling scrolling, infinite scroll pages
├── 08_pagination.py # Scraping multi-page results
├── 09_iframes_windows.py # Handling iframes & multiple browser tabs
├── 10_download_files.py # Automating file downloads
├── 11_login_session.py # Logging into websites (cookies, sessions)
├── 12_dynamic_content.py # Scraping AJAX / JS-heavy sites
├── 13_headless_browser.py # Running Selenium without GUI
├── 14_error_handling.py # Try/except + retries for robust scraping
│
├── projects/
│ ├── amazon_books.py # Example: scrape book data from Amazon
│ ├── linkedin_jobs.py # Example: scrape job postings
│ └── imdb_top_movies.py # Example: scrape top 250 movies




---

## 🚀 Learning Goals

- Set up Selenium with Python easily  
- Learn navigation, element selection, and interaction  
- Handle waits, scrolling, and pagination  
- Work with iframes, multiple tabs, and file downloads  
- Manage logins and sessions for protected content  
- Scrape JavaScript-heavy websites  
- Run Selenium in headless mode for automation  
- Apply error handling for robust scraping pipelines  
- Build small projects to showcase practical skills  

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
