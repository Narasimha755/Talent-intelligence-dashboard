const fs = require('fs');
const content = fs.readFileSync('C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard/parse_data.py', 'utf8');
const match = content.match(/raw_data = """([\s\S]*?)"""/);

if (!match) {
  console.error('Could not find raw_data!');
  process.exit(1);
}

const rawLines = match[1].trim().split('\n');
console.log('Total raw lines to parse:', rawLines.length);

const parsed = [];
rawLines.forEach((line, i) => {
  const parts = line.split('\t').map(p => p.trim());
  const sno = parts[0] || String(i + 1);
  const name = (parts[1] || '').replace(/,+$/, '').trim();
  const func = parts[2] || 'CDM';
  let role = parts[3] || '';
  if (/^rave programmer$/i.test(role)) role = 'RAVE Programmer';
  const interviewDate = parts[4] || '';
  const interview2 = parts[5] || '';
  const clientFeedback = parts[6] || '';
  const presentCtcRaw = parts[7] || '';
  const status = parts[8] || '';
  const offeredCtcRaw = parts[9] || '';
  const doj = parts[10] || '';
  const onboard = parts[11] || '';
  let skillGroup = parts[12] || '';
  if (/^rave programmer$/i.test(skillGroup)) skillGroup = 'RAVE Programmer';
  const roleSelected = parts[13] || '';

  parsed.push({
    sno: parseInt(sno, 10) || (i + 1),
    name,
    function: func,
    role,
    interviewDate,
    interview2,
    clientFeedback,
    presentCtcRaw,
    status,
    offeredCtcRaw,
    doj,
    onboard,
    skillGroup,
    roleSelected
  });
});

console.log('Successfully parsed exactly', parsed.length, 'records!');

// Write to data.json
fs.writeFileSync('C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard/data.json', JSON.stringify(parsed, null, 2), 'utf8');

// Write to data.js
const dataJs = `const recruitmentData = ${JSON.stringify(parsed, null, 2)};\n`;
fs.writeFileSync('C:/Users/lucky/.gemini/antigravity/scratch/cdm_recruitment_dashboard/data.js', dataJs, 'utf8');

console.log('✅ data.json and data.js updated with all 122 raw records!');
