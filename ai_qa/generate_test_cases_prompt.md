# GenAI Prompt: Generate QA Test Coverage from Discovery Files

You are a Senior QA Automation Engineer.

Use the following CloudPOS4U discovery files as source context:

1. discovery/api_inventory.md
2. discovery/frontend_routes.md
3. discovery/workflows.md
4. discovery/test_inventory.md

Your task is to generate a complete QA coverage matrix for the CloudPOS4U POS platform.

For each module, generate:

- Functional UI test cases
- API test cases
- Negative test cases
- Boundary test cases
- Security/authorization test cases
- Performance test scenarios
- Database validation ideas
- Required test data
- Automation priority
- Risk level
- Recommended tool
- Current coverage status
- Suggested next automation task

Output format:

## Module Name

### Business Risk
Explain the business risk if this module fails.

### UI Test Cases

| ID | Scenario | Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|

### API Test Cases

| ID | Method | Endpoint | Scenario | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|

### Negative Test Cases

| ID | Scenario | Expected Result | Priority |
|---|---|---|---|

### Performance Scenarios

| ID | Scenario | Load | Expected KPI |
|---|---|---|---|

### Database Validation

| ID | Validation | Expected Result |
|---|---|---|

### Recommended Next Automation

List the next 3 automation tasks for this module.

Important rules:
- Do not invent endpoints unless clearly marked as "to be discovered".
- Use existing automated tests from test_inventory.md.
- Mark known defects clearly.
- Prioritize revenue-critical workflows first.
- Keep output practical for Selenium, Pytest, Postman, JMeter, and Jenkins.