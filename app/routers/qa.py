# app/routers/qa.py

from fastapi import APIRouter, HTTPException
from app.database.rdf_client import RDFClient
from app.services.chatgpt import ChatGPTClient
from pydantic import BaseModel

router = APIRouter(prefix="/qa", tags=["Q&A"])

rdf_client = RDFClient()
chatgpt_client = ChatGPTClient()


class QARequest(BaseModel):
    user_query: str


@router.post("/")
def ask_question(payload: QARequest):
    user_query = payload.user_query.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="La requête ne peut pas être vide.")
    
    sparql_query = f"""
    PREFIX ex: <http://localhost:7200/ex#>
    SELECT ?p ?o
    WHERE {{
      ?s ?p ?o .
      FILTER(CONTAINS(LCASE(STR(?s)), LCASE("{user_query}")) ||
             CONTAINS(LCASE(STR(?p)), LCASE("{user_query}")) ||
             CONTAINS(LCASE(STR(?o)), LCASE("{user_query}")))
    }}
    LIMIT 50
    """
    rdf_data = rdf_client.select_query(sparql_query)

    if not rdf_data:
        raise HTTPException(status_code=404, detail="Aucune donnée trouvée pour la requête.")

    # Formater les données pour ChatGPT
    formatted_data = "\n".join([f"{item['p']} : {item['o']}" for item in rdf_data])

    prompt = f"Voici quelques informations pertinentes :\n{formatted_data}\n\nQuestion de l'utilisateur : {user_query}\n\nRéponse :"

    # Générer une réponse avec ChatGPT
    chatgpt_response = chatgpt_client.generate_response(prompt)

    return {"response": chatgpt_response}
