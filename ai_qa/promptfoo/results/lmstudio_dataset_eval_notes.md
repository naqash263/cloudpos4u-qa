# LM Studio Promptfoo Dataset Evaluation Notes

## Objective
Evaluate local LM Studio model behavior for CloudPOS4U AI order extraction.

## Provider
LM Studio OpenAI-compatible server

## Model
google/gemma-4-e4b

## Evaluation Scope
- JSON-only output contract
- Intent extraction
- Order type extraction
- Menu item extraction
- Quantity extraction
- Unavailable item handling

## Key QA Checks
- Output must start with `{`
- Output must end with `}`
- No reasoning text allowed
- No markdown allowed
- Returned JSON must contain expected intent
- Returned JSON must contain expected order type
- Returned JSON must contain expected menu item

## Senior QA Value
This demonstrates prompt regression testing using a dataset-driven approach. It helps compare model reliability and detect regressions when prompt wording or local model selection changes.