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