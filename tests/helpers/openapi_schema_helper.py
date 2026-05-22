import yaml
from pathlib import Path


OPENAPI_FILE = Path("contracts/openapi/cloudpos4u.openapi.yaml")


class OpenAPISchemaHelper:

    @staticmethod
    def load_spec():
        with open(OPENAPI_FILE, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    @staticmethod
    def get_component_schema(schema_name):
        spec = OpenAPISchemaHelper.load_spec()
        return spec["components"]["schemas"][schema_name]