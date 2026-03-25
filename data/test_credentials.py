"""
Test data for login credentials.

This module contains credential data used across login test scenarios.
Uses dataclass for type safety and clear structure.
"""

from dataclasses import dataclass


@dataclass
class LoginCredential:
    """
    Represents a login credential test case.
    
    Attributes:
        scenario: Human-readable description of the test scenario
        username: Username to use in the test
        password: Password to use in the test
        test_id: Unique test case identifier
        priority: Test priority level (default: "High")
    """
    scenario: str
    username: str
    password: str
    test_id: str
    priority: str = "High"


# Invalid credentials test data for negative scenarios
INVALID_CREDENTIALS = [
    LoginCredential(
        scenario="Invalid username with valid password",
        username="WrongUser",
        password="admin123",
        test_id="TC-LOGIN-003-1"
    ),
    LoginCredential(
        scenario="Valid username with invalid password",
        username="Admin",
        password="wrongpassword",
        test_id="TC-LOGIN-003-2"
    ),
    LoginCredential(
        scenario="Both username and password invalid",
        username="InvalidUser",
        password="wrongpass123",
        test_id="TC-LOGIN-003-3"
    ),
]

# Valid credentials for positive scenarios
VALID_ADMIN_CREDENTIALS = LoginCredential(
    scenario="Valid admin login",
    username="Admin",
    password="admin123",
    test_id="TC-LOGIN-001"
)
