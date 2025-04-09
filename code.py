import streamlit as st
import requests
import openpyxl
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup

# Form input untuk data
st.title('DASHBOARD FENOMENA')
st.write("Selamat datang di dashboard untuk melihat fenomena di Kabupaten Pulang Pisau!")

st.header("Antara News")
st.write("https://kalteng.antaranews.com/kabar-daerah/pulang-pisau")

awal = st.number_input("Halaman Awal [Antara News]", min_value=1)
akhir = st.number_input("Halaman Akhir [Antara News]", min_value=2, max_value=100)

st.header("Fast News")
st.write("https://fastnews.co.id/category/berita-daerah/pulang-pisau")

awal2 = st.number_input("Halaman Awal [Fast News]", min_value=1)
akhir2 = st.number_input("Halaman Akhir [Fast News]", min_value=2, max_value=100)

st.header("ProKalteng News")
st.write("https://prokalteng.jawapos.com/pemerintahan/pemkab-pulang-pisau")

awal3 = st.number_input("Halaman Awal [ProKalteng News]", min_value=1)
akhir3 = st.number_input("Halaman Akhir [ProKalteng News]", min_value=2, max_value=100)

st.header("News Way")
st.write("https://newsway.co.id/category/kalteng/pulang-pisau")

awal4 = st.number_input("Halaman Awal [News Way]", min_value=1)
akhir4 = st.number_input("Halaman Akhir [News Way]", min_value=2, max_value=100)

# Menggunakan data yang dimasukkan
article_results1= []
for page in range(awal,akhir):
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

article_results11= []
for page in range(awal2,akhir2): 
  url = f'https://fastnews.co.id/category/berita-daerah/pulang-pisau/page/{page}/'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('div', class_='col-md-12 col-sm-12 col-xs-12')
  for article in articles:
    title = article.find('h4',class_='entry-title').find('a')['title']
    date = article.find('span', class_='posted-on').text.strip()
    url = article.find('h4',class_='entry-title').find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    content = cSoup.find('div', class_='entry-content bloglo-entry').text.strip()

    article_results11.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})
    
df_11 = pd.DataFrame(article_results11)

article_results8= []
for page in range(awal3,akhir3):
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

    article_results8.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})

df_8 = pd.DataFrame(article_results8)

article_results12= []
for page in range(awal4,akhir4): 
  url = f'https://newsway.co.id/category/kalteng/pulang-pisau/page/{page}/'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('div', class_='post56__text')
  for article in articles:
    title = article.find('a').text.strip()
    date = article.find('div', class_='meta56__item meta56__date').text.strip()
    url = article.find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    content = cSoup.find('div', class_='entry-content single56__content single56__post_content single56__body_area').text.strip()

    article_results12.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url
        })
df_12 = pd.DataFrame(article_results12)

file_path = 'Artikel.xlsx'

# Tombol untuk generate Excel
if st.button('Generate File'):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df_1.to_excel(writer, sheet_name='ANTARA NEWS', index=False)
        df_11.to_excel(writer, sheet_name='FAST NEWS', index=False)
        df_8.to_excel(writer, sheet_name='PROKALTENG NEWS', index=False)
        df_12.to_excel(writer, sheet_name='NEWS WAY', index=False)
    
    st.success("Output berhasil dibuat dan disimpan sebagai Artikel.xlsx")

# Setelah file dibuat, menyediakan tombol untuk mengunduh file Excel
    with open(file_path, "rb") as f:
        st.download_button(
            label="Download File",
            data=f,
            file_name="Artikel.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Menampilkan Data di Streamlit
st.write("Antara News")
st.dataframe(df_1)

st.write("Fast News")
st.dataframe(df_11)

st.write("ProKalteng News")
st.dataframe(df_8)

st.write("News Way")
st.dataframe(df_12)
