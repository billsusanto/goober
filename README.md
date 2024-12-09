# Goober
a Web search engine from the ground up that is capable of handling tens of thousands of Web pages, under harsh operational constraints and having a query response time under 300ms 

How It Works
1. User Input: The user types a query in the search bar on the frontend (page.tsx).
2. API Call: The frontend sends the query to the /api/query endpoint (search.py).
3. Query Processing:
4. The backend reads the dataset (final_indicies).
5. Tokenizes and stems the query (tokenizer.py).
6. Scores and ranks documents (query.py).
7. Response: The backend returns the top 10 results, which are displayed on the frontend.
