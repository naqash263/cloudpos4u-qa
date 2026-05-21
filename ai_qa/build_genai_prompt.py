from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DISCOVERY_DIR = BASE_DIR / "discovery"
OUTPUT_FILE = BASE_DIR / "ai_qa" / "cloudpos4u_genai_qa_prompt.md"


FILES_TO_INCLUDE = [
    DISCOVERY_DIR / "generated_api_inventory.md",
    DISCOVERY_DIR / "generated_frontend_routes.md",
    DISCOVERY_DIR / "generated_automation_backlog.md",
    DISCOVERY_DIR / "test_inventory.md",
    DISCOVERY_DIR / "workflows.md",
]


def read_file(path):
    if not path.exists():
        return f"\n\n## Missing file: {path.name}\n"

    return path.read_text(encoding="utf-8", errors="ignore")


def main():
    sections = []

    sections.append("""# CloudPOS4U GenAI QA Coverage Prompt

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
""")

    for file_path in FILES_TO_INCLUDE:
        sections.append(f"\n\n---\n\n# Source File: {file_path.name}\n\n")
        sections.append(read_file(file_path))

    OUTPUT_FILE.write_text("\n".join(sections), encoding="utf-8")

    print(f"Generated GenAI QA prompt: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()