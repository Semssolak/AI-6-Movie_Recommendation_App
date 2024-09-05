# Movie Recommendation System

This project is a **Movie Recommendation System** built using **Streamlit**. The application takes a movie title as input from the user and suggests 5 movies similar to the input movie using a correlation method based on user ratings. 

![Movie Recommendation System](moviepictures.webp)

## How It Works
- The application loads a dataset of user ratings for movies.
- It calculates the correlation between the user ratings of the input movie and other movies.
- Movies with the highest correlation to the input movie (and with more than 100 ratings) are recommended to the user.

### How to Use
1. **Movie Input**: Enter the name of a movie you like in the input field.
2. **Recommendation**: Press the "Recommend" button, and the app will suggest 5 similar movies.
3. **Dataset**: You can use your own dataset by changing the user rating and movie titles dataset paths in the `main.py` file.

## Customize for Different Datasets
- If you want to use this application with a different dataset, replace the `users.data` and `movie_id_titles.csv` files with your own.
- Make sure your dataset has the necessary columns (`user_id`, `item_id`, `rating`, `timestamp`, and `title`).
- Update the paths in the `main.py` file to point to your new datasets.
  
## For example:
```python
df = pd.read_csv('path_to_your_user_data.csv', sep='\t', names=column_names)
movie_titles = pd.read_csv('path_to_your_movie_titles.csv') 
```

## File Structure
The following files are necessary to run the application:

- main.py: The main script that runs the Streamlit app.
- users.data: A dataset of user ratings for various movies.
- movie_id_titles.csv: A dataset of movie titles corresponding to the movie IDs.

## Installation
First, install Streamlit by running the following command in your terminal:

```bash
pip install streamlit
```

## Running the Application
To run the app, use the following command in your terminal:

```bash
streamlit run main.py
```
Once the app is running, it will automatically open in your web browser.


## Closing the Application
To stop the application, press Ctrl + C in the terminal where it's running.

## Example Datasets
You can experiment with different datasets by changing the files used in main.py. Just make sure the data format is consistent with the expected columns.
Enjoy your movie recommendations!
