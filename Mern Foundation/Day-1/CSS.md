## CSS Essentials Cheat Sheet (Day 1)
Purpose: High–signal reference for core layout, styling, responsiveness, performance, and maintainability.

### 1. Cascade & Specificity
Specificity order (highest → lowest): inline style (1000) > id (#) (100) > class / attr / pseudo-class (.btn, [x], :hover) (10) > element (div) (1) > universal (*) (0). Later equal‑specificity wins. Avoid !important (nukes cascade).
```
/* Debug specificity */
button.primary {}      /* 1 element + 1 class = 11 */
#cta.primary {}        /* 100 + 10 = 110 */
```
Rule: Increase specificity only intentionally; prefer classes.

### 2. Box Model
Content + padding + border + margin. Use `box-sizing: border-box;` globally to include padding/border in declared width/height.
```css
*,*::before,*::after { box-sizing: border-box; }
```

### 3. Display Values
Common: `block`, `inline`, `inline-block`, `flex`, `grid`, `none`, `contents`.  
`inline` ignores width/height; `inline-block` allows them; `flex` for 1‑D alignment; `grid` for 2‑D.

### 4. Positioning & Flow
`static` (default), `relative` (offset w/out removing space), `absolute` (removed; positioned to nearest positioned ancestor), `fixed` (viewport), `sticky` (hybrid).  
Stacking: z-index works only on positioned elements (creates stacking contexts under certain properties like transform).

### 5. Flexbox (1‑D Layout)
Container props: `display:flex; flex-direction: row|column; justify-content` (main axis), `align-items` (cross), `flex-wrap`.  
Item props: `flex: grow shrink basis; align-self`.  
Centering: `display:flex; justify-content:center; align-items:center;`.
```css
.row { display:flex; gap:1rem; }
.grow { flex:1 1 0; }
```

### 6. CSS Grid (2‑D Layout)
```css
.grid { display:grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap:1rem; }
.hero { grid-column: 1 / -1; }
```
Named areas:
```css
.layout { display:grid; grid-template:
	"header header" 60px
	"nav    main" 1fr
	"footer footer" 40px / 200px 1fr; }
.layout > header { grid-area: header; }
```

### 7. Units & Sizing
Relative: `em` (based on font-size), `rem` (root), `%` (parent), `vh/vw` viewport.  
Use `rem` for scalable typography; clamp fluid size:
```css
html { font-size: 16px; }
h1 { font-size: clamp(1.8rem, 2vw + 1rem, 3rem); }
```

### 8. Colors & Variables
Prefer HSL for manipulation.
```css
:root {
	--color-bg:#0f1115;
	--color-accent:hsl(280 80% 60%);
	--radius: .5rem;
}
button { background:var(--color-accent); border-radius:var(--radius); }
button:hover { filter:brightness(1.1); }
```
Dark mode:
```css
@media (prefers-color-scheme: dark){ body { background:#0f1115; color:#eee; } }
```

### 9. Typography Essentials
Line length: aim 45–75 characters.  
Line height: ~1.4–1.6 paragraph text.  
Font loading: `font-display: swap` in @font-face.  
```css
body { font: 400 1rem/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
```

### 10. Spacing System
Define scale: 4 or 8 pixel base.
```css
:root { --space-1: .25rem; --space-2:.5rem; --space-3:1rem; --space-4:1.5rem; }
.stack > * + * { margin-top: var(--space-3); }
```

### 11. Responsive Design
Mobile-first: write base styles, add min-width breakpoints.
```css
@media (min-width: 640px){ .nav { display:flex; } }
@media (min-width: 1024px){ .sidebar { display:block; } }
```
Container queries (supported modern browsers):
```css
@container (min-width: 500px){ .card { flex-direction: row; } }
```

### 12. Pseudo-Classes & Elements
Pseudo-classes: `:hover`, `:focus-visible`, `:active`, `:disabled`, `:nth-child(n)`, `:not()`, `:is()`, `:has()` (parent querying).  
Pseudo-elements: `::before`, `::after` (need `content:""`), `::marker`, `::selection`.
```css
button:focus-visible { outline:2px solid var(--color-accent); outline-offset:2px; }
li::marker { color: var(--color-accent); }
```

### 13. Transitions & Animations
```css
.btn { transition: background-color .25s, transform .25s; }
.btn:hover { transform: translateY(-2px); }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
.fade { animation: fadeIn .4s ease-out; }
```
Performance: animate `transform` & `opacity` for GPU-friendly changes.

### 14. Layout Patterns Quick Ref
Pattern | CSS
-------|----
Centered fixed width | `.wrap{width:min(100%, 70ch); margin-inline:auto;}`
Auto-spacing vertical list | `.stack > * + * { margin-top: var(--space-3); }`
Flex gap columns | `.cols { display:flex; gap:1rem; flex-wrap:wrap; }`
Holy Grail layout | grid with header, footer, nav fixed, main fluid

### 15. Layering & Z-Index
New stacking contexts created by: position + z-index, `opacity<1`, `transform`, `filter`, `isolation:isolate`, `will-change`. Debug by avoiding large arbitrary z-index numbers; keep a scale (e.g., 10, 100, 1000 for overlays/modals/toasts).

### 16. Images & Object Fit
```css
.cover-img { width:100%; height:300px; object-fit:cover; }
```
Use `aspect-ratio` for placeholders:
```css
.thumb { aspect-ratio:16/9; background:#222; }
```

### 17. Modern Features
- `:has()` parent selection
- `clamp(min, ideal, max)` fluid sizing
- `aspect-ratio: w / h`
- `@supports (display: grid){ ... }` feature queries
- `color-mix(in srgb, red 40%, blue)` (emerging support)

### 18. CSS Architecture
Naming: BEM (`.card__title`, `.card--featured`).  
Layers (if using cascade layers):
```css
@layer reset, base, components, utilities;
@layer reset { * { margin:0; padding:0; } }
@layer base { body { font-family: system-ui; } }
@layer components { .card { padding:1rem; background:#222; } }
@layer utilities { .mt-4 { margin-top:1rem; } }
```
Keep components encapsulated; use utility classes for spacing exceptions.

### 19. Accessibility & Focus
Never remove focus outlines without replacement. Provide color + shape contrast.
```css
:focus-visible { outline:2px solid var(--color-accent); outline-offset:2px; }
```
Reduced motion respect:
```css
@media (prefers-reduced-motion:reduce){ * { animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; } }
```

### 20. Performance Tips
- Combine / minimize reflows; batch DOM writes.
- Avoid large shadow DOM / deep selectors (keep specificity low).
- Use `content-visibility:auto;` for below-fold heavy sections.
- Limit web fonts; subset & preload (`<link rel="preload" as="font" ...>`).
- Use `will-change` sparingly (only before animation).

### 21. Debugging Tools
Browser DevTools: Layout (grid/flex overlay), Performance panel, Lighthouse, Contrast checker, Animations inspector.  
Add temporary outline:
```css
* { outline:1px solid rgba(255,0,0,.05); }
```

### 22. Common Pitfalls & Fixes
Pitfall | Cause | Fix
--------|-------|----
Overflow scrollbars | No width constraints | Use `max-width` wrappers
Text overflow ellipses failing | Missing constraints | Add `white-space:nowrap; overflow:hidden; text-overflow:ellipsis;`
Flex items squished | No `min-width` | Set `min-width:0` on flex children (for overflowing text)
Images causing layout shift | No dimensions | Add `width`/`height` or `aspect-ratio`
z-index not working | New stacking context ancestor | Remove transform / adjust context

### 23. Utility Class Examples
```css
.hidden { display:none !important; }
.sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; border:0; }
.text-center { text-align:center; }
.flex { display:flex; }
.grid { display:grid; }
.gap-2 { gap:.5rem; }
```

### 24. Transitions Cheat Table
Property | Animate? | Notes
---------|----------|------
opacity | Yes | Cheap
transform | Yes | GPU friendly
color/background-color | Yes | Repaint only
height/width | Caution | Might trigger layout; consider transform scale
box-shadow | Costly | Avoid heavy blur

### 25. Media Query Reference
Breakpoint strategy (example):
```css
@media (min-width:480px){ /* phones+ */ }
@media (min-width:768px){ /* tablets */ }
@media (min-width:1024px){ /* small desktops */ }
@media (min-width:1280px){ /* large desktops */ }
```
Avoid device-specific; focus on design breakpoints.

### 26. Example Component (Card)
```css
.card { background:#1e2228; border:1px solid #2b3037; padding:1rem; border-radius:.75rem; display:flex; flex-direction:column; gap:.75rem; }
.card--highlight { border-color: var(--color-accent); box-shadow:0 0 0 2px color-mix(in srgb, var(--color-accent) 40%, transparent); }
.card__title { font-size:1.125rem; line-height:1.3; }
.card__meta { font-size:.75rem; opacity:.7; }
.card__cta { align-self:flex-start; }
```

### 27. Refactoring Checklist
- Duplicate colors? Extract variables.
- Repeated spacing? Create scale tokens.
- Long selectors? Replace with class.
- Many overrides? Simplify source order / layers.
- !important usage? Remove via specificity planning.

### 28. Practice Prompts
1. Build a responsive 3→2→1 column grid using `auto-fit` + `minmax`.  
2. Create fluid typography using `clamp` for headings.  
3. Implement a skeleton loader (animated gradient).  
4. Build dark mode toggle switching a root class.  
5. Convert legacy float layout to flex and grid.

### 29. Reflection Prompts
1. Which layout method (flex vs grid) did you overuse?  
2. One variable you can introduce to reduce duplication?  
3. Did you rely on pixel units where relative would scale better?

End of CSS essentials cheat sheet.
