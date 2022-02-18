from flask import Flask, jsonify, make_response, Response
from utils import create_response_context
import const

app = Flask(__name__)


@app.route("/api/v1/")
def index() -> Response:
    return make_response(jsonify({'status': 'API is working'}), 200)


@app.route('/api/v1/<string:chess_figure>/<string:current_field>/', methods=["GET"])
@app.route('/api/v1//<string:chess_figure>/<string:current_field>/<string:dest_field>/', methods=['GET'])
def figure_moves(chess_figure: str, current_field: str, dest_field: str = None) -> Response:
    figure_type, Figure = const.CHESS_FIGURES.get(chess_figure, (None, None))

    if not figure_type:
        status_code = 404
        context = create_response_context(availableMoves=[],
                                          figure=chess_figure,
                                          error='Figure does not exist.',
                                          currentField=current_field,
                                          )

        return make_response(jsonify(context), status_code)

    figure = Figure(current_field, figure_type)

    if current_field not in const.CHESS_FIELDS:
        status_code = 409
        context = create_response_context(availableMoves=[],
                                          figure=chess_figure,
                                          error='Field does not exist.',
                                          currentField=current_field,
                                          )
        return make_response(jsonify(context), status_code)

    if not dest_field:
        status_code = 200
        context = create_response_context(availableMoves=figure.list_available_moves(),
                                          figure=chess_figure,
                                          error=None,
                                          currentField=current_field,
                                          )
        return make_response(jsonify(context), status_code)
    else:
        move_permission = figure.validate_move(dest_field)
        if dest_field not in const.CHESS_FIELDS:
            status_code = 409
            context = create_response_context(move=move_permission,
                                              figure=chess_figure,
                                              error='Destination field does not exist',
                                              currentField=current_field,
                                              destField=dest_field,
                                              )
            return make_response(jsonify(context), status_code)

        if move_permission == 'invalid':
            status_code = 409
            context = create_response_context(move=move_permission,
                                              figure=chess_figure,
                                              error='Current move is not permitted.',
                                              currentField=current_field,
                                              destField=dest_field,
                                              )
            return make_response(jsonify(context), status_code)


        else:
            status_code = 200
            context = create_response_context(move=move_permission,
                                              figure=chess_figure,
                                              error=None,
                                              currentField=current_field,
                                              destField=dest_field,
                                              )
            return make_response(jsonify(context), status_code)


@app.errorhandler(404)
def page_not_found(error: str) -> Response:
    return make_response(jsonify({"error": "Page not found"}), 404)


@app.errorhandler(500)
def server_error() -> Response:
    return make_response(jsonify({"error": "Internal server error"}))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
