# BIS Mitra frontend

React + Vite prototype for an SIH 2026 project. It has two experiences: a home page and a continuous chat at `/chat`. Responses and contextual cards are **mock demonstrations**. The project is independent and is not an official BIS service.

## Run locally

```bash
npm install
npm run dev
```

Open the local URL printed by Vite. Run `npm run build` for a production bundle. The development server is configured to listen on all interfaces; Vite normally uses port 5173.

## Backend handoff

The integration point is `src/services/api.js`. Replace the body of `sendMessage(message, conversationHistory)` with a request to your Flask endpoint. It currently returns `{ text, cards }`, where cards are typed as `standard`, `journey`, or `lab`. The chat sends history as `{ role, content }` items, and `ChatMessage.jsx` renders the response. Set your API base URL through a `VITE_` environment variable if needed, for example `VITE_API_BASE_URL=http://localhost:5000`; do not put secrets in frontend variables.

## Mock content

- A welcome message and five editable prompt suggestions.
- Intent-based follow-ups for standards, certification, testing, documents and laboratories.
- Illustrative standard, laboratory and compliance journey cards, with no invented IS number, laboratory listing, verified test list or official approval.

The official BIS website link in the footer is real; contextual source links appear only when a future response supplies an actual `sourceUrl`.
