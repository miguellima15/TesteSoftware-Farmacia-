import time
from farmacia import Farmacia

def test_performance_venda():
    farmacia = Farmacia()
    farmacia.cadastrar_medicamento("001", "Paracetamol", 1000, 5.0)
    start_time = time.time()
    for _ in range(100):
        farmacia.vender_medicamento("001", 10)
    end_time = time.time()
    assert (end_time - start_time) < 1  # Verificar se o teste foi concluído em menos de 1 segundo