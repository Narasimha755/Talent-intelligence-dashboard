const fs = require('fs');
const path = require('path');

const dir = 'C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard';
const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
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
standalone = standalone.replace('<link rel="stylesheet" href="styles.css">', () => `<style>\n${css}\n</style>`);

if (chartJs) {
  standalone = standalone.replace('<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>', () => `<script>\n${chartJs}\n</script>`);
}
if (lucideJs) {
  standalone = standalone.replace('<script src="https://unpkg.com/lucide@latest"></script>', () => `<script>\n${lucideJs}\n</script>`);
}

standalone = standalone.replace('<script src="data.js"></script>', () => `<script>\n${data}\n</script>`);
standalone = standalone.replace('<script src="app.js"></script>', () => `<script>\n${app}\n</script>`);

fs.writeFileSync(path.join(dir, 'index_standalone.html'), standalone, 'utf8');
console.log('✅ index_standalone.html generated successfully! File size:', (standalone.length / 1024).toFixed(1), 'KB');
