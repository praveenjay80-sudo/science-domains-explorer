import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a debug/refresh button
old_actionbar = '<button class="btn btn-accent" onclick="app.generateNewItem()">➕ Generate New Item</button>'
new_actionbar = '<button class="btn btn-accent" onclick="app.generateNewItem()">➕ Generate New Item</button>\n            <button class="btn btn-secondary" onclick="app.forceRefresh()">🔄 Refresh View</button>'

content = content.replace(old_actionbar, new_actionbar)

# Add forceRefresh function
old_parsejson = 'parseJSONResponse(text) {'
new_parsejson = '''forceRefresh() {
                console.log('Force refreshing...');
                console.log('Current data:', this.data);
                this.saveData();
                this.updateStats();
                this.render();
                this.showNotification('View refreshed!');
            }

            parseJSONResponse(text) {'''

content = content.replace(old_parsejson, new_parsejson, 1)

# Fix saveData to ensure proper storage
old_savedata = 'this.saveData();\n            },\n\n            // ============ BIBLIOGRAPHY'
new_savedata = '''this.saveData();

                // Force update after adding items
                setTimeout(() => {
                    this.updateStats();
                    this.render();
                }, 50);
            },

            // ============ BIBLIOGRAPHY'''

content = content.replace(old_savedata, new_savedata)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added refresh functionality')
