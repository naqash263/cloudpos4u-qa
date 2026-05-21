# CloudPOS4U GenAI QA Coverage Prompt

You are a Senior QA Automation Engineer and GenAI QA Specialist.

You are given real CloudPOS4U discovery data extracted from:

- Browser HAR network traffic
- Backend route discovery
- Frontend route discovery
- Existing automation inventory
- Business workflow notes

Your task is to generate a complete QA coverage matrix and automation backlog.

## Important Rules

- Do not invent endpoints unless marked as "to be discovered".
- Use the discovered API inventory as source of truth.
- Use existing automation status from the test inventory.
- Identify missing UI/API/performance/security/DB coverage.
- Prioritize revenue-critical and security-sensitive workflows.
- Include GenAI QA opportunities where useful.
- Keep output practical for Selenium, Pytest, Postman, JMeter, Allure, Jenkins, and GitHub Actions.

## Required Output

Generate the following:

1. Executive QA coverage summary
2. Module-wise risk analysis
3. UI automation test cases
4. API automation test cases
5. Negative and boundary test cases
6. Security/authorization test cases
7. Performance testing candidates
8. Database validation candidates
9. GenAI-assisted QA opportunities
10. Prioritized automation backlog
11. Suggested next 10 tests to automate
12. Known defects and validation gaps
13. Regression suite grouping
14. Smoke suite grouping
15. CI/CD execution recommendation

Use clear tables wherever possible.



---

# Source File: generated_api_inventory.md


# Generated CloudPOS4U API Inventory

This file was generated from HAR and backend route discovery output.

| Method | Endpoint | Module | Last Seen Status | Priority | Source | Suggested Automation |
|---|---|---|---|---|---|---|
| GET | /api/aggregator/config/038f901a-732e-4f4f-a05f-008d789f58f1 | To classify | 200 | Medium | HAR | API test + schema validation |
| GET | /api/ai/config | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/branch | Branches | 200 | Medium | HAR | API test + schema validation |
| GET | /api/branch/038f901a-732e-4f4f-a05f-008d789f58f1 | Branches | 304 | Medium | HAR | API test + schema validation |
| GET | /api/category | Menu / Dishes | 304 | Medium | HAR | API test + schema validation |
| GET | /api/customer-prospect | Customers | 304 | Medium | HAR | API test + schema validation |
| GET | /api/customer-prospect/statistics | Customers | 304 | Medium | HAR | API test + schema validation |
| GET | /api/deal | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/delivery-boy | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/delivery-boy/available | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/department | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/dish | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/00000000-0000-0000-0000-000000000000 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/179b313e-5c67-491f-8e93-b3ee56cbe543 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/206c608f-2398-437f-8647-d1eb00255b20 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/2581da77-cbd8-4924-9a78-ce0a69615f14 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/28754367-18c5-401c-ab7b-6e5f79e36bc3 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/2cd327f3-cc50-4343-a3fb-4c24e7d897b1 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/2d1dad30-115a-40f4-ab25-496bac5f1da0 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/39a1249f-3e76-47c2-a79d-08d3de982661 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/3f4d2d31-9a1e-4d00-94c6-904ec6dff064 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/446adcd9-d3e1-4a41-b2ac-2812e2c6d90e | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/48a4a2bb-db6f-4414-9b23-6802378d9b6b | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/4e527416-dd4d-42c6-98ff-384f38d682b9 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/5087fb70-3c1e-4215-8472-8eaab01a73d6 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/547780a2-4a9f-44f0-a879-d0725a17a541 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/597f00de-62a9-44b4-9540-b15e34f8b3ca | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/5d6f9114-1b6e-4d44-89c5-8832359ffc92 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/5f392a68-6d3b-4c64-9c83-49d50d7bf478 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/61fa7c5b-a024-4647-a3e6-ce1be484cbf4 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/629f916e-f5b9-4ffc-b70d-ce054cfbfb40 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/65311a8d-3eff-4913-b699-5977d55a39a9 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/69084ed7-38a8-4059-8711-d4dcd597c3d9 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/6926d004-c78c-4462-b26e-ebdf62dd16ca | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/7b913575-092e-4a97-a064-afd064875dc0 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/95a00b06-929d-444e-8782-3a3ff994b3df | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/99799115-6e84-40c3-879c-bdcdaf8a6f4d | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/9ad65cfc-447b-4b30-8191-77f37a21abc0 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/9f9a5ce9-350b-45fa-955e-23a6d40c8dee | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/a0a8ef5f-7abc-443e-a918-71606e7fe5bc | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/a7ea57d0-31ea-449a-9a7a-e40258f3ea23 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/b0985823-715d-4343-95a1-17edaa34b7b4 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/b16ca2e1-1129-4efd-9692-4067f9de0551 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/b182b1d8-6c9f-43af-8288-3720c4cf0e9e | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/bebd9969-b04b-45cf-bddb-c2b6602e80a9 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/c137e6b1-bda4-46eb-9370-aee227ea9b49 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/c2aa3c34-be47-40a0-b873-bda8a25c7d4e | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/c4d952d6-fc67-47e3-869d-cb0f51c7fdfe | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/d439eb1f-f6ae-4c14-8905-2f67dd327f25 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/dda70e47-fb38-4097-90cf-1ef4c97f20f6 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/e70a62d7-253a-4668-8b33-be896641c2c9 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/e85b533a-e037-4498-a6ae-5be62b79b98d | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/eb1356a3-bf8e-47b2-bc11-bcbde5086e28 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/ecd7252a-9b2c-414b-808a-6daa3f89c2f7 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/ee963fb6-04e3-49b1-a829-4b1ae9e82b5a | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/f9ec938b-6a39-474e-b258-8cf26f452f61 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish-spice/dish/fbfb8e4a-da7c-411e-856a-4df1eac443b2 | Menu / Dishes | 304 | High | HAR | API test + schema validation |
| GET | /api/dish/all | Menu / Dishes | 200 | High | HAR | API test + schema validation |
| GET | /api/inventory | Inventory | 200 | High | HAR | API test + schema validation |
| GET | /api/inventory/transactions | Inventory | 304 | High | HAR | API test + schema validation |
| GET | /api/order | Orders | 304 | Critical | HAR | API test + DB validation + performance test |
| GET | /api/payment-gateway/config/038f901a-732e-4f4f-a05f-008d789f58f1 | Payments | 200 | Medium | HAR | API test + schema validation |
| GET | /api/payroll/attendance/admin | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/payroll/entry | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/payroll/my/attendance | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/payroll/settings | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/position | To classify | 200 | Medium | HAR | API test + schema validation |
| GET | /api/settings | To classify | 200 | Medium | HAR | API test + schema validation |
| GET | /api/settings/firebase-config | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/shift/current | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/table | Tables | 304 | High | HAR | API test + schema validation |
| GET | /api/user | Authentication / Users | 401 | Medium | HAR | API test + schema validation |
| GET | /api/user/all | Authentication / Users | 200 | Medium | HAR | API test + schema validation |
| GET | /api/user/setup-status | Authentication / Users | 304 | Medium | HAR | API test + schema validation |
| GET | /api/vendor | To classify | 304 | Medium | HAR | API test + schema validation |
| GET | /api/whatsapp/dashboard | Reports / Dashboard | 304 | Medium | HAR | API test + schema validation |
| GET | /api/whatsapp/logs | To classify | 200 | Medium | HAR | API test + schema validation |
| GET | /api/whatsapp/status | To classify | 304 | Medium | HAR | API test + schema validation |
| POST | /api/deal/evaluate | To classify | 200 | High | HAR | API test + negative test |
| POST | /api/inventory | Inventory | 201 | High | HAR | API test + negative test |
| POST | /api/order/ | Orders | 201 | Critical | HAR | API test + DB validation + performance test |
| POST | /api/payment/create-order | Orders | 500 | Critical | HAR | API test + DB validation + performance test |
| POST | /api/user/login | Authentication / Users | 200 | Critical | HAR | API test + negative test |
| POST | /api/user/logout | Authentication / Users | 200 | High | HAR | API test + negative test |
| PUT | /api/branch/038f901a-732e-4f4f-a05f-008d789f58f1 | Branches | 200 | High | HAR | API test + negative test |
| PUT | /api/customer-prospect/5d1c1f29-2c47-4dcc-bb95-6e1937fe2b12 | Customers | 200 | High | HAR | API test + negative test |
| PUT | /api/department/d88f110e-50fc-44d6-bd1c-1d35d4e66f68 | To classify | 200 | High | HAR | API test + negative test |
| PUT | /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a/edit | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/order/a28768ca-ed67-4155-bb41-61ef1db990dd | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/order/aa1feaa0-8075-4ab5-a8dc-ac8a561557f2 | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595 | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595/edit | Orders | 200 | Critical | HAR | API test + DB validation + performance test |
| PUT | /api/position/0c89049f-ed84-4c85-9d78-2d92feceb1ff | To classify | 200 | High | HAR | API test + negative test |
| PUT | /api/user/37a742f2-f474-49d5-9a95-9500685e6c35 | Authentication / Users | 200 | High | HAR | API test + negative test |
| DELETE | /:categoryId/branches | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| DELETE | /:dishId/branches | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| DELETE | /:id | To classify | Not seen in HAR | High | Backend routes | To review |
| DELETE | /:id/address/:addressId | To classify | Not seen in HAR | High | Backend routes | To review |
| DELETE | /:id/hard | To classify | Not seen in HAR | High | Backend routes | To review |
| DELETE | /bulk-remove | To classify | Not seen in HAR | High | Backend routes | To review |
| DELETE | /holidays/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| DELETE | /workflows/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| GET | / | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:categoryId/branches | Menu / Dishes | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:code | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:customerId([0-9a-fA-F-]{36}) | Customers | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:customerId([0-9a-fA-F-]{36})/history | Customers | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:dishId/branches | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| GET | /:filename | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id/analytics | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id/history | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id/stats | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id/transactions | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:id/verify-domain | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:loanId/history | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:loanId/schedule | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /:slug | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /active | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /admin | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /admin/tenant-history/:tenantId | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /all | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /analytics | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /available | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /available-gateways | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /balances/:userId | Authentication / Users | Not seen in HAR | Medium | Backend routes | To review |
| GET | /branch/:branchId | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /branch/:code | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /branches | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /channel/:channel | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /check | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /check-subdomain/:subdomain | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /cleanable | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /communication/channels | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /communication/channels/stats | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /config | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /config/:branchId | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /confirm-email | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /connections | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /customer/:customerId | Customers | Not seen in HAR | Medium | Backend routes | To review |
| GET | /dashboard | Reports / Dashboard | Not seen in HAR | Medium | Backend routes | To review |
| GET | /deals/:branchId | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /featured/:branchId | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /firebase-config | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /forecast | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /get-branches | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /gift-cards | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /gift-cards/verify/:code | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /google/locations | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /health | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /holidays | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /inventory-predictions | Inventory | Not seen in HAR | High | Backend routes | To review |
| GET | /logs | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /loyalty/summary | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /menu | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| GET | /menu/:branchId | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| GET | /my-subscription | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /my-usage | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /opportunities | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /order/:id | Orders | Not seen in HAR | Critical | Backend routes | To review |
| GET | /order/:orderIdentifier | Orders | Not seen in HAR | Critical | Backend routes | To review |
| GET | /orders | Orders | Not seen in HAR | Critical | Backend routes | To review |
| GET | /overdue | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /preview-context | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /preview/:id | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /price-intelligence | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /product-performance | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /profile | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /profit-analysis | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /prospect | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /prospect/:id | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /public | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /qr | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /search-by-phone | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /settings | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /sitemap.xml | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /statistics | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /stats | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /stats/:branchId | Branches | Not seen in HAR | Medium | Backend routes | To review |
| GET | /status | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /subscriptions | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /table/:branchId/:tableNo | Tables | Not seen in HAR | High | Backend routes | To review |
| GET | /track/:orderId | Orders | Not seen in HAR | Critical | Backend routes | To review |
| GET | /transactions | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /types | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /unverified | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /upcoming | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /verified | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /workflows | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /workflows/:id | To classify | Not seen in HAR | Medium | Backend routes | To review |
| GET | /workflows/:id/executions | To classify | Not seen in HAR | Medium | Backend routes | To review |
| PATCH | /:id/status | To classify | Not seen in HAR | High | Backend routes | To review |
| PATCH | /:id/toggle | To classify | Not seen in HAR | High | Backend routes | To review |
| PATCH | /balances/:userId | Authentication / Users | Not seen in HAR | High | Backend routes | To review |
| PATCH | /holidays/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| PATCH | /schedule/settings/:userId | Authentication / Users | Not seen in HAR | High | Backend routes | To review |
| PATCH | /workflows/:id/toggle | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | / | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:categoryId/branches | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| POST | /:dishId/branches | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| POST | /:gateway | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/calculate-distance | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/convert-to-order | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /:id/follow-up-email | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/force-cancel | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/interaction | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/launch | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/pause | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/regenerate | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/test-email | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:id/upload-receipt | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:loanId/bulk-reschedule | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:loanId/generate | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:platform/connect | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /:platform/disconnect | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /admin/cancel-subscription | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /admin/extend-trial | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /admin/upgrade-plan | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /analyze-receipt | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /apply | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /apply/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /approve-branch | Branches | Not seen in HAR | High | Backend routes | To review |
| POST | /ask | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /ask-staff | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /auth/request-otp | Authentication / Users | Not seen in HAR | High | Backend routes | To review |
| POST | /auth/verify-otp | Authentication / Users | Not seen in HAR | High | Backend routes | To review |
| POST | /branches/:branchId/calculate-distance | Branches | Not seen in HAR | High | Backend routes | To review |
| POST | /bulk-assign | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /cancel-plan | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /careem | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /change-plan | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /check-loan-reminders | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /check-low-stock | Inventory | Not seen in HAR | High | Backend routes | To review |
| POST | /check-subscription-expiry | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /communication/channels | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /communication/channels/:id/test | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /config | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /config/:branchId | Branches | Not seen in HAR | High | Backend routes | To review |
| POST | /connect | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /create | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /deals/evaluate | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /deliverect | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /deliveroo | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /disconnect | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /evaluate | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /generate-daily-reports | Reports / Dashboard | Not seen in HAR | High | Backend routes | To review |
| POST | /gift-cards/purchase | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /gift-cards/send-otp | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /google/sync-menu | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| POST | /holidays | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /installment/:installmentId/pay | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /inventory-intelligence | Inventory | Not seen in HAR | High | Backend routes | To review |
| POST | /issue | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /keeta | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /logout | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /loyalty/transfer | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /mamopay | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /menu-inquiry | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| POST | /merge | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /noon | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /order | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /orders | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /otter | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /pair | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /payment/create-order | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /paytabs | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /post | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /post/all | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /preview-audience | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /process-depreciation | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /process-recurring-expenses | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /prospect/interaction | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /proxy/branch | Branches | Not seen in HAR | High | Backend routes | To review |
| POST | /proxy/tenant | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /redeem | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /register | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /reorder | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /resend-verification | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /restart | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /revert-plan-change | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /save | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /send | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /send-order-notification | Orders | Not seen in HAR | Critical | Backend routes | To review |
| POST | /send-otp | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /smiles | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /stripe | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /talabat | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /telr | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /test | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /test-email | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /test-embedding | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /test-firebase | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /test/:branchId | Branches | Not seen in HAR | High | Backend routes | To review |
| POST | /top-up | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /transfer | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /upload-image | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /validate-promo | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /verify-numbers | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /verify-otp | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /verify-payment | Payments | Not seen in HAR | High | Backend routes | To review |
| POST | /webhook | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /webhook/:gateway | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /webhook/confirmation | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /workflows | To classify | Not seen in HAR | High | Backend routes | To review |
| POST | /workflows/:id/execute | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:categoryId/branch/:branchId | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| PUT | /:dishId/branch/:branchId | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| PUT | /:dishId/branch/:branchId/availability | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| PUT | /:dishId/branch/:branchId/price | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/activate | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/address | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/ai-settings | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/assign-manager | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/deactivate | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/domain | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/proxy | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/reset-password | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/status | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/translate | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/types | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:id/verify | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /:platform/config | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /bulk-update-pricing | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /communication/channels/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /installment/:installmentId/reschedule | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /profile | To classify | Not seen in HAR | High | Backend routes | To review |
| PUT | /workflows/:id | To classify | Not seen in HAR | High | Backend routes | To review |
| USE | /api/aggregator | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/aging | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/ai | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/api-tokens | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/automation | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/blogs | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/branch | Branches | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/category | Menu / Dishes | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/category-branch | Menu / Dishes | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/cron | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/customer | Customers | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/customer-prospect | Customers | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/database-setup | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/deal | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/delivery-boy | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/department | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/dish | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| USE | /api/dish-branch | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| USE | /api/dish-spice | Menu / Dishes | Not seen in HAR | High | Backend routes | To review |
| USE | /api/expense | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/expense-budget | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/feedback | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/financial-summary | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/fixed-asset | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/floor | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/gift-card | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/inventory | Inventory | Not seen in HAR | High | Backend routes | To review |
| USE | /api/leave | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/loan | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/loan-installment | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/loyalty | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/marketing-campaign | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/n8n | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/order | Orders | Not seen in HAR | Critical | Backend routes | To review |
| USE | /api/payment | Payments | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/payment-gateway | Payments | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/payroll | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/plans | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/platform-payments | Payments | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/platform-settings | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/position | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/promo-codes | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/public | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/purchase-order | Orders | Not seen in HAR | Critical | Backend routes | To review |
| USE | /api/search | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/semantic-cache | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/settings | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/shift | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/shift-template | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/social-media | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/system-logs | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/table | Tables | Not seen in HAR | High | Backend routes | To review |
| USE | /api/templates | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/tenants | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/user | Authentication / Users | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/vendor | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/webhooks | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/webhooks/subscription | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /api/whatsapp | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /blog | To classify | Not seen in HAR | Medium | Backend routes | To review |
| USE | /uploads | To classify | Not seen in HAR | Medium | Backend routes | To review |


---

# Source File: generated_frontend_routes.md


# Generated CloudPOS4U Frontend Route Inventory

This file was generated from frontend route discovery output.

| Route | Module Guess | Priority | Suggested UI Automation |
|---|---|---|---|
| / | To classify | High | Smoke test |
| /aggregator-reconciliation | To classify | High | Smoke test |
| /ai-assistant | To classify | High | Smoke test |
| /ai-insights | To classify | High | Smoke test |
| /ai-training | To classify | High | Smoke test |
| /auth | Authentication / Users | Critical | Authentication validation |
| /automation | To classify | High | Smoke test |
| /automation?view=marketing | To classify | High | Smoke test |
| /billing | To classify | High | Smoke test |
| /billing/success | To classify | High | Smoke test |
| /blog | To classify | High | Smoke test |
| /blog/:slug | To classify | High | Smoke test |
| /branches | Branches | High | Smoke test |
| /branches/:id/settings | Branches | High | Smoke test |
| /confirm-email | To classify | High | Smoke test |
| /consolidated-pl | To classify | High | Smoke test |
| /customer-prospects | Customers | High | Smoke test |
| /customer/orders | Orders | High | End-to-end business flow |
| /dashboard | Reports / Dashboard | High | Smoke test |
| /deals | To classify | High | Smoke test |
| /delivery-boys | To classify | High | Smoke test |
| /delivery-performance | To classify | High | Smoke test |
| /departments | To classify | High | Smoke test |
| /display | To classify | High | Smoke test |
| /employee-requests | To classify | High | Smoke test |
| /expenses | To classify | High | Smoke test |
| /feedback | To classify | High | Smoke test |
| /financial-dashboard | Reports / Dashboard | High | Smoke test |
| /fixed-asset-registry | To classify | High | Smoke test |
| /floor-plan | To classify | High | Smoke test |
| /floors | To classify | High | Smoke test |
| /gift-cards | To classify | High | Smoke test |
| /guides/aggregator-reconciliation | To classify | High | Smoke test |
| /home | To classify | High | Smoke test |
| /inventory | Inventory | High | Smoke test |
| /landing | To classify | High | Smoke test |
| /loans | To classify | High | Smoke test |
| /login | Authentication / Users | High | Authentication validation |
| /loyalty | To classify | High | Smoke test |
| /management | To classify | High | Smoke test |
| /menu | Menu / Dishes | Critical | End-to-end business flow |
| /mobile-attendance | To classify | High | Smoke test |
| /my-deliveries | To classify | High | Smoke test |
| /my-history | To classify | High | Smoke test |
| /my-payroll | To classify | High | Smoke test |
| /my-schedule | To classify | High | Smoke test |
| /orders | Orders | High | End-to-end business flow |
| /payment-history | Payments | High | Smoke test |
| /payroll | To classify | High | Smoke test |
| /payroll-reports | Reports / Dashboard | High | Smoke test |
| /payroll-settings | To classify | High | Smoke test |
| /payroll/* | To classify | High | Smoke test |
| /payroll/attendance | To classify | High | Smoke test |
| /payroll?tab=reports | Reports / Dashboard | High | Smoke test |
| /pos/cfd | To classify | High | Smoke test |
| /pos/kitchen | To classify | High | Smoke test |
| /pos/public/orders | Orders | High | End-to-end business flow |
| /pos/track-order | Orders | High | End-to-end business flow |
| /pos/waiter | To classify | High | Smoke test |
| /positions | To classify | High | Smoke test |
| /privacy-policy | To classify | High | Smoke test |
| /public/orders | Orders | High | End-to-end business flow |
| /purchase-orders | Orders | High | End-to-end business flow |
| /reconciliation | To classify | High | Smoke test |
| /register | To classify | High | Smoke test |
| /secure-admin-login-8822 | Authentication / Users | High | Authentication validation |
| /settings | To classify | High | Smoke test |
| /setup-wizard | To classify | High | Smoke test |
| /shifts | To classify | High | Smoke test |
| /super-admin/ai-settings | To classify | High | Smoke test |
| /super-admin/ai-training | To classify | High | Smoke test |
| /super-admin/blog | To classify | High | Smoke test |
| /super-admin/blog/edit/:id | To classify | High | Smoke test |
| /super-admin/blog/new | To classify | High | Smoke test |
| /super-admin/email-settings | To classify | High | Smoke test |
| /super-admin/gateways | To classify | High | Smoke test |
| /super-admin/plans | To classify | High | Smoke test |
| /super-admin/platform-settings | To classify | High | Smoke test |
| /super-admin/promo-codes | To classify | High | Smoke test |
| /super-admin/subscriptions | To classify | High | Smoke test |
| /super-admin/system-logs | To classify | High | Smoke test |
| /super-admin/templates | To classify | High | Smoke test |
| /super-admin/tenants | To classify | High | Smoke test |
| /super-admin/whatsapp-health | To classify | High | Smoke test |
| /tables | Tables | High | Smoke test |
| /terms-conditions | To classify | High | Smoke test |
| /track-order | Orders | High | End-to-end business flow |
| /users | Authentication / Users | High | Smoke test |
| /users?action=transfer | Authentication / Users | High | Smoke test |
| /users?branch= | Authentication / Users | High | Smoke test |
| /vendors | To classify | High | Smoke test |


---

# Source File: generated_automation_backlog.md


# Generated CloudPOS4U Automation Backlog

This backlog was generated from discovered APIs and frontend routes.

| ID | Area | Scenario | Tool | Priority | Status |
|---|---|---|---|---|---|
| API-001 | API | Validate GET /api/aggregator/config/038f901a-732e-4f4f-a05f-008d789f58f1 success response | Pytest Requests / Postman | Medium | Pending review |
| API-002 | API | Validate GET /api/ai/config success response | Pytest Requests / Postman | Medium | Pending review |
| API-003 | API | Validate GET /api/branch success response | Pytest Requests / Postman | Medium | Pending review |
| API-004 | API | Validate GET /api/branch/038f901a-732e-4f4f-a05f-008d789f58f1 success response | Pytest Requests / Postman | Medium | Pending review |
| API-005 | API | Validate GET /api/category success response | Pytest Requests / Postman | Medium | Pending review |
| API-006 | API | Validate GET /api/customer-prospect success response | Pytest Requests / Postman | Medium | Pending review |
| API-007 | API | Validate GET /api/customer-prospect/statistics success response | Pytest Requests / Postman | Medium | Pending review |
| API-008 | API | Validate GET /api/deal success response | Pytest Requests / Postman | Medium | Pending review |
| API-009 | API | Validate GET /api/delivery-boy success response | Pytest Requests / Postman | Medium | Pending review |
| API-010 | API | Validate GET /api/delivery-boy/available success response | Pytest Requests / Postman | Medium | Pending review |
| API-011 | API | Validate GET /api/department success response | Pytest Requests / Postman | Medium | Pending review |
| API-012 | API | Validate GET /api/dish success response | Pytest Requests / Postman | High | Pending review |
| API-013 | API | Validate GET /api/dish-spice/dish/00000000-0000-0000-0000-000000000000 success response | Pytest Requests / Postman | High | Pending review |
| API-014 | API | Validate GET /api/dish-spice/dish/179b313e-5c67-491f-8e93-b3ee56cbe543 success response | Pytest Requests / Postman | High | Pending review |
| API-015 | API | Validate GET /api/dish-spice/dish/206c608f-2398-437f-8647-d1eb00255b20 success response | Pytest Requests / Postman | High | Pending review |
| API-016 | API | Validate GET /api/dish-spice/dish/2581da77-cbd8-4924-9a78-ce0a69615f14 success response | Pytest Requests / Postman | High | Pending review |
| API-017 | API | Validate GET /api/dish-spice/dish/28754367-18c5-401c-ab7b-6e5f79e36bc3 success response | Pytest Requests / Postman | High | Pending review |
| API-018 | API | Validate GET /api/dish-spice/dish/2cd327f3-cc50-4343-a3fb-4c24e7d897b1 success response | Pytest Requests / Postman | High | Pending review |
| API-019 | API | Validate GET /api/dish-spice/dish/2d1dad30-115a-40f4-ab25-496bac5f1da0 success response | Pytest Requests / Postman | High | Pending review |
| API-020 | API | Validate GET /api/dish-spice/dish/39a1249f-3e76-47c2-a79d-08d3de982661 success response | Pytest Requests / Postman | High | Pending review |
| API-021 | API | Validate GET /api/dish-spice/dish/3f4d2d31-9a1e-4d00-94c6-904ec6dff064 success response | Pytest Requests / Postman | High | Pending review |
| API-022 | API | Validate GET /api/dish-spice/dish/446adcd9-d3e1-4a41-b2ac-2812e2c6d90e success response | Pytest Requests / Postman | High | Pending review |
| API-023 | API | Validate GET /api/dish-spice/dish/48a4a2bb-db6f-4414-9b23-6802378d9b6b success response | Pytest Requests / Postman | High | Pending review |
| API-024 | API | Validate GET /api/dish-spice/dish/4e527416-dd4d-42c6-98ff-384f38d682b9 success response | Pytest Requests / Postman | High | Pending review |
| API-025 | API | Validate GET /api/dish-spice/dish/5087fb70-3c1e-4215-8472-8eaab01a73d6 success response | Pytest Requests / Postman | High | Pending review |
| API-026 | API | Validate GET /api/dish-spice/dish/547780a2-4a9f-44f0-a879-d0725a17a541 success response | Pytest Requests / Postman | High | Pending review |
| API-027 | API | Validate GET /api/dish-spice/dish/597f00de-62a9-44b4-9540-b15e34f8b3ca success response | Pytest Requests / Postman | High | Pending review |
| API-028 | API | Validate GET /api/dish-spice/dish/5d6f9114-1b6e-4d44-89c5-8832359ffc92 success response | Pytest Requests / Postman | High | Pending review |
| API-029 | API | Validate GET /api/dish-spice/dish/5f392a68-6d3b-4c64-9c83-49d50d7bf478 success response | Pytest Requests / Postman | High | Pending review |
| API-030 | API | Validate GET /api/dish-spice/dish/61fa7c5b-a024-4647-a3e6-ce1be484cbf4 success response | Pytest Requests / Postman | High | Pending review |
| API-031 | API | Validate GET /api/dish-spice/dish/629f916e-f5b9-4ffc-b70d-ce054cfbfb40 success response | Pytest Requests / Postman | High | Pending review |
| API-032 | API | Validate GET /api/dish-spice/dish/65311a8d-3eff-4913-b699-5977d55a39a9 success response | Pytest Requests / Postman | High | Pending review |
| API-033 | API | Validate GET /api/dish-spice/dish/69084ed7-38a8-4059-8711-d4dcd597c3d9 success response | Pytest Requests / Postman | High | Pending review |
| API-034 | API | Validate GET /api/dish-spice/dish/6926d004-c78c-4462-b26e-ebdf62dd16ca success response | Pytest Requests / Postman | High | Pending review |
| API-035 | API | Validate GET /api/dish-spice/dish/7b913575-092e-4a97-a064-afd064875dc0 success response | Pytest Requests / Postman | High | Pending review |
| API-036 | API | Validate GET /api/dish-spice/dish/95a00b06-929d-444e-8782-3a3ff994b3df success response | Pytest Requests / Postman | High | Pending review |
| API-037 | API | Validate GET /api/dish-spice/dish/99799115-6e84-40c3-879c-bdcdaf8a6f4d success response | Pytest Requests / Postman | High | Pending review |
| API-038 | API | Validate GET /api/dish-spice/dish/9ad65cfc-447b-4b30-8191-77f37a21abc0 success response | Pytest Requests / Postman | High | Pending review |
| API-039 | API | Validate GET /api/dish-spice/dish/9f9a5ce9-350b-45fa-955e-23a6d40c8dee success response | Pytest Requests / Postman | High | Pending review |
| API-040 | API | Validate GET /api/dish-spice/dish/a0a8ef5f-7abc-443e-a918-71606e7fe5bc success response | Pytest Requests / Postman | High | Pending review |
| API-041 | API | Validate GET /api/dish-spice/dish/a7ea57d0-31ea-449a-9a7a-e40258f3ea23 success response | Pytest Requests / Postman | High | Pending review |
| API-042 | API | Validate GET /api/dish-spice/dish/b0985823-715d-4343-95a1-17edaa34b7b4 success response | Pytest Requests / Postman | High | Pending review |
| API-043 | API | Validate GET /api/dish-spice/dish/b16ca2e1-1129-4efd-9692-4067f9de0551 success response | Pytest Requests / Postman | High | Pending review |
| API-044 | API | Validate GET /api/dish-spice/dish/b182b1d8-6c9f-43af-8288-3720c4cf0e9e success response | Pytest Requests / Postman | High | Pending review |
| API-045 | API | Validate GET /api/dish-spice/dish/bebd9969-b04b-45cf-bddb-c2b6602e80a9 success response | Pytest Requests / Postman | High | Pending review |
| API-046 | API | Validate GET /api/dish-spice/dish/c137e6b1-bda4-46eb-9370-aee227ea9b49 success response | Pytest Requests / Postman | High | Pending review |
| API-047 | API | Validate GET /api/dish-spice/dish/c2aa3c34-be47-40a0-b873-bda8a25c7d4e success response | Pytest Requests / Postman | High | Pending review |
| API-048 | API | Validate GET /api/dish-spice/dish/c4d952d6-fc67-47e3-869d-cb0f51c7fdfe success response | Pytest Requests / Postman | High | Pending review |
| API-049 | API | Validate GET /api/dish-spice/dish/d439eb1f-f6ae-4c14-8905-2f67dd327f25 success response | Pytest Requests / Postman | High | Pending review |
| API-050 | API | Validate GET /api/dish-spice/dish/dda70e47-fb38-4097-90cf-1ef4c97f20f6 success response | Pytest Requests / Postman | High | Pending review |
| API-051 | API | Validate GET /api/dish-spice/dish/e70a62d7-253a-4668-8b33-be896641c2c9 success response | Pytest Requests / Postman | High | Pending review |
| API-052 | API | Validate GET /api/dish-spice/dish/e85b533a-e037-4498-a6ae-5be62b79b98d success response | Pytest Requests / Postman | High | Pending review |
| API-053 | API | Validate GET /api/dish-spice/dish/eb1356a3-bf8e-47b2-bc11-bcbde5086e28 success response | Pytest Requests / Postman | High | Pending review |
| API-054 | API | Validate GET /api/dish-spice/dish/ecd7252a-9b2c-414b-808a-6daa3f89c2f7 success response | Pytest Requests / Postman | High | Pending review |
| API-055 | API | Validate GET /api/dish-spice/dish/ee963fb6-04e3-49b1-a829-4b1ae9e82b5a success response | Pytest Requests / Postman | High | Pending review |
| API-056 | API | Validate GET /api/dish-spice/dish/f9ec938b-6a39-474e-b258-8cf26f452f61 success response | Pytest Requests / Postman | High | Pending review |
| API-057 | API | Validate GET /api/dish-spice/dish/fbfb8e4a-da7c-411e-856a-4df1eac443b2 success response | Pytest Requests / Postman | High | Pending review |
| API-058 | API | Validate GET /api/dish/all success response | Pytest Requests / Postman | High | Pending review |
| API-059 | API | Validate GET /api/inventory success response | Pytest Requests / Postman | High | Pending review |
| API-060 | API | Validate GET /api/inventory/transactions success response | Pytest Requests / Postman | High | Pending review |
| API-061 | API | Validate GET /api/order success response | Pytest Requests / Postman | Critical | Pending review |
| API-062 | API | Validate GET /api/payment-gateway/config/038f901a-732e-4f4f-a05f-008d789f58f1 success response | Pytest Requests / Postman | Medium | Pending review |
| API-063 | API | Validate GET /api/payroll/attendance/admin success response | Pytest Requests / Postman | Medium | Pending review |
| API-064 | API | Validate GET /api/payroll/entry success response | Pytest Requests / Postman | Medium | Pending review |
| API-065 | API | Validate GET /api/payroll/my/attendance success response | Pytest Requests / Postman | Medium | Pending review |
| API-066 | API | Validate GET /api/payroll/settings success response | Pytest Requests / Postman | Medium | Pending review |
| API-067 | API | Validate GET /api/position success response | Pytest Requests / Postman | Medium | Pending review |
| API-068 | API | Validate GET /api/settings success response | Pytest Requests / Postman | Medium | Pending review |
| API-069 | API | Validate GET /api/settings/firebase-config success response | Pytest Requests / Postman | Medium | Pending review |
| API-070 | API | Validate GET /api/shift/current success response | Pytest Requests / Postman | Medium | Pending review |
| API-071 | API | Validate GET /api/table success response | Pytest Requests / Postman | High | Pending review |
| API-072 | API | Validate GET /api/user success response | Pytest Requests / Postman | Medium | Pending review |
| API-073 | API | Validate GET /api/user/all success response | Pytest Requests / Postman | Medium | Pending review |
| API-074 | API | Validate GET /api/user/setup-status success response | Pytest Requests / Postman | Medium | Pending review |
| API-075 | API | Validate GET /api/vendor success response | Pytest Requests / Postman | Medium | Pending review |
| API-076 | API | Validate GET /api/whatsapp/dashboard success response | Pytest Requests / Postman | Medium | Pending review |
| API-077 | API | Validate GET /api/whatsapp/logs success response | Pytest Requests / Postman | Medium | Pending review |
| API-078 | API | Validate GET /api/whatsapp/status success response | Pytest Requests / Postman | Medium | Pending review |
| API-079 | API | Validate POST /api/deal/evaluate success response | Pytest Requests / Postman | High | Pending review |
| API-080 | API Negative | Validate unauthorized/invalid payload for POST /api/deal/evaluate | Pytest Requests | High | Pending review |
| API-081 | API | Validate POST /api/inventory success response | Pytest Requests / Postman | High | Pending review |
| API-082 | API Negative | Validate unauthorized/invalid payload for POST /api/inventory | Pytest Requests | High | Pending review |
| API-083 | API | Validate POST /api/order/ success response | Pytest Requests / Postman | Critical | Pending review |
| API-084 | API Negative | Validate unauthorized/invalid payload for POST /api/order/ | Pytest Requests | Critical | Pending review |
| API-085 | API | Validate POST /api/payment/create-order success response | Pytest Requests / Postman | Critical | Pending review |
| API-086 | API Negative | Validate unauthorized/invalid payload for POST /api/payment/create-order | Pytest Requests | Critical | Pending review |
| API-087 | API | Validate POST /api/user/login success response | Pytest Requests / Postman | Critical | Pending review |
| API-088 | API Negative | Validate unauthorized/invalid payload for POST /api/user/login | Pytest Requests | Critical | Pending review |
| API-089 | API | Validate POST /api/user/logout success response | Pytest Requests / Postman | High | Pending review |
| API-090 | API Negative | Validate unauthorized/invalid payload for POST /api/user/logout | Pytest Requests | High | Pending review |
| API-091 | API | Validate PUT /api/branch/038f901a-732e-4f4f-a05f-008d789f58f1 success response | Pytest Requests / Postman | High | Pending review |
| API-092 | API Negative | Validate unauthorized/invalid payload for PUT /api/branch/038f901a-732e-4f4f-a05f-008d789f58f1 | Pytest Requests | High | Pending review |
| API-093 | API | Validate PUT /api/customer-prospect/5d1c1f29-2c47-4dcc-bb95-6e1937fe2b12 success response | Pytest Requests / Postman | High | Pending review |
| API-094 | API Negative | Validate unauthorized/invalid payload for PUT /api/customer-prospect/5d1c1f29-2c47-4dcc-bb95-6e1937fe2b12 | Pytest Requests | High | Pending review |
| API-095 | API | Validate PUT /api/department/d88f110e-50fc-44d6-bd1c-1d35d4e66f68 success response | Pytest Requests / Postman | High | Pending review |
| API-096 | API Negative | Validate unauthorized/invalid payload for PUT /api/department/d88f110e-50fc-44d6-bd1c-1d35d4e66f68 | Pytest Requests | High | Pending review |
| API-097 | API | Validate PUT /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a success response | Pytest Requests / Postman | Critical | Pending review |
| API-098 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a | Pytest Requests | Critical | Pending review |
| API-099 | API | Validate PUT /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a/edit success response | Pytest Requests / Postman | Critical | Pending review |
| API-100 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/9de62509-5111-4f12-ba4d-7e30ed0a225a/edit | Pytest Requests | Critical | Pending review |
| API-101 | API | Validate PUT /api/order/a28768ca-ed67-4155-bb41-61ef1db990dd success response | Pytest Requests / Postman | Critical | Pending review |
| API-102 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/a28768ca-ed67-4155-bb41-61ef1db990dd | Pytest Requests | Critical | Pending review |
| API-103 | API | Validate PUT /api/order/aa1feaa0-8075-4ab5-a8dc-ac8a561557f2 success response | Pytest Requests / Postman | Critical | Pending review |
| API-104 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/aa1feaa0-8075-4ab5-a8dc-ac8a561557f2 | Pytest Requests | Critical | Pending review |
| API-105 | API | Validate PUT /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595 success response | Pytest Requests / Postman | Critical | Pending review |
| API-106 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595 | Pytest Requests | Critical | Pending review |
| API-107 | API | Validate PUT /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595/edit success response | Pytest Requests / Postman | Critical | Pending review |
| API-108 | API Negative | Validate unauthorized/invalid payload for PUT /api/order/b41af83c-81a5-4752-aa80-ed8fe7d5c595/edit | Pytest Requests | Critical | Pending review |
| API-109 | API | Validate PUT /api/position/0c89049f-ed84-4c85-9d78-2d92feceb1ff success response | Pytest Requests / Postman | High | Pending review |
| API-110 | API Negative | Validate unauthorized/invalid payload for PUT /api/position/0c89049f-ed84-4c85-9d78-2d92feceb1ff | Pytest Requests | High | Pending review |
| API-111 | API | Validate PUT /api/user/37a742f2-f474-49d5-9a95-9500685e6c35 success response | Pytest Requests / Postman | High | Pending review |
| API-112 | API Negative | Validate unauthorized/invalid payload for PUT /api/user/37a742f2-f474-49d5-9a95-9500685e6c35 | Pytest Requests | High | Pending review |
| UI-001 | UI | Validate page load and core action for / | Selenium Pytest | High | Pending review |
| UI-002 | UI | Validate page load and core action for /aggregator-reconciliation | Selenium Pytest | High | Pending review |
| UI-003 | UI | Validate page load and core action for /ai-assistant | Selenium Pytest | High | Pending review |
| UI-004 | UI | Validate page load and core action for /ai-insights | Selenium Pytest | High | Pending review |
| UI-005 | UI | Validate page load and core action for /ai-training | Selenium Pytest | High | Pending review |
| UI-006 | UI | Validate page load and core action for /auth | Selenium Pytest | Critical | Pending review |
| UI-007 | UI | Validate page load and core action for /automation | Selenium Pytest | High | Pending review |
| UI-008 | UI | Validate page load and core action for /automation?view=marketing | Selenium Pytest | High | Pending review |
| UI-009 | UI | Validate page load and core action for /billing | Selenium Pytest | High | Pending review |
| UI-010 | UI | Validate page load and core action for /billing/success | Selenium Pytest | High | Pending review |
| UI-011 | UI | Validate page load and core action for /blog | Selenium Pytest | High | Pending review |
| UI-012 | UI | Validate page load and core action for /blog/:slug | Selenium Pytest | High | Pending review |
| UI-013 | UI | Validate page load and core action for /branches | Selenium Pytest | High | Pending review |
| UI-014 | UI | Validate page load and core action for /branches/:id/settings | Selenium Pytest | High | Pending review |
| UI-015 | UI | Validate page load and core action for /confirm-email | Selenium Pytest | High | Pending review |
| UI-016 | UI | Validate page load and core action for /consolidated-pl | Selenium Pytest | High | Pending review |
| UI-017 | UI | Validate page load and core action for /customer-prospects | Selenium Pytest | High | Pending review |
| UI-018 | UI | Validate page load and core action for /customer/orders | Selenium Pytest | High | Pending review |
| UI-019 | UI | Validate page load and core action for /dashboard | Selenium Pytest | High | Pending review |
| UI-020 | UI | Validate page load and core action for /deals | Selenium Pytest | High | Pending review |
| UI-021 | UI | Validate page load and core action for /delivery-boys | Selenium Pytest | High | Pending review |
| UI-022 | UI | Validate page load and core action for /delivery-performance | Selenium Pytest | High | Pending review |
| UI-023 | UI | Validate page load and core action for /departments | Selenium Pytest | High | Pending review |
| UI-024 | UI | Validate page load and core action for /display | Selenium Pytest | High | Pending review |
| UI-025 | UI | Validate page load and core action for /employee-requests | Selenium Pytest | High | Pending review |
| UI-026 | UI | Validate page load and core action for /expenses | Selenium Pytest | High | Pending review |
| UI-027 | UI | Validate page load and core action for /feedback | Selenium Pytest | High | Pending review |
| UI-028 | UI | Validate page load and core action for /financial-dashboard | Selenium Pytest | High | Pending review |
| UI-029 | UI | Validate page load and core action for /fixed-asset-registry | Selenium Pytest | High | Pending review |
| UI-030 | UI | Validate page load and core action for /floor-plan | Selenium Pytest | High | Pending review |
| UI-031 | UI | Validate page load and core action for /floors | Selenium Pytest | High | Pending review |
| UI-032 | UI | Validate page load and core action for /gift-cards | Selenium Pytest | High | Pending review |
| UI-033 | UI | Validate page load and core action for /guides/aggregator-reconciliation | Selenium Pytest | High | Pending review |
| UI-034 | UI | Validate page load and core action for /home | Selenium Pytest | High | Pending review |
| UI-035 | UI | Validate page load and core action for /inventory | Selenium Pytest | High | Pending review |
| UI-036 | UI | Validate page load and core action for /landing | Selenium Pytest | High | Pending review |
| UI-037 | UI | Validate page load and core action for /loans | Selenium Pytest | High | Pending review |
| UI-038 | UI | Validate page load and core action for /login | Selenium Pytest | High | Pending review |
| UI-039 | UI | Validate page load and core action for /loyalty | Selenium Pytest | High | Pending review |
| UI-040 | UI | Validate page load and core action for /management | Selenium Pytest | High | Pending review |
| UI-041 | UI | Validate page load and core action for /menu | Selenium Pytest | Critical | Pending review |
| UI-042 | UI | Validate page load and core action for /mobile-attendance | Selenium Pytest | High | Pending review |
| UI-043 | UI | Validate page load and core action for /my-deliveries | Selenium Pytest | High | Pending review |
| UI-044 | UI | Validate page load and core action for /my-history | Selenium Pytest | High | Pending review |
| UI-045 | UI | Validate page load and core action for /my-payroll | Selenium Pytest | High | Pending review |
| UI-046 | UI | Validate page load and core action for /my-schedule | Selenium Pytest | High | Pending review |
| UI-047 | UI | Validate page load and core action for /orders | Selenium Pytest | High | Pending review |
| UI-048 | UI | Validate page load and core action for /payment-history | Selenium Pytest | High | Pending review |
| UI-049 | UI | Validate page load and core action for /payroll | Selenium Pytest | High | Pending review |
| UI-050 | UI | Validate page load and core action for /payroll-reports | Selenium Pytest | High | Pending review |
| UI-051 | UI | Validate page load and core action for /payroll-settings | Selenium Pytest | High | Pending review |
| UI-052 | UI | Validate page load and core action for /payroll/* | Selenium Pytest | High | Pending review |
| UI-053 | UI | Validate page load and core action for /payroll/attendance | Selenium Pytest | High | Pending review |
| UI-054 | UI | Validate page load and core action for /payroll?tab=reports | Selenium Pytest | High | Pending review |
| UI-055 | UI | Validate page load and core action for /pos/cfd | Selenium Pytest | High | Pending review |
| UI-056 | UI | Validate page load and core action for /pos/kitchen | Selenium Pytest | High | Pending review |
| UI-057 | UI | Validate page load and core action for /pos/public/orders | Selenium Pytest | High | Pending review |
| UI-058 | UI | Validate page load and core action for /pos/track-order | Selenium Pytest | High | Pending review |
| UI-059 | UI | Validate page load and core action for /pos/waiter | Selenium Pytest | High | Pending review |
| UI-060 | UI | Validate page load and core action for /positions | Selenium Pytest | High | Pending review |
| UI-061 | UI | Validate page load and core action for /privacy-policy | Selenium Pytest | High | Pending review |
| UI-062 | UI | Validate page load and core action for /public/orders | Selenium Pytest | High | Pending review |
| UI-063 | UI | Validate page load and core action for /purchase-orders | Selenium Pytest | High | Pending review |
| UI-064 | UI | Validate page load and core action for /reconciliation | Selenium Pytest | High | Pending review |
| UI-065 | UI | Validate page load and core action for /register | Selenium Pytest | High | Pending review |
| UI-066 | UI | Validate page load and core action for /secure-admin-login-8822 | Selenium Pytest | High | Pending review |
| UI-067 | UI | Validate page load and core action for /settings | Selenium Pytest | High | Pending review |
| UI-068 | UI | Validate page load and core action for /setup-wizard | Selenium Pytest | High | Pending review |
| UI-069 | UI | Validate page load and core action for /shifts | Selenium Pytest | High | Pending review |
| UI-070 | UI | Validate page load and core action for /super-admin/ai-settings | Selenium Pytest | High | Pending review |
| UI-071 | UI | Validate page load and core action for /super-admin/ai-training | Selenium Pytest | High | Pending review |
| UI-072 | UI | Validate page load and core action for /super-admin/blog | Selenium Pytest | High | Pending review |
| UI-073 | UI | Validate page load and core action for /super-admin/blog/edit/:id | Selenium Pytest | High | Pending review |
| UI-074 | UI | Validate page load and core action for /super-admin/blog/new | Selenium Pytest | High | Pending review |
| UI-075 | UI | Validate page load and core action for /super-admin/email-settings | Selenium Pytest | High | Pending review |
| UI-076 | UI | Validate page load and core action for /super-admin/gateways | Selenium Pytest | High | Pending review |
| UI-077 | UI | Validate page load and core action for /super-admin/plans | Selenium Pytest | High | Pending review |
| UI-078 | UI | Validate page load and core action for /super-admin/platform-settings | Selenium Pytest | High | Pending review |
| UI-079 | UI | Validate page load and core action for /super-admin/promo-codes | Selenium Pytest | High | Pending review |
| UI-080 | UI | Validate page load and core action for /super-admin/subscriptions | Selenium Pytest | High | Pending review |
| UI-081 | UI | Validate page load and core action for /super-admin/system-logs | Selenium Pytest | High | Pending review |
| UI-082 | UI | Validate page load and core action for /super-admin/templates | Selenium Pytest | High | Pending review |
| UI-083 | UI | Validate page load and core action for /super-admin/tenants | Selenium Pytest | High | Pending review |
| UI-084 | UI | Validate page load and core action for /super-admin/whatsapp-health | Selenium Pytest | High | Pending review |
| UI-085 | UI | Validate page load and core action for /tables | Selenium Pytest | High | Pending review |
| UI-086 | UI | Validate page load and core action for /terms-conditions | Selenium Pytest | High | Pending review |
| UI-087 | UI | Validate page load and core action for /track-order | Selenium Pytest | High | Pending review |
| UI-088 | UI | Validate page load and core action for /users | Selenium Pytest | High | Pending review |
| UI-089 | UI | Validate page load and core action for /users?action=transfer | Selenium Pytest | High | Pending review |
| UI-090 | UI | Validate page load and core action for /users?branch= | Selenium Pytest | High | Pending review |
| UI-091 | UI | Validate page load and core action for /vendors | Selenium Pytest | High | Pending review |


---

# Source File: test_inventory.md


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


---

# Source File: workflows.md


# CloudPOS4U Workflow Inventory

This file tracks important business workflows and their QA automation status.

## Automated Workflows

### 1. Admin Login

**Business Purpose:**  
Allows admin user to access the POS admin panel.

**Coverage:**
- UI valid login: Done
- UI invalid login: Done
- API valid login: Done
- API invalid login: Done
- JMeter login performance: Done

**Tools:**
- Selenium
- Pytest
- Python Requests
- Postman
- JMeter
- Allure
- Jenkins

---

### 2. Dashboard Validation

**Business Purpose:**  
Verifies that the dashboard loads successfully after login.

**Coverage:**
- UI dashboard load after login: Done

**Tools:**
- Selenium
- Pytest
- Allure

---

### 3. POS Cash Paid Order Creation

**Business Purpose:**  
Validates the most critical POS revenue workflow: creating a cash paid takeaway order.

**Coverage:**
- UI order creation: Done
- API order creation: Done
- JMeter order creation performance: Done
- Allure reporting: Done
- Jenkins execution: Done

**Tools:**
- Selenium
- Pytest
- Python Requests
- JMeter
- Allure
- Jenkins

---

### 4. Menu / Dish Loading

**Business Purpose:**  
Verifies menu items are available and can be loaded for POS order creation.

**Coverage:**
- API get all dishes: Done
- JMeter get dishes performance: Done
- Dynamic dish extraction for order tests: Done

---

## Pending Workflows to Discover

| Workflow | Description | Priority |
|---|---|---|
| Orders List | View and search created orders | High |
| Order Details | Verify order detail page and invoice data | High |
| Cancel Order | Cancel existing order and validate status | High |
| Dine-in Table Order | Select table and create dine-in order | High |
| Delivery Order | Create delivery order with customer address | High |
| Customer Creation | Add/edit/search customer profile | Medium |
| Inventory Deduction | Verify stock deduction after order | High |
| User Role Permission | Validate restricted access for cashier/waiter/admin | High |
| Reports | Validate sales/dashboard reports | Medium |
| Gift Card Payment | Redeem gift card during checkout | Medium |
| Loyalty Points Payment | Redeem loyalty points during checkout | Medium |
| Split Payment | Pay using multiple methods | Medium |