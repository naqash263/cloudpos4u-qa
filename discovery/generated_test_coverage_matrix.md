

# CloudPOS4U GenAI QA Coverage Matrix & Automation Backlog

## 1. Executive QA Coverage Summary

| Metric | Status | Details |
| :--- | :--- | :--- |
| **Overall Coverage** | **~65%** | Critical revenue workflows (Login, POS Order) are automated. High-risk API endpoints (Orders, Payments) have partial coverage. GenAI features are largely untested. |
| **UI Automation** | **Low-Medium** | Core pages (Login, Dashboard, Menu) covered. Complex flows (Delivery, Dine-in, Split Payment) pending. |
| **API Automation** | **Medium** | GET endpoints validated for schema. POST/PUT critical paths (Order Creation, Update) partially automated. Negative testing exists but needs expansion. |
| **Performance** | **Low** | Only Login and Menu Load tested via JMeter. Order creation under load is a known gap. |
| **Security** | **Critical Gap** | Auth endpoints validated for success/fail. RBAC, Token Expiry, and Injection vulnerabilities not yet automated. |
| **GenAI Coverage** | **Zero** | AI Assistant, Insights, and Training routes exist but have no test cases defined. |

**Key Insight:** The system relies heavily on manual verification for complex order states (Delivery vs. Dine-in) and inventory logic. Automation should shift focus from "Page Load" to "Business Logic Validation" (e.g., Stock deduction after order).

---

## 2. Module-wise Risk Analysis

| Module | Risk Level | Criticality | Reasoning |
| :--- | :--- | :--- | :--- |
| **Orders** | 🔴 **Critical** | High | Direct revenue flow. Errors here cause lost sales or incorrect billing. |
| **Payments** | 🔴 **Critical** | High | Financial integrity. Requires DB validation and gateway integration checks. |
| **Authentication** | 🟠 **High** | Medium | Security risk if tokens leak or unauthorized access occurs. |
| **Inventory** | 🟠 **High** | Medium | Stock discrepancies lead to overselling or negative inventory issues. |
| **GenAI (AI/LLM)** | 🟡 **Medium** | Low-Med | New feature area. Risk of hallucination or incorrect data interpretation. |
| **Menu/Dishes** | 🟢 **Low** | Medium | Mostly read operations. High volume but low business impact if one item fails. |
| **Reports/Analytics** | 🟢 **Low** | Low | Read-only data. Impact is informational, not transactional. |

---

## 3. UI Automation Test Cases (Selenium + Pytest)

| ID | Route | Scenario | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UI-001** | `/login` | Valid Admin Login | Critical | Selenium | Done |
| **UI-002** | `/login` | Invalid Credentials / OTP Flow | Critical | Selenium | Done |
| **UI-003** | `/menu` | Load Menu Items (Cashier View) | Critical | Selenium | Done |
| **UI-004** | `/orders` | View Order List & Search | High | Selenium | Pending |
| **UI-005** | `/orders/:id` | View Order Details & Invoice | High | Selenium | Pending |
| **UI-006** | `/pos/cfd` | Create Dine-in Order (Table Selection) | High | Selenium | Pending |
| **UI-007** | `/pos/kitchen` | Kitchen Display System (KDS) View | Medium | Selenium | Pending |
| **UI-008** | `/delivery-boys` | Assign Delivery Boy to Order | Medium | Selenium | Pending |
| **UI-009** | `/ai-assistant` | GenAI Chat Interface Load & Input | High | Selenium | Pending |
| **UI-010** | `/inventory` | View Stock Levels & Low Stock Alerts | High | Selenium | Pending |
| **UI-011** | `/customer-prospects` | Add/Edit Customer Profile | Medium | Selenium | Pending |

---

## 4. API Automation Test Cases (Pytest + Requests)

| ID | Endpoint | Method | Scenario | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **API-001** | `/api/user/login` | POST | Valid Login (JWT Token) | Critical | Pytest | Done |
| **API-002** | `/api/order/` | POST | Create Order (Cash Paid) | Critical | Pytest | Done |
| **API-003** | `/api/order/:id` | GET | Fetch Order Details | High | Pytest | Pending |
| **API-004** | `/api/order/:id` | PUT | Update Order Status | High | Pytest | Pending |
| **API-005** | `/api/dish/all` | GET | Retrieve All Dishes | High | Pytest | Done |
| **API-006** | `/api/inventory` | GET | Fetch Inventory Levels | High | Pytest | Pending |
| **API-007** | `/api/branch` | GET | Fetch Branch Config | Medium | Pytest | Pending |
| **API-008** | `/api/payment/create-order` | POST | Process Payment Gateway | Critical | Pytest | Pending |
| **API-009** | `/api/deal/evaluate` | POST | GenAI Deal Evaluation | High | Pytest | Pending |
| **API-010** | `/api/ai/config` | GET | AI Model Configuration | Medium | Pytest | Pending |

---

## 5. Negative and Boundary Test Cases

| ID | Scenario | Expected Result | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NEG-001** | POST `/api/order/` with Empty Items Array | 400 Bad Request / Validation Error | Critical | Pytest | Known Defect |
| **NEG-002** | POST `/api/order/` with Invalid Dish ID | 404 Not Found / 400 Bad Request | High | Pytest | Known Defect |
| **NEG-003** | POST `/api/user/login` with SQL Injection Payload | 400 Bad Request / Sanitized Input | Critical | Pytest | Pending |
| **NEG-004** | PUT `/api/order/:id` without Auth Token | 401 Unauthorized | High | Pytest | Pending |
| **NEG-005** | POST `/api/inventory` with Negative Stock Value | 400 Bad Request (Validation) | High | Pytest | Pending |
| **NEG-006** | GET `/api/order/:id` with Expired JWT Token | 401 Unauthorized | Medium | Pytest | Pending |
| **NEG-007** | POST `/api/deal/evaluate` with Malformed JSON | 400 Bad Request | High | Pytest | Pending |

---

## 6. Security/Authorization Test Cases

| ID | Scenario | Endpoint | Expected Result | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SEC-001** | Access `/api/order` without Auth Header | 401 Unauthorized | Critical | Pytest | Pending |
| **SEC-002** | Admin User accessing Cashier Endpoint (RBAC) | 403 Forbidden | High | Pytest | Pending |
| **SEC-003** | Token Expiry Check (JWT Expired) | 401 Unauthorized | Medium | Pytest | Pending |
| **SEC-004** | XSS Payload in `/ai-assistant` Input Field | Escaped / Sanitized | High | Selenium | Pending |
| **SEC-005** | Rate Limiting on `/api/user/login` (Brute Force) | 429 Too Many Requests | Medium | JMeter | Pending |

---

## 7. Performance Testing Candidates (JMeter)

| ID | Endpoint/Route | Scenario | Target TPS | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PERF-001** | `/api/order/` (POST) | Create 50 Orders Concurrently | 50 TPS | Critical | JMeter | Pending |
| **PERF-002** | `/api/dish/all` (GET) | Load Menu for 100 Users | 100 TPS | High | JMeter | Done |
| **PERF-003** | `/login` (POST) | Login Burst Test | 50 TPS | Medium | JMeter | Done |
| **PERF-004** | `/api/payment/create-order` | Payment Gateway Latency Check | < 2s | Critical | JMeter | Pending |

---

## 8. Database Validation Candidates

| ID | Action | DB Query Logic | Priority | Tool | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DB-001** | Order Creation | `SELECT count(*) FROM orders WHERE status='COMPLETED'` matches API response | Critical | Pytest + DB Driver | Pending |
| **DB-002** | Inventory Deduction | `SELECT stock FROM inventory WHERE id=X` decreases by order quantity | High | Pytest + DB Driver | Pending |
| **DB-003** | Payment Transaction | Verify transaction ID exists in payment_gateway table | Critical | Pytest + DB Driver | Pending |
| **DB-004** | User Session | `SELECT session_token FROM auth_sessions` matches JWT payload | Medium | Pytest + DB Driver | Pending |

---

## 9. GenAI-assisted QA Opportunities

| ID | Opportunity | Description | Tool | Priority | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GEN-001** | AI Hallucination Check | Verify `/api/deal/evaluate` returns factual data, not made-up info | Pytest + LLM Validator | High | Pending |
| **GEN-002** | Receipt Analysis Validation | Upload receipt to `/api/analyze-receipt`, verify extracted fields match DB | Selenium + OCR | Medium | Pending |
| **GEN-003** | AI Assistant Response Time | Measure latency of `/ai-assistant` endpoint under load | JMeter | Medium | Pending |
| **GEN-004** | Prompt Injection Security | Test `/ai-assistant` with malicious prompts to ensure safety filters work | Selenium + Pytest | High | Pending |

---

## 10. Prioritized Automation Backlog

| ID | Area | Scenario | Tool | Priority | Status | Effort (Hrs) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B-001** | API | Order Creation with DB Validation | Pytest | Critical | Pending | 4 |
| **B-002** | UI | Dine-in Table Selection Flow | Selenium | Critical | Pending | 6 |
| **B-003** | API | Payment Gateway Integration (Split Pay) | Pytest | High | Pending | 5 |
| **B-004** | API | Inventory Stock Deduction Logic | Pytest + DB | High | Pending | 4 |
| **B-005** | UI | AI Assistant Chat Interface | Selenium | High | Pending | 3 |
| **B-006** | Perf | Order Creation Load Test (JMeter) | JMeter | High | Pending | 2 |
| **B-007** | API | Deal Evaluation (GenAI) Response Accuracy | Pytest + LLM | Medium | Pending | 3 |
| **B-008** | UI | Customer Prospect Management | Selenium | Medium | Pending | 4 |
| **B-009** | API | Branch Configuration Updates | Pytest | Medium | Pending | 2 |
| **B-010** | Security | RBAC Role Access Control | Pytest | High | Pending | 3 |

---

## 11. Suggested Next 10 Tests to Automate

Based on risk and effort, these should be implemented immediately:

1.  **API:** `POST /api/order/` with DB validation (Stock deduction check).
2.  **UI:** `/pos/cfd` Dine-in order creation flow (Table selection -> Checkout).
3.  **API:** `POST /api/payment/create-order` Split payment logic.
4.  **Security:** `GET /api/order/:id` without Auth Header (401 check).
5.  **Perf:** `/api/dish/all` GET under load (JMeter).
6.  **GenAI:** `/api/deal/evaluate` Response Schema Validation.
7.  **UI:** `/ai-assistant` Page Load & Input Field Interaction.
8.  **API:** `PUT /api/order/:id/edit` Status Update Logic.
9.  **DB:** Verify Order Status in DB matches API Response after creation.
10. **Negative:** `POST /api/order/` with Empty Items Array (Validation Error).

---

## 12. Known Defects and Validation Gaps

| ID | Defect/Gap | Description | Severity | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **DEF-001** | Order Creation Empty Items | API returns success but DB shows no items added. | Critical | Dev Team |
| **DEF-002** | Invalid Dish ID Handling | API returns 500 instead of 400 for invalid dish ID. | High | Dev Team |
| **GAP-001** | Inventory Deduction Logic | No automated check to verify stock decreases after order. | High | QA Lead |
| **GAP-002** | GenAI Hallucination | No validation layer for AI-generated deal evaluations. | Medium | QA Lead |
| **GAP-003** | Split Payment UI | UI flow for split payment (Card + Cash) not automated. | High | QA Lead |

---

## 13. Regression Suite Grouping

| Suite Name | Test Count | Execution Time | Trigger | Content |
| :--- | :--- | :--- | :--- | :--- |
| **Smoke** | ~20 | < 5 mins | Every Commit | Login, Dashboard, POS Cash Order, API Health. |
| **Core Business** | ~50 | ~15 mins | Nightly Build | All Orders, Payments, Inventory, Auth, Menu Load. |
| **Full Regression** | ~120 | ~45 mins | Pre-Release | Core + Perf + Security + GenAI Basic Checks. |

---

## 14. Smoke Suite Grouping (CI/CD Ready)

| Test ID | Description | Tool | Priority |
| :--- | :--- | :--- | :--- |
| **S-001** | `POST /api/user/login` (Valid) | Pytest | Critical |
| **S-002** | `GET /api/dish/all` (Schema Check) | Pytest | Critical |
| **S-003** | `POST /api/order/` (Cash Paid) | Pytest | Critical |
| **S-004** | `/login` Page Load & Redirect | Selenium | Critical |
| **S-005** | `/dashboard` Page Load | Selenium | High |
| **S-006** | `GET /api/branch` (Config Check) | Pytest | High |

---

## 15. CI/CD Execution Recommendation

| Pipeline Stage | Action | Tool | Trigger |
| :--- | :--- | :--- | :--- |
| **Build** | Run Unit Tests + Lint | GitHub Actions | On Push |
| **Smoke** | Run Smoke Suite (API + UI) | Jenkins / GH Actions | On PR Merge |
| **Nightly** | Run Core Business + Perf (JMeter) | Jenkins | Cron (Daily 2 AM) |
| **Pre-Release** | Run Full Regression + Security Scan | Jenkins | Tagged Release |
| **Post-Deploy** | Run Smoke Suite on Staging | GitHub Actions | On Deploy to Prod |

**Recommendation:** Integrate Allure reports into the Jenkins post-build step for visual defect tracking. Use Pytest markers (`@pytest.mark.smoke`, `@pytest.mark.performance`) to allow selective execution in CI/CD pipelines.