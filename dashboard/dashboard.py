import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_byage_df(df):
    df['Age Group'] = df['Age'].apply(lambda x: 'Young' if x <= 30 else ('Senior' if x > 51 else 'Middle-aged'))
    byage = df.groupby('Age Group').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return byage

def create_byloc_df(df):
    byloc = df.groupby('Location').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return byloc

def create_bygender_df(df):
    bygender = df.groupby('Gender').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bygender

def create_bysubs_df(df):
    bysubs = bysubs = df.groupby('Subscription Status').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bysubs

def create_bypromo_df(df):
    bypromo = df.groupby(['Discount Applied', 'Promo Code Used']).agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bypromo 

def create_bypayment_df(df):
    bypayment = df.groupby('Payment Method').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bypayment

def create_bycategory_df(df):
    bycategory = df.groupby('Category').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bycategory

def create_byitems_df(df):
    byitems = df.groupby(['Category', 'Item Purchased']).agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return byitems

def create_bysize_df(df):
    bysize = df.groupby('Size').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bysize

def create_bycolor_df(df):
    bycolor = df.groupby('Color').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return bycolor

def create_byrating_df(df):
    df['Rating Group'] = df['Review Rating'].apply(lambda x: 'Fair' if x < 3.5 else('Excellent' if x >= 4 else 'Decent'))
    byrating = df.groupby('Rating Group').agg({'Customer ID': 'nunique'}).rename(columns={'Customer ID': 'Customer Count'}).reset_index()
    return byrating 

# load data
df = pd.read_csv('https://raw.githubusercontent.com/semidust/Consumer-Behavior-Analysis/main/dashboard/shopping_behavior_updated.csv')

byage_df = create_byage_df(df)
byloc_df = create_byloc_df(df)
bygender_df = create_bygender_df(df)
bysubs_df = create_bysubs_df(df)
bypromo_df = create_bypromo_df(df)
bypayment_df = create_bypayment_df(df)
bycategory_df = create_bycategory_df(df)
byitems_df = create_byitems_df(df)
bysize_df = create_bysize_df(df)
bycolor_df = create_bycolor_df(df)
byrating_df = create_byrating_df(df)

st.title("Customer Behavior Dashboard :sparkles:")
st.divider()

# customer counts
col1, col2, col3 = st.columns(3)

with col1:
    subscribed_cust = df[df['Subscription Status'] == 'Yes'].shape[0]
    st.metric('Subscribed Customers', value='{:,}'.format(subscribed_cust))

with col2:
    notsubscribed_cust = df[df['Subscription Status'] == 'No'].shape[0]
    st.metric('Non-Subscribed Customers', value='{:,}'.format(notsubscribed_cust))

with col3:
    total_cust = df['Customer ID'].nunique()
    st.metric('Total Customers', value='{:,}'.format(total_cust))

st.divider()

st.header(':blue[Customer Profile]')
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['AGE', 'LOCATION', 'PAYMENT', 'GENDER', 'SUBSCRIPTION STATUS', 'PROMO USED'])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=byage_df.sort_values(by='Customer Count', ascending=False),
            x='Age Group',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=byloc_df.sort_values(by='Customer Count', ascending=False).head(),
            x='Location',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)

with tab3:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=bypayment_df.sort_values(by='Customer Count', ascending=False).head(),
            x='Payment Method',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)    

with tab4:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#D47DA4', '#72BCD4']

        plt.pie(
            data=bygender_df,
            x='Customer Count',
            autopct="%.1f%%",
            colors=colors,
            wedgeprops={'width': 0.4},
            pctdistance=1.2,
            textprops={'color': 'black'}
        )
        
        plt.legend(title='Gender', labels= bygender_df['Gender'], loc='upper left')
        st.pyplot(fig)

with tab5:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#D47DA4', '#72BCD4']

        plt.pie(
            data=bysubs_df,
            x='Customer Count',
            autopct="%.1f%%",
            colors=colors,
            wedgeprops={'width': 0.4},
            pctdistance=1.2,
            textprops={'color': 'black'}
        )
        
        plt.legend(title='Subscribed', labels= bysubs_df['Subscription Status'], loc='upper right')
        st.pyplot(fig)

with tab6:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#D47DA4', '#72BCD4']

        plt.pie(
            data=bypromo_df,
            x='Customer Count',
            autopct="%.1f%%",
            colors=colors,
            wedgeprops={'width': 0.4},
            pctdistance=1.2,
            textprops={'color': 'black'}
        )
        
        plt.legend(title='Promo', labels= bypromo_df['Promo Code Used'], loc='upper right')
        st.pyplot(fig)

st.header(':blue[Product Preferences]')
tab1, tab2, tab3, tab4, tab5 = st.tabs(['CATEGORY', 'ITEMS', 'SIZE', 'COLOR', 'RATING'])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=bycategory_df.sort_values(by='Customer Count', ascending=False),
            x='Category',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=byitems_df.sort_values(by='Customer Count', ascending=False).head(),
            x='Item Purchased',
            y='Customer Count',
            palette=colors
        )
        
        plt.title('Best-selling Items')
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=byitems_df.sort_values(by='Customer Count', ascending=True).head(),
            x='Item Purchased',
            y='Customer Count',
            palette=colors
        )
        
        plt.title('Least-selling Items')
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)

with tab3:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=bysize_df.sort_values(by='Customer Count', ascending=False),
            x='Size',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig)    

with tab4:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=bycolor_df.sort_values(by='Customer Count', ascending=False).head(7),
            x='Color',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig) 

with tab5:
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ['#72BCD4', '#C4E9F5', '#C4E9F5']

        sns.barplot(
            data=byrating_df.sort_values(by='Customer Count', ascending=False),
            x='Rating Group',
            y='Customer Count',
            palette=colors
        )
        
        plt.xlabel(None)
        plt.ylabel(None)
        st.pyplot(fig) 
    

