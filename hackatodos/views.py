import json

import openai
from http import HTTPStatus

from ninja import NinjaAPI
from ninja.responses import Response


api = NinjaAPI()


@api.post("/insights")
def insights(request) -> Response:
    data = json.loads(request.body)
    timeframe = data.get("timeframe", "last month")
    database = data.get("database", {})

    prompt = (
        f"Based on the provided data, generate insights about the clinic's performance. "
        f"The timeframe to analyze is {timeframe}. Here is the data snapshot: {database}. "
        f"Provide key metrics on patient registrations, conversion rates, and lead quality."
        f" (Objective answer and in Portuguese)"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            temperature=1,
            max_tokens=1000
        )

        return Response({"insights": response["choices"][0]["message"]["content"]}, status=HTTPStatus.OK)

    except Exception as e:
        return Response({"error": str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
