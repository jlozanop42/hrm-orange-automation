"""
Login functionality tests for HR Orange Application.

This module contains test cases for verifying login functionality including
successful authentication and error scenarios.
"""

import re
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
    expect(page).to_have_url(re.compile(r".*/dashboard"))
    
    # And: Dashboard heading should be visible
    dashboard_page.ensure_page_loaded()

def test_forgot_password_navigation(page: Page):
    """
    Test that clicking 'Forgot your password?' link navigates to password reset page.
    
    Test Case ID: TC-LOGIN-002
    Priority: Medium
    Category: Positive
    
    This test verifies that the 'Forgot your password?' link correctly navigates
    the user to the password reset request page with the expected URL pattern.
    
    Steps:
        1. Navigate to the login page
        2. Locate and verify 'Forgot your password?' link is visible
        3. Click on the 'Forgot your password?' link
        4. Verify navigation to password reset page
    
    Args:
        page (Page): Playwright page fixture from conftest.py
    """
    # Given: User is on the login page
    login_page = LoginPage(page)
    login_page.navigate()
    
    # And: The forgot password link is visible
    expect(login_page.forgot_password_link).to_be_visible()
    
    # When: User clicks the forgot password link
    login_page.click_forgot_password()
    
    # Then: User should be redirected to the password reset request page
    expect(page).to_have_url(re.compile(r".*/auth/requestPasswordResetCode$"))
    
    # And: Verify the expected full URL (for documentation purposes)
    # Expected: https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode