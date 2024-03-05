from base64 import b64encode
import streamlit as st
import pandas as pd

def filter_columns(df):
    # Select only the specified columns
    columns_to_keep = ['Stock Number', 'Product Name', 'Email Address']
    filtered_df = df[columns_to_keep]
    return filtered_df

def main():
    st.title("CSV Column Filter")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file, skiprows=1)  # skip the first row
        
        # Print columns
        # st.write("Columns of the uploaded CSV:")
        # st.write(df.columns.tolist())
        
        st.write("Original DataFrame:")
        st.write(df)
        
        # Filter columns
        filtered_df = filter_columns(df)
        
        st.write("Filtered DataFrame:")
        st.write(filtered_df)
        
        # Download link
        st.markdown(get_download_link(filtered_df), unsafe_allow_html=True)

def get_download_link(df):
    csv = df.to_csv(index=False)
    href = f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="filtered_data.csv">Download Filtered CSV File</a>'
    return href

if __name__ == "__main__":
    main()
