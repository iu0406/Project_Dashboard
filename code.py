import streamlit as st
import requests
import openpyxl
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup

# Form input untuk data
st.title('DASHBOARD FENOMENA')
st.write("Selamat datang di dashboard untuk melihat fenomena Kabupaten Pulang Pisau!")

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

st.header("Trans Hapakat News")
st.write("https://www.transhapakat.web.id/?s=pulang+pisau")
awal5 = st.number_input("Halaman Awal [Trans Hapakat News]", min_value=1)
akhir5 = st.number_input("Halaman Akhir [Trans Hapakat News]", min_value=2, max_value=100)

st.header("Kalteng Pos News")
st.write("https://www.kaltengpos.info/pulang-pisau")
awal6 = st.number_input("Halaman Awal [Kalteng Pos News]", min_value=1)
akhir6 = st.number_input("Halaman Akhir [Kalteng Pos News]", min_value=2, max_value=100)

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

article_results10= []
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

    article_results10.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})
    
df_10 = pd.DataFrame(article_results10)

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
for page in range(awal4, akhir4):
    url = f'https://newsway.co.id/category/kalteng/pulang-pisau/page/{page}/'
    ge = requests.get(url)
    soup = BeautifulSoup(ge.text, 'html.parser')
    
    # Mengambil kelas 'primary56'
    primary_divs = soup.find_all('div', class_='primary56')

    for primary_div in primary_divs:
        articles = primary_div.find_all('div', class_='post56__text')

        for article in articles:      
            title = article.find('a').text.strip()
            date = article.find('div', class_='meta56__item meta56__date').text.strip()
            article_url = article.find('a')['href']

            cPage = requests.get(article_url)
            cSoup = BeautifulSoup(cPage.text, 'html.parser')

            content = cSoup.find('div', class_='entry-content single56__content single56__post_content single56__body_area').text.strip()

            article_results12.append({
                'date': date,
                'title': title,
                'content': content,
                'url': article_url})
  
df_12 = pd.DataFrame(article_results12)

article_results2= []
for page in range(awal5,akhir5): 
  url = f'https://www.transhapakat.web.id/page/{page}/?s=pulang+pisau'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('div', class_='td-block-span6')
  for article in articles:
    title = article.find('h3',class_='entry-title td-module-title').find('a')['title']
    date = article.find('span', class_='td-post-date').text.strip()
    url = article.find('h3',class_='entry-title td-module-title').find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    content = cSoup.find('p').text.strip()

    article_results2.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})

df_2 = pd.DataFrame(article_results2)

article_results6= []
for page in range(awal6,akhir6):
  url = f'https://www.kaltengpos.info/pulang-pisau?page={page}'
  ge = requests.get(url)
  soup = BeautifulSoup(ge.text,'html.parser')
  articles = soup.find_all('div', class_='latest__item')
  for article in articles:
    title = article.find('h2',class_='latest__title').text.strip()
    date = article.find('date', class_='latest__date').text.strip()
    url = article.find('h2',class_='latest__title').find('a')['href']

    cPage = requests.get(url)
    cSoup = BeautifulSoup(cPage.text,'html.parser')

    content = cSoup.find('article', class_='read__content clearfix').text.strip()

    article_results6.append({
        'date':date,
        'title':title,
        'content':content,
        'url':url})

df_6 = pd.DataFrame(article_results6)

file_path = 'Artikel.xlsx'

# Tombol untuk generate Excel
if st.button('Generate File'):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df_1.to_excel(writer, sheet_name='ANTARA NEWS', index=False)
        df_10.to_excel(writer, sheet_name='FAST NEWS', index=False)
        df_8.to_excel(writer, sheet_name='PROKALTENG NEWS', index=False)
        df_12.to_excel(writer, sheet_name='NEWS WAY', index=False)
        df_2.to_excel(writer, sheet_name='TRANS HAPAKAT NEWS', index=False)
        df_6.to_excel(writer, sheet_name='KALTENG POS NEWS', index=False)
    
    st.success("Output berhasil dibuat dan disimpan: Artikel.xlsx")

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
st.dataframe(df_10)

st.write("ProKalteng News")
st.dataframe(df_8)

st.write("News Way")
st.dataframe(df_12)

st.write("Trans Hapakat News")
st.dataframe(df_2)

st.write("Kalteng Pos News")
st.dataframe(df_6)
