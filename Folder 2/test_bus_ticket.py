import bus_ticket

def test_age_for_bus_ticket():
    assert bus_ticket.cal_bus_ticket_price(35) == 4
    
def test_65_and_over():
    assert bus_ticket.cal_bus_ticket_price(65) == 0