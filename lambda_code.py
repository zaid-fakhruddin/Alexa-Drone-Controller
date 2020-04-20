from __future__ import print_function
import boto3
import json


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_forward_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "forward"
    speech_output = "going forward"
    reprompt_text = "send another command"
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "forward"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_flip_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "flip"
    speech_output = "flip"
    reprompt_text = "send another command"
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "flip"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_launch_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "launch"
    speech_output = "ok boomer"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "launch"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_backwards_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "backwards"
    speech_output = "going backwards"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "backwards"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_left_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "left"
    speech_output = "going left"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "left"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_right_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "right"
    speech_output = "right"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "right"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_up_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "up"
    speech_output = "up"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    # Change topic, qos and payload
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "upup"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_down_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "down"
    speech_output = "down"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "down"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_emergency_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "emergency"
    speech_output = "emergency"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "emergency"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_land_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "land"
    speech_output = "land"
    reprompt_text = "You never responded to the first test message. Sending another one."
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "land"})
    )
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "conn"})
    )
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to zeyds drone controller. To start, connect to the drone by saying, launch drone. You can control the drone using commands like, forward, left, right, and backwards. Once finished, just say land."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "try again"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    client = boto3.client('iot-data', region_name='us-east-1')
    response = client.publish(
        topic='myTopic',
        qos=1,
        payload=json.dumps({"control": "stop"})
    )
    card_title = "Session Ended"
    speech_output = "Thank you for trying zaids drone controller. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "forward":
        return get_forward_response()
    elif intent_name == "launch":
        return get_launch_response()
    elif intent_name == "backwards":
        return get_backwards_response()
    elif intent_name == "left":
        return get_left_response()
    elif intent_name == "right":
        return get_right_response()
    elif intent_name == "up":
        return get_up_response()
    elif intent_name == "down":
        return get_down_response()
    elif intent_name == "emergency":
        return get_emergency_response()
    elif intent_name == "land":
        return get_land_response()
    elif intent_name == "flip":
        return get_flip_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])