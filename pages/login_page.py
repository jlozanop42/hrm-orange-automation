"""
Login Page Object Model for HR Orange Application.

This module provides the LoginPage class that encapsulates all interactions
with the login page of the HR Orange application.
"""

import re
from playwright.sync_api import Page, expect
from utils.config import config


class LoginPage:
    """
    Page Object for the Login Page.
    
    The login page is the entry point for users to access the HR Orange system.
    It provides authentication functionality with username and password fields.
    
    Attributes:
        page (Page): Playwright page instance for browser interactions
    """
    
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def forgot_password_link(self):
        """
        Get the 'Forgot your password?' link locator.
        
        Returns:
            Locator: Playwright locator for the forgot password link
        """
        return self.page.get_by_role("link", name="Forgot your password?")
    
    def navigate(self):
        """
        Navigate to the login page.
        
        Uses the BASE_URL from configuration, which can be set via environment
        variable to test different environments (QA, Staging, Production).
        """
        self.page.goto(config.BASE_URL)
    
    def login(self, username: str, password: str):
        """
        Perform login with valid credentials and wait for navigation to dashboard.
        
        This method fills in the username and password fields, clicks the login
        button, and waits for successful navigation to the dashboard page.
        Use this method when you expect login to succeed.
        
        Navigation guard: Uses expect().to_have_url() which auto-waits for
        navigation to complete, retrying until URL matches or timeout.
        
        Args:
            username (str): Valid username for authentication
            password (str): Valid password for authentication
        
        Returns:
            DashboardPage: Page object for the dashboard page after successful login
        """
        # Import here to avoid circular dependency
        from pages.dashboard_page import DashboardPage
        
        # Fill username field - using role="textbox" (most semantic)
        self.page.get_by_role("textbox", name="Username").fill(username)
        
        # Fill password field - using role="textbox" with accessible name
        # Note: Password inputs are exposed as textbox role in accessibility tree
        self.page.get_by_role("textbox", name="Password").fill(password)
        
        # Click login button and wait for navigation to dashboard
        # Note: expect() provides auto-waiting and retries until URL matches
        self.page.get_by_role("button", name="Login").click()
        expect(self.page).to_have_url(re.compile(r".*dashboard"))
        
        # Return dashboard page object for method chaining
        return DashboardPage(self.page)
    
    def login_with_invalid_credentials(self, username: str, password: str):
        """
        Attempt login with invalid credentials that will fail.
        
        This method fills in credentials and clicks login, but does NOT wait
        for navigation since invalid credentials keep you on the login page.
        Use this method when testing error scenarios.
        
        Args:
            username (str): Username (valid or invalid)
            password (str): Password (valid or invalid)
        
        Returns:
            LoginPage: Returns self for method chaining on the login page
        """
        # Fill username field - using role="textbox" (most semantic)
        self.page.get_by_role("textbox", name="Username").fill(username)
        
        # Fill password field - using role="textbox" with accessible name
        self.page.get_by_role("textbox", name="Password").fill(password)
        
        # Click login button
        self.page.get_by_role("button", name="Login").click()
        
        # Return self since we stay on login page for failed login
        return self
    
    def click_forgot_password(self):
        """
        Click the 'Forgot your password?' link to navigate to password reset page.
        
        This method clicks the forgot password link which navigates to the
        password reset request page. Use this to access password recovery flow.
        
        Navigation occurs to: /auth/requestPasswordResetCode
        
        Returns:
            None: Navigation happens but no page object is returned yet
                  (PasswordResetPage can be added when needed)
        """
        # Click the forgot password link using the property
        self.forgot_password_link.click()
