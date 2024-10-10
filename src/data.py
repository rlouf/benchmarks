models = [
    "NousResearch/Nous-Hermes-llama-2-7b",  # 32,000 tokens vocabulary
    "gpt2",  # 50,257 tokens vocabulary
    "NousResearch/Hermes-3-Llama-3.1-8B",  # 128,256 tokens vocabulary
    "unsloth/gemma-2-2b-it-bnb-4bit",  # 256,128 tokens vocabulary
]

regex_cases = [
    {
        "name": "Phone Number",
        "regex": r'\d{3}-\d{2}-\d{4}',
        "example": '203-22-1234'
    },
    {
        "name": "URL",
        "regex": r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?',
        "example": 'https://github.com/outlines-dev/outlines'
    },
    {
        "name": "GSM8K",
        "regex": r'A: [\w \.\*\-=\+,\?/]{10,50}\. The answer is [1-9][0-9]{0,9}\.',
        "example": 'A: Some thoughts before answering. The answer is 42.'
    },
    {
        "name": "Complex string",
        "regex": r'(0|[1-9][0-9]*)|true|false|([a-zA-Z_][a-zA-Z_0-9]*)',
        "example": 'AVeryLongStringtoTest1234'
    },
    {
        "name": "Long integer",
        "regex": r'\+[1-9]\d{1,14}',
        "example": '1234567891234'
    }
]

json_cases = [
    {
        "name": "RPG character",
        "schema":
        {
            "$defs": {
                "Armor": {
                    "enum": ["leather", "chainmail", "plate"],
                    "title": "Armor",
                    "type": "string",
                }
            },
            "properties": {
                "name": {"maxLength": 10, "title": "Name", "type": "string"},
                "age": {"title": "Age", "type": "integer"},
                "armor": {"$ref": "#/$defs/Armor"},
                "strength": {"title": "Strength", "type": "integer"},
            },
            "required": ["name", "age", "armor", "strength"],
            "title": "Character",
            "type": "object",
        },
        "example": """{'name': 'Super Warrior', 'age': 26,  'armor': 'leather', 'armor': 10}""",
    },
    {
        "name": "Simple nested schema",
        "schema": {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": "Schema for a recording",
            "type": "object",
            "definitions": {
                "artist": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "functions": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["id", "name", "functions"],
                }
            },
            "properties": {
                "id": {"type": "number"},
                "work": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "composer": {"$ref": "#/definitions/artist"},
                    },
                },
                "recording_artists": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/artist"},
                },
            },
            "required": ["id", "work", "recording_artists"],
        },
        "example": """{'id': 999, 'work': {'id': 1, 'name': 'Strasbourg Saint-Denis', 'composer': 'Roy Hargrove'}, 'recording_artists': [{'id': 2, 'name': 'Roy Hargrove', 'functions': ['Trumpet', 'Singing']}]}""",
    },
]