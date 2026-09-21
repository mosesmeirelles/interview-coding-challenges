def find_crashing_pods_optimized(payload: dict) -> list[str]:
    # Usamos uma list comprehension aninhada. 
    # É mais rápido em Python pois evita as chamadas repetidas ao método .append()
    
    regions = payload.get("data", {})
    
    return [
        pod.get("name", "unknown_pod")
        for clusters in regions.values() if clusters  # Pega os dicionários de clusters, ignora None
        for cluster_data in clusters.values()         # Itera sobre os dados de cada cluster
        for pod in cluster_data.get("pods", [])       # Itera sobre os pods
        if pod.get("state") == "CrashLoopBackOff"     # Filtro final
    ]

# --- TDD / Live Testing Setup ---
if __name__ == "__main__":
    mock_payload = {
        "data": {
            "us_east": {
                "c1": {"pods": [{"name": "pod-1", "state": "Running"}, {"name": "pod-2", "state": "CrashLoopBackOff"}]}
            },
            "sa_east": None, # Testando comportamento nulo
            "eu_west": {
                "c2": {} # Testando cluster sem a chave pods
            }
        }
    }

    # Se falhar, o Python lança um AssertionError com a sua mensagem
    assert find_crashing_pods_optimized(mock_payload) == ["pod-2"], "Deveria encontrar apenas o pod-2"
    
    assert find_crashing_pods_optimized({}) == [], "Deveria retornar lista vazia para payload vazio"
    assert find_crashing_pods_optimized({"data": None}) == [], "Deveria lidar com data == None"
    
    print("✅ Todos os testes passaram! Código seguro para produção.")
