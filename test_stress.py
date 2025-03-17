from farmacia import Farmacia

def test_stress_vendas():
    farmacia = Farmacia()
    farmacia.cadastrar_medicamento("001", "Paracetamol", 10000, 5.0)
    for _ in range(1000):
        farmacia.vender_medicamento("001", 10)
    assert farmacia.medicamentos[0].quantidade == 0
    assert len(farmacia.vendas) == 1000
    