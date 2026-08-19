
const { JSDOM } = require('jsdom');
const fs = require('fs');

const html = fs.readFileSync('whatsthetime.html', 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
const window = dom.window;

const start = process.hrtime.bigint();
const N = 20000;
for (let i = 0; i < N; i++) {
  window.tick();
}
const end = process.hrtime.bigint();
const totalMs = Number(end - start) / 1e6;
console.log(`Total time for ${N} tick() calls: ${totalMs.toFixed(2)}ms (${(totalMs/N).toFixed(4)}ms/call)`);
