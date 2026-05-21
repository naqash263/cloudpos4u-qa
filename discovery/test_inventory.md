# CloudPOS4U Test Inventory

This file tracks current and planned tests across UI, API, performance, reporting, and CI/CD.

## Existing Automated Tests

| Test Area | Test Name / Scenario | Type | Tool | Status |
|---|---|---|---|---|
| Authentication | Valid admin login | UI | Selenium + Pytest | Done |
| Authentication | Invalid admin login | UI | Selenium + Pytest | Done |
| Dashboard | Dashboard loads after login | UI | Selenium + Pytest | Done |
| POS Orders | Create cash paid order | UI | Selenium + Pytest | Done |
| Authentication | Login API success | API | Python Requests + Pytest | Done |
| Authentication | Login API invalid password | API | Python Requests + Pytest | Done |
| Orders | Create cash paid order API | API | Python Requests + Pytest | Done |
| Orders | Create order without authentication | API Negative | Python Requests + Pytest | Done |
| Menu | Get all dishes | API | Python Requests / Postman / JMeter | Done |
| Orders | Create order with empty items | API Negative | Pytest | Known Defect |
| Orders | Create order with invalid dish ID | API Negative | Pytest | Known Defect |
| Authentication | Login load test | Performance | JMeter | Done |
| Menu | Get dishes load test | Performance | JMeter | Done |
| Orders | Create order load test | Performance | JMeter | Done |
| CI/CD | GitHub Actions execution | Pipeline | GitHub Actions | Done |
| CI/CD | Jenkins pipeline execution | Pipeline | Jenkinsfile | Done |
| Reporting | Pytest HTML report | Report | pytest-html | Done |
| Reporting | Allure report | Report | Allure | Done |
| Reporting | JMeter HTML report | Report | JMeter | Done |

## Planned Tests

| Module | Scenario | Test Type | Priority |
|---|---|---|---|
| Orders | View order list | UI/API | High |
| Orders | View order details | UI/API | High |
| Orders | Cancel order | UI/API | High |
| Tables | Select table and create dine-in order | UI/API | High |
| Delivery | Create delivery order | UI/API | High |
| Customers | Create customer | UI/API | Medium |
| Inventory | Verify stock deduction after order | API/DB | High |
| Users/Roles | Verify permission-based access | UI/API | High |
| Reports | Validate sales totals | UI/API/DB | Medium |
| Payments | Split payment validation | UI/API | Medium |
| Gift Cards | Gift card payment | UI/API | Medium |
| Loyalty | Loyalty points payment | UI/API | Medium |