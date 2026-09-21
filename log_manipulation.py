import re
from collections import defaultdict, Counter

# Simulando as linhas de um arquivo de log
log_lines = [
    '192.168.1.10 - - [21/Sep/2026:14:00:01 -0300] "GET /api/v1/users HTTP/1.1" 200 512',
    '10.0.0.5 - - [21/Sep/2026:14:00:02 -0300] "POST /api/v1/payments HTTP/1.1" 500 128',
    '192.168.1.10 - - [21/Sep/2026:14:00:03 -0300] "GET /api/v1/users HTTP/1.1" 200 512',
    '10.0.0.5 - - [21/Sep/2026:14:00:04 -0300] "POST /api/v1/payments HTTP/1.1" 500 128',
    '172.16.0.2 - - [21/Sep/2026:14:00:05 -0300] "GET /health HTTP/1.1" 500 64',
]

def get_top_failing_ips(logs: list[str], top_n: int = 3) -> list[tuple[str, int]]:
    # Regex para capturar o IP (grupo 1) e o Status Code (grupo 2)
    # Padrão: Inicia com IP, tem coisas no meio (.*?), captura o código numérico após as aspas
    log_pattern = re.compile(r'^(\d{1,3}(?:\.\d{1,3}){3}).*?" \w+ .*? HTTP/1.\d" (\d{3})')
    
    error_counts = defaultdict(int)
    
    for line in logs:
        match = log_pattern.search(line)
        if match:
            ip = match.group(1)
            status_code = match.group(2)
            
            if status_code.startswith('5'):  # Filtra apenas erros 5xx
                error_counts[ip] += 1
                
    # Counter transforma o dicionário e nos dá o método most_common()
    return Counter(error_counts).most_common(top_n)

print(get_top_failing_ips(log_lines)) 
# Saída esperada: [('10.0.0.5', 2), ('172.16.0.2', 1)]
