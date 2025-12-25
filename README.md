# Amazon Product Price Scraper 🛒

This project is a Python-based web scraping application that extracts product details from Amazon.  
It supports scraping **multiple products from search result pages** and displays the data using a **Streamlit frontend**.

---

## 📌 Features

- Scrapes Amazon product details using Python
- Supports multi-product scraping from search result pages
- Handles pagination (1–2 pages)
- Extracts:
  - Product Name
  - Price
  - Rating
  - Availability
- Stores data in a CSV file
- Interactive Streamlit web interface
- Implements ethical scraping practices

---

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – for sending HTTP requests
- **BeautifulSoup** – for parsing HTML
- **Streamlit** – for frontend UI
- **CSV module** – for data storage

---

## 📂 Project Structure

amazon-price-scraper/
│
├── app.py              # Streamlit frontend
├── scraper.py          # Backend scraping logic
├── amazon_products.csv # Output CSV file

## Run the Streamlit App
streamlit run app.py


