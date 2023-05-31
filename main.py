from flask import Flask, render_template, url_for

# website flask return website interface
website = Flask(
    __name__
)

# website route to index.html
@website.route(
    "/"
)

def index():
    
    return render_template(
        "index.html"
    )

# init main
if __name__ == "__main__":
    
    website.run()