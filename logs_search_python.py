# Payload JSON simulado (já convertido para dict)
api_response = {
    "data": {
        "region_us_east": {
            "cluster_1": {
                "status": "healthy",
                "pods": [
                    {"name": "auth-service-abc", "state": "Running"},
                    {"name": "payment-service-xyz", "state": "CrashLoopBackOff"}
                ]
            },
            "cluster_2": {
                "status": "provisioning" 
                # Note que este cluster não tem a chave "pods"
            }
        },
        "region_sa_east": None # Região fora do ar
    }
}

def find_crashing_pods(payload: dict) -> list[str]:
    crashing_pods = []
    
    # Navegação defensiva: se "data" não existir, retorna dict vazio para não quebrar o loop
    regions = payload.get("data", {})
    
    for region_name, clusters in regions.items():
        if not clusters: # Pula se a região for None (como region_sa_east)
            continue
            
        for cluster_name, cluster_data in clusters.items():
            # O pulo do gato: usar .get() e fornecer uma lista vazia [] como fallback
            pods = cluster_data.get("pods", [])
            
            for pod in pods:
                if pod.get("state") == "CrashLoopBackOff":
                    crashing_pods.append(pod.get("name", "unknown_pod"))
                    
    return crashing_pods

print(find_crashing_pods(api_response))
# Saída esperada: ['payment-service-xyz']
