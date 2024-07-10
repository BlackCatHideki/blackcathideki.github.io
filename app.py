from flask import Flask, render_template, url_for

# Initialize Flask application
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def index():
    # Personal and professional information to be displayed on the homepage
    name = 'Hideki'
    tags = 'Gluttony kitty'
    description = "🐱 Chubby furry cat ♥️ Eating, Anime & Linux 💻 Bioengineering & AI 🎮 Wakfu 🇬🇧 🇪🇸 Speaker"
    links = [
        # Social and professional links to be included on the homepage
        {'name': 'BlueSky', 'url': 'https://bsky.app/profile/techcathideki.bsky.social', 'icon': 'fa-bluesky'},
        {'name': 'Discord', 'url': 'https://discordapp.com/users/techcathideki', 'icon': 'fa-discord'},
        {'name': 'Facebook', 'url': 'https://www.facebook.com/techcatHideki/', 'icon': 'fa-facebook'},
        {'name': 'GitHub', 'url': 'https://github.com/techcathideki', 'icon': 'fa-github'},
        {'name': 'Line', 'url': 'https://line.me/ti/p/iTlebHiBCU', 'icon': 'fa-line'},
        {'name': 'pixiv', 'url': 'https://www.pixiv.net/en/users/103988843', 'icon': 'fa-pixiv'},
        {'name': 'Steam', 'url': 'https://steamcommunity.com/id/techcatHideki/', 'icon': 'fa-steam'},
        {'name': 'Telegram', 'url': 'https://telegram.me/techcatHideki', 'icon': 'fa-telegram'},
        {'name': 'Twitter', 'url': 'https://twitter.com/techcatHideki', 'icon': 'fa-x-twitter'}
    ]
    # Render the homepage template with the provided information
    return render_template('index.html', name=name, tags=tags, description=description, links=links)

# Define route for handling 404 errors
@app.route("/<path:error404>")
def error404(error404):
    # Information to be displayed on the 404 error page
    name = 'Error 404'
    description = 'This page could not be found'
    # Render the 404 error template with the provided information
    return render_template('404.html', name=name, description=description)

# Run the Flask application if this script is executed as the main program
if __name__ == '__main__':
    app.run()
