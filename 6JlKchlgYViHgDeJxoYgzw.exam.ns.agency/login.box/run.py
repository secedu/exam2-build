import os
from safespace import create_app
app = create_app()
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6443))
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
