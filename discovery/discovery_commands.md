# CloudPOS4U Discovery Commands

Use these commands to discover frontend routes and backend API endpoints.

## Frontend Route Discovery

Run inside the CloudPOS4U frontend project:

```bash
grep -R "path=" src \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  > discovery_frontend_routes.txt

grep -R "Route" src \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  >> discovery_frontend_routes.txt

grep -R "navigate(" src \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  >> discovery_frontend_routes.txt

grep -R "href=" src \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  >> discovery_frontend_routes.txt


Backend API Discovery

Run inside the CloudPOS4U backend project:

grep -R "router.get\|router.post\|router.put\|router.delete\|app.use" . \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  > discovery_api_routes.txt