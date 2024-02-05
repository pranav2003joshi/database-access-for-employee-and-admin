from flask import Flask, render_template, request, jsonify
import pandas as pd

class SecureDataFrame:
    def __init__(self, data=None, access_key=None):
        self._df = pd.DataFrame(data) if data is not None else pd.DataFrame()
        self._access_key = access_key

    def _check_access(self, provided_key):
        return provided_key == self._access_key

    def read_dataframe(self, access_key):
        if self._check_access(access_key):
            return self._df.copy()
        else:
            raise PermissionError("Invalid access key")

    def modify_dataframe(self, access_key, modifications):
        if self._check_access(access_key):
            for index, modification in modifications.items():
                self._df.at[index, 'Value'] = modification
        else:
            raise PermissionError("Invalid access key")

    def delete_row(self, access_key, index):
        if self._check_access(access_key):
            self._df.drop(index, inplace=True)
        else:
            raise PermissionError("Invalid access key")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read_dataframe', methods=['POST'])
def read_dataframe():
    try:
        provided_key = request.form['access_key']
        result = secure_df.read_dataframe(provided_key)
        return jsonify({'success': True, 'data': result.to_dict(orient='records')})
    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/modify_dataframe', methods=['POST'])
def modify_dataframe():
    try:
        provided_key = request.form['access_key']
        modifications = {
            int(request.form['index']): request.form['value']
        }
        secure_df.modify_dataframe(provided_key, modifications)
        result = secure_df.read_dataframe(provided_key)
        return jsonify({'success': True, 'data': result.to_dict(orient='records')})
    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_row', methods=['POST'])
def delete_row():
    try:
        provided_key = request.form['access_key']
        index = int(request.form['index'])
        secure_df.delete_row(provided_key, index)
        result = secure_df.read_dataframe(provided_key)
        return jsonify({'success': True, 'data': result.to_dict(orient='records')})
    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Example data and access key
    data = {'Index': [1, 2, 3], 'Geometry': ['A', 'B', 'C']}
    access_key = "secure_access_key"

    # Initialize SecureDataFrame
    secure_df = SecureDataFrame(data, access_key)

    app.run(debug=True)
