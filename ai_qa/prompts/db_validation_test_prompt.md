# GenAI Prompt: Generate DB Validation Test for CloudPOS4U Order Creation

You are a Senior QA Automation Engineer.

Generate a Pytest database validation test for CloudPOS4U.

Project structure:

- API client: utils/api/cloudpos_api_client.py
- DB client: utils/db_client.py
- Payload builder: utils/payload_builder.py
- Config: utils/config.py
- DB tests folder: tests/db/
- Markers: api, db, regression

Existing API flow:
1. Login using CloudPOSAPIClient
2. Fetch available dishes using get_all_dishes()
3. Build order payload using PayloadBuilder.cash_paid_order()
4. Create order using create_order()
5. Validate API response status 201

Required DB validation:
1. Read orderNumber from API response
2. Query PostgreSQL orders table by order_number
3. Validate:
   - order exists
   - order_number matches API response
   - customer_name matches payload
   - order_type = Takeaway
   - payment_method = Cash
   - payment_status = Paid
   - branch_id matches authenticated branch

Rules:
- Use pytest
- Use allure steps
- Use @pytest.mark.db
- Use @pytest.mark.api
- Use @pytest.mark.regression
- Use CloudPOSAPIClient, not old APIClient
- Keep code clean and aligned with current framework
- Return only Python test code