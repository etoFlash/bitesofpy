from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    return list(filter(lambda x: x["id"] == qid, quotes))


def _quote_exists(existing_quote):
    """Recommended helper"""
    return bool(_get_quote(existing_quote))


def _get_index(qid):
    for i, q in enumerate(quotes):
        if q["id"] == qid:
            return i


def _quote_exist_by_values(quote, movie):
    return any([q["quote"] == quote and q["movie"] == movie
               for q in quotes])


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes=quotes)


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    if not _quote_exists(qid):
        abort(404)

    return jsonify(quotes=_get_quote(qid))


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    quote = request.json.get("quote")
    movie = request.json.get("movie")

    if not all([quote, movie]) or _quote_exist_by_values(quote, movie):
        abort(400)

    new_quote = {"id": len(quotes) + 1,
                 "quote": quote,
                 "movie": movie}
    quotes.append(new_quote)
    return jsonify(quote=new_quote), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    quote = request.json.get("quote")
    movie = request.json.get("movie")

    if not _quote_exists(qid):
        abort(404)
    elif not all([quote, movie]):
        abort(400)

    idx = _get_index(qid)
    quotes[idx] = {"id": qid,
                   "quote": quote,
                   "movie": movie}

    return jsonify(quote=quotes[idx])


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if not _quote_exists(qid):
        abort(404)

    global quotes
    del quotes[_get_index(qid)]

    return "", 204
