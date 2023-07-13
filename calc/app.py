# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
@app.route('/add')
def do_add():
    # Retrieve the query parameters 'a' and 'b' from the request
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    # Perform the addition operation
    result = add(a,b)
    # Return the result as a string
    return str(result)



@app.route('/sub')
def do_sub():
    """Substract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    # Perform the addition operation
    result = sub(a,b)

    # Return the result as a string
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = mult(a,b)

    return str(result)


@app.route('/div')
def do_div():
    """Divide a by b."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = div(a,b)

    return str(result) 