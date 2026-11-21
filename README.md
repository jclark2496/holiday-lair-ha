# Holiday Lair

A cozy, dark pine-green holiday dashboard for Home Assistant, designed for phones
(Companion app or a wall/kiosk tablet in portrait). It is a **layout, card and theme
template**: you bring your own devices and swap in your own entity IDs.

| Home | Living Room | Music |
|---|---|---|
| ![Home](docs/screenshot-home.png) | ![Living Room](docs/screenshot-living-room.png) | ![Music](docs/screenshot-music.png) |

*Screenshots are real renders of this dashboard on a throwaway Home Assistant test
instance with demo entities (iPhone-sized viewport).*

## Features

- Home view with a time-of-day greeting, a weather / alarm / locks status strip,
  scene buttons, a holiday tree-lights toggle, an Assist voice button and big
  navigation tiles
- Lights view with room subviews (Living Room, Kitchen) using Mushroom light cards
  with brightness sliders
- Security view: disarm / arm home / arm away buttons and door-lock tiles
- Music view: a media control card plus speaker shortcuts
- Climate view: the built-in thermostat card
- A dark-only **Holiday Pine** theme (text contrast checked against WCAG AA)
- Original hand-drawn SVG art (pines, a snowy cabin, string lights, stars, snow)
- Two optional automation blueprints: play your own sound when the tree lights
  turn on, and a holiday-lights on/off schedule
- Kiosk mode (no header or sidebar) with a documented way out (`?disable_km`)

## Prerequisites

Home Assistant 2026.10 or newer with [HACS](https://hacs.xyz/) and these frontend
cards (installed through HACS; nothing is bundled here):

- [button-card](https://github.com/custom-cards/button-card)
- [Mushroom](https://github.com/piitaya/lovelace-mushroom)
- [card-mod](https://github.com/thomasloven/lovelace-card-mod)
- [layout-card](https://github.com/thomasloven/lovelace-layout-card)
- [Kiosk Mode](https://github.com/NemesisRE/kiosk-mode)

## Quickstart

1. Install the five HACS cards above.
2. Copy `themes/holiday-pine.yaml` to `/config/themes/` and reload themes.
3. Copy the files in `assets/` to `/config/www/holiday-lair/`.
4. Create a new dashboard with the URL `holiday-lair`, open the raw configuration
   editor and paste `dashboard.yaml`.
5. Replace the placeholder entity IDs with your own.

Full steps, the placeholder list and troubleshooting are in [SETUP.md](SETUP.md).

## Bring your own sound clip

No audio ships with this project. If you want a sound when the tree lights come on,
put a short clip that you own (or have the rights to use) in `/media`, then pick it
in the "play a sound when the tree lights turn on" blueprint.

## Credits

The dashboard is built on the excellent community cards listed under Prerequisites.
They are separate projects with their own licenses and are not included in this
repository. The theme, art, blueprints and dashboard layout in this repository are
original and released under the MIT license.

## Note and disclaimer

Holiday Lair is a generic holiday theme. It is not affiliated with or endorsed by
Home Assistant, the Open Home Foundation, or any card author, film, book or brand.

Provided as is, without warranty. Review every action (alarm, locks, lights) before
using it on a real system; the security buttons send real arm/disarm commands.
