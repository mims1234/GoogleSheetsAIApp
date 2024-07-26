# Google Sheets AI App - FREE SETUP

Check out my Blog to understand the code : [Supercharge Your Google Sheets with AI for FREE: A Step-by-Step Guide](https://genxclub.hashnode.dev/supercharge-your-google-sheets-with-ai-for-free-a-step-by-step-guide)

## CODE SETUP

1. Open your Google Sheet: Start by opening the Google Sheet where you want to add AI capabilities.
 ![image](https://github.com/user-attachments/assets/16a0115a-fd11-45fd-984c-d486f8408992)

3. Access the Apps Script editor:
  - Click on "Extensions" in the top menu
  - Select "Apps Script" from the dropdown

3. Set up your API key:
  - Click on "Project settings" in the left-hand menu of the Apps Script editor
  - Scroll down to the "Script properties" section
  - Get GROQ_API_KEY [click here](https://genxclub.hashnode.dev/how-to-obtain-your-groq-api-key-a-step-by-step-guide)
  - Add a new property with the following details:

    Property name: `GROQ_API_KEY`
    Value: `[Your Groq API key]`

  - Click "Save" to store your API key securely

4. Setting up the code 
  - Copy the code from `googleSheetAIScript.py`
  - Replace the code 
  - Save the code

![image](https://github.com/user-attachments/assets/42f8a6fd-db3f-4e34-880f-caaee5e46b95)


5. All done setup
  - Now you can use it on the Sheets 
 
## DEMO

Here in this screenshot showing three rows labeled CONTENT, PROMPT, and AI - REPLY. The CONTENT cell contains "Lewis Hamilton won his first World Driver Championship in F1". The PROMPT cell asks "Reply only the Year that it occurred". 

![image](https://github.com/user-attachments/assets/4a68eac9-44cb-48ac-a6ba-5de667c3e2fb)

This demo illustrates the simplicity and effectiveness of our AI integration:

Content Input: In cell B1, we've entered a fact about Lewis Hamilton's first World Driver Championship in F1.
AI Prompt: Cell B2 contains a specific instruction for the AI, asking it to reply with only the year of the event.
AI Response: In cell B3, we see the AI's response: "2008". This demonstrates how the AI accurately extracted the requested information from the given content.

![image](https://github.com/user-attachments/assets/66d9a247-ca85-45ab-bd0f-e103d91b9744)

This example showcases how you can use AI to quickly extract specific information from your data, answer questions, or generate insights based on the content in your spreadsheet cells. The possibilities are vast, ranging from data analysis and summarization to content generation and fact-checking.

Thanks for checking out please Star and Share 
