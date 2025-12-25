#TO create env:
mkdir amazon
cd amazon

python3 -m venv .env
source .env/bin/activate


#To install librabries:
python3 -m pip install requests beautifulsoup4 lxml pandas

#To run: 
streamlit run app.py 

