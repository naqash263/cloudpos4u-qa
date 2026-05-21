# CloudPOS4U Frontend Route Inventory

This file tracks discovered frontend routes/pages and their automation priority.

## Current UI Coverage

| Route | Page / Module | Purpose | Automation Status | Priority |
|---|---|---|---|---|
| /auth | Login | Admin authentication | Automated | Critical |
| /dashboard | Dashboard | Admin overview and KPIs | Automated | High |
| /menu | POS Menu / Order Screen | Create POS order | Automated | Critical |

## Routes Pending Discovery

| Route / Module | Expected Purpose | Priority |
|---|---|---|
| /orders | View and manage orders | High |
| /tables | Table management / dine-in flow | High |
| /customers | Customer management | Medium |
| /inventory | Inventory and stock management | High |
| /reports | Sales and operational reports | Medium |
| /users | User and role management | High |
| /settings | System settings | Medium |
| /delivery | Delivery order tracking | Medium |
| /loyalty | Loyalty points | Medium |
| /gift-cards | Gift card management | Medium |

## Discovery Notes

Frontend routes should be extracted from React routing files such as:

- App.jsx
- App.js
- routes.jsx
- router.jsx
- main.jsx
- Sidebar.jsx
- Navigation components