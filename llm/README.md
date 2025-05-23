# Introduction

Common codes snippets for querying LLM APIs.

# OpenAI JSON Schema

The following function converts a Pydantic model to an OpenAI JSON schema with required fields.

```python
import json
from pydantic import BaseModel

class MyModel(BaseModel):
    name: str
    age: int

def pydantic_model_to_openai_schema(pydantic_model, name) -> str:
    model_schema_dict = pydantic_model.model_json_schema()
    model_schema_dict['additionalProperties'] = False
    openai_schema = {
        "name": name,
        "strict": True,
        "schema": model_schema_dict
    }
    openai_schema_json_str = json.dumps(openai_schema, indent=2)
    return openai_schema_json_str
```