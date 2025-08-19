import streamlit as st
import requests
import openpyxl
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup

# Form input untuk data
st.title('PROCRANE')
st.write("Selamat datang di PROCRANE untuk melihat fenomena Kabupaten Pulang Pisau!")

st.header("Antara News")
st.write("https://kalteng.antaranews.com/kabar-daerah/pulang-pisau")
awal = st.number_input("Halaman Awal [Antara News]", min_value=1)
akhir = st.number_input("Halaman Akhir [Antara News]", min_value=2, max_value=100)

st.header("ProKalteng News")
st.write("https://prokalteng.jawapos.com/pemerintahan/pemkab-pulang-pisau")
awal2 = st.number_input("Halaman Awal [ProKalteng News]", min_value=1)
akhir2 = st.number_input("Halaman Akhir [ProKalteng News]", min_value=2, max_value=100)

# Menggunakan data yang dimasukkan
article_results1= []
for page in range(awal,akhir+1):
  url = f'https://kalteng.antaranews.com/kabar-daerah/pulang-pisau/{page}'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('article', class_='simple-post simple-big clearfix')
  for article in articles:
    title = article.find('h3').find('a')['title']
    date = article.find('span').text.strip()
    url = article.find('h3').find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    content = cSoup.find('div', class_='post-content clearfix font17').text.strip()

    article_results1.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})
    
df_1 = pd.DataFrame(article_results1)

article_results2= []
for page in range(awal2,akhir2+1):
  url = f'https://prokalteng.jawapos.com/pemerintahan/pemkab-pulang-pisau/page/{page}/'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('div', class_='tdb_module_loop td_module_wrap td-animation-stack td-cpt-post')
  for article in articles:
    title = article.find('p', class_= 'entry-title td-module-title').text.strip()
    url = article.find('p', class_= 'entry-title td-module-title').find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    date = cSoup.find('time', class_='entry-date updated td-module-date').text.strip()
    content = cSoup.find('div', class_='td_block_wrap tdb_single_content tdi_85 td-pb-border-top td_block_template_1 td-post-content tagdiv-type').text.strip()

    article_results2.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})

df_2 = pd.DataFrame(article_results2)

file_path = 'Fenomena.xlsx'

# Tombol untuk generate Excel
if st.button('Generate File'):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df_1.to_excel(writer, sheet_name='ANTARA NEWS', index=False)
        df_2.to_excel(writer, sheet_name='PROKALTENG NEWS', index=False)
      
    st.success("Output berhasil dibuat dan disimpan: Fenomena.xlsx")

# Setelah file dibuat, menyediakan tombol untuk mengunduh file Excel
    with open(file_path, "rb") as f:
        st.download_button(
            label="Download File",
            data=f,
            file_name="Fenomena.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# Menampilkan Data di Streamlit
st.write("Antara News")
st.dataframe(df_1)

st.write("ProKalteng News")
st.dataframe(df_2)
