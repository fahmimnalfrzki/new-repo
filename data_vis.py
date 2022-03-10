import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#set config
st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    st.title('Data Visualization of Supermarket Sales')
    st.write('Sumber data: https://www.kaggle.com/aungpyaeap/supermarket-sales')
    def get_data():
        return pd.read_csv('supermarket_sales - Sheet1.csv')
    data = get_data()
    data.rename(columns={'Total': 'Revenue'},inplace=True)
    dout = data[data.Revenue>=1000].index
    data.drop(dout,axis=0,inplace=True)


    c1,c2=st.columns(2)

    with c1:
        st.header('Quantity Product Sold')
        product=data.groupby('Product line').sum()['Quantity'].sort_values(ascending=True)
        plt.figure(figsize=(12,6))
        plt.title('Top Product')
        plt.barh(product.index,product,color=['teal','coral','purple','#48D1CC','pink','maroon'])
        plt.xlabel('Quantity')
        plt.ylabel('Product')
        st.pyplot()
        st.markdown('Produk paling banyak terjual adalah dari penjualan aksesoris elektronik')

    with c2:
        st.header('GMV in January')
        data['gmv'] = data['Unit price']*data['Quantity']
        gmv_jan = data[data['Date']<='1/31/2019'].groupby('Date').mean()['gmv']
        gmv_jan.plot(kind='line',title='GMV in January',figsize=(13,6))
        st.pyplot()
        st.markdown('GMV pada bulan januari mengalami tren negatif')

    c3,c4 = st.columns(2)
    with c3:
        st.header('3 Month Revenue')
        
        Rd = data.groupby('Date').sum()['Revenue']
        Rd.plot(kind='area',figsize=(10,5),title='3 Month Revenue',color='teal')
        st.pyplot()
        st.markdown('Rekap pendapatan selama 3 bulan')
        Jan = data[data.Date<='1/31/2019'].groupby('Date').sum()['Revenue']
        feb = data[(data.Date>'1/31/2019')&(data.Date<'2/31/2019')].groupby('Date').sum()['Revenue']
        Mar = data[(data.Date>'2/31/2019')&(data.Date<'3/31/2019')].groupby('Date').sum()['Revenue']
        rec = st.radio('Select a month: ',('January','February','March'))
        if rec=='January':
            st.write('Rekap pendapatan bulan Januari: ', Jan.sum())
        elif rec=='February':
            st.write('Rekap pendapatan bulan Februari: ', feb.sum())
        else:
            st.write('Rekap pendapatan bulan Maret: ', Mar.sum())

    with c4:
        st.header('Payment Method')
        P=data.groupby('Payment').count()['Invoice ID']
        P.plot(kind='pie',figsize=(5,5),autopct='%.2f%%',title='Metode Pembayaran')
        st.pyplot()
        st.markdown('Pembayaran yang sering digunakan adalah dengan E-wallet dan Cash')
    
    st.header('Distribusi Data')
    data.plot(kind='box',figsize=(12,5))
    st.pyplot()

    cb = st.radio("Select a column: ",
        ('Unit price', 'Quantity','Tax 5%','Revenue','Cost of goods sold','Rating'))
    if cb=='Unit price':
        data['Unit price'].plot(kind='box')
        st.pyplot()
    elif cb == 'Quantity':
        data.Quantity.plot(kind='box')
        st.pyplot()
    elif cb == 'Tax 5%':
        data['Tax 5%'].plot(kind='box')
        st.pyplot()
    elif cb == 'Revenue':
        data.Revenue.plot(kind='box')
        st.pyplot()
    elif cb == 'Cost of goods sold':
        data.cogs.plot(kind='box')
        st.pyplot()
    else:
        data.Rating.plot(kind='box')
        st.pyplot()
       

