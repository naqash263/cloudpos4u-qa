import json
import re
from pathlib import Path
from urllib.parse import urlparse


BASE_DIR = Path(__file__).resolve().parents[1]
DISCOVERY_DIR = BASE_DIR / "discovery"

HAR_FILE = DISCOVERY_DIR / "cloudpos4u_network.har"
API_ROUTES_FILE = DISCOVERY_DIR / "discovery_api_routes.txt"
FRONTEND_ROUTES_FILE = DISCOVERY_DIR / "discovery_frontend_routes.txt"

OUTPUT_API_MD = DISCOVERY_DIR / "generated_api_inventory.md"
OUTPUT_FRONTEND_MD = DISCOVERY_DIR / "generated_frontend_routes.md"
OUTPUT_BACKLOG_MD = DISCOVERY_DIR / "generated_automation_backlog.md"


def extract_from_har():
    endpoints = {}

    if not HAR_FILE.exists():
        print(f"Missing HAR file: {HAR_FILE}")
        return endpoints

    with open(HAR_FILE, "r", encoding="utf-8") as file:
        har_data = json.load(file)

    entries = har_data.get("log", {}).get("entries", [])

    for entry in entries:
        request = entry.get("request", {})
        response = entry.get("response", {})

        method = request.get("method")
        url = request.get("url", "")
        status = response.get("status")

        parsed = urlparse(url)
        path = parsed.path

        if "/api/" not in path:
            continue

        key = f"{method} {path}"

        request_body = ""
        post_data = request.get("postData", {})
        if post_data:
            request_body = post_data.get("text", "")

        endpoints[key] = {
            "method": method,
            "path": path,
            "status": status,
            "url": url,
            "request_body": request_body,
        }

    return endpoints


def extract_backend_routes():
    routes = set()

    if not API_ROUTES_FILE.exists():
        print(f"Missing API routes file: {API_ROUTES_FILE}")
        return routes

    content = API_ROUTES_FILE.read_text(encoding="utf-8", errors="ignore")

    patterns = [
        r"router\.(get|post|put|patch|delete)\(['\"]([^'\"]+)['\"]",
        r"app\.use\(['\"]([^'\"]+)['\"]",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if isinstance(match, tuple):
                if len(match) == 2:
                    method, path = match
                    routes.add(f"{method.upper()} {path}")
                elif len(match) == 1:
                    routes.add(f"USE {match[0]}")
            else:
                routes.add(f"USE {match}")

    return routes


def extract_frontend_routes():
    routes = set()

    if not FRONTEND_ROUTES_FILE.exists():
        print(f"Missing frontend routes file: {FRONTEND_ROUTES_FILE}")
        return routes

    content = FRONTEND_ROUTES_FILE.read_text(encoding="utf-8", errors="ignore")

    patterns = [
        r'path=["\']([^"\']+)["\']',
        r'navigate\(["\']([^"\']+)["\']',
        r'href=["\']([^"\']+)["\']',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, content)
        for route in matches:
            if route.startswith("/") and not route.startswith("//"):
                routes.add(route)

    return sorted(routes)


def guess_module(path):
    lowered = path.lower()

    if "login" in lowered or "auth" in lowered or "user" in lowered:
        return "Authentication / Users"
    if "dish" in lowered or "menu" in lowered or "category" in lowered:
        return "Menu / Dishes"
    if "order" in lowered:
        return "Orders"
    if "table" in lowered:
        return "Tables"
    if "customer" in lowered:
        return "Customers"
    if "inventory" in lowered or "stock" in lowered:
        return "Inventory"
    if "payment" in lowered:
        return "Payments"
    if "report" in lowered or "dashboard" in lowered:
        return "Reports / Dashboard"
    if "branch" in lowered:
        return "Branches"

    return "To classify"


def guess_priority(method, path):
    lowered = path.lower()

    if "login" in lowered or "order" in lowered:
        return "Critical"
    if "dish" in lowered or "menu" in lowered or "inventory" in lowered or "table" in lowered:
        return "High"
    if method in ["POST", "PUT", "PATCH", "DELETE"]:
        return "High"

    return "Medium"


def write_api_inventory(har_endpoints, backend_routes):
    lines = [
        "# Generated CloudPOS4U API Inventory",
        "",
        "This file was generated from HAR and backend route discovery output.",
        "",
        "| Method | Endpoint | Module | Last Seen Status | Priority | Source | Suggested Automation |",
        "|---|---|---|---|---|---|---|",
    ]

    seen = set()

    for key, data in sorted(har_endpoints.items()):
        method = data["method"]
        path = data["path"]
        module = guess_module(path)
        priority = guess_priority(method, path)
        status = data["status"]

        automation = "API test + negative test"
        if method == "GET":
            automation = "API test + schema validation"
        if "order" in path.lower():
            automation = "API test + DB validation + performance test"

        lines.append(
            f"| {method} | {path} | {module} | {status} | {priority} | HAR | {automation} |"
        )
        seen.add(f"{method} {path}")

    for route in sorted(backend_routes):
        if route in seen:
            continue

        parts = route.split(" ", 1)
        method = parts[0]
        path = parts[1] if len(parts) > 1 else ""

        module = guess_module(path)
        priority = guess_priority(method, path)

        lines.append(
            f"| {method} | {path} | {module} | Not seen in HAR | {priority} | Backend routes | To review |"
        )

    OUTPUT_API_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {OUTPUT_API_MD}")


def write_frontend_inventory(frontend_routes):
    lines = [
        "# Generated CloudPOS4U Frontend Route Inventory",
        "",
        "This file was generated from frontend route discovery output.",
        "",
        "| Route | Module Guess | Priority | Suggested UI Automation |",
        "|---|---|---|---|",
    ]

    for route in frontend_routes:
        module = guess_module(route)
        priority = "Critical" if route in ["/auth", "/menu"] else "High"
        automation = "Smoke test"
        if "order" in route.lower() or route == "/menu":
            automation = "End-to-end business flow"
        elif "login" in route.lower() or "auth" in route.lower():
            automation = "Authentication validation"

        lines.append(
            f"| {route} | {module} | {priority} | {automation} |"
        )

    OUTPUT_FRONTEND_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {OUTPUT_FRONTEND_MD}")


def write_automation_backlog(har_endpoints, frontend_routes):
    lines = [
        "# Generated CloudPOS4U Automation Backlog",
        "",
        "This backlog was generated from discovered APIs and frontend routes.",
        "",
        "| ID | Area | Scenario | Tool | Priority | Status |",
        "|---|---|---|---|---|---|",
    ]

    counter = 1

    for key, data in sorted(har_endpoints.items()):
        method = data["method"]
        path = data["path"]
        priority = guess_priority(method, path)

        lines.append(
            f"| API-{counter:03d} | API | Validate {method} {path} success response | Pytest Requests / Postman | {priority} | Pending review |"
        )
        counter += 1

        if method in ["POST", "PUT", "PATCH", "DELETE"]:
            lines.append(
                f"| API-{counter:03d} | API Negative | Validate unauthorized/invalid payload for {method} {path} | Pytest Requests | {priority} | Pending review |"
            )
            counter += 1

    ui_counter = 1

    for route in frontend_routes:
        priority = "Critical" if route in ["/auth", "/menu"] else "High"
        lines.append(
            f"| UI-{ui_counter:03d} | UI | Validate page load and core action for {route} | Selenium Pytest | {priority} | Pending review |"
        )
        ui_counter += 1

    OUTPUT_BACKLOG_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {OUTPUT_BACKLOG_MD}")


def main():
    har_endpoints = extract_from_har()
    backend_routes = extract_backend_routes()
    frontend_routes = extract_frontend_routes()

    print(f"HAR API endpoints found: {len(har_endpoints)}")
    print(f"Backend routes found: {len(backend_routes)}")
    print(f"Frontend routes found: {len(frontend_routes)}")

    write_api_inventory(har_endpoints, backend_routes)
    write_frontend_inventory(frontend_routes)
    write_automation_backlog(har_endpoints, frontend_routes)


if __name__ == "__main__":
    main()