## Importing libraries and files
# import os
from dotenv import load_dotenv

load_dotenv()
from langchain_community.document_loaders import PyPDFLoader

from crewai.tools import tool  # Import the tool decorator
 #from crewai_tools.tools.serper_dev_tool import SerperDevTool
## Creating search tool
#search_tool = SerperDevTool()

## Creating custom pdf reader tool
@tool
def read_data_tool(path: str = 'data/TSLA-Q2-2025-Update.pdf') -> str:
    """Tool to read data from a pdf file from a path

    Args:
        path (str, optional): Path of the pdf file. Defaults to 'data/TSLA-Q2-2025-Update.pdf'.

    Returns:
        str: Full Financial Document file
    """
    loader = PyPDFLoader(path)
    docs = loader.load()

    full_report = ""
    for doc in docs:
        content = doc.page_content
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")
        full_report += content + "\n"

    return full_report


## Creating Investment Analysis Tool
@tool
def analyze_investment_tool(financial_document_data: str) -> str:
    """Analyze financial document for investment opportunities"""
    # Process and analyze the financial document data
    processed_data = financial_document_data

    # Clean up the data format
    i = 0
    while i < len(processed_data):
        if processed_data[i:i + 2] == "  ":  # Remove double spaces
            processed_data = processed_data[:i] + processed_data[i + 1:]
        else:
            i += 1

    # TODO: Implement investment analysis logic here
    return "Investment analysis functionality to be implemented"


## Creating Risk Assessment Tool
@tool
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """Create risk assessment from financial document"""
    # TODO: Implement risk assessment logic here
    return "Risk assessment functionality to be implemented"