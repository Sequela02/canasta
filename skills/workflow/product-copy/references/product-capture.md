# Product Capture

Use real product evidence for marketing whenever the operational client can render the story truthfully.

## Evidence Order

1. Real interface, real components, and sanitized demo data captured from the current client.
2. Real interface captured from a dedicated non-production demo tenant.
3. Faithful coded product simulation only when the real client cannot be run or the feature does not exist yet; label it as a concept and do not present it as a screenshot.
4. Diagram or typographic explanation when showing the interface would add noise or expose implementation detail.

Do not hand-build a dashboard-shaped illustration when a current product surface can provide stronger proof.

## Reproducible Capture Pattern

- Run the real application at a fixed local URL and viewport.
- Seed only boundary state such as local storage, cookies, device adapters, or permissions.
- Intercept network requests in Playwright and return deterministic, non-customer fixtures that satisfy current API contracts.
- Prefer routing/interception over source changes. If a desktop renderer needs a browser adapter or Vite config, create it at runtime and delete it in `finally`.
- Wait for the intended state, `document.fonts.ready`, and any chart rendering. Disable animation and caret rendering before the screenshot.
- Use stable locale, timezone, theme, viewport, and device scale. Avoid real current dates when they make the fixture expire.
- Remove development overlays and verify that no server, temporary config, credentials, customer data, or mock application remains after capture.
- Keep the runner and final optimized media; do not keep cloned application pages.

Treat capture fixtures as public marketing data. Use fictional names, IDs, amounts, titles, emails, and locations. Never derive them from production.

## Presentation

- Preserve readable interface detail. Crop to the feature being explained instead of shrinking an entire desktop into decoration.
- Build frames, perspective, backgrounds, shadows, masks, and export layouts locally first. Prefer HTML/CSS/SVG rendered by Playwright for responsive compositions and Sharp for deterministic raster processing.
- Use Canvas only when pixel-level procedural composition is genuinely simpler than HTML/CSS/SVG. Keep the composition source and command versioned.
- Prefer WebP or AVIF for web delivery unless alpha is required. Keep the source PNG only when it is the reproducible capture master.
- For UI with small text, use lossless WebP or PNG and verify source-to-rendered pixel density. Lossy photo defaults and persistent 3D transforms can make a high-resolution capture look soft.
- External mockup compositors are an exception for exploration, not part of the required pipeline. If one is used, upload sanitized assets only, record the export settings, and keep an owned uncomposited source.
- Alternative text should name the visible product state, not say “dashboard image.”

## Hybrid context plates

When the product needs physical or human context but no authorized photograph can perform that job, an openly synthetic or illustrated context plate may surround an authentic capture. Keep the screen blank during plate generation, capture the current product with fictional or approved data, and composite it locally with recorded geometry and checksums. Describe the result as mixed product evidence and editorial context; never imply that the setting, person, customer, or deployment is real. Keep direct state galleries focused on product evidence unless the context itself answers a distinct visitor question.

Verification: run the capture twice, compare the output state, inspect desktop and mobile crops, and confirm the script cleans temporary files and child processes after both success and failure.
