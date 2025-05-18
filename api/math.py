from math_app import add, subtract, multiply, divide

def handler(request):
    op = request.args.get('operation')
    x = request.args.get('x')
    y = request.args.get('y')

    if op not in ['add', 'subtract', 'multiply', 'divide']:
        return {
            'statusCode': 400,
            'body': 'Invalid operation'
        }

    try:
        x_val = float(x)
        y_val = float(y)
    except (TypeError, ValueError):
        return {
            'statusCode': 400,
            'body': 'Invalid numbers'
        }

    if op == 'add':
        result = add(x_val, y_val)
    elif op == 'subtract':
        result = subtract(x_val, y_val)
    elif op == 'multiply':
        result = multiply(x_val, y_val)
    elif op == 'divide':
        try:
            result = divide(x_val, y_val)
        except ValueError as e:
            return {
                'statusCode': 400,
                'body': str(e)
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Unknown operation'
        }

    return {
        'statusCode': 200,
        'body': str(result)
    }
