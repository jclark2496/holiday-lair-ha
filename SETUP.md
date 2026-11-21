# Holiday Lair setup

Tested by the author on a throwaway Home Assistant 2026.11.2 instance with demo and
template entities, with button-card 7.0.1, Mushroom 5.2.3, card-mod 4.2.1,
layout-card 2.4.7 and Kiosk Mode 15.0.0. It should work on 2026.10 and newer, but it
has not been tested on other versions or on a physical phone.

## 1. HACS prerequisites

In HACS > Frontend (or HACS search), install:

- [ ] **button-card** - [custom-cards/button-card](https://github.com/custom-cards/button-card)
- [ ] **Mushroom** - [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom)
- [ ] **card-mod** - [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod)
- [ ] **layout-card** - [thomasloven/lovelace-layout-card](https://github.com/thomasloven/lovelace-layout-card)
- [ ] **Kiosk Mode** - [NemesisRE/kiosk-mode](https://github.com/NemesisRE/kiosk-mode)

HACS adds each card as a dashboard resource. Refresh the browser (or clear the
Companion app frontend cache) after installing.

## 2. Theme

1. Copy `themes/holiday-pine.yaml` to `/config/themes/holiday-pine.yaml`.
2. Make sure `configuration.yaml` loads themes:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Restart Home Assistant, or run the `frontend.reload_themes` action.

Every view in the dashboard sets `theme: holiday-pine`, so you do not need to change
your profile theme. The theme is dark-only on purpose.

## 3. Art

Copy everything in `assets/` to `/config/www/holiday-lair/` (create the folder).
Files in `/config/www/` are served at `/local/`, so the dashboard loads them from
`/local/holiday-lair/...`. If you add `www/` for the first time, restart Home
Assistant once.

## 4. Create the dashboard

1. Settings > Dashboards > **Add dashboard** > "New dashboard from scratch".
2. Title `Holiday Lair`, URL **`holiday-lair`**.
3. Open it, then the pencil (edit) > three-dot menu > **Raw configuration editor**.
4. Replace everything with the contents of `dashboard.yaml` and save.

Using a different URL? Find and replace `/holiday-lair/` in `dashboard.yaml` with
your URL (for example `/my-dash/`) before pasting.

## 5. Replace the placeholders

Use find-and-replace in the raw editor (or your text editor) for each placeholder:

| Placeholder | Use your... |
|---|---|
| `weather.home` | weather entity |
| `alarm_control_panel.alarm` | alarm panel |
| `lock.front_door_lock`, `lock.back_door_lock` | door locks |
| `scene.cozy_evening`, `scene.holiday_party`, `scene.goodnight` | three scenes |
| `light.tree_lights` | holiday tree lights (light or light group) |
| `light.front_porch` | an outdoor light |
| `light.living_room_main`, `light.living_room_lamp`, `light.living_room_accent` | living room lights |
| `light.kitchen`, `light.kitchen_island`, `light.kitchen_counter` | kitchen lights |
| `media_player.speaker`, `media_player.speaker_2` | speakers |
| `climate.thermostat` | thermostat |

Don't have one of these? Delete that card (or point it at a similar entity). Rename
rooms and labels by editing the `name:` / `title:` values. Keep the alarm action
names (`alarm_control_panel.alarm_disarm` and friends): those are actions, not
entities. If your alarm needs a code, use the alarm's more-info dialog (long-press
a button) instead of the quick buttons.

## 6. Optional blueprints

Import from `blueprints/automation/holiday_lair/` (copy the folder to
`/config/blueprints/automation/holiday_lair/` and reload automations, or use
Settings > Automations > Blueprints > Import with the raw file URL):

- **Play a sound when the tree lights turn on**: pick a light, a speaker, your own
  sound, a volume and whether to play it as an announcement.
- **Holiday lights on/off schedule**: pick a light, on at sunset (with offset) or at
  a fixed time, an off time, and optionally an `input_boolean` that must be on.

**Bring your own sound clip.** No audio is included. Put a short clip you own or have
the rights to use in `/media` (it shows under "My media"), then select it in the
blueprint.

## 7. Kiosk mode and the escape hatch

The dashboard hides the header and sidebar (`kiosk_mode` at the top of
`dashboard.yaml`). To get them back:

- Use **Menu (gear) > Show standard navigation**, which opens
  `/holiday-lair/home?disable_km`, or
- add `?disable_km` to the dashboard URL yourself, for example
  `https://<your-home-assistant>/holiday-lair/home?disable_km`.

To turn kiosk mode off for good, delete the `kiosk_mode:` block.

## Troubleshooting

- **"Custom element doesn't exist: button-card"** (or mushroom/layout-card): the
  HACS card isn't installed or the resource didn't load. Reinstall, then hard-refresh
  (Companion app: Settings > Companion app > Debugging > Reset frontend cache).
- **Cards look unstyled or square**: card-mod is missing.
- **Views stack full-width instead of a centered phone column**: layout-card is
  missing.
- **Pictures don't show**: check the SVGs are in `/config/www/holiday-lair/` and open
  `/local/holiday-lair/hero-cabin.svg` in a browser.
- **Theme not applied / light text on light cards**: the `holiday-pine` theme isn't
  loaded. Check step 2 and Developer tools > Actions > `frontend.reload_themes`.
- **"Entity not available"**: a placeholder still needs replacing (step 5).
- **Stuck without a header**: add `?disable_km` to the URL (step 7).

## Contrast check

`tools/contrast.py` prints WCAG contrast ratios for the palette (all text pairs are
4.5:1 or better). On the test instance the Mushroom light-card labels measured
10.7:1 (`#F4F0E4` on `#103D2B`) with the browser in both light and dark mode.
