#TODO: Add the data schema to the prompt

ANNOTATE_WITH_EXPLANATION = """
You will be given a row of data from a table.

Your job is to annotate the data according to the criteria given by the user.

You should also add some rationale for your annotation.

Return the annotation in the following format:

{{
    "annotation": <annotation>,
    "rationale": <rationale>
}}

The criteria for annotation are as follows:

{criteria}

The user has also provided some examples of how to annotate the data. If there are no examples you should use your own judgement.

{examples}

the data will follow:
"""

ANNOTATE_WITHOUT_EXPLANATION = """
You will be given a row of data from a table.

Your job is to annotate the data according to the criteria given by the user.

Return the annotation in the following format:

{
    "annotation": <annotation>,
}

The criteria for annotation are as follows:

{criteria}

The user has also provided some examples of how to annotate the data. If there are no examples you should use your own judgement.

{examples}

the data will follow:
"""

