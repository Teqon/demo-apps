# Design QA — Video section

- Source visual truth: `/var/folders/bc/17p9h13s3v9cdtj1k38s8kjc0000gn/T/codex-clipboard-3fd537ee-64ad-4198-beb9-1e4a48a27483.png`
- Implementation screenshot: `/Users/rich/Documents/GitHub/demo-apps/AmiTaPreparaV2/tmp/video-section-final.png`
- Desktop viewport: 1280 × 720
- Mobile viewport: 390 × 844
- State: video section with settled reveal animations

## Full-view comparison evidence

The implementation uses the same three featured videos, order, 16:9 thumbnail treatment, centered play affordance, white background, three-column desktop composition, and centered uppercase titles shown in the reference. The existing site header and brand hierarchy are intentionally retained.

## Focused-region comparison evidence

The video section was inspected directly at desktop and mobile sizes. All three YouTube thumbnails loaded at 1280 × 720 intrinsic resolution. The desktop grid shows three equal-width cards; mobile stacks them into one column without horizontal overflow. The second title wraps cleanly to two lines, matching the reference behavior.

## Required fidelity surfaces

- Fonts and typography: existing Ami Ta Prepará type system retained; video titles use the established heading family and weight with reference-aligned uppercase treatment.
- Spacing and layout rhythm: three equal desktop columns, consistent thumbnail proportions, centered titles, and responsive one-column mobile layout.
- Colors and visual tokens: existing black, white, and yellow site palette retained.
- Image quality and asset fidelity: real YouTube max-resolution thumbnails are used; no placeholder images remain in this section.
- Copy and content: titles and video IDs match the supplied playlist; section placeholder text was replaced with relevant Papiamentu copy.

## Interaction and technical checks

- Each featured card links to its matching YouTube video within the playlist.
- “Mira tur videonan” links to the full playlist.
- Both Facebook links use the supplied Facebook URL.
- PAP/NL/EN UI has been removed.
- No horizontal overflow at desktop or mobile widths.
- No browser console warnings or errors were observed.

## Comparison history

- P2: Lazy-loaded mobile thumbnails initially allowed an unloaded card to collapse. Fixed by making the thumbnail wrapper a block-level element with a fixed 16:9 aspect ratio. Post-fix evidence confirms all three mobile cards retain their intended height.
- P2: Initial YouTube `hqdefault` images contained lower-resolution letterboxing. Replaced with available 1280 × 720 `maxresdefault` thumbnails. Post-fix evidence confirms all three assets load at full 16:9 resolution.

## Follow-up polish

- P3: The government reference includes carousel arrows. The implementation instead shows the three featured videos together and provides a direct full-playlist link; this avoids adding carousel complexity while preserving access to all five videos.

final result: passed
