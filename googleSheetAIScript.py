// **IMPORTANT: SET UP API_KEY AT SCRIPT PROPERTIES BEFORE USING THIS SCRIPT**

// To set up Script Properties:
// 1. Click on "Project settings" in the left-hand menu.
// 2. Scroll down to the "Script properties" section.
// 3. Add a new property with the following settings:
//    - Property name: GROQ_API_KEY
//    - Value: <paste your Groq API key here>
// 4. Click "Save" to save the changes.

/**
 * Retrieves the Groq API key from the script properties.
 * @return {string} The Groq API key.
 */
function getApiKey() {
  var properties = PropertiesService.getScriptProperties();
  var apiKey = properties.getProperty('GROQ_API_KEY');
  return apiKey;
}

/**
 * Replaces cell references in the input prompt with their corresponding values.
 * @param {string} inputPrompt The original prompt.
 * @param {Sheet} activeSheet The active sheet.
 * @param {Range} activeCell The cell that called the function.
 * @return {string} The processed prompt with cell values.
 */
function resolveCellReferences(inputPrompt, activeSheet, activeCell) {
  const cellPattern = /\b[A-Z]+\d+\b/g;
  return inputPrompt.replace(cellPattern, (match) => {
    try {
      // Attempt to retrieve the cell value and convert it to a string
      return activeSheet.getRange(match).getValue().toString();
    } catch (error) {
      // If the cell reference is invalid, return the original match
      return match;
    }
  });
}

/**
 * Custom function to call Groq from a cell.
 * @param {string} userPrompt The input prompt for Groq, can include cell references.
 * @param {number} tokenLimit The maximum number of tokens for the response. Optional, default is 450.
 * @return The generated text from Groq.
 * @customfunction
 */
function GROQ(userPrompt, tokenLimit = 450) {
  const API_KEY = getApiKey(); // Retrieve the Groq API key
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const cell = sheet.getActiveCell();
  
  // Resolve cell references in the user prompt
  userPrompt = resolveCellReferences(userPrompt, sheet, cell);
  
  // Validate the user prompt
  if (!userPrompt) {
    return "Error: Please provide a prompt.";
  }
  
  // Define the API endpoint and request body
  const endpoint = 'https://api.groq.com/openai/v1/chat/completions';
  const requestBody = {
    'model': 'mixtral-8x7b-32768',
    'messages': [
      {'role': 'system', 'content': 'You are a helpful assistant.'},
      {'role': 'user', 'content': userPrompt}
    ],
    'max_tokens': tokenLimit
  };
  
  // Define the API request options
  const requestOptions = {
    'method': 'post',
    'contentType': 'application/json',
    'headers': {
      'Authorization': 'Bearer ' + API_KEY
    },
    'payload': JSON.stringify(requestBody),
    'muteHttpExceptions': true
  };
  
  try {
    // Send the API request and retrieve the response
    const apiResponse = UrlFetchApp.fetch(endpoint, requestOptions);
    const responseCode = apiResponse.getResponseCode();
    const responseText = apiResponse.getContentText();
    
    // Handle API errors
    if (responseCode !== 200) {
      return `Error: API returned status ${responseCode}. ${responseText}`;
    }
    
    // Parse the API response and extract the generated text
    const responseData = JSON.parse(responseText);
    return responseData.choices[0].message.content.trim();
  } catch (error) {
    // Handle any errors that occur during the API request
    return "Error: " + error.toString();
  }
}
