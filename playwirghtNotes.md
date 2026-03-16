 
Playwright Assertions & POM Best Practices
Key Differences vs Selenium (Java)
 
1. Assertions: The Fundamental Shift
Selenium (Java)
•	Assertions are:
o	Immediate
o	Passive
o	Non-waiting
•	Responsibility:
o	Always in the test
•	Page Objects:
o	Expose data or state
o	Never assert
This led to rules like:
“No assertions in Page Objects.”
 
Playwright
•	Assertions (expect) are:
o	Auto-waiting
o	Retrying
o	Event-driven
•	They behave more like synchronization guarantees than classic assertions.
Key consequence:
Assertions can safely be used to validate UI state readiness.
 
2. Tests vs Page Objects — What Actually Changed
What Did NOT Change
•	Business rules belong in tests
•	Data correctness belongs in tests
•	Test intent should remain explicit
What DID Change
•	UI state validation (visibility, presence, text) can live closer to the UI
•	Playwright assertions reduce flakiness when colocated with locators
 
3. Two Valid Assertion Patterns in Playwright
Pattern A — Tests Own Assertions (Java-aligned, conservative)
Page Object
def get_order_name_cell_by_id(self, order_id):
    return self.page.locator("tr", has_text=order_id).locator("td:nth-child(2)")
Test
expect(
    my_orders_page.get_order_name_cell_by_id(order_id)
).to_have_text(expected_product_name)
Characteristics
•	Clear separation of concerns
•	Familiar to Java/Selenium engineers
•	Fully Playwright-compliant
 
Pattern B — Page Objects Enforce UI Invariants (Playwright-idiomatic)
Page Object
def ensure_order_is_visible(self, order_id):
    expect(self.page.locator("tr", has_text=order_id)).to_be_visible()
Test
my_orders_page.ensure_order_is_visible(order_id)
Characteristics
•	Assertions represent UI readiness, not business logic
•	Strong synchronization
•	Less boilerplate
•	Better diagnostics
 

4. The Real Rule (This Resolves the Debate)
The problem is not where assertions live,
but what they assert.
❌ Not OK in Page Objects
•	Business rules
•	Calculations
•	Cross-page logic
✅ Acceptable in Page Objects
•	Visibility
•	Presence
•	Text existence
•	Count of elements
These are UI invariants, not test logic.
 
5. Locator Assertions vs Python assert
Python assert
•	No waiting
•	No retry
•	High flakiness risk
Playwright expect
•	Auto-wait
•	Retry until timeout
•	Event-based
•	Rich diagnostics
Best practice:
Use expect() whenever asserting UI state.
 
6. Page Object Return Values: Locators > Strings
Selenium Habit
String text = element.getText();
assertEquals(text, expected);
Playwright Best Practice
locator = page_object.get_element()
expect(locator).to_have_text(expected)
 
What “Lazy Locators” Mean (Important Concept)
In Playwright, a Locator does not immediately query the DOM.
Instead:
•	It stores how to find an element
•	The DOM lookup happens only when an action or assertion is executed
Example:
locator = page.locator("tr", has_text=order_id)
At this moment:
•	No DOM lookup has happened
•	No failure can occur
Only when you do:
expect(locator).to_have_text("Product A")
Playwright:
1.	Queries the DOM
2.	Retries until the condition is met or timeout occurs
3.	Fails with diagnostics if needed
Why This Matters
•	Locators stay valid across re-renders
•	No stale element references
•	Assertions become stable
•	Tests naturally synchronize with the UI
This is fundamentally different from Selenium’s WebElement, which is eager and fragile.
 



7. Navigation Synchronization (Important Shift)
Selenium
•	Explicit waits after actions
•	Often manual and error-prone
Playwright
with page.expect_navigation():
    page.click(...)
Key idea:
Wait around the action, not after it.
 
8. Final Mindset Shift Summary
Selenium (Java)	Playwright (Python)
Assertions are passive	Assertions are active
Tests must wait	Assertions wait
Page Objects expose data	Page Objects may enforce UI state
WebElements are eager	Locators are lazy
Flakiness handled manually	Flakiness handled by framework
 
Bottom Line
You did not learn “wrong” with Selenium.
Playwright simply provides stronger primitives that:
•	Reduce flakiness
•	Improve readability
•	Simplify synchronization
•	Allow flexible architecture
Your cautious approach is sound.
Your adaptation to Playwright is on the right path.









 
Playwright Team Guidelines
Assertions, Page Objects, and Good Practices (Do / Don’t)
 
1. Assertions
✅ DO
•	Use Playwright expect() for all UI-related assertions
•	Assert UI state, not implementation details
•	Let assertions auto-wait instead of adding sleeps or manual waits
•	Keep test intent explicit and readable
expect(locator).to_have_text("Product A")
❌ DON’T
•	Use assert for UI timing-sensitive checks
•	Add time.sleep() for synchronization
•	Assert on raw strings when a locator can be asserted
assert element.text_content() == "Product A"  # avoid
 
2. Page Objects vs Tests
✅ DO
•	Let tests express intent
•	Let Page Objects encapsulate selectors and interactions
•	Allow Page Objects to enforce UI invariants when appropriate
dashboard_page.ensure_orders_loaded()
❌ DON’T
•	Put business rules or calculations in Page Objects
•	Spread selectors across tests
•	Mix API validation logic into Page Objects
 
3. Assertions Inside Page Objects
✅ DO
•	Use assertions in Page Objects only for UI state readiness
•	Use intent-revealing method names
def ensure_order_is_visible(self, order_id):
    expect(self.page.locator("tr", has_text=order_id)).to_be_visible()
❌ DON’T
•	Assert business logic in Page Objects
•	Hide critical test expectations behind vague method names
def check_order(self):  # unclear
    ...
 
4. Locator Usage
✅ DO
•	Return Locators, not strings or booleans
•	Prefer semantic selectors (get_by_role, get_by_test_id)
•	Rely on Playwright’s lazy locator model
def get_order_name_cell(self, order_id):
    return self.page.locator("tr", has_text=order_id).locator("td:nth-child(2)")
❌ DON’T
•	Return text_content() from Page Objects unless necessary
•	Store locators as static values
•	Mix XPath and CSS without reason
 


5. Lazy Locators (Key Principle)
✅ DO
•	Understand that locators are evaluated only when used
•	Let assertions trigger DOM resolution
•	Trust Playwright to retry until conditions are met
❌ DON’T
•	Assume locator creation queries the DOM
•	Manually wait for elements before asserting
 
6. Navigation & Synchronization
✅ DO
•	Guard navigation-triggering actions
with page.expect_navigation():
    page.click("text=Login")
•	Wait for conditions, not time
❌ DON’T
•	Click and immediately query the next page
•	Use fixed sleeps after navigation
 
7. Test Design
✅ DO
•	Keep tests short and scenario-focused
•	Use parameterization for data-driven tests
•	Let API calls set up state when possible
❌ DON’T
•	Duplicate flows across tests
•	Chain excessive UI actions in a single test
•	Depend on UI-only setup when API setup is available
 
8. Error Handling & Diagnostics
✅ DO
•	Prefer assertions that give rich diagnostics
•	Fail fast when UI invariants are broken
•	Let Playwright generate traces and screenshots
❌ DON’T
•	Swallow failures with conditional logic
•	Log instead of asserting
 
9. Selenium → Playwright Mindset Shift
✅ DO
•	Think in terms of events and conditions
•	Trust Playwright’s auto-waiting
•	Use framework primitives instead of manual control
❌ DON’T
•	Recreate Selenium wait patterns
•	Treat Playwright like “Selenium with a new API”
 
10. Guiding Principles (Memorize These)
•	Tests describe what should happen
•	Page Objects handle how it happens
•	Assertions synchronize the test with the UI
•	Locators are lazy; assertions make them real
•	Flakiness is a design smell, not a timing issue
 
Final Rule of Thumb
If you feel the need to add a sleep,
you are missing a Playwright assertion.
 
If you want, next we can:
•	Turn this into a one-page Confluence doc
•	Add code examples per rule
•	Review your current tests against this checklist
•	Create a PR review checklist for the team
Just tell me how you want to continue.



PLAYWRIGHT SUMMARY
This is a very common and very specific IDE vs. runtime mismatch, and at this point in your framework maturity it is expected. Let’s resolve it cleanly and permanently.
I will assume:
•	Tests run successfully with pytest
•	Only the IDE (PyCharm / VS Code) is complaining
That distinction matters.
 
Why the IDE Is Complaining (Root Cause)
Your imports are correct at runtime:
from framework.page_objects.LoginPage import LoginPage
pytest knows how to resolve them because:
•	You run pytest from the project root
•	framework/ is on sys.path
However, IDEs do static analysis, not runtime resolution.
They do not automatically assume your project root is a Python source root.
So the IDE does not know that framework/ is a package root.
 
✅ Correct Fix (IDE-Aware, Production-Grade)
Option 1 — Mark framework as a Sources Root (Best)
PyCharm
1.	Right-click on framework/
2.	Mark Directory As → Sources Root
3.	Restart indexing (automatic)
VS Code
Add this to .vscode/settings.json:
{
  "python.analysis.extraPaths": ["./framework"]
}
This tells the language server:
“Treat framework as importable root”
 
✅ Required Files (Double-Check)
Ensure these exist:
framework/
├── __init__.py
├── page_objects/
│   ├── __init__.py
│   └── LoginPage.py
├── utils/
│   ├── __init__.py
│   └── APIUtils.py
Without __init__.py, IDEs will complain even if pytest runs.
 
Recommended Project Layout (Long-Term)
If this is a framework, not just tests, the most professional layout is:
project_root/
├── framework/
│   ├── __init__.py
│   ├── page_objects/
│   ├── utils/
│   └── data/
├── tests/
│   └── test_e2e_web_api.py
├── conftest.py
├── pytest.ini
Then imports are always:
from framework.page_objects.LoginPage import LoginPage
And both pytest and IDEs agree.
 
❌ What You Should NOT Do
❌ Ignore IDE warnings
They usually indicate real configuration issues.
❌ Modify sys.path
import sys
sys.path.append("framework")
This is fragile and unprofessional.
❌ Switch to relative imports in tests
from ..page_objects.LoginPage import LoginPage
pytest does not reliably support this.
 
Sanity Check (Very Important)
From project root, run:
python -c "from framework.page_objects.LoginPage import LoginPage"
If this works:
•	Your runtime is correct
•	Any remaining issue is IDE configuration only
 
Bottom Line
•	Your imports are correct
•	pytest is behaving correctly
•	The IDE needs to be told what the source root is
•	Marking framework/ as a source root is the correct fix
•	This is normal when moving from Java to Python
 
If you tell me:
•	Which IDE you use
•	How you run pytest (terminal / IDE runner)
I can give you exact, step-by-step configuration instructions for your setup.


