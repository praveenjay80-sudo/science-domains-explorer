#!/usr/bin/env python3
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science Domains Explorer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --primary: #2563eb; --bg: #0f172a; --surface: #1e293b;
            --text: #f8fafc; --text-muted: #94a3b8; --border: #475569;
        }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }
        .header { background: var(--surface); padding: 1.5rem; border-bottom: 1px solid var(--border); }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .btn { padding: 0.6rem 1.2rem; border-radius: 8px; border: none; cursor: pointer; background: var(--surface); color: var(--text); border: 1px solid var(--border); margin: 0.5rem; }
        .btn:hover { opacity: 0.8; }
        .btn-primary { background: var(--primary); }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .card { background: var(--surface); padding: 1rem; border-radius: 8px; border: 1px solid var(--border); }
        .modal { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); align-items: center; justify-content: center; }
        .modal.active { display: flex; }
        .modal-content { background: var(--surface); padding: 2rem; border-radius: 8px; max-width: 500px; }
        input, select { width: 100%; padding: 0.5rem; margin: 0.5rem 0; background: #1e293b; border: 1px solid #475569; color: white; }
        .notification { position: fixed; bottom: 1rem; right: 1rem; background: green; padding: 1rem; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="container" style="display: flex; justify-content: space-between;">
            <h1>Science Domains Explorer</h1>
            <button class="btn" onclick="app.showSettings()">Settings</button>
        </div>
    </div>
    <div class="container">
        <button class="btn btn-primary" onclick="app.generate()">Generate Items</button>
        <button class="btn" onclick="app.clear()">Clear</button>
        <div id="content" class="grid"></div>
    </div>
    <div class="modal" id="modal" onclick="if(event.target.id==='modal')app.closeModal()">
        <div class="modal-content">
            <h2>Settings</h2>
            <select id="provider">
                <option value="mock">Mock Data</option>
                <option value="ollama">Ollama</option>
            </select>
            <input id="url" placeholder="Ollama URL" value="http://localhost:11434">
            <button class="btn btn-primary" onclick="app.save()">Save</button>
            <button class="btn" onclick="app.test()">Test</button>
        </div>
    </div>
    <script>
        const app = {
            data: [],
            init() {
                console.log('App init');
                this.load();
                this.render();
            },
            load() {
                const stored = localStorage.getItem('items');
                this.data = stored ? JSON.parse(stored) : [];
            },
            saveStore() {
                localStorage.setItem('items', JSON.stringify(this.data));
            },
            render() {
                const el = document.getElementById('content');
                if (this.data.length === 0) {
                    el.innerHTML = '<p style="color: var(--text-muted)">No items. Click Generate.</p>';
                    return;
                }
                el.innerHTML = this.data.map(item => `
                    <div class="card">
                        <h3>${item.name}</h3>
                        <p>${item.desc}</p>
                    </div>
                `).join('');
            },
            generate() {
                this.data = [
                    {name: 'Mathematics', desc: 'Study of numbers'},
                    {name: 'Physics', desc: 'Study of matter'},
                    {name: 'Biology', desc: 'Study of life'}
                ];
                this.saveStore();
                this.render();
                this.notify('Items generated!');
            },
            clear() {
                this.data = [];
                this.saveStore();
                this.render();
                this.notify('Cleared!');
            },
            showSettings() {
                document.getElementById('modal').classList.add('active');
            },
            closeModal() {
                document.getElementById('modal').classList.remove('active');
            },
            save() {
                const config = {
                    provider: document.getElementById('provider').value,
                    url: document.getElementById('url').value
                };
                localStorage.setItem('config', JSON.stringify(config));
                this.notify('Saved!');
                this.closeModal();
            },
            async test() {
                const url = document.getElementById('url').value;
                try {
                    const res = await fetch(url + '/api/tags');
                    this.notify(res.ok ? 'Connected!' : 'Failed');
                } catch(e) {
                    this.notify('Error: ' + e.message);
                }
            },
            notify(msg) {
                const n = document.createElement('div');
                n.className = 'notification';
                n.textContent = msg;
                document.body.appendChild(n);
                setTimeout(() => n.remove(), 2000);
            }
        };
        window.onload = () => app.init();
    </script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Created fresh index.html')
