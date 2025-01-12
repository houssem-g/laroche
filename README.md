# LaRoche

## Overview

LaRoche is a containerized application that integrates GraphDB, FastAPI, and ChatGPT to provide a query system. Users can query data from a triplestore stored in GraphDB, and if the data is not found, ChatGPT is used to provide an intelligent response.

---

## How to Run the Project

### 1. Create an `.env` File
- Navigate to the `./backend` directory.
- Create an `.env` file with the following content:
  ```env
  GRAPHDB_URL_SELECT=http://graphdb:7200/repositories/myRepo
  GRAPHDB_URL_UPDATE=http://graphdb:7200/repositories/myRepo/statements
  GRAPHDB_URL=http://graphdb:7200
  OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE

2. Start the Application
    Run the following command from the root directory:
        `docker-compose up --build`

3. Access GraphDB
    Open http://localhost:7200/ in your browser.

4. Create a Repository in GraphDB
    In the GraphDB interface:
    Create a repository named myRepo.
    Use the default configuration.
    Select OWL-Horst(optimized) as the Ruleset.

5. Add a Triple to GraphDB
    Open the backend Swagger documentation at: http://127.0.0.1:8000/docs#/items/create_item_items__post.
    Add a sample triple to GraphDB by sending the following JSON payload:
    {
        "subject": "MySubject",
        "predicate": "hasName",
        "obj": "HelloWorld"
    }

6. Test the Frontend
    Open the frontend in your browser at http://localhost:3000.
    Enter a query for MySubject. The backend will:
    Query the GraphDB container for the subject.
    If no match is found, ChatGPT will provide a response based on its knowledge.

### Known Issues
OpenAI Model Error:
You might encounter the following error:

   `The model `gpt-4o` does not exist or you do not have access to it.`

Solution:
Ensure your OpenAI account has sufficient credits (recommend adding ~$5).
If the error persists, create a new API key using the following link: OpenAI API Keys.


### Notes
Ensure Docker is installed and running on your system.
Use docker-compose to simplify the setup and run all services seamlessly.