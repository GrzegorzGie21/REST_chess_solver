from flask import Flask, jsonify, make_response, Response

app = Flask(__name__)


@app.route("/api/v1/")
def index() -> Response:
    return make_response(jsonify({'status': 'API is working'}), 200)


@app.errorhandler(404)
def page_not_found(error: str) -> Response:
    return make_response(jsonify({"error": "Page not found"}), 404)


@app.errorhandler(500)
def server_error() -> Response:
    return make_response(jsonify({"error": "Internal server error"}))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
