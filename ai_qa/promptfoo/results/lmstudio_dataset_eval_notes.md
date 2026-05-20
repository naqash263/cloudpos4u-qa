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

## QA Value
This demonstrates prompt regression testing using a dataset-driven approach. It helps compare model reliability and detect regressions when prompt wording or local model selection changes.

## Latest Evaluation Result After Prompt Fix

Total test cases: 9  
Passed: 9  
Failed: 0  
Pass rate: 100%  
Provider: LM Studio  
Model: google/gemma-4-e4b or currently selected local model

## Fixed Issue

Previous failure:
The model correctly detected `menu_query` for "Do you have kulfi falooda?" but did not extract the queried item.

Fix:
Added explicit prompt rules for menu_query scenarios:
- Extract mentioned menu item into items
- Use quantity 1 by default
- Set needsConfirmation to false

Result:
All 9 Promptfoo test cases passed after the prompt update.

## QA Learning

This demonstrates prompt regression testing. A failed AI behavior was identified, prompt rules were improved, and the full dataset was rerun to confirm no regression.