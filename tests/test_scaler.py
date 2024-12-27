from scaler import generate_scale

def test_generate_major_scale():
    assert generate_scale('C', [2, 2, 1, 2, 2, 2, 1]) == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']