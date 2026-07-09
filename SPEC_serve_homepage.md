# Spec: Add a local-serve setup for homepage-clone

Goal: make it trivial to view `homepage-clone/` locally.

## Requirements

1. Add a `package.json` at the repo root with a `start` script that serves
   the `homepage-clone/` directory as static files on port 4173, using the
   `serve` package (e.g. `serve -l 4173 homepage-clone`).
2. Update `homepage-clone/README.md` (if needed) so the documented command
   matches the new `npm start` script.

## Out of scope

- Do not modify any files inside `homepage-clone/` other than the README
  line referenced above.
- Do not create git commits.
