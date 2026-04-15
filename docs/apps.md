# Microsoft App Registrations (Entra ID)

| Sovellus nimi                  | Application (client) ID                  | Käyttötarkoitus                       |          | Scope / Permissions                          | Status |
|-------------------------------|------------------------------------------|------------------------------------------|-------------|----------------------------------------------|--------|
| n8n		                | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx    | n8n OAuth2 (Graph API)                 | 2026-04-01 | User.Read, Mail.Send, Calendars.ReadWrite... | Active |
| qdrant			| yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy    | Forms → n8n trigger                    | 2026-04-01 | ...                                          | Active |
| xAi -api	                | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx    | n8n OAuth2 		                   | 2026-04-01 | 						 | Active |
| Wordpress rest-api            | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx    | n8n automaatiot 	                   | 2026-04-01 |						 | Active |



**Huomioita:**
- Secretit ovat tallennettu n8n Credentials -osioon (ei GitHubiin!)
- Certificate / Secret vanhenee: [päivämäärä]