from pathlib import Path
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]

PROMPT_FILE = BASE_DIR / "ai_qa" / "cloudpos4u_genai_qa_prompt.md"
OUTPUT_FILE = BASE_DIR / "discovery" / "generated_test_coverage_matrix.md"

LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
MODEL_NAME = "local-model"


def read_prompt() -> str:
    if not PROMPT_FILE.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {PROMPT_FILE}. "
            "Run: python ai_qa/build_genai_prompt.py"
        )

    return PROMPT_FILE.read_text(encoding="utf-8", errors="ignore")


def call_lmstudio(prompt: str) -> str:
    client = OpenAI(
        base_url=LM_STUDIO_BASE_URL,
        api_key="lm-studio"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Senior QA Automation Engineer and GenAI QA Specialist. "
                    "You produce practical QA coverage matrices, automation backlogs, "
                    "risk-based testing plans, and CI/CD-ready recommendations."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=8000
    )

    return response.choices[0].message.content


def main():
    prompt = read_prompt()

    print("Sending CloudPOS4U QA discovery prompt to LM Studio...")
    result = call_lmstudio(prompt)

    OUTPUT_FILE.write_text(result, encoding="utf-8")

    print(f"Generated coverage matrix: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()