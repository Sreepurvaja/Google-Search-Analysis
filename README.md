# Google-Search-Analysis

Approximately 3.5 billion searches are performed on Google daily, which means that approximately 40,000 searches are performed every second on Google. So Google search is a great use case for analyzing data based on search queries.

Google doesn’t give much access to the data about daily search queries, but another application of google known as Google Trends can be used for the task of Google search analysis. Google Trends provides an API that can be used to analyze the daily searches on Google. This API is known as pytrends, you can easily install it in your systems by using the pip command; 


        pip install pytrends.

# Google Search Analysis with Flask

This Flask application allows users to analyze Google search trends based on keywords. Users can input a keyword, and the application will fetch Google Trends data for that keyword and visualize the top 10 regions where the keyword is most popular.

## Features

- Input a keyword and visualize Google search trends data.
- Displays the top 10 regions where the keyword is most popular.
- Uses the Google Trends API to fetch data.
- Built with Python Flask for the backend and Jinja2 templating for rendering HTML templates.

## Run the Flask application:

       python app.py


## Usage

1. Enter a keyword in the input field and click "Submit".
2. The application will fetch Google Trends data for the keyword and display the top 10 regions where it's most popular.
3. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Screenshots




        
        
