## Flask Application Design for Inch to CM Calculator

### HTML Files

**index.html:** This will be the main page of the application where users can input the inch value and submit it for conversion.
- **Content**:
  - Heading: Inch to CM Converter
  - Form with a single input field for inches
  - Submit button

**results.html:** This page will display the converted value in centimeters.
- **Content**:
  - Heading: Result
  - Paragraph to display the converted value (e.g., "1 inch is equal to 2.54 centimeters")

### Routes

**@app.route('/')**
- **Method**: GET
- **Purpose**: Renders the index.html file, displaying the input form for inches.

**@app.route('/calculate', methods=["POST"])**
- **Method**: POST
- **Purpose**: Handles the form submission.
  - Extracts the inch value from the request.
  - Converts the inch value to centimeters (1 inch = 2.54 centimeters).
  - Redirects to the results.html file, passing the converted value as a parameter.

**@app.route('/results')**
- **Method**: GET
- **Purpose**: Renders the results.html file with the converted value passed from the calculate route.