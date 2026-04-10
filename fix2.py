import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add console logging to init
old_init = '''init() {
                // Initialize domains if not present
                if (!this.data.domains) {'''

new_init = '''init() {
                console.log('App initializing...');
                console.log('Stored data:', this.data);

                // Initialize domains if not present
                if (!this.data.domains) {'''

content = content.replace(old_init, new_init)

# Add logging to render
old_render = '''render() {
                this.renderTabs();'''

new_render = '''render() {
                console.log('Rendering... Domain:', this.currentDomain, 'Field:', this.currentField, 'Subfield:', this.currentSubfield);
                const data = this.getCurrentData();
                console.log('Current data items:', data.items.length, data.items);
                this.renderTabs();'''

content = content.replace(old_render, new_render, 1)

# Fix getCurrentData to return properly
old_getdata = '''getCurrentData() {
                if (this.searchQuery) {'''

new_getdata = '''getCurrentData() {
                console.log('Getting data for domain:', this.currentDomain);
                if (this.searchQuery) {'''

content = content.replace(old_getdata, new_getdata)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added debugging logs')
