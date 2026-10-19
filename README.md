# Domtek website redesign

Responsive static website retaining the existing product content, imagery, specifications, colour charts and downloadable resources.

## Local preview

Requires Python 3. No package installation is needed.

```sh
python3 -m http.server 8765 --directory dist
```

Open http://localhost:8765/.

## Structure

- `dist/`: ready-to-host HTML pages, CSS, JavaScript, images and dealer data.
- `build.py`: regenerates HTML pages from the content snapshot and shared templates.
- `dist/pages.json`: captured page content used by the generator.
- `assets.json`: original media URLs mapped to local assets.
- `navigation.json`: navigation content snapshot.
- `dealers-all.json`: public dealer directory snapshot from 19 October 2026.
- `check.py`: checks generated pages for missing local link and media targets.

## Rebuild and check

```sh
python3 build.py
python3 check.py
node --check dist/app.js
```

Edit shared templates in `build.py`, styles in `dist/style.css`, and browser interactions in `dist/app.js`. Rebuild after changing templates or page content. The rebuild preserves the stylesheet and JavaScript.

## Deploy

Publish the contents of `dist/` to a static host supporting directory `index.html` files. No server runtime or secrets are required.

## Integration notes

- Contact opens an email draft to `info@domtek.ca`. A server-side submission service is not connected.
- Dealer search filters the captured 79-dealer directory by name, city, province, postal code or address. It does not perform a live radius search.
- PDF downloads reference the existing Domtek website. Embedded videos use their existing services.
- The existing client website and domain were not changed.
