
from tickets.loader import load_tickets


def create_csv(tmp_path, content):
    file_path = tmp_path / "test_tickets.csv"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)


def test_valid_ticket(tmp_path):
    content = (
        "ticket_id,customer_name,service_type,status,created_date,description\n"
        "T001,Aarav,Repair,open,2026-11-20,AC repair\n"
    )

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 1
    assert len(invalid) == 0


def test_missing_field(tmp_path):
    content = (
        "ticket_id,customer_name,service_type,status,created_date,description\n"
        "T002,,Repair,open,2026-11-20,AC repair\n"
    )

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_invalid_date(tmp_path):
    content = (
        "ticket_id,customer_name,service_type,status,created_date,description\n"
        "T003,Aarav,Repair,open,wrong-date,AC repair\n"
    )

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_invalid_enum(tmp_path):
    content = (
        "ticket_id,customer_name,service_type,status,created_date,description\n"
        "T004,Aarav,Repair,unknown,2026-11-20,AC repair\n"
    )

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_empty_csv(tmp_path):
    file_path = create_csv(tmp_path, "")

    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 0
