# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("My Parents new healthy diner")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)


name_on_order = st.text_input("Name of Smoothie:")
st.write("The name on your Smothiee will be:", name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# editable_df = st.data_editor(my_dataframe)

submitted = st.button('submit')

# if submitted:
#     st.success('Someone clicked the button', icon = '👍')

#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)

if ingredients_list:  
   ingredients_string=''
   
   for fruit_chosen in ingredients_list:
       ingredients_string += fruit_chosen + ' '

   #st.write(ingredients_string)

   my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

   st.write(my_insert_stmt)
   # st.stop() 
   time_to_insert = st.button('Submit order')
   if time_to_insert:
       session.sql(my_insert_stmt).collect()
       st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit")
# st.text(fruityvice_response.json())
fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)


 






