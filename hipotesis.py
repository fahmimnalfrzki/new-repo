import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np


def app():
    st.title('Hyphothesis Testing')
    
    def get_data():
        return pd.read_csv('supermarket_sales - Sheet1.csv')
    data = get_data()
    data.rename(columns={'Total': 'Revenue'},inplace=True)
    dout = data[data.Revenue>=1000].index
    data.drop(dout,axis=0,inplace=True)

    Y = data[data.City == 'Yangon'].groupby('Date').sum()['Quantity']
    N = data[data.City == 'Naypyitaw'].groupby('Date').sum()['Quantity']
    M = data[data.City == 'Mandalay'].groupby('Date').sum()['Quantity']

    with st.expander("Mean Quantity Product"):
        st.write('Rata-rata jumlah produk terjual di kota Yangon: ',Y.mean())
        st.write('Rata-rata jumlah produk terjual di kota Naypyitaw: ',N.mean())
        st.write('Rata-rata jumlah produk terjual di kota Mandalay: ',M.mean())

    st.write('''
    Hipotesis yang akan diuji adalah apakah rerata jumlah penjualan produk di Yangon, 
    Naypyitaw dan Mandalay terdapat perbedaan secara signifikan atau tidak. Maka dugaan awal 
    (atau yang didefinisikan sebagai **H0** ) adalah tidak ada perbedaan secara signifikan terhadap rerata ketiga kota.
    Sedangkan dugaan alternatif (didefinisikan sebagai **H1**) adalah ketiga kota reratanya berbeda secara signifikan.
    ''')
    st.markdown('''**Hipotesa** \n
    H0: Yangon_quantity.mean = Naypyitaw_quantity.mean = Mandalay_quantity.mean\n    
    H1: Yangon_quantity.mean != Naypyitaw_quantity.mean != Mandalay_quantity.mean''')

    st.subheader('Uji ANOVA')
    f,p = stats.f_oneway(Y,N,M)
    st.markdown('''Dari hasil perhitungan menggunakan uji ANOVA didapat hasil sebagai berikut:''')
    st.write('Pvalue : ', p)
    st.write('f-stat: ', f)
    st.subheader('Kesimpulan')
    st.markdown('''Pada taraf signifikan 5% nilai p-value > 0.05 maka keputusan yang diambil adalah **H0 diterima**, 
                artinya rerata jumlah produk terjual di ketiga kota tidak berbeda secara signifikan. 
    ''')
    y_pop = np.random.normal(Y.mean(),Y.std(),10000)
    n_pop = np.random.normal(N.mean(),N.std(),10000)
    m_pop = np.random.normal(M.mean(),M.std(),10000)

    plt.figure(figsize=(16,5))
    sns.distplot(y_pop, label='Yangon Average Quantity *Pop',color='blue')
    sns.distplot(n_pop, label='Naypyitaw Average Quantity *Pop',color='red')
    sns.distplot(m_pop, label='Mandalay Average Quantity *Pop',color='yellow')

    plt.axvline(Y.mean(), color='blue', linewidth=2, label='Yangon mean')
    plt.axvline(N.mean(), color='red',  linewidth=2, label='Naypyitaw mean')
    plt.axvline(M.mean(), color='yellow',  linewidth=2, label='Mandalay mean')

    plt.legend()
    st.pyplot()

    st.markdown('''Jika digambarkan dalam grafik distribusi maka mean dari ketiga kota tersebut
                    hampir menyatu. Hal ini wajar terjadi mengingat rerata jumlah produk yang terjual di kota
                    Yangon, Naypyitaw dan Mandalay tidak berbeda secara signifikan.
    ''')


