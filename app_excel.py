from flask import Flask, jsonify, send_file
import subprocess
import os
import logging

app = Flask(__name__)
script_process = None  # To store the running process

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Route to download an Excel file
@app.route('/download-excel', methods=['GET'])
def download_excel():
    try:
        excel_path = os.path.join(os.getcwd(), 'attendance.xlsx')  # Make path dynamic
        logging.debug(f"Sending file: {excel_path}")
        return send_file(excel_path, as_attachment=True)
    except Exception as e:
        logging.error(f"Error downloading file: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

# Route to run the Python script in the background (without sending a response)
@app.route('/run-python', methods=['GET'])
def run_python():
    global script_process
    try:
        # Start the Python script in the background
        script_path = os.path.join(os.getcwd(), 'attendify_ofc.py')  # Make path dynamic
        logging.debug(f"Starting script: {script_path}")
        script_process = subprocess.Popen(
            ['python', script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Return a blank response with status 200 (OK) instead of sending any message
        return '', 200
    except Exception as e:
        logging.error(f"Error running script: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

# Route to check if the script is still running
@app.route('/check-script-status', methods=['GET'])
def check_script_status():
    if script_process and script_process.poll() is None:
        # Script is still running
        logging.debug("Script is still running")
        return jsonify({"status": "running"})
    else:
        # Script has finished
        logging.debug("Script has completed")
        return jsonify({"status": "completed"})

if __name__ == '__main__':
    app.run(debug=True)
