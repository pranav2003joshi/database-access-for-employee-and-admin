# database-access-for-employee-and-admin

1. **SecureDataFrame Class:**
   - This class encapsulates a pandas DataFrame and includes methods to read, modify, and delete rows, with access control using an access key.
   - The DataFrame (`_df`) and the access key (`_access_key`) are initialized in the constructor.
   - The `_check_access` method compares the provided access key with the stored access key and returns `True` if they match.

2. **Flask Web Application (`app`):**
   - Three routes are defined: `/`, `/read_dataframe`, `/modify_dataframe`, and `/delete_row`.
   - The `/` route renders an HTML template (`index.html`).
   - The `/read_dataframe` route handles POST requests to read the DataFrame. It checks the access key, reads the DataFrame, and returns the data in JSON format.
   - The `/modify_dataframe` route handles POST requests to modify the DataFrame. It checks the access key, applies modifications, reads the modified DataFrame, and returns the data in JSON format.
   - The `/delete_row` route handles POST requests to delete a row from the DataFrame. It checks the access key, deletes the specified row, reads the modified DataFrame, and returns the data in JSON format.

3. **Example Usage (`if __name__ == '__main__':`):**
   - An instance of `SecureDataFrame` (`secure_df`) is created with example data and an access key.
   - The Flask application is initialized, and the server is started with `app.run(debug=True)`.

4. **Access Control:**
   - Each route checks the provided access key against the access key stored in the `secure_df` instance.
   - If the access key is valid, the requested operation is performed. If not, a `PermissionError` is raised.

5. **HTML Template (`index.html`):**
   - The `/` route renders an HTML template named `index.html`, which can be customized based on the application's needs.

In summary, this Flask application demonstrates a simple example of providing secure access to a pandas DataFrame through a web interface. It uses access keys to control read, modify, and delete operations on the DataFrame, showcasing a basic form of authentication and authorization.
