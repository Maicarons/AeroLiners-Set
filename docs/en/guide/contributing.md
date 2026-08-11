# Contributing

Contributions to AeroLiners Set (and its documentation) are welcome — whether fixing graphics, adding models, translating, or improving docs.

## Reporting bugs

1. Open an Issue or Pull Request on the project's GitHub repository: <https://github.com/Maicarons/AeroLiners-Set>.
2. Check the **Issues** tab first to confirm the problem hasn't been reported.
3. Submit a **New Issue**, including as much as possible:
   - AeroLiners Set version
   - OpenTTD version
   - Steps to reproduce / bug details
   - Savegame and screenshots if necessary
   - If "it only appeared after a certain version update", note the **last good version** and the **first broken version** to help locate the change

## Submitting code

This repository (`Maicarons/AeroLiners-Set`) is an independent continuation of the upstream project:

- **Upstream**: <https://github.com/RvP93/WorldAirlinersSet>
- It is recommended to `git fetch upstream` and rebase before modifying, to avoid diverging too far from upstream.

General flow:

```bash
git checkout -b my-fix
# modify source / docs
git commit -m "Brief description of change"
git push origin my-fix
# Open a Pull Request on GitHub
```

::: warning Multiplayer compatibility
If you modify the source (even a single pixel), the compiled `.grf` will no longer be multiplayer-compatible with the official AeroLiners Set; different `grfcodec`/`nmlc` versions also change the checksum. Only replace it in "personal use" or "coordinated group" scenarios.
:::

## Improving this VitePress documentation

Docs live in `docs/`, managed with [VitePress](https://vitepress.dev/):

- Pages are `docs/*.md` and `docs/guide/*.md`; the English versions are under `docs/en/`.
- Site config is in `docs/.vitepress/config.js` (navigation, sidebar, footer, i18n locales).

Local preview:

```bash
npm run docs:dev      # dev server (hot reload)
npm run docs:build    # build static site to docs/.vitepress/dist
npm run docs:preview  # preview the build locally
```

> When running the Node build on this machine, if you hit an error from a sandbox-injected safe-delete shim, prefix the command with `NODE_OPTIONS=""` (see the note in [Building from Source](/guide/building)). A normal local build needs no such step.

## Types of contribution

| What you want to contribute | Where to go |
| --- | --- |
| Add / fix models or liveries | the corresponding directory under `src/gfx/`, see [Liveries & Graphics](/guide/liveries) |
| Translate interface text | `lang/*.lng`, see [Translating](/guide/translating) |
| Adjust cost / range parameters | `src/header.pnml`, `src/basecost.pnml` |
| Improve documentation | Markdown files under `docs/` |

Back: [Translating →](/guide/translating) ｜ Next: [Changelog →](/guide/changelog)
