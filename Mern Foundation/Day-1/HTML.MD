## HTML & DOM Essentials Cheat Sheet (Day 1)
Purpose: Fast, practical reference. Focus on core tags, structure, semantics, accessibility, and DOM scripting anchors.

### 1. Minimal Page Skeleton
```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<title>Page Title</title>
		<meta name="description" content="Short description for SEO" />
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<header>Site Header / Nav</header>
		<main>
			<h1>Main Heading</h1>
			<p>Content...</p>
		</main>
		<footer>&copy; 2025</footer>
		<script src="app.js" defer></script>
	</body>
</html>
```
Key: `<!DOCTYPE html>` standards mode, `lang`, responsive meta, semantic `header/main/footer`.

### 2. Semantics Core (Use Instead of Generic <div>)
Role | Tag | Purpose
-----|-----|--------
Top branding / nav | `<header>` | Intro / branding / masthead
Navigation links | `<nav>` | Major site navigation
Main content | `<main>` | Unique per page (1 per doc)
Standalone block | `<section>` | Thematic grouping (with heading)
Self-contained item | `<article>` | Independent distributable content
Sidebar / complementary | `<aside>` | Tangential info (ads, related)
Footer | `<footer>` | Page or section footer
Inline emphasis | `<em>` | Stress emphasis (screen readers)
Strong importance | `<strong>` | High importance
Figure + caption | `<figure>/<figcaption>` | Media with caption
Time/date | `<time>` | Machine-readable datetime via `datetime` attr

### 3. Text & Inline Essentials
Tag | Use | Example
----|-----|--------
`<h1>`..`<h6>` | Hierarchy (one `<h1>`) | `<h2>Subsection</h2>`
`<p>` | Paragraph | `<p>Paragraph text.</p>`
`<a>` | Link | `<a href="/about" rel="noopener">About</a>`
`<span>` | Inline wrapper (no semantics) | `<span class="badge">New</span>`
`<code>` | Code snippet | `<code>let x=1;</code>`
`<pre>` | Preformatted block | `<pre>{\n  "a":1\n}</pre>`
`<br>` | Line break (sparingly) | poetry / addresses
`<hr>` | Thematic break | Section separation

### 4. Lists & Tables
Lists:
```html
<ul>
	<li>Milk</li>
	<li>Bread</li>
</ul>
<ol start="3" reversed>
	<li>Third</li>
	<li>Second</li>
</ol>
<dl>
	<dt>API</dt><dd>Application Programming Interface</dd>
</dl>
```
Tables (semantic):
```html
<table>
	<caption>Sales Q1</caption>
	<thead><tr><th scope="col">Product</th><th scope="col">Units</th></tr></thead>
	<tbody><tr><th scope="row">Widget</th><td>120</td></tr></tbody>
	<tfoot><tr><td colspan="2">Updated weekly</td></tr></tfoot>
</table>
```
Use `<th scope="col|row">` for accessibility.

### 5. Forms (Modern Basics)
```html
<form action="/subscribe" method="post" novalidate>
	<label for="email">Email</label>
	<input id="email" name="email" type="email" required placeholder="you@example.com" />
	<fieldset>
		<legend>Preferences</legend>
		<label><input type="checkbox" name="daily" /> Daily Updates</label>
		<label><input type="checkbox" name="weekly" /> Weekly Digest</label>
	</fieldset>
	<button type="submit">Subscribe</button>
</form>
```
Key attributes: `required`, `pattern`, `min`, `max`, `step`, `disabled`, `aria-invalid`.

### 6. Media & Assets
Images:
```html
<img src="hero.jpg" alt="Team collaborating" width="600" height="400" loading="lazy" />
```
Responsive `<picture>`:
```html
<picture>
	<source srcset="hero.avif" type="image/avif" />
	<source srcset="hero.webp" type="image/webp" />
	<img src="hero.jpg" alt="Hero banner" />
</picture>
```
Video:
```html
<video controls width="400" poster="thumb.jpg">
	<source src="clip.mp4" type="video/mp4" />
	<p>Your browser does not support video.</p>
</video>
```

### 7. Meta & SEO Essentials
```html
<meta name="description" content="Concise description ~155 chars" />
<meta property="og:title" content="Page Title" />
<meta property="og:type" content="website" />
<link rel="canonical" href="https://example.com/page" />
```
Favicons: multiple sizes with `<link rel="icon" ...>`.

### 8. Accessibility (a11y) Quick Wins
- Always provide meaningful `alt` text or `alt=""` for decorative images.
- Use headings in order (no jumping from `<h1>` to `<h4>`).
- Form inputs: pair `<label for>` with matching `id`.
- Color contrast: meet WCAG AA (contrast ratio ≥ 4.5:1 normal text).
- Keyboard: ensure focusable interactive elements (use semantic `<button>` not `<div>` clickable).
- Landmarks: header / nav / main / footer / aside.
- ARIA: Use only when no native semantic element fits.

### 9. Performance Snippets
- Put critical CSS inline (small) or `<link rel="preload">` large fonts.
- Defer non-critical scripts: `<script src="app.js" defer></script>`.
- Lazy load below-the-fold images: `loading="lazy"`.
- Minimize DOM depth; avoid excessive nesting.
- Use `rel="noopener"` on external target `_blank` links.

### 10. DOM Selection (JS Hooks)
Prefer class/data attributes for JS hooks:
```html
<button class="btn" data-action="toggle" id="togglePanel">Toggle</button>
<div id="panel" hidden>Panel Content</div>
```
JS examples:
```js
const btn = document.querySelector('[data-action="toggle"]');
btn.addEventListener('click', () => {
	const panel = document.getElementById('panel');
	panel.hidden = !panel.hidden;
});
```
Selection APIs:
- `getElementById('id')` (fast)
- `querySelector('.class')` first match
- `querySelectorAll('ul > li')` NodeList
- `closest(selector)` climb ancestors
- `dataset` for `data-*` attributes

### 11. DOM Manipulation Patterns
```js
// Create & append
const li = document.createElement('li');
li.textContent = 'Item';
document.querySelector('ul').append(li);

// Fragment for batch insert
const frag = document.createDocumentFragment();
for(let i=0;i<3;i++){ const li=document.createElement('li'); li.textContent='Row '+i; frag.append(li);} 
document.querySelector('ul').append(frag);

// Class & attribute
li.classList.add('highlight');
li.setAttribute('role','presentation');

// Delegation
document.addEventListener('click', e => {
	if(e.target.matches('[data-action="remove"]')){
		e.target.closest('li').remove();
	}
});
```
Avoid layout thrash: read DOM values (`offsetWidth`) before batching writes.

### 12. Forms & Validation (JS)
```js
const form = document.querySelector('form');
form.addEventListener('submit', e => {
	if(!form.checkValidity()){
		e.preventDefault();
		form.querySelectorAll(':invalid')[0].focus();
	}
});
```
Custom validity:
```js
emailInput.setCustomValidity('');
if(!/^[^@]+@[^@]+\.[^@]+$/.test(emailInput.value)){
	emailInput.setCustomValidity('Invalid email');
}
```

### 13. Attributes vs Properties
Attribute: initial HTML value (`element.getAttribute('value')`).  
Property: current live value (`element.value`).  
Sync occurs differently per element (important for forms).

### 14. Data Attributes
```html
<div data-user-id="42" data-plan="pro"></div>
```
JS: `el.dataset.userId === '42'`.

### 15. Common Pitfalls & Fixes
Pitfall | Issue | Fix
--------|-------|----
Using `<div>` for button | No semantics, inaccessible | Use `<button>`
Missing alt text | Screen reader ambiguity | Provide descriptive alt
Inline styles everywhere | Hard to maintain | External CSS / utility classes
Blocking render with large script | Slow FMP | Use `defer` / code split
Open external links w/out noopener | Security risk | Add `rel="noopener noreferrer"`

### 16. Key HTML5 Input Types
`email`, `url`, `number`, `date`, `datetime-local`, `range`, `color`, `file`, `checkbox`, `radio`, `search`, `password`.
Use built-in validation before custom JS.

### 17. Accessibility Testing Quick Pass
1. Tab through page – can you reach all interactive elements?  
2. Use browser dev tools accessibility tree – headings logical?  
3. Disable CSS – is content order still sensible?  
4. Run Lighthouse a11y audit – address high-impact items.  

### 18. SEO & Sharing Essentials
- Unique `<title>` per page
- One `<h1>` describing main content
- Descriptive link text (avoid “click here”)
- Structured data (JSON-LD) as needed
- Open Graph & Twitter card meta tags

### 19. Minimal Progressive Enhancement Pattern
HTML first (forms submit normally) → add JS enhancement (`fetch`) → fallback safe when JS off.

### 20. Checklist Before Ship
Area | Check
-----|------
Structure | Valid nested tags, one main landmark
Accessibility | Labels, alt, focus order
Performance | Defer scripts, lazy images
SEO | Title, meta description, canonical
Security | rel noopener, no inline event handlers (prefer addEventListener)

### 21. Practice Prompts
1. Build a semantic blog post (header, article, aside, footer).  
2. Create a form with email + password + show/hide toggle.  
3. Implement dynamic list add/remove with delegation.  
4. Convert a `<div>`-heavy layout into semantic tags.  
5. Add responsive image using `<picture>` with avif/webp fallback.

### 22. Reflection Prompts
1. One semantic tag you misused before?  
2. Largest a11y improvement you can still make?  
3. What will you standardize in every HTML head section now?

End of HTML & DOM essentials cheat sheet.
