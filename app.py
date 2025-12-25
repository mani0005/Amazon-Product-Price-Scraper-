import streamlit as st
from amazon_scraper import scrape_multiple_products

st.set_page_config(page_title="Amazon Multi-Product Scraper", layout="centered")

st.title("🛒 Amazon Multi-Product Scraper")
st.write("Scrape multiple products from Amazon search pages")

search_url = st.text_input(
    "Amazon Search URL",
    placeholder="https://www.amazon.in/s?k=mobile+phones"
)

pages = st.selectbox("Number of pages to scrape", [1, 2])

if st.button("Scrape Products"):
    if search_url:
        with st.spinner("Scraping products..."):
            products = scrape_multiple_products(search_url, pages)

        if products:
            st.success(f"Scraped {len(products)} products")

            for i, product in enumerate(products, start=1):
                st.markdown(f"### 📦 Product {i}")
                st.write(f"**Name:** {product[0]}")
                st.write(f"**Price:** ₹{product[1]}")
                st.write(f"**Rating:** {product[2]}")
                st.write(f"**Availability:** {product[3]}")
                st.divider()

            st.download_button(
                label="📥 Download CSV",
                data=open("amazon_products.csv", "rb"),
                file_name="amazon_products.csv",
                mime="text/csv"
            )
        else:
            st.error("No products found.")
    else:
        st.warning("Please enter a valid Amazon search URL.")
