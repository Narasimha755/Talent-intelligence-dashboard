const fs = require('fs');
const path = require('path');

const dir = 'C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard';
const html = fs.readFileSync(path.join(dir, 'index_source.html'), 'utf8');
const css = fs.readFileSync(path.join(dir, 'styles.css'), 'utf8');
const data = fs.readFileSync(path.join(dir, 'data.js'), 'utf8');
const app = fs.readFileSync(path.join(dir, 'app.js'), 'utf8');

const chartJs = fs.existsSync(path.join(dir, 'chart.min.js'))
  ? fs.readFileSync(path.join(dir, 'chart.min.js'), 'utf8')
  : '';
const lucideJs = fs.existsSync(path.join(dir, 'lucide.min.js'))
  ? fs.readFileSync(path.join(dir, 'lucide.min.js'), 'utf8')
  : '';

let standalone = html;

// Add cache busting and no-cache meta tags in <head>
const noCacheMeta = `
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
`;
standalone = standalone.replace('<meta name="viewport"', `${noCacheMeta}\n  <meta name="viewport"`);

// Inline CSS
standalone = standalone.replace(/<link\s+rel="stylesheet"\s+href="styles\.css[^"]*">/gi, () => `<style>\n${css}\n</style>`);

// Inline Chart.js & Lucide
if (chartJs) {
  standalone = standalone.replace(/<script\s+src="https:\/\/cdn\.jsdelivr\.net\/npm\/chart\.js"><\/script>/gi, () => `<script>\n${chartJs}\n</script>`);
}
if (lucideJs) {
  standalone = standalone.replace(/<script\s+src="https:\/\/unpkg\.com\/lucide@latest"><\/script>/gi, () => `<script>\n${lucideJs}\n</script>`);
}

// Inline Data.js & App.js (matches any ?v= query string)
standalone = standalone.replace(/<script\s+src="data\.js[^"]*"><\/script>/gi, () => `<script>\n${data}\n</script>`);
standalone = standalone.replace(/<script\s+src="app\.js[^"]*"><\/script>/gi, () => `<script>\n${app}\n</script>`);

fs.writeFileSync(path.join(dir, 'index_standalone.html'), standalone, 'utf8');
console.log('✅ index_standalone.html generated successfully! File size:', (standalone.length / 1024).toFixed(1), 'KB');

// Also write standalone content directly to index.html so GitHub Pages root URL is 100% self-contained!
fs.writeFileSync(path.join(dir, 'index.html'), standalone, 'utf8');
console.log('✅ index.html generated successfully as fully self-contained bundle! File size:', (standalone.length / 1024).toFixed(1), 'KB');
