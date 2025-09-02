let token = "";
async function register() {
  const email = document.getElementById('regEmail').value;
  const password = document.getElementById('regPass').value;
  const res = await fetch('http://localhost:8000/api/auth/register', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({email, password})});
  const data = await res.json(); token = data.access_token || ''; document.getElementById('token').innerText = token ? 'Token ✔️' : JSON.stringify(data);
}
async function login() {
  const email = document.getElementById('logEmail').value; const password = document.getElementById('logPass').value;
  const form = new URLSearchParams(); form.append('username', email); form.append('password', password);
  const res = await fetch('http://localhost:8000/api/auth/login', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:form});
  const data = await res.json(); token = data.access_token || ''; document.getElementById('token').innerText = token ? 'Token ✔️' : JSON.stringify(data);
}
async function createJob() {
  if (!token) return alert('Login first');
  const payload = {title:document.getElementById('title').value, company:document.getElementById('company').value, status:document.getElementById('status').value||'applied', applied_date:document.getElementById('applied_date').value||null, link:document.getElementById('link').value||null, notes:document.getElementById('notes').value||null};
  await fetch('http://localhost:8000/api/jobs', {method:'POST', headers:{'Content-Type':'application/json','Authorization':'Bearer '+token}, body:JSON.stringify(payload)});
  loadJobs();
}
async function loadJobs() {
  if (!token) return alert('Login first');
  const res = await fetch('http://localhost:8000/api/jobs', {headers:{'Authorization':'Bearer '+token}});
  const items = await res.json(); const ul = document.getElementById('jobsList'); ul.innerHTML=''; items.forEach(j=>{const li=document.createElement('li'); li.innerText=${j.id}:  @  []; ul.appendChild(li);});
}
