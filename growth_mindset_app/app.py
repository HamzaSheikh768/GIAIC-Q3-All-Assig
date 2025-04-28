import streamlit as st
import pandas as pd
import os
from io import BytesIO


st.set_page_config(page_title="Data Sweeper", layout="wide")

st.title("Data Sweeper Sterling Integrator By Muhammad Faizan")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization, creating the project for Quarter 3!")

uploaded_files = st.file_uploader("Upload Your Files (accepts CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file: {file_ext} format. Please upload a CSV or Excel file.")
            continue

        # Display file details
        st.write(f"### Preview of {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"Data Cleaning Options for {file.name}")

        if st.button(f"Remove duplicates from {file.name}"):
            df.drop_duplicates(inplace=True)
            st.write("Duplicates Removed!")

        if st.button(f"Fill missing values in {file.name}"):
            numeric_cols = df.select_dtypes(include=['number']).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            st.write("Missing values have been filled!")

        # Column Selection
        st.subheader(f"Select Columns to Keep for {file.name}")
        selected_columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader(f"Data Visualization for {file.name}")
        if st.checkbox(f"Show Visualization for {file.name}"):
            if df.select_dtypes(include='number').shape[1] >= 2:
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
            else:
                st.warning("Not enough numeric columns to display a chart.")

        # File Conversion
        st.subheader(f"Conversion Options for {file.name}")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type ="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files processed successfully!")  
