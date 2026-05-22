# CloudPOS4U.com QA Automation Framework
---
- This repository contains a complete QA automation framework for CloudPOS4U, a restaurant POS platform.
- This framework covers UI automation, API automation,GenAI QA testing, performance testing, reporting, logging, and CI/CD execution using Selenium, Pytest, Python Requests, Postman, JMeter, Allure, GitHub Actions, and Jenkins.
---

## 1. Project Overview

CloudPOS4U QA Automation validates critical business workflows across:

- Admin login
- Dashboard access
- POS menu access
- POS order creation
- Unauthorized access handling
- Menu API performance
- Order creation performance
- API authentication
- API order creation
- Negative API validation
- Real AI API endpoints
- GenAI output contract validation
- Prompt regression testing
- JMeter performance testing

This framework is built as a practical senior QA automation portfolio using real product APIs and UI flows.

---

## 2. Technology Stack

| Area | Tools |
|---|---|
| UI Automation | Selenium WebDriver |
| Test Framework | Pytest |
| API Automation | Python Requests |
| API Manual Validation | Postman |
| GenAI QA | Promptfoo, LM Studio, Pytest AI Contract Tests |
| Performance Testing | Apache JMeter |
| Reporting | Pytest HTML, Allure Report, JMeter HTML Report |
| CI/CD | GitHub Actions, Jenkins |
| Browser | Chrome / Chromium |
| Backend/API | Node.js APIs |
| Database | PostgreSQL |
| Version Control | GitHub |

---
### Main tested URLs:

```text
Frontend/Admin URL:
https://bakebite-pos.cloudpos4u.com

Application URL:
https://bakebite-pos.cloudpos4u.com

API Base URL:
https://bakebite-pos.cloudpos4u.com/api
````

---

## 3. Current Test Coverage

### UI Tests

| Area | Coverage |
|---|---|
| Authentication | Valid login and invalid login |
| Dashboard | Dashboard loads after successful login |
| POS Order Flow | Create cash-paid takeaway order |

### API Tests

| Area | Coverage |
|---|---|
| Auth API | Login success and invalid password |
| Dish API | Get available dishes |
| Order API | Create cash-paid order |
| Security | Create order without authentication |
| Negative API | Missing branch ID, invalid token |
| Known Defects | Empty items and invalid dish ID marked with `xfail` |

### GenAI QA Tests

| Area | Coverage |
|---|---|
| Promptfoo | Dataset-driven prompt regression testing |
| LM Studio | Local model evaluation |
| JSON Parser | Extract JSON from clean, markdown, or reasoning text |
| Schema Contract | Validate required LLM output fields |
| Real AI APIs | `/api/ai/ask`, `/api/ai/ask-staff`, forecast, inventory, price intelligence, profit analysis |
| Scope Control | Validate AI does not hallucinate unsupported menu access |

### Performance Tests

| Area | Coverage |
|---|---|
| Login API | JMeter load test |
| Dish API | Authenticated menu/dish API test |
| Order API | Create order transaction performance |

---

## 4. Project Structure

```
cloudpos4u-qa/
├── README.md
├── Jenkinsfile
├── pytest.ini
├── requirements.txt
├── .gitignore
│
├── conftest.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── menu_page.py
│
├── utils/
│   ├── config.py
│   ├── logger.py
│   ├── payload_builder.py
│   ├── db_client.py
│   ├── api_client.py
│   │
│   └── api/
│       ├── base_client.py
│       ├── auth_client.py
│       ├── menu_client.py
│       ├── order_client.py
│       ├── ai_client.py
│       └── cloudpos_api_client.py
│
├── tests/
│   ├── helpers/
│   │   └── api_assertions.py
│   │
│   ├── ui/
│   │   ├── auth/
│   │   │   ├── test_login.py
│   │   │   └── test_invalid_login.py
│   │   ├── dashboard/
│   │   │   └── test_dashboard.py
│   │   └── orders/
│   │       └── test_create_order.py
│   │
│   ├── api/
│   │   ├── conftest.py
│   │   ├── auth/
│   │   │   └── test_login_api.py
│   │   └── orders/
│   │       ├── test_orders_api.py
│   │       └── test_negative_orders_api.py
│   │
│   ├── ai/
│   │   ├── conftest.py
│   │   ├── contract/
│   │   │   ├── test_json_output_parser.py
│   │   │   └── test_ai_order_extraction_contract.py
│   │   ├── live/
│   │   │   └── test_lmstudio_live_order_extraction.py
│   │   └── real_api/
│   │       ├── test_ai_staff_assistant_api.py
│   │       ├── test_ai_analytics_endpoints.py
│   │       └── test_ai_provider_connectivity.py
│   │
│   └── db/
│       └── test_order_db_validation.py
│
├── ai_qa/
│   ├── build_genai_prompt.py
│   ├── cloudpos4u_genai_qa_prompt.md
│   ├── lmstudio_client.py
│   ├── order_extraction_prompt_builder.py
│   ├── run_lmstudio_coverage.py
│   │
│   ├── parsers/
│   │   └── json_output_parser.py
│   │
│   ├── prompts/
│   │   ├── test_case_generation_prompt.md
│   │   ├── test_data_generation_prompt.md
│   │   └── defect_analysis_prompt.md
│   │
│   ├── promptfoo/
│   │   ├── run_promptfoo.sh
│   │   ├── prompts/
│   │   │   └── order_extraction_prompt.txt
│   │   ├── datasets/
│   │   │   └── order_assistant_cases.csv
│   │   ├── configs/
│   │   │   ├── promptfoo-lmstudio.yaml
│   │   │   ├── promptfoo-openai.yaml
│   │   │   └── promptfoo-ollama.yaml
│   │   └── results/
│   │       └── lmstudio_dataset_eval_notes.md
│   │
│   ├── samples/
│   │   ├── generated_test_cases_cash_paid_order.json
│   │   ├── defect_analysis_empty_order.json
│   │   └── llm_outputs/
│   │       └── order_extraction_outputs.json
│   │
│   ├── rag_eval/
│   └── langsmith/
│
├── discovery/
│   ├── discovery_commands.md
│   ├── api_inventory.md
│   ├── frontend_routes.md
│   ├── test_inventory.md
│   ├── workflows.md
│   ├── generated_api_inventory.md
│   ├── generated_frontend_routes.md
│   ├── generated_automation_backlog.md
│   └── generated_test_coverage_matrix.md
│
├── performance/
│   └── cloudpos4u-performance.jmx
│
├── postman/
│   ├── CloudPOS4U_QA_API_Collection.json
│   └── CloudPOS4U_Postman_Environment.json
│
├── jenkins-cloudpos4u/
│   └── Dockerfile
│
└── docs/
    ├── PureCS_QA_Interview_Cheat_Sheet.md
    └── GenAI_QA_Strategy.md
````

---

## 5. Environment Variables

Create a local `.env` file:

```env
BASE_URL=https://bakebite-pos.cloudpos4u.com/auth
API_BASE_URL=https://bakebite-pos.cloudpos4u.com/api

ADMIN_EMAIL=your_admin_email
ADMIN_PASSWORD=your_admin_password

DB_HOST=your_db_host
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

AI_TEST_PROVIDER=
AI_TEST_MODEL=
AI_TEST_API_KEY=

AI_EMBEDDING_API_KEY=
AI_EMBEDDING_MODEL=text-embedding-3-small
```

Important:

```text
Do not commit real credentials, tokens, passwords, or API keys.
```

---

## 6. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

---

## 7. Run Stable Regression Suite

This command runs stable UI, API, and GenAI contract tests.

It excludes:

* `ai_live` tests because they require LM Studio running locally
* `ai_api` tests because they call real project AI APIs and may depend on AI settings/data

```bash
pytest tests/ui tests/api tests/ai -m "not ai_live and not ai_api"
```

Expected result currently:

```text
19 passed, 2 xfailed
```

The `xfailed` tests are known backend validation defects:

* API allows creating order with empty items list
* API allows creating order with invalid dish ID

---

## 8. Run UI Tests

```bash
pytest tests/ui -s
```

---

## 9. Run API Tests

```bash
pytest tests/api -s
```

---

## 10. Run GenAI Contract Tests

These tests validate parser behavior, JSON output schema, intent, order type, menu item extraction, quantity extraction, and unavailable item handling.

```bash
pytest tests/ai -m "not ai_live and not ai_api" -s
```

---

## 11. Run Real Project AI API Tests

These tests call real CloudPOS4U.com AI endpoints.

```bash
pytest tests/ai -m ai_api -s
```

Currently covered endpoints:

```text
POST /api/ai/ask
POST /api/ai/ask-staff
GET  /api/ai/forecast
GET  /api/ai/inventory-predictions
GET  /api/ai/price-intelligence
GET  /api/ai/profit-analysis
```

Provider connectivity tests are skipped unless these values are configured:

```env
AI_TEST_PROVIDER=
AI_TEST_MODEL=
AI_TEST_API_KEY=
AI_EMBEDDING_API_KEY=
```

Recent result:

```text
7 passed, 2 skipped
```

---

## 12. Run Live LM Studio AI Test

Make sure LM Studio server is running:

```text
LM Studio → Developer → Start Server
```

Then run:

```bash
pytest tests/ai -m ai_live -s
```

Live LLM tests are not included in normal CI because they require a local model server.

---

## 13. Promptfoo GenAI Evaluation

Promptfoo is used for prompt/model regression testing.

It validates:

* JSON-only output
* Intent classification
* Order type extraction
* Payment method extraction
* Menu item extraction
* Quantity extraction
* Unavailable item handling
* Hallucination control
* Local model behavior through LM Studio

Run Promptfoo with LM Studio:

```bash
./ai_qa/promptfoo/run_promptfoo.sh lmstudio no-cache
```

Run with OpenAI:

```bash
./ai_qa/promptfoo/run_promptfoo.sh openai no-cache
```

Run with Ollama:

```bash
./ai_qa/promptfoo/run_promptfoo.sh ollama no-cache
```

Current Promptfoo result:

```text
9 passed / 9 total
100% pass rate
```

Promptfoo helped identify and fix a real prompt issue:

```text
Input: Do you have kulfi falooda?

Issue:
Model classified intent as menu_query but did not extract Kulfi Falooda as the queried item.

Fix:
Added explicit menu_query extraction rule.

Result:
All dataset cases passed after prompt update.
```

---

## 14. Generate Pytest HTML Report

```bash
pytest tests/ui tests/api tests/ai -m "not ai_live and not ai_api" \
  --html=reports/report.html \
  --self-contained-html
```

Open:

```text
reports/report.html
```

---

## 15. Generate Allure Report

Run tests with Allure results:

```bash
rm -rf reports/allure-results reports/allure-report

pytest tests/ui tests/api tests/ai -m "not ai_live and not ai_api" \
  --alluredir=reports/allure-results
```

Add environment metadata:

```bash
cat > reports/allure-results/environment.properties <<EOF
Project=CloudPOS4U QA Automation
Environment=Local
Frontend=https://bakebite-pos.cloudpos4u.com
API=https://bakebite-pos.cloudpos4u.com/api
Browser=Chrome/Chromium
Framework=Pytest + Selenium + Requests
Reporting=Allure
CI=GitHub Actions + Jenkins
Database=PostgreSQL
GenAI_QA=Enabled
Promptfoo=Enabled locally
LMStudio=Optional live test
EOF
```

Generate Allure report using Docker:

```bash
docker run --rm \
  -v "$(pwd)":/work \
  -w /work \
  tobix/allure-cli \
  generate reports/allure-results -o reports/allure-report --clean
```

Serve report:

```bash
cd reports/allure-report
python3 -m http.server 8089
```

Open:

```text
http://localhost:8089
```

---

## 16. Run JMeter Performance Test

```bash
jmeter -n \
  -j reports/jmeter.log \
  -t performance/cloudpos4u-performance.jmx \
  -l reports/jmeter-results.jtl \
  -e \
  -o reports/jmeter-report
```

Open:

```text
reports/jmeter-report/index.html
```

---

## 17. Jenkins Pipeline

The repository includes a `Jenkinsfile` for pipeline-as-code.

Jenkins runs:

```text
1. Prepare workspace
2. Create Python virtual environment
3. Install dependencies
4. Run stable UI/API/AI contract tests
5. Generate Pytest HTML report
6. Generate Allure report
7. Run JMeter performance test
8. Archive reports
```

Jenkins stable Pytest command:

```bash
pytest tests/ui tests/api tests/ai -m "not ai_live and not ai_api" \
  --html=reports/report.html \
  --self-contained-html \
  --alluredir=reports/allure-results
```

Archived reports:

```text
reports/report.html
reports/allure-report/
reports/allure-results/
reports/jmeter-report/
reports/jmeter-results.jtl
reports/logs/
```

---

## 18. GitHub Actions

GitHub Actions runs stable UI and API tests using repository secrets.

Required secrets:

```text
BASE_URL
API_BASE_URL
ADMIN_EMAIL
ADMIN_PASSWORD
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD

DB validation tests are tenant-schema aware. The framework uses `DB_SCHEMA` from environment variables and safely queries tenant tables using PostgreSQL identifiers. DB tests require an active SSH tunnel and `RUN_DB_TESTS=true`.
```

AI provider keys should only be added if AI provider connectivity tests are required.

---

## 19. Postman Collection

The repository includes Postman assets:

```text
postman/
  CloudPOS4U_QA_API_Collection.json
  CloudPOS4U_Postman_Environment.json
```

Covered API flows:

* Login success
* Login invalid password
* Get all dishes
* Create cash-paid order
* Create order without authentication
* AI endpoints where applicable

---

## 20. Logging

Logs are generated under:

```text
reports/logs/
```

Logs include:

* UI actions
* API requests
* Response status codes
* AI endpoint calls
* Error responses

---

## 21. Known Defects

The automation suite currently tracks known backend validation defects using `pytest.mark.xfail`.

| Defect            | Current Behavior        | Expected Behavior                  |
| ----------------- | ----------------------- | ---------------------------------- |
| Empty order items | API returns 201 Created | API should return 400 or 422       |
| Invalid dish ID   | API returns 201 Created | API should return 400, 404, or 422 |

These are marked as expected failures so CI remains stable while defect visibility is preserved.

---

## 22. Key QA Concepts Demonstrated

This framework demonstrates:

* Selenium automation
* Page Object Model
* BasePage design pattern
* Explicit waits
* API automation
* Modular API client design
* Pytest fixtures
* Negative API testing
* Known defect tracking with `xfail`
* Postman validation
* JMeter performance testing
* Allure reporting
* Jenkins pipeline-as-code
* GitHub Actions
* GenAI prompt regression testing
* LM Studio local model testing
* Promptfoo dataset evaluation
* LLM output parser validation
* AI response schema validation
* Real AI API testing
* AI scope-control testing
* Hallucination prevention checks

---

## 23. Summary

This framework validates CloudPOS4U across UI, API, performance, and GenAI layers.

The stable CI suite covers deterministic UI/API/AI contract tests.
The real AI API suite validates live CloudPOS4U AI endpoints.
Promptfoo validates prompt and model behavior separately through dataset-driven GenAI regression testing.

This demonstrates practical readiness for senior automation QA and GenAI QA responsibilities.

---


## Author

**Naqash Thaheem**

Automation / QA / AI Systems professional focused on building practical automation frameworks, API workflows, CI/CD pipelines, and performance testing setups for real-world products.

```

