

# from flask import Flask, request, jsonify
# from elasticsearch import Elasticsearch
#
# app = Flask(__name__)
#
# # Elasticsearch connection
# es = Elasticsearch(["http://127.0.0.1:9200"])
#
#
# @app.route('/data', methods=['GET'])
# def get_jobs():
#     search_query = request.args.get('query', '')  # Get the search query from the request parameters
#
#     # Elasticsearch query
#     es_query = {
#         "query": {
#             "match": {
#                 "Descripción": {
#                     "query": search_query,
#                     "analyzer": "spanish_fuzzy",
#                     "fuzziness": "AUTO"
#                 }
#             }
#         }
#     }
#
#     # Execute the Elasticsearch query
#     response = es.search(index='data6', body=es_query)
#
#     # Extract Descripción field from the Elasticsearch response
#     descriptions = [hit['_source']['Descripción'] for hit in response['hits']['hits']]
#
#     # Return Descripción field data as JSON response
#     return jsonify(descriptions)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from elasticsearch import Elasticsearch
#
# app = Flask(__name__)
#
# # Elasticsearch connection to Elastic Cloud
# cloud_id = "your-elastic-cloud-id"  # Replace with your Elastic Cloud ID
# cloud_auth = ("your-elastic-cloud-username", "your-elastic-cloud-password")  # Replace with your Elastic Cloud credentials
#
# es = Elasticsearch(cloud_id=cloud_id, http_auth=cloud_auth)
#
# @app.route('/data', methods=['GET'])
# def get_jobs():
#     search_query = request.args.get('query', '')  # Get the search query from the request parameters
#
#     # Elasticsearch query
#     es_query = {
#         "query": {
#             "match": {
#                 "Descripción": {
#                     "query": search_query,
#                     "analyzer": "spanish_fuzzy",
#                     "fuzziness": "AUTO"
#                 }
#             }
#         }
#     }
#
#     # Execute the Elasticsearch query
#     response = es.search(index='data', body=es_query)
#
#     # Extract Descripción field from the Elasticsearch response
#     descriptions = [hit['_source']['Descripción'] for hit in response['hits']['hits']]
#
#     # Return Descripción field data as JSON response
#     return jsonify(descriptions)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elasticsearch connection to Elastic Cloud
client = Elasticsearch(
    "https://f6d1377bf7d74ba5900ed9881cf6e1b5.us-central1.gcp.cloud.es.io:443",
    api_key="NmNGMTU0b0Jqd2dadGs0VEJTY0I6RDJ4U3VFb2lRdzZET25wWG1NTFZwZw=="
)


@app.route('/data', methods=['GET'])
def get_jobs():
    search_query = request.args.get('query', '')  # Get the search query from the request parameters

    # Elasticsearch query
    es_query = {
        "query": {
            "match": {
                "Descripción": {
                    "query": search_query,
                    "analyzer": "spanish_fuzzy",
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    # Execute the Elasticsearch query
    response = client.search(index='data', body=es_query)

    # Extract Descripción field from the Elasticsearch response
    descriptions = [hit['_source']['Descripción'] for hit in response['hits']['hits']]

    # Return Descripción field data as JSON response
    return jsonify(descriptions)

if __name__ == '__main__':
    app.run(debug=True)
