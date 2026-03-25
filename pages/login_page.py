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
        return self.page.locator(selector = "div[class*='forgot'] p")
    
    @property
    def error_message(self):
        """
        Get the error message banner locator.
        
        The error banner appears after failed login attempts with invalid credentials.
        It's a div with class containing 'alert' and displays "Invalid credentials".
        
        Returns:
            Locator: Playwright locator for the error message banner
        """
        return self.page.locator("div[class*='alert'] p")
    
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
    
    def ensure_invalid_login_error_displayed(self):
        """
        Ensure invalid login error is displayed and fields are cleared.
        
        This method verifies the complete error state after a failed login attempt:
        - Error message "Invalid credentials" is visible
        - User remains on login page (URL hasn't changed)
        - Both username and password fields are cleared
        
        Use this after calling login_with_invalid_credentials() to verify
        the expected error handling behavior.
        
        This is a UI invariant check - it enforces that the page is in the
        correct error state, not business logic.
        """
        # Assert: Error message is displayed
        expect(self.error_message).to_contain_text("Invalid credentials")
        
        # Assert: User remains on login page (URL doesn't change to dashboard)
        expect(self.page).to_have_url(re.compile(r".*/auth/login$"))
        
        # Assert: Username field is cleared (empty value)
        expect(self.page.get_by_role("textbox", name="Username")).to_have_value("")
        
        # Assert: Password field is cleared (empty value)
        expect(self.page.get_by_role("textbox", name="Password")).to_have_value("")
