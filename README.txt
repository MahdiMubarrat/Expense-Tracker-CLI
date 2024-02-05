***Expense Tracker CLI***

**Usage Instructions**

Type the number associated with the function to use them

1.Sign Up: Create a new user account 
2.Log In: Access your account 
3.Exit: Exit the application

1.Add: Record a new income or expense. Specify the type (income/expense), amount, and category.
2.Edit: Modify an existing transaction. Choose the transaction by its listed number, and enter the new details.
3.Delete: Remove an existing transaction. Select the transaction by its listed number to delete it.
4.View: Display a list of all recorded transactions.
5.Budget: Define a budget limit for a specific category.
6.Logout: Exit your account.

**Data Storage**
User data is stored locally in JSON files.
Each user's data is stored in a separate file named after their username.
This includes their password, transaction records, and budget settings.

**Security Note**
This application stores passwords in plain text,
which is not secure for real-world applications.
It's advisable to enhance password handling with encryption for any serious use.

**Future Enhancements**
Improve password security.
Implement more advanced budgeting features.
Add data visualization for expenses and income.
Create a Currency Converter.