## Automated Test for TruckClub

This test suite, ensures the following:

   1. Launches the business page
         - Asserts the Mission Statement is displayed.

   2. Visits the contact form,
         - Click submit button on Empty form.
         - And ensures failing validation exists.


## How to Run the Test Suite

   1. `cd` into project.
   2. Activate virtual environment `source venv/bin/activate`.
   3. Run the tests with `venv/bin/python3 -m unittest test_script.business_test`.