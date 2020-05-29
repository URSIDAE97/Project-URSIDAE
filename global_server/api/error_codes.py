from flask import jsonify


def missing_request_body():
    """
    api request is missing the json body part
    :return: error code 400 (Bad request)
    """
    return jsonify({'msg': 'Request is missing the body part'}), 400


def missing_required_parameters():
    """
    api request is missing some of the required parameters
    :return: error code 400 (Bad request)
    """
    return jsonify({'msg': 'Request is missing some required parameters'}), 400


def unauthorized():
    """
    api request rejected due to incorrect user credentials
    :return: error code 401 (Unauthorized)
    """
    return jsonify({'msg': 'Incorrect user credentials'}), 401
