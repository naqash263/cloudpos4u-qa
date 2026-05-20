from pathlib import Path


PROMPT_FILE = Path("ai_qa/promptfoo/prompts/order_extraction_prompt.txt")


def build_order_extraction_prompt(customer_message: str) -> str:
    prompt_template = PROMPT_FILE.read_text(encoding="utf-8")

    return prompt_template.replace(
        "{{customer_message}}",
        customer_message
    )