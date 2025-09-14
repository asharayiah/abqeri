// Minimal client for Abqeri Cloud API
let API_BASE = "";
fetch('config.json').then(r=>r.json()).then(cfg=>{
  API_BASE = cfg.API_BASE;
  document.getElementById('env').innerText = 'API: ' + API_BASE;
});

let token = null;

document.getElementById('btnLogin').onclick = async () => {
  const email = document.getElementById('email').value || 'guest@abqeri.com';
  const apiKey = document.getElementById('apiKey').value || '';
  const r = await fetch(API_BASE + '/auth/login', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({email, api_key: apiKey})
  });
  const j = await r.json();
  token = j.token;
  document.getElementById('authOut').textContent = JSON.stringify(j, null, 2);
};

document.getElementById('btnSubmit').onclick = async () => {
  const backend = document.getElementById('backend').value;
  const entry = document.getElementById('entry').value || 'ai_test:main';
  let params = {};
  try { params = JSON.parse(document.getElementById('params').value || '{}'); } catch(e){}
  const fd = new FormData();
  fd.append('backend', backend);
  fd.append('entry', entry);
  fd.append('params', JSON.stringify(params));
  const file = document.getElementById('file').files[0];
  if (file) fd.append('file', file);
  const r = await fetch(API_BASE + '/jobs', {
    method:'POST',
    headers: token ? {'Authorization':'Bearer '+token} : {},
    body: fd
  });
  const j = await r.json();
  document.getElementById('jobOut').textContent = JSON.stringify(j, null, 2);
  document.getElementById('jobId').value = j.id || '';
};

document.getElementById('btnStatus').onclick = async () => {
  const id = document.getElementById('jobId').value;
  const r = await fetch(API_BASE + '/jobs/' + id, {
    headers: token ? {'Authorization':'Bearer '+token} : {}
  });
  const j = await r.json();
  document.getElementById('statusOut').textContent = JSON.stringify(j, null, 2);
};

document.getElementById('btnResults').onclick = async () => {
  const id = document.getElementById('jobId').value;
  const r = await fetch(API_BASE + '/jobs/' + id + '/results', {
    headers: token ? {'Authorization':'Bearer '+token} : {}
  });
  const j = await r.json();
  document.getElementById('statusOut').textContent = JSON.stringify(j, null, 2);
};
