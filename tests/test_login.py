"""
Login functionality tests for HR Orange Application.

This module contains test cases for verifying login functionality including
successful authentication and error scenarios.
"""

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    """
    Test successful login with valid credentials.
    
    This test verifies that a user can successfully log in with valid credentials
    and is redirected to the dashboard page.
    
    Steps:
        1. Navigate to the login page
        2. Enter valid username and password
        3. Click login button
        4. Verify user lands on the dashboard page
    
    Args:
        page (Page): Playwright page fixture from conftest.py
    """
    # Given: User is on the login page
    login_page = LoginPage(page)
    login_page.navigate()
    
    # When: User logs in with valid credentials
    dashboard_page = login_page.login(
        username="Admin",
        password="admin123"
    )
    
    # Then: User should land on the dashboard page
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    # And: Dashboard heading should be visible
    expect(dashboard_page.get_dashboard_heading()).to_be_visible()
