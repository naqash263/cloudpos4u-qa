# GenAI QA Test Case Generation Prompt

You are a Senior QA Engineer.

Generate test cases for the following feature:

Feature:
{{FEATURE_DESCRIPTION}}

Application Context:
CloudPOS4U is a restaurant POS platform with:
- Admin login
- Dashboard
- POS menu
- Dish selection
- Cart
- Order creation
- Payment method
- Payment status
- Invoice popup
- API backend
- PostgreSQL database

Generate:
1. Positive test cases
2. Negative test cases
3. Boundary test cases
4. API test cases
5. UI automation candidates
6. Performance test ideas
7. Security/authorization test cases

For each test case, include:
- test_id
- category
- scenario
- preconditions
- steps
- test_data
- expected_result
- automation_priority: High / Medium / Low
- automation_layer: UI / API / DB / Performance / Security

Rules:
- Return valid JSON only.
- Do not include markdown.
- Do not invent unsupported system features.
- Keep test cases practical for Selenium, Pytest, Postman, JMeter, and Jenkins.