from base64 import b64encode
import base64
import streamlit as st
import pandas as pd

def filter_columns(df):
    # Select only the specified columns
    columns_to_keep = ["First Name", 'Last Name', 'Email', 'Phone Number', 'Company/School', 'Title/Position/Role']
    filtered_df = df[columns_to_keep]
    return filtered_df

def main():
    st.title("CSV Cleaner")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file, skiprows=1)  # skip the first row
        
        # # Print columns
        # st.write("Columns of the uploaded CSV:")
        # st.write(df.columns.tolist())
        
        st.write("Original Sheet:")
        st.write(df)
        
        # Filter columns
        filtered_df = filter_columns(df)
        
        st.write("Filtered Sheet:")
        st.write(filtered_df)
        
        # Download link
        # st.markdown(get_download_link(filtered_df), unsafe_allow_html=True)
        st.download_button(label="Download Filtered Sheet", data=get_download_link(filtered_df), file_name='data.csv', mime='text/csv')

def get_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Bypass pandas to write directly to string
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download CSV File</a>'
    return href

if __name__ == "__main__":
    main()
