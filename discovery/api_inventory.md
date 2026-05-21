# CloudPOS4U API Inventory

This file tracks discovered backend APIs, their purpose, authentication requirements, automation status, and testing priority.

## Current API Coverage

| Method | Endpoint | Module | Auth Required | Required Headers / Cookies | Current Status | Automation Status | Priority |
|---|---|---|---|---|---|---|---|
| POST | /api/user/login | Authentication | No | Content-Type: application/json | Working | Automated in Pytest + Postman + JMeter | Critical |
| GET | /api/dish/all | Menu / Dishes | Yes | Authorization, x-branch-id, x-branch-code | Working | Automated in Pytest + Postman + JMeter | High |
| POST | /api/order/ | Orders | Yes | Authorization, Cookie accessToken, x-branch-id, x-branch-code | Working | Automated in Pytest + Postman + JMeter | Critical |

## Known API Validation Findings

| Endpoint | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| POST /api/order/ | Create order with empty items list | 400 or 422 validation error | 201 Created | Known defect |
| POST /api/order/ | Create order with invalid dish ID | 400, 404, or 422 validation error | 201 Created | Known defect |

## APIs Pending Discovery

| Module | Possible APIs to Discover | Priority |
|---|---|---|
| Orders | GET order list, GET order details, update order, cancel order | High |
| Tables | Get tables, reserve table, update table status | High |
| Customers | Create customer, search customer, update customer | Medium |
| Inventory | Get stock, update stock, stock movement | High |
| Users / Roles | Create user, update role, permission validation | High |
| Reports | Sales reports, order reports, dashboard KPIs | Medium |
| Payments | Cash, card, online, split payment flows | High |
| Gift Cards | Validate gift card, redeem gift card | Medium |
| Loyalty | Points balance, redeem points | Medium |
| Delivery | Assign delivery boy, update delivery status | Medium |