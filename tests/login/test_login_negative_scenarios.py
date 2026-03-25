"""
Negative test scenarios for login functionality.

This module contains test cases for validating login behavior with invalid
credentials, ensuring proper error handling and security measures.

Test Case Reference: TC-LOGIN-003 (Invalid Credentials)
"""

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from data.test_credentials import INVALID_CREDENTIALS


@pytest.mark.parametrize("credential", INVALID_CREDENTIALS, ids=lambda c: c.scenario)
def test_invalid_credentials(page: Page, credential):
    """
    Test login attempts with various invalid credential combinations.
    
    Test Case ID: TC-LOGIN-003
    Priority: High
    Category: Negative
    
    Verifies that the system properly rejects login attempts with invalid
    credentials and displays appropriate error messages. Parametrized test
    runs multiple scenarios with different credential combinations.
    
    Test Scenarios:
        - Invalid username with valid password
        - Valid username with invalid password
        - Both username and password invalid
    
    Steps:
        1. Navigate to the login page
        2. Enter test credentials (username and password)
        3. Click login button
        4. Verify error message is displayed
        5. Verify user remains on login page
    
    Args:
        page (Page): Playwright page fixture
        credential (LoginCredential): Test data containing username, password,
                                      and scenario description
    """
    # Arrange: User is on the login page
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Act: User attempts login with invalid credentials
    login_page.login_with_invalid_credentials(
        username=credential.username,
        password=credential.password
    )
    
    # Assert: Error state is displayed correctly
    login_page.ensure_invalid_login_error_displayed()
