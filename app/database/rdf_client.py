# app/database/rdf_client.py

from SPARQLWrapper import SPARQLWrapper, JSON, POST, POSTDIRECTLY
from app.config import settings


class RDFClient:
    """
    An OOP interface to interact with a GraphDB repository via SPARQL.
    """

    def __init__(self, endpoint_url_select: str = settings.GRAPHDB_URL_SELECT, endpoint_url_update: str = settings.GRAPHDB_URL_UPDATE):
        self.endpoint_url_select = endpoint_url_select
        self.endpoint_url_update = endpoint_url_update

    def create_data(self, subject: str, predicate: str, obj: str) -> bool:
        """
        Insert a triple (subject, predicate, object).
        Returns True if successful, False otherwise.
        """
        insert_query = f"""
        PREFIX ex: <http://localhost:7200/ex#>
        INSERT DATA {{
          ex:{subject} ex:{predicate} "{obj}" .
        }}
        """
        return self._update_query(insert_query)

    def read_data(self, subject: str):
        """
        Simple read example: get all predicates and objects for a given subject.
        """
        select_query = f"""
        PREFIX ex: <http://localhost:7200/ex#>
        SELECT ?p ?o
        WHERE {{
          ex:{subject} ?p ?o .
        }}
        """
        return self._select_query(select_query)

    def delete_data(self, subject: str, predicate: str = None):
        """
        Delete example: remove all triples for a subject if no predicate is given,
        or remove just the specified predicate/object pairs if provided.
        """
        if predicate:
            delete_query = f"""
            PREFIX ex: <http://localhost:7200/ex#>
            DELETE WHERE {{
              ex:{subject} ex:{predicate} ?o .
            }}
            """
        else:
            delete_query = f"""
            PREFIX ex: <http://localhost:7200/ex#>
            DELETE WHERE {{
              ex:{subject} ?p ?o .
            }}
            """
        return self._update_query(delete_query)

    def update_data(self, subject: str, old_predicate: str, new_predicate: str):
        """
        Basic SPARQL approach to 'update': typically a DELETE + INSERT.
        This is just a simplified example, might need more robust logic in production.
        """
        update_query = f"""
        PREFIX ex: <http://localhost:7200/ex#>
        DELETE {{
          ex:{subject} ex:{old_predicate} ?o .
        }}
        INSERT {{
          ex:{subject} ex:{new_predicate} ?o .
        }}
        WHERE {{
          ex:{subject} ex:{old_predicate} ?o .
        }}
        """
        return self._update_query(update_query)

    def _select_query(self, query: str):
        """
        Helper method to perform SPARQL SELECT queries.
        """
        sparql = SPARQLWrapper(self.endpoint_url_select)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        sparql.addCustomHttpHeader("Accept", "application/sparql-results+json")
        results = sparql.query().convert()
        data = []
        for binding in results["results"]["bindings"]:
            row = {var: binding[var]["value"] for var in binding}
            data.append(row)
        return data

    def _update_query(self, query: str) -> bool:
        """
        Helper method to perform SPARQL UPDATE queries
        (INSERT, DELETE, or combined).
        """
        try:
            sparql = SPARQLWrapper(self.endpoint_url_update)
            sparql.setMethod(POST)
            sparql.setRequestMethod(POSTDIRECTLY)
            sparql.addCustomHttpHeader("Content-Type", "application/sparql-update")
            sparql.setQuery(query)
            sparql.query()

            return True
        except Exception as e:
            print(f"SPARQL Update Error: {e}")
            return False
