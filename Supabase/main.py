# main.py

import os
from fastapi import FastAPI, Depends, HTTPException, Header
from supabase import create_client, Client
from gotrue.errors import AuthApiError
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.get("/all-data")
def get_all_database_info():
    """
    An endpoint to automatically discover and fetch all records from all tables
    in the public schema of the database.
    """
    all_data = {}
    try:
        # Step 1: Call the RPC to get all table names.
        # This requires the 'get_all_table_names' function created in the Supabase SQL Editor.
        tables_response = supabase.rpc('get_all_table_names', {}).execute()
        
        if tables_response.data:
            table_names = [item['table_name'] for item in tables_response.data]

            # Step 2: Loop through each table name and fetch its data.
            for table_name in table_names:
                records_response = supabase.table(table_name).select('*').execute()
                all_data[table_name] = records_response.data
        
        return all_data

    except Exception as e:
        error_message = str(e)
        # Provide a helpful error if the user forgot to create the SQL function.
        if "function public.get_all_table_names() does not exist" in error_message:
            raise HTTPException(
                status_code=500, 
                detail="Error: The helper function 'get_all_table_names' was not found in your database. Please create it using the Supabase SQL Editor."
            )
        raise HTTPException(status_code=500, detail=f"An error occurred: {error_message}")

