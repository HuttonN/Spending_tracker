# Spending Tracker

Spending Tracker is a web application that helps you track your expenses and manage your budget. It allows you to record your transactions, categorize them with tags and merchants, and provides a spending summary with filtering and sorting options. With Spending Tracker, you can gain better control over your finances and make informed decisions about your spending.

## Features

- **Transaction Management:** Add new transactions with details such as tag, merchant, date, and amount. View a list of all transactions with the ability to filter and sort them.
- **Tag Management:** Manage tags to categorize your transactions. Create new tags, edit existing ones, and activate or deactivate them as needed.
- **Merchant Management:** Manage merchants to track where you spend your money. Add new merchants, edit their details, and activate or deactivate them.
- **Budgeting:** Set a budget for your expenses and monitor your spending against the budget.
- **User-Friendly Interface:** The web application has a clean and intuitive interface, making it easy to navigate and use.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- SQL

## Installation

1. Clone the repository: ```git clone https://github.com/justneil11/spending-tracker.git```

2. Install the required dependencies:

3. Set up the database:
- Create a new PostgreSQL database.
- Set the database URL in the `config.py` file.

4. Run the application: ``` flask run ``` while at the ``` Spending_Tracker_Project ``` level

5. Access the application in your web browser at `http://localhost:4999`.

## Usage

- Add transactions by providing the necessary details such as tag, merchant, date, and amount.
- View and manage your transactions, tags, and merchants through the respective sections of the application.
- Use the filtering and sorting options in the spending summary section to analyze your expenses.

## Future features:

In future I hope to implement the following features:

- Addition of an analysis section where a user can view their spending patterns and set a budget
- Integrate Machine Learning to suggest a budget based on spending history
- Add user authentication and registeration functionality
- Add charts and visualisations (probably on the analysis page)
- Allow the user to import and/or export data by CSV or other suitable format
- Allow the user to filter by transaction dates as well

## Future fixes/improvements:

In future I hope to improve the exisitng code by adjusting for the following:

- Make the design responsive for use on different devices
- Analyze and optimise database queries and application performance to ensure efficient handling of a larger volume of transactions and improve response times.
- Implement additional security measures, such as input sanitization, protection against common web vulnerabilities, and secure authentication protocols.
- Review and refactor existing code to improve readability, maintainability, and adherence to coding best practices. Update documentation to provide clear instructions on project setup and usage.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the existing coding style and guidelines.

## Acknowledgements

- The Spending Tracker application was developed as part of a personal project started as a student @CodeClan.
- The project was built using the Flask web framework and various open-source libraries and resources.
