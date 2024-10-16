# NLP-Based SQL Query Generator Using Gemini Model

This project utilizes an NLP model (Gemini), Google GenAI, and Streamlit to create a web-based interface that allows users to ask natural language questions, which are then converted into SQL queries. The application interacts with an SQLite3 database, fetches the relevant data, and returns it in a user-friendly format.

## Features
- Converts user natural language input into SQL queries using the Gemini model and Google GenAI.
- Executes SQL queries using SQLite3 to retrieve data from a pre-existing database.
- Displays the data in a Streamlit-based web application.
- Simple and intuitive user interface for non-technical users to interact with databases.
  
## Technology Stack
- **Streamlit**: Provides the web interface for user interaction.
- **Gemini Model & Google GenAI**: Powers the natural language processing to generate SQL queries.
- **SQLite3**: Lightweight database management system used for data storage and query execution.

## Requirements

To run this project, you will need the following installed on your local machine:

- Python 3.7+
- Streamlit
- Google Generative AI SDK
- SQLite3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rugvedp/NLP.git
   cd NLP
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

   _Note: The `requirements.txt` file should contain the dependencies for Streamlit, Google GenAI SDK, SQLite3, etc._

3. Set up your SQLite3 database. Place your `.db` file in the project directory or update the path in the code.

4. Configure your Google GenAI credentials to enable NLP-powered query generation. Follow [Google GenAI API documentation](https://cloud.google.com/genai/docs) to set up your API keys.

## How to Run

1. Open a terminal in the project directory.
2. Start the Streamlit app by running the following command:

   ```bash
   streamlit run main.py
   ```

3. In your web browser, navigate to `http://localhost:5000` to interact with the app.

## Usage

1. Once the app is running, input a natural language query into the text box (e.g., "Count of students who have strong Python").
2. The Gemini model processes your input and converts it into an SQL query.
3. The SQL query is executed on the SQLite3 database, and the results are displayed in a table below.

## Example Queries

- "How many entries of records are present? "
- "Tell me all the students studying in Computer Science Major?"

## Project Structure

```plaintext
├── main.py               # Main Streamlit application
├── students.db          # SQLite3 database file
├── requirements.txt     # Required Python libraries
├── README.md            # Project documentation
```

## Future Enhancements

- Add support for more complex queries involving JOINs, subqueries, etc.
- Extend support to multiple databases beyond SQLite3.
- Improve the natural language processing accuracy by fine-tuning the Gemini model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any inquiries or issues, feel free to reach out at rugvedp00@gmail.com.

---

You can modify this README based on specific project details and update the relevant sections for API keys, database setup, and deployment details.
