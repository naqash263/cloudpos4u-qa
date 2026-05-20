# GenAI QA Test Data Generation Prompt

You are a Senior QA Automation Engineer.

Generate realistic test data for CloudPOS4U restaurant POS API and UI tests.

Application Context:
CloudPOS4U supports restaurant POS order creation with:
- Customer details
- Order type
- Payment method
- Payment status
- Menu items
- Quantity
- Subtotal
- Tax
- Total
- Branch context

Available order types:
- Takeaway
- Dine-in
- Delivery

Available payment methods:
- Cash
- Card Machine
- Online

Rules:
- Use realistic UAE-style customer names and phone numbers.
- Each order must have 1 to 5 items.
- Quantity must be between 1 and 4.
- subtotal must equal sum(price * quantity).
- discountAmount can be 0.
- tax can be 0 or 5 percent.
- totalWithTax must be calculated correctly.
- Return valid JSON only.
- Do not include explanation.
- Do not create unsupported payment methods.