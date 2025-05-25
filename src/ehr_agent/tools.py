"""
Browser automation tools for EHR Agent using Playwright.
"""

from typing import Any
from playwright.sync_api import sync_playwright
from claude_code_sdk import tool


@tool(schema={"url":"string"})
def navigate(url: str = "https://www.google.com") -> str:
    """
    Navigate to a URL using Playwright and return the page title.
    
    Args:
        url: The URL to navigate to
        
    Returns:
        The title of the page
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(url)
            title = page.title()
            return title
        finally:
            browser.close()