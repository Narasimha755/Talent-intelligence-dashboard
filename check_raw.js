const fs = require('fs');
const content = fs.readFileSync('C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard/parse_data.py', 'utf8');
const match = content.match(/raw_data = """([\s\S]*?)"""/);
if (match) {
  const rawLines = match[1].trim().split('\n');
  console.log('Total raw lines in parse_data.py:', rawLines.length);
  rawLines.forEach((line, i) => {
    const parts = line.split('\t');
    if (parts.length < 14) {
      console.log(`Line ${i+1} has only ${parts.length} tabs: [${line}]`);
    }
  });
}
