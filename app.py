from flask import Flask
from flask import jsonify
from flask import render_template
import json

from grid_webservices.k8s import KubernetesClient

app = Flask(__name__)
kubernetes = KubernetesClient.create_inside_cluster()


@app.route("/")
def index():
    return render_template("index.html.j2")


@app.route("/api/v1")
def api():
    ingresses = kubernetes.get(
        "/apis/networking.k8s.io/v1beta1/ingresses",
        params={"labelSelector": "webservice.toolforge.org/gridengine=true", "limit": 1000},
    )["items"]

    tools = {}
    for ingress in ingresses:
        namespace: str = ingress["metadata"]["namespace"]
        if not namespace.startswith("tool-"):
            continue
        namespace = namespace[5:]
        tools[namespace] = {"active": True}

    return jsonify(tools), 200


@app.route("/healthz")
def healthz():
    response = kubernetes.get("/api")
    if "v1" not in response["versions"]:
        return jsonify({"error": f"Kubernetes API connection failed: {json.dumps(response)}"}), 500
    return jsonify({}), 200


if __name__ == "__main__":
    app.run()
